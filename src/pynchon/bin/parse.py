""" pynchon.bin.project
"""
import os, glob
import json
import pynchon
from pynchon import (
    util,
)
from .common import kommand
from pynchon.bin import groups, options

LOGGER = pynchon.get_logger(__name__)
PARENT = groups.parse


@kommand(
    name="pyright",
    parent=PARENT,
    formatters=dict(markdown=pynchon.T_TOC_CLI),
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
