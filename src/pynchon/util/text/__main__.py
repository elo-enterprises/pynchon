""" pynchon.util.text CLI
"""
from pynchon import shimport
from pynchon.cli import click, common
from pynchon.util import lme, typing

LOGGER = lme.get_logger(__name__)
entry = common.entry_for(__name__)

registry = (
    shimport.wrap('pynchon.util.text')
    .filter_folder(include_main=True)
    .prune(
        name_is='entry',  # default
    )
    .map(
        lambda ch: [
            ch.name.replace('.__main__', '').split('.')[-1],
            ch.namespace['entry'],
        ]
    )
    .starmap(
        lambda name, fxn: [
            setattr(fxn, 'name', name),
            click.group_copy(fxn, entry),
        ]
    )
)

if __name__ == '__main__':
    entry()
