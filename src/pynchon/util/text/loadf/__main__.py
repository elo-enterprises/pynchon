""" pynchon.util.text.loadf CLI
"""
import os
import sys

from pynchon import click, abcs
from pynchon.cli import options
from pynchon.util import text, typing, lme

LOGGER = lme.get_logger(__name__)
from pynchon.util.os import invoke
from . import json5_load

def entry() -> None: pass
entry.__doc__ = (__doc__ or "")

@click.argument("files", nargs=-1)
def json_load(
    files: typing.List[str],
) -> None:
    """
    loads json5 file(s) and outputs json.
    if multiple files are provided, files will
    be merged with overwrites in the order provided
    """
    out: typing.Dict[str, typing.Any] = {}
    for file in files:
        obj = text.loadf_json(file=file)
        out = {**out, **obj}
    print(text.to_json(out))

entry = click.group('loadf')(entry)
entry.command('json')(json_load)
entry.command('json5')(json5_load)
entry.command('j5')(json5_load)

if __name__ == '__main__':
    entry()
