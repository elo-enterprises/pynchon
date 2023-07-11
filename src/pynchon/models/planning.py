""" pynchon.models.planning
"""
import typing
import collections

from pynchon import abcs, app
from pynchon.base import BaseModel
from pynchon.fleks import meta

from pynchon.util import lme, typing  # noqa

ResourceType = typing.Union[str, abcs.Path]


class Goal(BaseModel):
    """ """

    class Config(BaseModel.Config):
        exclude: typing.Set[str] = {"udiff"}

    resource: ResourceType = typing.Field(default="?r", required=False)
    command: str = typing.Field(default="?c")
    type: typing.StringMaybe = typing.Field(default=None, required=False)
    owner: typing.StringMaybe = typing.Field(default=None)
    label: typing.StringMaybe = typing.Field(default=None)
    udiff: typing.StringMaybe = typing.Field(default=None)

    def __rich__(self) -> str:
        """ """
        from pynchon import shfmt

        fmt = shfmt.bash_fmt(self.command)
        if self.udiff:
            from rich.markdown import Markdown

            return app.Panel(Markdown(f"```diff\n{self.udiff}\n```"))
        else:
            return app.Panel(
                app.Syntax(
                    fmt,
                    "bash",
                    line_numbers=False,
                    word_wrap=True,
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
                subtitle=app.Text(f"{self.label or self.owner}", style="dim italic"),
            )

    # def __str__(self):
    #     """ """
    #     tmp = abcs.Path(self.resource).absolute().relative_to(abcs.Path(".").absolute())
    #     return f"<{self.__class__.__name__}[{tmp}]>"


class Action(typing.BaseModel):
    """ """

    type: str = typing.Field(default="unknown_action_type")
    ok: bool = typing.Field(default=None)
    changed: bool = typing.Field(default=None)
    resource: ResourceType = typing.Field(default="??")
    command: str = typing.Field(default="echo")

    @property
    def status_string(self):
        if self.ok is None:
            tmp = "pending"
        elif self.ok:
            tmp = "ok"
        else:
            tmp = "failed"
        return tmp

    def __str__(self):
        return f"<{self.__class__.__name__}[{self.status_string}]>"


# class Plan(typing.List[Goal], metaclass=meta.namespace):
class Plan(typing.BaseModel):
    """ """

    goals: typing.List[Goal] = typing.Field(default=[])

    def __contains__(self, g):
        return g in self.goals

    def __len__(self):
        return len(self.goals)

    # def __init__(self, *args, **kwargs):
    #     for arg in args:
    #         if not isinstance(arg, (Goal,)):
    #             err = f"plan can only include goals, got {arg} with type={type(arg)}"
    #             raise TypeError(err)
    #         typing.BaseModel.__init__(self, goals=args)
    #
    def __rich__(self) -> str:
        syntaxes = [g.__rich__() for g in self.goals]

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
            title=app.Text(
                f"{self.__class__.__name__}", justify="left", style="italic"
            ),
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

    #
    # @property
    # def _dict(self):
    #     """ """
    #     result = collections.OrderedDict()
    #     result["resources"] = list({g.resource for g in self})
    #     actions_by_type = collections.defaultdict(list)
    #     for g in self:
    #         actions_by_type[g.type].append(g.command)
    #     result.update(**actions_by_type)
    #     return result
    #
    def append(self, other: Goal):
        """ """
        if other in self:
            return
        elif isinstance(other, (Goal,)):
            self.goals += [other]
        elif isinstance(other, (Plan,)):
            self.goals += other.goals
        elif isinstance(
            other,
            (
                list,
                tuple,
            ),
        ):
            self.goals += other
        else:
            raise NotImplementedError(type(other))

    def __add__(self, other):
        """ """
        if isinstance(other, (Goal,)):
            return Plan(goals=self.goals + [other])
        elif isinstance(other, (Plan,)):
            return Plan(goals=self.goals + other.goals)
        elif isinstance(
            other,
            (
                list,
                tuple,
            ),
        ):
            return Plan(goals=self.goals + other)
        else:
            raise NotImplementedError(type(other))

    __iadd__ = __add__

    # def __str__(self):
    #     return f"<{self.__class__.__name__}[{len(self)} goals]>"


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


# from pynchon.util.text import dumps
# dumps.JSONEncoder.register_encoder(type=Plan,)
