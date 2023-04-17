""" pynchon.bin.groups:
    Top-level subcommands
"""
import functools

import click


class group(object):
    """ """

    def __init__(
        self,
        name=None,
        group=None,
        parent=None,
    ):
        self.name = name
        self.parent = parent
        self.group = group or (self.parent.group if parent else click.group)

    def wrapper(self, *args, **kargs):
        result = self.fxn(*args, **kargs)
        return result

    def __call__(self, fxn):
        self.fxn = fxn
        return self.group(self.name)(self.wrapper)


@click.version_option()
@click.group("pynchon")
def entry():
    """pynchon: a utility for docs generation and template-rendering"""


@group("gen", parent=entry)
def gen():
    """
    Generate docs
    """


# def _proj():
#     """ Project subcommands """
# project = group('project', help=_proj.__doc__, parent=entry)(_proj)
# proj = group('proj', help='Alias for `project` subcommand', parent=entry)(_proj)

from .dot import *
from .gen import gen_api, gen_cli


@entry.command("plan")
def plan() -> None:
    """
    shortcut for `pynchon project plan`
    """
    raise NotImplementedError()


@entry.command("config")
def config() -> None:
    """
    shortcut for `pynchon project config`
    """
    raise NotImplementedError()


@group("render", parent=entry)
def render():
    """
    Misc. helpers for rendering text
    """


@group("project", parent=entry)
def project():
    """
    Project Automation
    """


@group("parse", parent=entry)
def parse():
    """
    Helpers for parsing output from other tools
    """


@group("ast", parent=entry)
def ast():
    """
    AST Inspector
    """
