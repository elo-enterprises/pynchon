""" pynchon.util.files CLI
"""
from pynchon.util import typing, lme  # noqa
from pynchon.cli import click, common, options  # noqa
from pynchon.util.tagging import tags

LOGGER = lme.get_logger(__name__)

from pynchon import shimport

entry = common.entry_for(__name__)


tmp = (
    shimport.wrapper('pynchon.util.files')
    .prune(
        filter_instances=typing.FunctionType,
        filter_module_origin='pynchon.util.files',
    )
    .map_ns(
        lambda _name, fxn: [fxn, tags[fxn].get('click_aliases', []) + [fxn.__name__]]
    )
    .starmap(
        lambda fxn, aliases: [
            entry.command(
                name=alias.replace('_', '-'),
                help=(
                    fxn.__doc__
                    if alias == fxn.__name__
                    else f'alias for `{fxn.__name__}`'
                ),
            )(fxn)
            for alias in aliases
        ]
    )
)

if __name__ == '__main__':
    entry()