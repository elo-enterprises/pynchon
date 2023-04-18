""" pynchon.bin.gen:
    Option parsing for the `gen` subcommand
"""
from pynchon import constants
from pynchon.bin import groups

# from pynchon.api import render
from pynchon.util import lme

from . import options

PARENT = groups.gen

LOGGER = lme.get_logger(__name__)


@groups.group("api", parent=PARENT)
def gen_api() -> None:
    """
    Generate API docs from python modules, packages, etc
    """


import click

from pynchon.bin.common import kommand


@kommand(
    name="fixme",
    parent=groups.gen,
    formatters=dict(markdown=constants.T_FIXME),
    options=[
        options.format_markdown,
        click.option(
            "--output",
            "-o",
            default="docs/FIXME.md",
            help=("output file to write.  (optional)"),
        ),
        options.stdout,
        options.header,
    ],
)
def gen_fixme(output, format, stdout, header):
    """
    Generate FIXME.md files, aggregating references to all FIXME's in code-base
    """
    from pynchon.api import project
    from pynchon.util.os import invoke

    config = project.get_config()
    src_root = config.pynchon['src_root']
    exclude_patterns = config.pynchon.get('exclude_patterns', [])
    cmd = invoke(f'grep --line-number -R FIXME {src_root}')
    assert cmd.succeeded
    items = []
    for line in cmd.stdout.split('\n'):
        line = line.strip()
        if not line or line.startswith('Binary file'):
            continue
        bits = line.split(":")
        file = bits.pop(0)
        line_no = bits.pop(0)
        items.append(dict(file=file, line=':'.join(bits), line_no=line_no))
    return dict(items=items)


@groups.group("dot", parent=PARENT)
def gen_dot():
    """
    Generate .dot files
    """


@groups.group("cli", parent=PARENT)
def gen_cli():
    """Generate CLI docs"""
