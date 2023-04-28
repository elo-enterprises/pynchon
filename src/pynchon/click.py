""" pynchon.click
"""
from click import (  # noqa
    echo,
    argument,
    option,
    version_option,
    command,
    Command,
    group,
    Group,
    Context,
    HelpFormatter,  # noqa
)  # noqa

def group_merge(g1:Group, g2:Group):
    """ """
    def fxn(): pass
    fxn.__doc__ = g1.help
    tmp = g2.group(g1.name)(fxn)
    for cmd in g1.commands.values():
        tmp.add_command(cmd)
group_copy=group_merge
