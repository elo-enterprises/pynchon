""" pynchon.util.text CLI
"""
from pynchon.cli import click, common
from pynchon.util import lme, typing

LOGGER = lme.get_logger(__name__)
entry = common.entry_for(__name__)

common.subsume_subs(root='pynchon.util.text', parent=entry)

if __name__ == '__main__':
    entry()
