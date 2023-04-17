""" pynchon.bin.gen:
    Option parsing for the `gen` subcommand
"""
# from pynchon.api import render
from pynchon.bin import groups

PARENT = groups.gen


@groups.group("api", parent=PARENT)
def gen_api():
    """
    Generate API docs from python modules, packages, etc
    """


@groups.group("fixme", parent=PARENT)
def gen_fixme():
    """
    Generate FIXME.md files, aggregating references to all FIXME's in code-base
    """


@groups.group("dot", parent=PARENT)
def gen_dot():
    """
    Generate .dot files
    """


@groups.group("cli", parent=PARENT)
def gen_cli():
    """Generate CLI docs"""
