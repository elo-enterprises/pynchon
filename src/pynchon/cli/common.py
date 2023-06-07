""" pynchon.cli.common:
    Common options/arguments and base classes for CLI
"""
import json
import functools

import click

from pynchon import shimport
from pynchon.cli import click

from pynchon.util import lme, text, typing  # noqa

LOGGER = lme.get_logger(__name__)


def load_groups_from_children(root=None, parent=None):
    shimport.wrap(root).filter_folder(include_main=True).prune(
        name_is="entry",  # default
    ).map(
        lambda ch: [
            ch.name.replace(".__main__", "").split(".")[-1],
            ch.namespace["entry"],
        ]
    ).starmap(
        lambda name, fxn: [
            setattr(fxn, "name", name),
            click.group_merge(fxn, parent),
        ]
    )


class handler:
    """ """

    priority = -1

    def __init__(self, parent=None):
        self.parent = parent
        self.logger = lme.get_logger(self.__class__.__name__)

    def match(self, call_kwargs):
        return False

    def __call__(self, result, **call_kwargs):
        return self.handle(result, **call_kwargs)


# class stdout_handler(handler):
#     """ """
#
#     priority = 9
#
#     def match(self, kwargs):
#         return "stdout" in kwargs and kwargs["stdout"]
#
#     def handle(self, result, **call_kwargs):
#         print_json(result)
#
#
# class output_handler(handler):
#     """ """
#
#     priority = 10
#
#     def match(_, kwargs):
#         return "output" in kwargs and kwargs["output"]
#
#     def handle(self, result, output=None, **call_kwargs) -> None:
#         if isinstance(result, (str,)):
#             self.logger.debug(f"Saving to file: {output}")
#             with open(output, "w") as fhandle:
#                 fhandle.write(result)
#         else:
#             self.logger.warning(
#                 f"skipping output_handler; result is not a string! (got {type(result)})"
#             )
#


def entry_for(
    name,
):
    # from pynchon import shimport
    import importlib

    unf = importlib.import_module(name)
    mdoc = unf.__doc__

    def entry() -> typing.NoneType:
        pass

    entry.__doc__ = (mdoc or "").lstrip().split("\n")[0]

    class Groop(click.Group):
        pass

    entry = click.group(name.split(".")[-1], cls=Groop)(entry)
    return entry


class kommand:
    """ """

    is_group = False

    def __init__(
        self,
        name=None,
        parent=None,
        arguments=[],
        alias=None,
        options=[],
        transformers=[],
        handlers=[],
        formatters={},
        cls=None,
        help=None,
        **click_kwargs,
    ):
        self.name = name
        self.alias = alias
        self.parent = parent or click
        self.options = options
        self.arguments = arguments
        self.click_kwargs = click_kwargs
        self.formatters = {**formatters, **dict(json=self.format_json)}
        self.transformers = sorted(
            transformers,
            key=lambda t: t.priority,
        )
        self.handlers = sorted(
            handlers
            + [
                # output_handler(parent=self),
                # stdout_handler(parent=self),
            ],
            key=lambda h: h.priority,
        )
        cls and click_kwargs.update(cls=cls)
        help and click_kwargs.update(help=help.lstrip())
        if not self.is_group:
            self.cmd = self.parent.command(self.name, **click_kwargs)
        else:
            self.cmd = self.parent.group(self.name, **click_kwargs)
        self.cmd.alias = alias
        self.logger = lme.get_logger(f"cmd[{name}]")

    def format_json(self, result):
        """

        :param result:

        """
        self.logger.debug("Formatter for: `json`")
        return json.dumps(result, indent=2)

    def wrapper(self, *args, **call_kwargs):
        assert self.fxn

        @functools.wraps(self.fxn)
        def newf(*args, **call_kwargs):
            self.logger.info(f"Wrapping invocation: {self.parent.name}.{self.name}")
            call_kwargs and self.logger.debug(f" with: {call_kwargs}")
            result = self.fxn(*args, **call_kwargs)
            if result is not None:
                result and LOGGER.info(f"json conversion for type: {type(result)}")
                tmp = text.to_json(result)
                print(tmp)
            return result

        return newf

    def __call__(self, fxn: typing.Callable):
        self.fxn = fxn
        assert fxn, "function cannot be None!"

        f = self.cmd(self.wrapper())
        tmp = [x.strip() for x in (f.help or fxn.__doc__ or "").split("\n")]
        f.help = " ".join(tmp).lstrip()

        for opt in self.options:
            f = opt(f)
        for arg in self.arguments:
            f = arg(f)
        return f


class groop(kommand):
    """# class BetterGroup(click.Group):
    #     def format_usage(self,ctx,formatter):
    #         super(BetterGroup,self).format_usage(ctx,formatter)
    #     def format_epilog(self,ctx,formatter):
    #         return super(BetterGroup,self).format_epilog(ctx,formatter)
    #     def format_help(self, ctx, formatter):
    #         super(BetterGroup,self).format_help(ctx,formatter)
    #     def format_options(self,ctx,formatter):
    #         super(BetterGroup,self).format_options(ctx,formatter)
    #     def format_help_text(self,ctx,formatter):
    #         super(BetterGroup,self).format_help_text(ctx,formatter)


    """

    is_group = True
