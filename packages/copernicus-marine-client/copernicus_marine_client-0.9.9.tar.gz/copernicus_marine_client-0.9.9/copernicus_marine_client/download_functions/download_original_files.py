import datetime
import pathlib
import re
from itertools import chain
from multiprocessing.pool import ThreadPool
from pathlib import Path
from typing import List, Optional, Tuple

import boto3
import botocore
from numpy import append, arange
from tqdm import tqdm

from copernicus_marine_client.catalogue_parser.request_structure import (
    GetRequest,
)
from copernicus_marine_client.core_functions.utils import (
    construct_query_params_for_marine_data_store_monitoring,
    construct_url_with_query_params,
    flatten,
    get_unique_filename,
)
from copernicus_marine_client.download_functions.download_get import (
    download_get,
)

# Some buckets do not support listing. While these buckets are being replaced
# by other ones that are listable, we need to recognise the non-listable ones
# LIST via CDN.
MARINE_DATA_LAKE_CDN_LISTING_ENDPOINT = "https://marine.copernicus.eu"
MARINE_DATA_LAKE_NON_LISTABLE_BUCKETS = {
    "mdl-native": {
        "endpoint_url": MARINE_DATA_LAKE_CDN_LISTING_ENDPOINT,
        "bucket": "mdl-native-list",
    },
    "mdl-native-dta": {
        "endpoint_url": MARINE_DATA_LAKE_CDN_LISTING_ENDPOINT,
        "bucket": "mdl-native-list-dta",
    },
}


def download_original_files(
    username: str,
    password: str,
    get_request: GetRequest,
) -> list[pathlib.Path]:
    filenames_in, filenames_out, locator = download_get(
        username,
        password,
        get_request,
        _download_header,
        create_filenames_out,
    )
    endpoint: str
    bucket: str
    endpoint, bucket = locator
    return download_files(
        username, endpoint, bucket, filenames_in, filenames_out
    )


def download_files(
    username: str,
    endpoint_url: str,
    bucket: str,
    filenames_in: List[str],
    filenames_out: List[pathlib.Path],
) -> list[pathlib.Path]:
    pool = ThreadPool()
    nfiles_per_process, nfiles = 1, len(filenames_in)
    indexes = append(
        arange(0, nfiles, nfiles_per_process, dtype=int),
        nfiles,
    )
    groups_in_files = [
        filenames_in[indexes[i] : indexes[i + 1]]
        for i in range(len(indexes) - 1)
    ]
    groups_out_files = [
        filenames_out[indexes[i] : indexes[i + 1]]
        for i in range(len(indexes) - 1)
    ]

    for groups_out_file in groups_out_files:
        parent_dir = Path(groups_out_file[0]).parent
        if not parent_dir.is_dir():
            pathlib.Path.mkdir(parent_dir, parents=True)

    download_summary_list = pool.imap(
        _download_files,
        zip(
            [username] * len(groups_in_files),
            [endpoint_url] * len(groups_in_files),
            [bucket] * len(groups_in_files),
            groups_in_files,
            groups_out_files,
        ),
    )
    download_summary = list(
        tqdm(download_summary_list, total=len(groups_in_files))
    )
    return flatten(download_summary)


def _download_header(
    data_path: str, regex: Optional[str], username: str, _password: str
) -> Tuple[str, Tuple[str, str], list[str], float]:
    (endpoint_url, bucket, path) = parse_original_files_dataset_url(data_path)
    filenames, sizes, total_size = [], [], 0.0
    raw_filenames = _list_files_on_marine_data_lake_s3(
        username, endpoint_url, bucket, path
    )
    filename_filtered = []
    for filename, size, last_modified_datetime in raw_filenames:
        if not regex or re.match(regex, filename):
            filenames += [filename]
            sizes += [float(size)]
            total_size += float(size)
            filename_filtered.append((filename, size, last_modified_datetime))

    message = "You requested the download of the following files:\n"
    for filename, size, last_modified_datetime in filename_filtered[:20]:
        message += str(filename)
        datetime_iso = re.sub(
            r"\+00:00$",
            "Z",
            last_modified_datetime.astimezone(datetime.timezone.utc).isoformat(
                timespec="seconds"
            ),
        )
        message += f" - {format_file_size(float(size))} - {datetime_iso}\n"
    if len(filenames) > 20:
        message += f"Printed 20 out of {len(filenames)} files\n"
    message += (
        f"\nTotal size of the download: {format_file_size(total_size)}\n\n"
    )
    locator = (endpoint_url, bucket)
    return (message, locator, filenames, total_size)


