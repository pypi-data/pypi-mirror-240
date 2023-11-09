import logging
import pathlib
from datetime import datetime
from importlib.metadata import version
from typing import Callable, Iterable, Iterator, Optional, TypeVar

import xarray
from requests import PreparedRequest

logger = logging.getLogger("copernicus_marine_root_logger")

OVERWRITE_SHORT_OPTION = "--overwrite"
OVERWRITE_LONG_OPTION = "--overwrite-output-data"
OVERWRITE_OPTION_HELP_TEXT = (
    "If specified and if the file already exists on destination, then it will be "
    "overwritten instead of creating new one with unique index."
)

FORCE_DOWNLOAD_CLI_PROMPT_MESSAGE = "Do you want to proceed with download?"

DEFAULT_CLIENT_BASE_DIRECTORY = (
    pathlib.Path.home() / ".copernicus-marine-client"
)

# Client name, to be used in custom query parameters for each request to MDS S3
# endpoints, in order to track statistics of usage
CLIENT_NAME = "copernicus-marine-client"

DATETIME_SUPPORTED_FORMATS = [
    "%Y",
    "%Y-%m-%d",
    "%Y-%m-%dT%H:%M:%S",
    "%Y-%m-%d %H:%M:%S",
    "%Y-%m-%dT%H:%M:%S.%fZ",
]


def get_unique_filename(
    filepath: pathlib.Path, overwrite_option: bool
) -> pathlib.Path:
    if not overwrite_option:
        parent = filepath.parent
        filename = filepath.stem
        extension = filepath.suffix
        counter = 1

        while filepath.exists():
            filepath = parent / (
                filename + "_(" + str(counter) + ")" + extension
            )
            counter += 1

    return filepath


_T = TypeVar("_T")
_S = TypeVar("_S")


def map_reject_none(
    function: Callable[[_S], Optional[_T]], iterable: Iterable[_S]
) -> Iterable[_T]:
    return (element for element in map(function, iterable) if element)


def next_or_raise_exception(
    iterator: Iterator[_T], exception_to_raise: Exception
) -> _T:
    try:
        return next(iterator)
    except Exception as exception:
        raise exception_to_raise from exception


def flatten(list: list[list[_T]]) -> list[_T]:
    return [item for sublist in list for item in sublist]


def construct_url_with_query_params(url, query_params: dict) -> Optional[str]:
    req = PreparedRequest()
    req.prepare_url(url, query_params)
    return req.url


def construct_query_params_for_marine_data_store_monitoring(
    username: Optional[str] = None,
) -> dict:
    query_params = {"x-cop-client": CLIENT_NAME}
    if username:
        query_params["x-cop-user"] = username
    return query_params


class WrongDatetimeFormat(Exception):
    ...


def datetime_parser(string: str):
    for format in DATETIME_SUPPORTED_FORMATS:
        try:
            return datetime.strptime(string, format)
        except ValueError:
            pass
    raise WrongDatetimeFormat(string)


def add_copernicus_marine_client_version_in_dataset_attributes(
    dataset: xarray.Dataset,
) -> xarray.Dataset:
    dataset.attrs["copernicus_marine_client_version"] = version(
        "copernicus-marine-client"
    )
    return dataset
