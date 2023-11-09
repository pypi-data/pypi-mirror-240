import logging
import pathlib
from typing import Optional

import click

from copernicus_marine_client.command_line_interface.exception_handler import (
    log_exception_and_exit,
)
from copernicus_marine_client.core_functions.login import login_function
from copernicus_marine_client.core_functions.utils import (
    DEFAULT_CLIENT_BASE_DIRECTORY,
)

logger = logging.getLogger("copernicus_marine_root_logger")


@click.group()
def cli_group_login() -> None:
    pass


@cli_group_login.command(
    "login",
    short_help="Login to the Copernicus Marine Service",
    help="""
    Login to the Copernicus Marine Service.

    Create a configuration file under the $HOME/.copernicus_marine_client directory (overwritable with option --credentials-file).
    """,  # noqa
    epilog="""
    Examples:

    \b
    COPERNICUS_MARINE_SERVICE_USERNAME=<USERNAME> COPERNICUS_MARINE_SERVICE_PASSWORD=<PASSWORD> copernicus-marine login

    \b
    copernicus-marine login --username <USERNAME> --password <PASSWORD>

    \b
    copernicus-marine login
    > Username: [USER-INPUT]
    > Password: [USER-INPUT]
    """,  # noqa
)
@click.option(
    "--username",
    prompt="username",
    hide_input=False,
    help="If not set, search for environment variable"
    + " COPERNICUS_MARINE_SERVICE_USERNAME"
    + ", or else ask for user input",
)
@click.option(
    "--password",
    prompt="password",
    hide_input=True,
    help="If not set, search for environment variable"
    + " COPERNICUS_MARINE_SERVICE_PASSWORD"
    + ", or else ask for user input",
)
@click.option(
    "--configuration-file-directory",
    type=click.Path(path_type=pathlib.Path),
    default=DEFAULT_CLIENT_BASE_DIRECTORY,
    help="Path to the directory where the configuration file is stored",
)
@click.option(
    "--overwrite-configuration-file",
    "-overwrite",
    is_flag=True,
    default=False,
    help="Flag to skip confirmation before overwriting configuration file",
)
@click.option(
    "--verbose",
    type=click.Choice(["DEBUG", "INFO", "WARN", "ERROR", "CRITICAL", "QUIET"]),
    default="INFO",
    help=(
        "Set the details printed to console by the command "
        "(based on standard logging library)."
    ),
)
@log_exception_and_exit
def login(
    username: Optional[str],
    password: Optional[str],
    configuration_file_directory: pathlib.Path,
    overwrite_configuration_file: bool,
    verbose: str = "INFO",
) -> None:
    if verbose == "QUIET":
        logger.disabled = True
        logger.setLevel(level="CRITICAL")
    else:
        logger.setLevel(level=verbose)
    login_function(
        username=username,
        password=password,
        configuration_file_directory=configuration_file_directory,
        overwrite_configuration_file=overwrite_configuration_file,
    )