def _list_files_on_marine_data_lake_s3(
    username: str,
    endpoint_url: str,
    bucket: str,
    prefix: str,
) -> list[tuple[str, int, datetime.datetime]]:
    def _add_custom_query_param(params, context, **kwargs):
        """
        Add custom query params for MDS's Monitoring
        """
        params["url"] = construct_url_with_query_params(
            params["url"],
            construct_query_params_for_marine_data_store_monitoring(username),
        )

    # For non-listable buckets, use the alternatives (CDN)
    original_bucket = bucket
    if bucket in MARINE_DATA_LAKE_NON_LISTABLE_BUCKETS:
        alternative = MARINE_DATA_LAKE_NON_LISTABLE_BUCKETS[bucket]
        bucket = alternative["bucket"]
        endpoint_url = alternative["endpoint_url"]

    s3_session = boto3.session.Session()
    s3_client = s3_session.client(
        "s3",
        config=botocore.config.Config(
            # Configures to use subdomain/virtual calling format.
            s3={"addressing_style": "virtual"},
            signature_version=botocore.UNSIGNED,
        ),
        endpoint_url=endpoint_url,
    )

    # Register the botocore event handler for adding custom query params
    # to S3 LIST requests
    s3_client.meta.events.register(
        "before-call.s3.ListObjects", _add_custom_query_param
    )

    paginator = s3_client.get_paginator("list_objects")
    page_iterator = paginator.paginate(Bucket=bucket, Prefix=prefix)

    s3_objects = chain(*map(lambda page: page["Contents"], page_iterator))

    files_already_found = []
    for s3_object in s3_objects:
        files_already_found.extend(
            [
                (
                    f"s3://{original_bucket}/" + s3_object["Key"],
                    s3_object["Size"],
                    s3_object["LastModified"],
                )
            ]
        )
    return files_already_found


def _download_files(
    tuple_original_files_filename: Tuple[
        str, str, str, list[str], list[pathlib.Path]
    ],
) -> list[pathlib.Path]:
    (
        username,
        endpoint_url,
        bucket,
        filenames_in,
        filenames_out,
    ) = tuple_original_files_filename

    def _add_custom_query_param(params, context, **kwargs):
        """
        Add custom query params for MDS's Monitoring
        """
        params["url"] = construct_url_with_query_params(
            params["url"],
            construct_query_params_for_marine_data_store_monitoring(username),
        )

    def _original_files_file_download(
        endpoint_url: str, bucket: str, file_in: str, file_out: pathlib.Path
    ) -> pathlib.Path:
        """
        Download ONE file and return a string of the result
        """
        s3_session = boto3.session.Session()
        s3_client = s3_session.client(
            "s3",
            config=botocore.config.Config(
                # Configures to use subdomain/virtual calling format.
                s3={"addressing_style": "virtual"},
                signature_version=botocore.UNSIGNED,
            ),
            endpoint_url=endpoint_url,
        )

        # Register the botocore event handler for adding custom query params
        # to S3 HEAD and GET requests
        s3_client.meta.events.register(
            "before-call.s3.HeadObject", _add_custom_query_param
        )
        s3_client.meta.events.register(
            "before-call.s3.GetObject", _add_custom_query_param
        )

        s3_client.download_file(
            bucket,
            file_in.replace(f"s3://{bucket}/", ""),
            file_out,
        )

        return file_out

    download_summary = []
    for file_in, file_out in zip(filenames_in, filenames_out):
        download_summary.append(
            _original_files_file_download(
                endpoint_url, bucket, file_in, file_out
            )
        )
    return download_summary


# /////////////////////////////
# --- Tools
# /////////////////////////////


# Example data_path
# https://s3.waw3-1.cloudferro.com/mdl-native-01/native/NWSHELF_MULTIYEAR_BGC_004_011/cmems_mod_nws_bgc-pft_myint_7km-3D-diato_P1M-m_202105
def parse_original_files_dataset_url(data_path: str) -> Tuple[str, str, str]:
    match = re.search(r"^(http|https):\/\/([\w\-\.]+)(\/.*)", data_path)
    if match:
        endpoint_url = match.group(1) + "://" + match.group(2)
        full_path = match.group(3)
        segments = full_path.split("/")
        bucket = segments[1]
        path = "/".join(segments[2:])
        return endpoint_url, bucket, path
    else:
        raise Exception(f"Invalid data path: {data_path}")


def create_filenames_out(
    filenames_in: list[str],
    overwrite: bool,
    output_directory: pathlib.Path = pathlib.Path("."),
    no_directories=False,
) -> list[pathlib.Path]:
    filenames_out = []
    for filename_in in filenames_in:
        filename_out = output_directory
        if no_directories:
            filename_out = (
                pathlib.Path(filename_out) / pathlib.Path(filename_in).name
            )
        else:
            # filename_in: s3://mdl-native-xx/native/<product-id>...
            filename_out = filename_out / pathlib.Path(
                "/".join(filename_in.split("/")[4:])
            )

        filename_out = get_unique_filename(
            filepath=filename_out, overwrite_option=overwrite
        )

        filenames_out.append(filename_out)
    return filenames_out


def format_file_size(
    size: float, decimals: int = 2, binary_system: bool = False
) -> str:
    if binary_system:
        units: list[str] = [
            "B",
            "KiB",
            "MiB",
            "GiB",
            "TiB",
            "PiB",
            "EiB",
            "ZiB",
        ]
        largest_unit: str = "YiB"
        step: int = 1024
    else:
        units = ["B", "kB", "MB", "GB", "TB", "PB", "EB", "ZB"]
        largest_unit = "YB"
        step = 1000

    for unit in units:
        if size < step:
            return ("%." + str(decimals) + "f %s") % (size, unit)
        size /= step

    return ("%." + str(decimals) + "f %s") % (size, largest_unit)
