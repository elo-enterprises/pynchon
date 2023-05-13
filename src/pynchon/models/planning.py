import typing
import collections
from dataclasses import dataclass

from pynchon import app, abcs
from pynchon.fleks import meta

from pynchon.util import lme, typing  # noqa

# from pynchon.fleks.plugin import Plugin as AbstractPlugin
# from pynchon.plugins.util import get_plugin_obj


# from pynchon.util.tagging import tags


@dataclass(frozen=True)
class Goal(metaclass=meta.namespace):
    """ """

    resource: str = "?r"
    command: str = "?c"
    type: str = "?t"
    owner: str = "?o"

    def __rich__(self) -> str:
        from pynchon.util import shfmt

        fmt = shfmt.bash_fmt(self.command)
        return app.Panel(
            app.Syntax(
                f"# {self.command}\n\n{fmt}", "bash", line_numbers=False, word_wrap=True
            ),
            # title=__name__,
            # title=f'[dim italic yellow]{self.type}',
            # title=f'[bold cyan on black]{self.type}',
            title=app.Text(self.type, style="dim bold"),
            title_align="left",
            style=app.Style(
                dim=True,
                # color='green',
                bgcolor="black",
                frame=False,
            ),
            subtitle=app.Text(f"{self.owner}",
            style="dim italic"),
        )

    def __str__(self):
        tmp = abcs.Path(self.resource).absolute().relative_to(abcs.Path('.').absolute())
        return f"<{self.__class__.__name__}[{tmp}]>"


@dataclass(frozen=True)
class Action(metaclass=meta.namespace):
    """ """

    type: str = "unknown_action_type"
    ok:bool = None
    changed:bool=None
    resource: str = "??"
    command: str = "echo"

    @property
    def status_string(self):
        if self.ok is None:
            tmp = 'pending'
        elif self.ok:
            tmp='ok'
        else:
            tmp='failed'
        return tmp

    def __str__(self):
        return f"<{self.__class__.__name__}[{self.status_string}]>"


class Plan(typing.List[Goal], metaclass=meta.namespace):
    """ """

    def __init__(self, *args):
        """

        :param *args:

        """
        for arg in args:
            if not isinstance(arg, (Goal,)):
                err = f"plan can only include goals, got {arg} with type={type(arg)}"
                raise TypeError(err)
            super().__init__(*args)

    def __rich__(self) -> str:
        syntaxes = [
            g.__rich__() for g in self
        ]

        table = app.Table.grid(
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
                # table.add_row(app.Align(app.Emoji("gear"), align='center')),
            ]
            for i, x in enumerate(syntaxes)
        ]

        panel = app.Panel(
            table,
            title=app.Text(f"{self.__class__.__name__}", justify="left", style="italic"),
            title_align="left",
            padding=1,
            style=app.Style(
                dim=True,
                # color='green',
                bgcolor="black",
                frame=False,
            ),
            subtitle=f"(Planned {len(self)} items)"  # subtitle=Text("✔", style='green')
            # if True
            # else Text('❌', style='red'),
        )
        return panel

    @property
    def _dict(self):
        """ """
        result = collections.OrderedDict()
        result["resources"] = list({g.resource for g in self})
        actions_by_type = collections.defaultdict(list)
        for g in self:
            actions_by_type[g.type].append(g.command)
        result.update(**actions_by_type)
        return result

    # @typing.validate_arguments
    def append(self, other: Goal):
        """
        :param other: Goal:
        """
        assert isinstance(other, (Goal,))
        return super().append(other)

    # @typing.validate_arguments
    def extend(self, other):
        """
        :param other:
        """
        assert isinstance(other, (Goal,))
        return super().extend(other)

    # @typing.validate_arguments
    def __add__(self, other):
        """
        :param other:
        """
        assert isinstance(other, (Plan,))
        return Plan(*(other + self))

    __iadd__ = __add__

    def __str__(self):
        return f"<{self.__class__.__name__}[{len(self)} goals]>"


class ApplyResults(typing.List[Action], metaclass=meta.namespace):
    @property
    def ok(self):
        return all([a.ok for a in self])

    @property
    def action_types(self):
        tmp = list({g.type for g in self})
        return {k: [] for k in tmp}

    @property
    def _dict(self):
        """ """
        result = collections.OrderedDict()
        result["ok"] = self.ok
        result["resources"] = list({a.resource for a in self})
        result["actions"] = [g.command for g in self]
        result["action_types"] = self.action_types
        result["changed"] = list({a.resource for a in self if a.changed})
        for g in self:
            result["action_types"][g.type].append(g.resource)
        return result

    def __str__(self):
        return f"<{self.__class__.__name__}[{len(self)} actions]>"
