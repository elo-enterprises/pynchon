""" pynchon.util.text.render CLI
"""
import os
import sys

from pynchon import shimport
from pynchon.cli import click, common, options
from pynchon.util import text, typing, lme
from pynchon.util.text import render as THIS
from pynchon.util.tagging import tags

LOGGER = lme.get_logger(__name__)

entry = common.entry_for(__name__)


tmp = (
    shimport.wrapper('pynchon.util.text.render')
    .prune(
        filter_instances=typing.FunctionType,
    )
    .map_ns(
        lambda _name, fxn: [fxn, tags[fxn].get('click_aliases', []) + [fxn.__name__]]
    )
    .starmap(lambda fxn, aliases: [entry.command(alias)(fxn) for alias in aliases])
)

if __name__ == '__main__':
    entry()
