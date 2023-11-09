import pathlib
from typing import Optional

from copernicus_marine_client.core_functions.login import login_function
from copernicus_marine_client.core_functions.utils import (
    DEFAULT_CLIENT_BASE_DIRECTORY,
)


def login(
    username: Optional[str] = None,
    password: Optional[str] = None,
    configuration_file_directory: pathlib.Path = DEFAULT_CLIENT_BASE_DIRECTORY,
    overwrite_configuration_file: bool = False,
) -> bool:
    return login_function(
        username=username,
        password=password,
        configuration_file_directory=configuration_file_directory,
        overwrite_configuration_file=overwrite_configuration_file,
    )
