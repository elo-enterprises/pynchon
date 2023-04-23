""" pynchon.bin.groups:
    Top-level subcommands
"""
from pynchon.util.os import invoke

from .entry import entry
from .common import groop


@groop("gen", parent=entry)
def gen():
    """
    Generate docs
    """


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
