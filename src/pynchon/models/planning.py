import typing
import collections

from pynchon import abcs
from pynchon.fleks import meta

# from pynchon.fleks.plugin import Plugin as AbstractPlugin
# from pynchon.plugins.util import get_plugin_obj

from pynchon.util import typing, lme  # noqa

# from pynchon.util.tagging import tags


class Goal(typing.NamedTuple, metaclass=meta.namespace):
    """ """

    resource: str = '??'
    command: str = 'echo'
    type: str = 'unknown'

    def __rich__(self) -> str:
        from pynchon.util import shfmt

        pretty = shfmt.bash_fmt(self.command)
        from rich.syntax import Syntax
        from rich.console import Console

        # console = kwargs.pop('console', None) or Console(stderr=True)
        # result = bash_fmt(*args, **kwargs)
        syntax = Syntax(pretty, 'bash', line_numbers=True)
        return syntax

    def __str__(self):
        return f"<{self.__class__.__name__}[{self.resource}]>"


class Action(typing.NamedTuple, metaclass=meta.namespace):
    """ """

    type: str = 'unknown_action_type'
    result: object = None
    resource: str = '??'
    command: str = 'echo'

    def __str__(self):
        return f"<{self.__class__.__name__}[{self.result}]>"


class Plan(typing.List[Goal], metaclass=meta.namespace):
    """ """

    def __rich__(self) -> str:
        syntaxes = [g.__rich__() for g in self]
        from rich import box
        from rich.text import Text
        from rich.table import Table
        from rich.syntax import Syntax
        from rich.console import Console
        from rich.markdown import Markdown

        table = Table(
            title=f'{self.__class__.__name__}',
            # box=box.MINIMAL_DOUBLE_HEAD,
            expand=True,
        )
        # table.add_column("idx", justify="left", style="bold magenta", no_wrap=True)
        table.add_column("action", justify="left", style="green", no_wrap=True)
        [[table.add_row(x), table.add_row()] for i, x in enumerate(syntaxes)]
        return table

    def __init__(self, *args):
        """ """
        for arg in args:
            if not isinstance(arg, (Goal,)):
                err = f'plan can only include goals, got {arg} with type={type(arg)}'
                raise TypeError(err)
            super(Plan, self).__init__(*args)

    def __str__(self):
        return f"<{self.__class__.__name__}[{len(self)} goals]>"

    @property
    def _dict(self):
        """ """
        result = collections.OrderedDict()
        result['resources'] = list(set([g.resource for g in self]))
        actions_by_type = collections.defaultdict(list)
        for g in self:
            actions_by_type[g.type].append(g.command)
        result.update(**actions_by_type)
        return result

    # @typing.validate_arguments
    def __add__(self, other):
        """ """
        assert isinstance(other, (Plan,))
        return Plan(*(other + self))

    __iadd__ = __add__

    # @typing.validate_arguments
    def append(self, other: Goal):
        """ """
        assert isinstance(other, (Goal,))
        return super(Plan, self).append(other)

    # @typing.validate_arguments
    def extend(self, other):
        """ """
        assert isinstance(other, (Goal,))
        return super(Plan, self).extend(other)


class ApplyResults(typing.List[Action], metaclass=meta.namespace):
    def __str__(self):
        return f"<{self.__class__.__name__}[{len(self)} actions]>"

    @property
    def _dict(self):
        """ """

        def past_tense(x):
            return f"{x}ed"

        result = collections.OrderedDict()
        result['ok'] = all([a.result for a in self])
        result['resources'] = list(set([a.resource for a in self]))
        result['actions'] = [g.command for g in self]
        result['state'] = list(set([g.type for g in self]))
        result['state'] = dict([past_tense(k), []] for k in result['state'])
        for g in self:
            result['state'][past_tense(g.type)].append(g.resource)
        return result
