""" pynchon.bin.dot:
    Option parsing for the `dot` subcommands
"""
import os

import click

from pynchon.bin import options
from pynchon.bin.gen import gen_dot as PARENT
from pynchon.util import lme
from pynchon.util.os import invoke

from .common import kommand

LOGGER = lme.get_logger(__name__)
files_arg = click.argument("files", nargs=-1)


@kommand(
    name="files",
    parent=PARENT,
    # formatters=dict(),
    options=[
        # options.file,
        # options.stdout,
        options.script,
        options.templates,
        click.option(
            "--script",
            default=None,
            help=("generates .dot files using script"),
        ),
        click.option(
            "--in-place",
            is_flag=True,
            default=False,
            help=("if true, writes to {file}.json (dropping any other extensions)"),
        ),
    ],
    arguments=[files_arg],
)
def gen_dot_files(files, in_place, templates, script):
    """
    Render .dot files for this project.
    This creates the .dot files themselves; use `pynchon render dot` to convert those to an image.
    """
    assert os.path.exists(script), f"script file @`{script}` is missing!"
    invoke(f"python {script}")
