import pathlib
from datetime import datetime
from typing import List, Optional, Union

import xarray

from copernicus_marine_client.catalogue_parser.request_structure import (
    LoadRequest,
)
from copernicus_marine_client.core_functions.deprecated import (
    deprecated_python_option,
    log_deprecated_message,
)
from copernicus_marine_client.core_functions.deprecated_options import (
    DEPRECATED_OPTIONS,
)
from copernicus_marine_client.download_functions.download_arco_series import (
    open_dataset_from_arco_series,
)
from copernicus_marine_client.download_functions.download_opendap import (
    open_dataset_from_opendap,
)
from copernicus_marine_client.download_functions.subset_parameters import (
    DepthParameters,
    GeographicalParameters,
    LatitudeParameters,
    LongitudeParameters,
    TemporalParameters,
)
from copernicus_marine_client.python_interface.exception_handler import (
    log_exception_and_exit,
)
from copernicus_marine_client.python_interface.load_utils import (
    load_data_object_from_load_request,
)
from copernicus_marine_client.python_interface.utils import homogenize_datetime


@log_exception_and_exit
def load_xarray_dataset(*args, **kwargs):
    """
    Deprecated function, use 'open_dataset' instead.
    """
    log_deprecated_message("load_xarray_dataset", "open_dataset")
    return open_dataset(*args, **kwargs)


@deprecated_python_option(**DEPRECATED_OPTIONS.dict_old_names_to_new_names)
@log_exception_and_exit
def open_dataset(
    dataset_url: Optional[str] = None,
    dataset_id: Optional[str] = None,
    username: Optional[str] = None,
    password: Optional[str] = None,
    variables: Optional[List[str]] = None,
    minimum_longitude: Optional[float] = None,
    maximum_longitude: Optional[float] = None,
    minimum_latitude: Optional[float] = None,
    maximum_latitude: Optional[float] = None,
    minimum_depth: Optional[float] = None,
    maximum_depth: Optional[float] = None,
    vertical_dimension_as_originally_produced: bool = True,
    start_datetime: Optional[Union[datetime, str]] = None,
    end_datetime: Optional[Union[datetime, str]] = None,
    force_service: Optional[str] = None,
    credentials_file: Optional[Union[pathlib.Path, str]] = None,
    overwrite_metadata_cache: bool = False,
    no_metadata_cache: bool = False,
) -> xarray.Dataset:
    """
    Load an xarray dataset from Copernicus Marine data source.

    This function allows loading an xarray dataset from a Copernicus Marine data source
    using either the ARCO series or OpenDAP protocol. It supports various parameters
    for customization, such as specifying geographical bounds, temporal range,
    depth range, and more.

    Args:
        dataset_url (str, optional): The URL of the dataset. Either `dataset_url` or `dataset_id` should be provided.
        dataset_id (str, optional): The ID of the dataset. Either `dataset_url` or `dataset_id` should be provided.
        username (str, optional): Username for authentication, if required.
        password (str, optional): Password for authentication, if required.
        variables (List[str], optional): List of variable names to be loaded from the dataset.
        minimum_longitude (float, optional): The minimum longitude for subsetting the data.
        maximum_longitude (float, optional): The maximum longitude for subsetting the data.
        minimum_latitude (float, optional): The minimum latitude for subsetting the data.
        maximum_latitude (float, optional): The maximum latitude for subsetting the data.
        minimum_depth (float, optional): The minimum depth for subsetting the data.
        maximum_depth (float, optional): The maximum depth for subsetting the data.
        vertical_dimension_as_originally_produced (bool, optional): If True, use the vertical dimension as originally produced.
        start_datetime (datetime, optional): The start datetime for temporal subsetting.
        end_datetime (datetime, optional): The end datetime for temporal subsetting.
        force_service (str, optional): Force the use of a specific service (ARCO or OpenDAP).
        credentials_file (Union[pathlib.Path, str], optional): Path to a file containing authentication credentials.
        overwrite_metadata_cache (bool, optional): If True, overwrite the metadata cache.
        no_metadata_cache (bool, optional): If True, do not use the metadata cache.

    Returns:
        xarray.Dataset: The loaded xarray dataset.
    """  # noqa
    start_datetime = homogenize_datetime(start_datetime)
    end_datetime = homogenize_datetime(end_datetime)
    credentials_file = (
        pathlib.Path(credentials_file) if credentials_file else None
    )
    load_request = LoadRequest(
        dataset_url=dataset_url,
        dataset_id=dataset_id,
        username=username,
        password=password,
        variables=variables,
        geographical_parameters=GeographicalParameters(
            latitude_parameters=LatitudeParameters(
                minimum_latitude=minimum_latitude,
                maximum_latitude=maximum_latitude,
            ),
            longitude_parameters=LongitudeParameters(
                minimum_longitude=minimum_longitude,
                maximum_longitude=maximum_longitude,
            ),
        ),
        temporal_parameters=TemporalParameters(
            start_datetime=start_datetime,
            end_datetime=end_datetime,
        ),
        depth_parameters=DepthParameters(
            minimum_depth=minimum_depth,
            maximum_depth=maximum_depth,
            vertical_dimension_as_originally_produced=vertical_dimension_as_originally_produced,  # noqa
        ),
        force_service=force_service,
        credentials_file=credentials_file,
        overwrite_metadata_cache=overwrite_metadata_cache,
        no_metadata_cache=no_metadata_cache,
    )
    dataset = load_data_object_from_load_request(
        load_request,
        open_dataset_from_arco_series,
        open_dataset_from_opendap,
    )
    return dataset
