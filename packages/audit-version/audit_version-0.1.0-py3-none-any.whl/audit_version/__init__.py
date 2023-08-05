# SPDX-FileCopyrightText: 2022 Geoffrey Lentner
# SPDX-License-Identifier: Apache-2.0

"""Initialization and entry-point for console application."""


# type annotations
from __future__ import annotations

# standard libs
import sys
import logging

# external libs
from cmdkit.app import Application
from cmdkit.cli import Interface

# public interface
__all__ = ['AuditVersionApp', 'main', '__version__', '__license__']

# project metadata
__appname__     = 'audit-version'
__version__     = '0.1.0'
__authors__     = 'Geoffrey Lentner'
__contact__     = 'glentner@purdue.edu'
__license__     = 'Apache Software License'
__copyright__   = '2022. All Rights Reserved.'
__website__     = 'https://github.com/glentner/audit-version-py'
__keywords__    = 'version-control semantic-versioning'
__description__ = 'Audit public interface for Python projects and suggest next semantic version'

# initialize application logger
log = logging.getLogger(__name__)


# inject logger setup into command-line framework
Application.log_critical = log.critical
Application.log_exception = log.exception


APP_NAME = __appname__
APP_USAGE = f"""\
usage: {APP_NAME} [-h] [-v] ...
{__description__}\
"""

APP_HELP = f"""\
{APP_USAGE}

options:
-h, --help             Show this message and exit.
-v, --version          Show the version and exit.

Issue tracking at:
{__website__}

Copyright {__copyright__}
{__authors__} <{__contact__}>.\
"""


class AuditVersionApp(Application):
    """Top-level application class for console application."""

    interface = Interface(APP_NAME, APP_USAGE, APP_HELP)
    interface.add_argument('-v', '--version', action='version', version=__version__)

    ALLOW_NOARGS = True

    def run(self: AuditVersionApp) -> None:
        """Business logic for console application (execution starts here)."""
        print('Success')


def main() -> int:
    """Entry-point for console application."""
    return AuditVersionApp.main(sys.argv[1:])
