""" pynchon.bin.groups:
    Top-level subcommands
"""
from .entry import entry
from .common import groop

#
# class group(object):
#     """ """
#
#     def __init__(
#         self,
#         name=None,
#         group=None,
#         parent=None,
#     ):
#         self.name = name
#         self.parent = parent
#         self.group = group or (self.parent.group if parent else click.group)
#
#     def wrapper(self, *args, **kargs):
#         result = self.fxn(*args, **kargs)
#         return result
#
#     def __call__(self, fxn):
#         self.fxn = fxn
#         return self.group(self.name)(self.wrapper)
#


@groop("gen", parent=entry)
def gen():
    """
    Generate docs
    """


# def _proj():
#     """ Project subcommands """
# project = group('project', help=_proj.__doc__, parent=entry)(_proj)
# proj = group('proj', help='Alias for `project` subcommand', parent=entry)(_proj)

from pynchon.util.os import invoke

from .dot import *  # noqa
from .gen import gen_api, gen_cli  # noqa


@entry.command("plan")
def plan() -> None:
    """
    shortcut for `pynchon project plan`
    """
    invoke('pynchon project plan', system=True)


@entry.command("config")
def config() -> None:
    """
    shortcut for `pynchon project config`
    """
    invoke('pynchon project config', system=True)


@groop("render", parent=entry)
def render():
    """
    Misc. helpers for rendering text
    """


@groop("project", parent=entry)
def project():
    """
    Project Automation
    """


@groop("parse", parent=entry)
def parse():
    """
    Helpers for parsing output from other tools
    """


@groop("ast", parent=entry)
def ast():
    """
    AST Inspector
    """
