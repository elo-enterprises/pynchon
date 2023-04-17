""" pynchon.bin.scaffold:
    Option parsing for the `scaffold` subcommand
"""
import json
import os
import sys

import click
import pyjson5
import yaml

import pynchon
from pynchon import abcs, util
from pynchon.api import render
from pynchon.bin import groups, options

from .common import kommand

PARENT = groups.entry

# @entry.group("scaffold")
@groups.group("scaffold", parent=groups.entry)
def scaffold():
    """
    Scaffolding Automation
    (Creates folder layouts and other boilerplate)
    """


@scaffold.command("list")
def scaffold_list():
    """list available scaffolds"""
