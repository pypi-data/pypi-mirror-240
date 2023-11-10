import logging
from datetime import datetime
from typing import Literal, Optional, Union

import xarray

from copernicus_marine_client.catalogue_parser.request_structure import (
    SubsetRequest,
)

logger = logging.getLogger("copernicus_marine_root_logger")


def build_filename_from_subset_request(
    subset_request: SubsetRequest,
    filename_extension: Literal[".nc", ".zarr"] = ".nc",
) -> str:
    return (
        subset_request.output_filename
        if subset_request.output_filename
        else _build_filename_from_subset_request_parameters(
            subset_request=subset_request,
            filename_extension=filename_extension,
        )
    )


def _build_filename_from_subset_request_parameters(
    subset_request: SubsetRequest,
    filename_extension: Literal[".nc", ".zarr"] = ".nc",
) -> str:
    dataset_id = subset_request.dataset_id or "data"
    variables = subset_request.variables or []
    longitude = _format_coordinates(
        subset_request.minimum_longitude,
        subset_request.maximum_longitude,
        "lon",
    )
    latitude = _format_coordinates(
        subset_request.minimum_latitude, subset_request.maximum_latitude, "lat"
    )
    depth = _format_coordinates(
        subset_request.minimum_depth, subset_request.maximum_depth, "depth"
    )
    datetime = _format_coordinates(
        subset_request.start_datetime, subset_request.end_datetime, "datetime"
    )

    filename = "-".join(
        list(
            filter(
                None,
                [dataset_id, *variables, longitude, latitude, depth, datetime],
            )
        )
    )
    return filename + filename_extension


def _format_coordinates(
    minimum_coordinates: Optional[Union[float, datetime]],
    maximum_coordinates: Optional[Union[float, datetime]],
    coordinate_type: Literal["lon", "lat", "depth", "datetime"],
) -> Optional[str]:
    if minimum_coordinates is None and maximum_coordinates is None:
        return None
    elif minimum_coordinates is not None and maximum_coordinates is None:
        return "min_" + _format_coordinate(
            minimum_coordinates, coordinate_type
        )
    elif minimum_coordinates is None and maximum_coordinates is not None:
        return "max_" + _format_coordinate(
            maximum_coordinates, coordinate_type
        )
    elif minimum_coordinates is not None and maximum_coordinates is not None:
        if coordinate_type == "depth":
            return f"from{minimum_coordinates}to{maximum_coordinates}m"
        elif isinstance(minimum_coordinates, datetime) and isinstance(
            maximum_coordinates, datetime
        ):
            return (
                f"from{minimum_coordinates.strftime('%Y-%m-%dT%H:%M:%S')}"
                f"to{maximum_coordinates.strftime('%Y-%m-%dT%H:%M:%S')}"
            )
        return _format_coordinate(
            minimum_coordinates, coordinate_type
        ) + _format_coordinate(maximum_coordinates, coordinate_type)
    return ""


def _format_coordinate(
    coordinate_value: Union[float, datetime],
    coordinate_type: Literal["lon", "lat", "depth", "datetime"],
) -> str:
    if isinstance(coordinate_value, datetime):
        return f"{coordinate_type}{coordinate_value.strftime('%Y-%m-%dT%H:%M:%S')}"

    formatted_value = f"{coordinate_type}{abs(coordinate_value):.2f}"
    if coordinate_type == "lat":
        suffix = "S" if coordinate_value < 0 else "N"
    elif coordinate_type == "lon":
        suffix = "W" if coordinate_value < 0 else "E"
    elif coordinate_type == "depth":
        suffix = "m"
    else:
        suffix = ""
    return f"{formatted_value}{suffix}"


def get_formatted_dataset_size_estimation(dataset: xarray.Dataset) -> str:
    coordinates_size = 1
    for coordinate in dataset.coords:
        coordinates_size *= dataset[coordinate].size
    estimate_size = (
        coordinates_size
        * len(list(dataset.data_vars))
        * dataset[list(dataset.data_vars)[0]].dtype.itemsize
        / 1048e3
    )
    return f"{estimate_size:.3f} MB"
