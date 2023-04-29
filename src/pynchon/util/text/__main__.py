""" pynchon.util.text CLI
"""
from pynchon import click
from pynchon.cli import options
from pynchon.util import lme, text, typing
from pynchon.util.os import invoke

LOGGER = lme.get_logger(__name__)


def entry() -> None:
    pass


entry.__doc__ = __doc__ or ""


from .loadf.__main__ import entry as loadf
from .render.__main__ import entry as render

#
# @entry.group('loads')
# def loads() -> None:
#     """load string to ~JSON"""


# @entry.group('loadf')
# def loadf() -> None:
#     """load file-content to ~JSON"""


# @entry.group('json')
# def _json() -> None:
#     """
#     helpers for working with json
#     """


# @cli.group('j2')
# def j2() -> None:
#     """
#     helpers for interacting with `j2`.
#     (assumes j2cli is installed already)
#     """


# entry.add_command(click.Command(json5_load, name='load-json5'))
# loadf.add_command(click.command(json5_load, name='json5'))

# @typing.validate_arguments(arbitrary_types_allowed)
entry = click.group()(entry)

if __name__ == '__main__':
    click.group_copy(render, entry)
    click.group_copy(loadf, entry)
    entry()
