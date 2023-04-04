""" pynchon.bin.project
"""
import glob
import json
import os

import pynchon
from pynchon import constants, util
from pynchon.bin import groups, options
from pynchon.util import lme

from .common import kommand

LOGGER = lme.get_logger(__name__)
PARENT = groups.parse


@kommand(
    name="pyright",
    parent=PARENT,
    formatters=dict(markdown=constants.T_TOC_CLI),
    options=[
        # options.file_setupcfg,
        # options.format,
        # options.stdout,
        # options.output,
        # options.header,
    ],
)
def parse_pyright():
    """
    Parses pyright output into a markdown-based report card
    """
    LOGGER.debug("hello pyright")
