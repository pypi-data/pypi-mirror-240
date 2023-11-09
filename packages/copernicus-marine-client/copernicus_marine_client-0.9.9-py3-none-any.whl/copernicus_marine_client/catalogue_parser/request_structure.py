import fnmatch
import logging
import pathlib
from dataclasses import dataclass, field
from datetime import datetime
from json import load
from typing import Any, Dict, List, Optional

from copernicus_marine_client.core_functions.deprecated_options import (
    DEPRECATED_OPTIONS,
)
from copernicus_marine_client.core_functions.utils import datetime_parser
from copernicus_marine_client.download_functions.subset_parameters import (
    DepthParameters,
    GeographicalParameters,
    TemporalParameters,
)

logger = logging.getLogger("copernicus_marine_root_logger")


@dataclass
class DatasetTimeAndGeographicalSubset:
    minimum_longitude: Optional[float] = None
    maximum_longitude: Optional[float] = None
    minimum_latitude: Optional[float] = None
    maximum_latitude: Optional[float] = None
    start_datetime: Optional[datetime] = None
    end_datetime: Optional[datetime] = None


@dataclass
class SubsetRequest:
    dataset_url: Optional[str] = None
    dataset_id: Optional[str] = None
    variables: Optional[List[str]] = None
    minimum_longitude: Optional[float] = None
    maximum_longitude: Optional[float] = None
    minimum_latitude: Optional[float] = None
    maximum_latitude: Optional[float] = None
    minimum_depth: Optional[float] = None
    maximum_depth: Optional[float] = None
    vertical_dimension_as_originally_produced: bool = True
    start_datetime: Optional[datetime] = None
    end_datetime: Optional[datetime] = None
    output_filename: Optional[pathlib.Path] = None
    force_service: Optional[str] = None
    output_directory: pathlib.Path = pathlib.Path(".")
    force_download: bool = False
    overwrite_output_data: bool = False

    def update(self, new_dict: dict):
        """Method to update values in SubsetRequest object.
        Skips "None" values
        """
        for key, value in new_dict.items():
            if value is None or (
                isinstance(value, (list, tuple)) and len(value) < 1
            ):
                pass
            else:
                self.__dict__.update({key: value})

    def enforce_types(self):
        type_enforced_dict = {}
        for key, value in self.__dict__.items():
            if key in [
                "minimum_longitude",
                "maximum_longitude",
                "minimum_latitude",
                "maximum_latitude",
                "minimum_depth",
                "maximum_depth",
            ]:
                new_value = float(value) if value is not None else None
            elif key in [
                "start_datetime",
                "end_datetime",
            ]:
                new_value = datetime_parser(value) if value else None
            elif key in ["force_download"]:
                new_value = (
                    True if value in [True, "true", "True", 1] else False
                )
            elif key in ["variables"]:
                new_value = list(value) if value is not None else None
            elif key in ["output_filename", "output_directory"]:
                new_value = pathlib.Path(value) if value is not None else None
            else:
                new_value = str(value) if value else None
            type_enforced_dict[key] = new_value
        self.__dict__.update(type_enforced_dict)

    def from_file(self, filepath: pathlib.Path):
        self.update(subset_request_from_file(filepath).__dict__)
        return self

    def get_time_and_geographical_subset(
        self,
    ) -> DatasetTimeAndGeographicalSubset:
        return DatasetTimeAndGeographicalSubset(
            minimum_longitude=self.minimum_longitude,
            maximum_longitude=self.maximum_longitude,
            minimum_latitude=self.minimum_latitude,
            maximum_latitude=self.maximum_latitude,
            start_datetime=self.start_datetime,
            end_datetime=self.end_datetime,
        )


def subset_request_from_file(filepath: pathlib.Path) -> SubsetRequest:
    json_file = open(filepath)
    json_content = load(json_file)

    json_with_deprecated_options_replace = {}

    for key, val in json_content.items():
        if key in DEPRECATED_OPTIONS:
            deprecated_option = DEPRECATED_OPTIONS[key]
            json_with_deprecated_options_replace[
                deprecated_option.new_name
            ] = val
        else:
            json_with_deprecated_options_replace[key] = val

    subset_request = SubsetRequest()
    subset_request.__dict__.update(json_with_deprecated_options_replace)
    subset_request.enforce_types()
    return subset_request


