""" pynchon.util.text CLI
"""
from pynchon import shimport
from pynchon.cli import click, common
from pynchon.util import lme, typing

LOGGER = lme.get_logger(__name__)
entry = common.entry_for(__name__)

from pynchon.util import text as THIS

for ch in shimport.wrap(THIS).filter_folder(
    include_main=True,
    prune=dict(
        name_is='entry',  # default
    )
):
    that = ch.namespace['entry']
    that.name = ch.name.replace('.__main__', '').split('.')[-1]
    click.group_copy(that, entry)

if __name__ == '__main__':
    entry()
