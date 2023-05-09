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

    resource: str = '?r'
    command: str = '?c'
    type: str = '?t'
    owner: str = '?o'

    def __rich__(self) -> str:
        from rich.text import Text
        from rich.emoji import Emoji
        from rich.panel import Panel
        from rich.style import Style
        from rich.syntax import Syntax
        from rich.console import Console

        from pynchon.util import shfmt

        fmt = shfmt.bash_fmt(self.command)
        return Panel(
            Syntax(
                f"# {self.command}\n\n{fmt}", 'bash', line_numbers=False, word_wrap=True
            ),
            # title=__name__,
            # title=f'[dim italic yellow]{self.type}',
            # title=f'[bold cyan on black]{self.type}',
            title=Text(self.type, style='dim bold'),
            title_align='left',
            style=Style(
                dim=True,
                # color='green',
                bgcolor='black',
                frame=False,
            ),
            subtitle=Text(f'{self.owner}', style='dim italic'),
        )

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
        from rich.align import Align
        from rich.emoji import Emoji
        from rich.style import Style
        from rich.table import Table
        from rich.syntax import Syntax
        from rich.console import Console
        from rich.markdown import Markdown

        table = Table.grid(
            # title=f'{__name__} ({len(self)} items)',
            # subtitle='...',
            # box=box.MINIMAL_DOUBLE_HEAD,
            expand=True,
            # border_style='dim italic yellow'
            # border_style='bold dim',
        )
        [
            [
                table.add_row(x),
                # table.add_row(Align(Emoji("gear"), align='center')),
            ]
            for i, x in enumerate(syntaxes)
        ]
        from rich.text import Text
        from rich.panel import Panel

        panel = Panel(
            table,
            title=Text(f'{__name__}', justify='left', style='italic'),
            title_align='left',
            padding=1,
            style=Style(
                dim=True,
                # color='green',
                bgcolor='black',
                frame=False,
            ),
            subtitle=f'(Planned {len(self)} items)'  # subtitle=Text("✔", style='green')
            # if True
            # else Text('❌', style='red'),
        )
        return panel

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
