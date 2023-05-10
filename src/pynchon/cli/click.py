""" pynchon.click
"""
import click

from click import (  # noqa
    echo,
    pass_context,
    get_current_context,
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


def walk_group(parent, path='', tree={}):
    """ """
    tree = {
        **tree,
        **{
            f"{path} {sub}": sub
            for sub, item in parent.commands.items()
            if isinstance(item, (Command,))
        },
    }
    for sub, item in parent.commands.items():
        if isinstance(item, (Group,)):
            tree.update(**walk_group(item, path=f'{path} {sub}'))
    return tree


def group_merge(g1: click.Group, g2: click.Group):
    """ """

    def fxn():
        pass

    fxn.__doc__ = g1.help
    tmp = g2.group(g1.name)(fxn)
    for cmd in g1.commands.values():
        tmp.add_command(cmd)


group_copy = group_merge
