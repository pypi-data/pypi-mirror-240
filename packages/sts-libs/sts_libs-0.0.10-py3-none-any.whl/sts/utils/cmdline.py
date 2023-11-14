"""cmdline.py: Module to execute a command line."""
import logging

#  Copyright: Contributors to the sts project
#  GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
from typing import Union

from testinfra.backend.base import CommandResult

from sts import host_init

host = host_init()


def run(cmd: str) -> CommandResult:
    logging.debug(f"Running command: '{cmd}'")
    return host.run(cmd)


def run_ret_out(
    cmd: str,
    return_output: bool = False,
) -> Union[int, tuple[int, str]]:
    """Runs cmd and returns rc int or rc int, output str tuple.

    For legacy compatibility only. TODO: remove it an it's usages
    """
    completed_command = host.run(cmd)

    if return_output:
        output = completed_command.stdout if completed_command.stdout else completed_command.stderr
        return completed_command.rc, output.rstrip()  # type: ignore [return-value]

    return completed_command.rc


def exists(cmd: str) -> bool:
    return host.exists(cmd)
