""" pynchon.bin.groups:
    Top-level subcommands
"""
from pynchon.util.os import invoke

from .entry import entry
from .common import groop



# @entry.command("plan")
# def plan() -> None:
#     """
#     shortcut for `pynchon project plan`
#     """
#     invoke('pynchon project plan', system=True)
