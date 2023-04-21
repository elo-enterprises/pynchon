""" pynchon.bin.scaffold:
    Option parsing for the `scaffold` subcommand
"""
from pynchon.bin import groups

from .common import groop

PARENT = groups.entry

# @entry.group("scaffold")
@groop("scaffold", parent=groups.entry)
def scaffold():
    """
    Scaffolding Automation
    (Creates folder layouts and other boilerplate)
    """


@scaffold.command("list")
def scaffold_list():
    """list available scaffolds"""


@scaffold.command("stat")
def scaffold_stat():
    """status of current scaffolding"""


@scaffold.command("diff")
def scaffold_diff():
    """diff with known scaffolding"""


@scaffold.command("apply")
def scaffold_apply():
    """apply results of scaffold-plan"""


@scaffold.command("plan")
def scaffold_plan():
    """plan application of scaffolding"""