def convert_motu_api_request_to_structure(
    motu_api_request: str,
) -> SubsetRequest:
    prefix = "python -m motuclient "
    string = motu_api_request.replace(prefix, "").replace("'", "")
    arguments = [
        substr.strip() for substr in string.split("--")[1:]
    ]  # for subsubstr in substr.split(" ", maxsplit=1)]
    arg_value_tuples = [
        tuple(substr.split(" ", maxsplit=1)) for substr in arguments
    ]
    motu_api_request_dict: Dict[str, Any] = {}
    for arg, value in arg_value_tuples:
        if arg == "variable":
            # special case for variable, since it can have multiple values
            motu_api_request_dict.setdefault(arg, []).append(value)
        else:
            motu_api_request_dict[arg] = value
    subset_request = SubsetRequest(
        output_directory=pathlib.Path("."),
        force_download=False,
        output_filename=None,
        force_service=None,
    )
    conversion_dict = {
        "product-id": "dataset_id",
        "latitude-min": "minimum_latitude",
        "latitude-max": "maximum_latitude",
        "longitude-min": "minimum_longitude",
        "longitude-max": "maximum_longitude",
        "depth-min": "minimum_depth",
        "depth-max": "maximum_depth",
        "date-min": "start_datetime",
        "date-max": "end_datetime",
        "variable": "variables",
    }
    for key, value in motu_api_request_dict.items():
        if key in conversion_dict.keys():
            subset_request.__dict__.update({conversion_dict[key]: value})
    subset_request.enforce_types()
    return subset_request


@dataclass
class GetRequest:
    dataset_url: Optional[str] = None
    dataset_id: Optional[str] = None
    no_directories: bool = False
    show_outputnames: bool = False
    output_directory: str = "."
    force_download: bool = False
    overwrite_output_data: bool = False
    force_service: Optional[str] = None
    filter: Optional[str] = None
    regex: Optional[str] = None

    def update(self, new_dict: dict):
        """Method to update values in GetRequest object.
        Skips "None" values
        """
        for key, value in new_dict.items():
            if value is None:
                pass
            else:
                self.__dict__.update({key: value})

    def enforce_types(self):
        type_enforced_dict = {}
        for key, value in self.__dict__.items():
            if key in [
                "no_directories",
                "show_outputnames",
                "force_download",
            ]:
                new_value = bool(value) if value is not None else None
            else:
                new_value = str(value) if value else None
            type_enforced_dict[key] = new_value
        self.__dict__.update(type_enforced_dict)

    def from_file(self, filepath: pathlib.Path):
        self = get_request_from_file(filepath)
        logger.info(filepath)
        return self


def get_request_from_file(filepath: pathlib.Path) -> GetRequest:
    json_file = open(filepath)
    get_request = GetRequest()
    get_request.__dict__.update(load(json_file))
    get_request.enforce_types()
    if get_request.filter:
        if get_request.regex:
            get_request.regex = (
                "("
                + get_request.regex
                + "|"
                + fnmatch.translate(get_request.filter)
                + ")"
            )
        else:
            get_request.regex = fnmatch.translate(get_request.filter)
    return get_request


@dataclass
class LoadRequest:
    dataset_url: Optional[str] = None
    dataset_id: Optional[str] = None
    username: Optional[str] = None
    password: Optional[str] = None
    variables: Optional[List[str]] = None
    geographical_parameters: GeographicalParameters = field(
        default_factory=GeographicalParameters
    )
    temporal_parameters: TemporalParameters = field(
        default_factory=TemporalParameters
    )
    depth_parameters: DepthParameters = field(default_factory=DepthParameters)
    force_service: Optional[str] = None
    credentials_file: Optional[pathlib.Path] = None
    overwrite_metadata_cache: bool = False
    no_metadata_cache: bool = False

    def get_time_and_geographical_subset(
        self,
    ) -> DatasetTimeAndGeographicalSubset:
        return DatasetTimeAndGeographicalSubset(
            minimum_longitude=self.geographical_parameters.longitude_parameters.minimum_longitude,  # noqa
            maximum_longitude=self.geographical_parameters.longitude_parameters.maximum_longitude,  # noqa
            minimum_latitude=self.geographical_parameters.latitude_parameters.minimum_latitude,  # noqa
            maximum_latitude=self.geographical_parameters.latitude_parameters.maximum_latitude,  # noqa
            start_datetime=self.temporal_parameters.start_datetime,
            end_datetime=self.temporal_parameters.end_datetime,
        )
