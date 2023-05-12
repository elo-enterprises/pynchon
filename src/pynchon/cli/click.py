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
    """

    :param parent: param path:  (Default value = '')
    :param tree: Default value = {})
    :param path:  (Default value = '')

    """
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
    """

    :param g1: click.Group:
    :param g2: click.Group:
    :param g1: click.Group: 
    :param g2: click.Group: 

    """

    def fxn():
        pass

    fxn.__doc__ = g1.help
    tmp = g2.group(g1.name)(fxn)
    for cmd in g1.commands.values():
        tmp.add_command(cmd)


def group_copy(g1:click.Group, **kwargs):
    """

    :param g1: click.Group:
    :param g1:click.Group: 
    :param **kwargs: 

    """
    tmp = [[k,v] for k,v in g1.__dict__.copy().items() if not k.startswith('_')]
    tmp=dict(tmp)
    # [tmp.pop(x) for x in tmp if x.startswith('_')]
    tmp.update(**kwargs)
    return click.Group(**tmp)
    # def fxn():
    #     pass
    #
    # fxn.__doc__ = g1.help
    # tmp = g2.group(g1.name)(fxn)
    # for cmd in g1.commands.values():
    #     tmp.add_command(cmd)
