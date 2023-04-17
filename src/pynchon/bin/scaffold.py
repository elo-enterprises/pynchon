""" pynchon.bin.scaffold:
    Option parsing for the `scaffold` subcommand
"""
from pynchon.bin import groups

PARENT = groups.entry

# @entry.group("scaffold")
@groups.group("scaffold", parent=groups.entry)
def scaffold():
    """
    Scaffolding Automation
    (Creates folder layouts and other boilerplate)
    """


@scaffold.command("list")
def scaffold_list():
    """list available scaffolds"""
