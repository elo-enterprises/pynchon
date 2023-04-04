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
    """pynchon CLI:"""
    # ensure that ctx.obj exists and is a dict (in case `cli()` is called
    # by means other than the `if` block below)
    # ctx.ensure_object(dict)


@group("gen", parent=entry)
def gen():
    """Generate docs"""


# def _proj():
#     """ Project subcommands """
# project = group('project', help=_proj.__doc__, parent=entry)(_proj)
# proj = group('proj', help='Alias for `project` subcommand', parent=entry)(_proj)

from .dot import *
from .gen import gen_api, gen_cli


@group("render", parent=entry)
def render():
    """Misc. helpers for rendering text"""


@group("project", parent=entry)
def project():
    """Project automation"""


@group("parse", parent=entry)
def parse():
    """Helpers for parsing output for other tools"""


@group("ast", parent=entry)
def ast():
    """Inspect AST"""
