""" pynchon.util.text CLI
"""
from pynchon import shimport
from pynchon.cli import click, common
from pynchon.util import lme, typing

LOGGER = lme.get_logger(__name__)
entry = common.entry_for(__name__)

from pynchon.util import text as THIS

subs = shimport.module(THIS).filter_folder(
    include_main=True,
    merge_filters=True,
    select=dict(
        name_is='entry',  # default
    ),
)
raise Exception(subs)
for ch in subs:
    setattr(
        THIS,
        ch.name.replace('.__main__', '').split('.')[-1],
        # FIXME: why, access should be safe based on filter
        getattr(ch.module, 'entry', None),
    )

if __name__ == '__main__':
    click.group_copy(THIS.render, entry)
    click.group_copy(THIS.loadf, entry)
    entry()
