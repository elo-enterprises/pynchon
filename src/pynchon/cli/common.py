""" pynchon.cli.common:
    Common options/arguments and base classes for CLI
"""
# import io
import json
import functools

import click
from rich import print_json

from pynchon.util import lme, typing

LOGGER = lme.get_logger(__name__)


def load_groups_from_children(root=None, parent=None):
    from pynchon import shimport
    from pynchon.cli import click

    shimport.wrap(root).filter_folder(include_main=True).prune(
        name_is='entry',  # default
    ).map(
        lambda ch: [
            ch.name.replace('.__main__', '').split('.')[-1],
            ch.namespace['entry'],
        ]
    ).starmap(
        lambda name, fxn: [
            setattr(fxn, 'name', name),
            click.group_copy(fxn, parent),
        ]
    )


# from rich.console import Console
# class BetterGroup(click.Group):
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


class handler(object):
    """ """

    priority = -1

    def __init__(self, parent=None):
        self.parent = parent
        self.logger = lme.get_logger(self.__class__.__name__)

    def match(self, call_kwargs):
        """ """
        return False

    def __call__(self, result, **call_kwargs):
        """ """
        return self.handle(result, **call_kwargs)


class stdout_handler(handler):
    """ """

    priority = 9

    def match(self, kwargs):
        """ """
        return "stdout" in kwargs and kwargs["stdout"]

    def handle(self, result, **call_kwargs):
        """ """
        print_json(result)


class output_handler(handler):
    """ """

    priority = 10

    def match(_, kwargs):
        """ """
        return "output" in kwargs and kwargs["output"]

    def handle(self, result, output=None, **call_kwargs) -> None:
        """ """
        if isinstance(result, (str,)):
            self.logger.debug(f"Saving to file: {output}")
            with open(output, "w") as fhandle:
                fhandle.write(result)
        else:
            self.logger.warning(
                f"skipping output_handler; result is not a string! (got {type(result)})"
            )


class format_handler(handler):
    """ """

    def match(_, kwargs):
        """ """
        return "format" in kwargs and kwargs["format"]

    def transform(self, result, format: str = None, **call_kwargs):
        """ """
        if format.lower() == "json":
            warning = "JSON used for `format`; header will be ignored"
            self.logger.warning(warning)
            msg = self.parent.formatters[format](result)
        elif format == "markdown":
            fmt = self.parent.formatters[format]
            if not callable(fmt):
                template = fmt

                def fmt(**kargs):
                    return template.render({**kargs, **result}) + "\n"

            self.logger.debug(f"Dispatching formatter for `markdown` @ {fmt.__name__}")
            self.logger.debug(f"context={result}")
            return fmt(**result)
        else:
            err = f"Unsupported mode for `format`: {format}"
            self.logger.critical(err)
            raise ValueError(err)
        self.logger.debug(f"Transform output: {type(msg)}")
        return msg


def entry_for(
    name,
):
    # from pynchon import shimport
    import importlib

    unf = importlib.import_module(name)
    mdoc = unf.__doc__

    def entry() -> typing.NoneType:
        pass

    entry.__doc__ = (mdoc or "").lstrip()

    class Groop(click.Group):
        pass

    entry = click.group(name.split('.')[-1], cls=Groop)(entry)
    return entry


class kommand(object):
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
    ):
        """ """
        self.name = name
        self.alias = alias
        self.parent = parent or click
        self.options = options
        self.arguments = arguments
        self.formatters = {**formatters, **dict(json=self.format_json)}
        self.transformers = sorted(
            transformers
            + [
                format_handler(parent=self),
            ],
            key=lambda t: t.priority,
        )
        self.handlers = sorted(
            handlers
            + [
                output_handler(parent=self),
                stdout_handler(parent=self),
            ],
            key=lambda h: h.priority,
        )
        click_kwargs = {}
        cls and click_kwargs.update(cls=cls)
        help and click_kwargs.update(help=help.lstrip())
        if not self.is_group:
            self.cmd = self.parent.command(self.name, **click_kwargs)
        else:
            self.cmd = self.parent.group(self.name, **click_kwargs)
        self.cmd.alias = alias
        self.logger = lme.get_logger(f"cmd[{name}]")

    def format_json(self, result):
        """ """
        self.logger.debug("Formatter for: `json`")
        return json.dumps(result, indent=2)

    def wrapper(self, *args, **call_kwargs):
        """ """
        assert self.fxn

        @functools.wraps(self.fxn)
        def newf(*args, **call_kwargs):
            self.logger.debug(f"Invoking {self.parent.name}.{self.name}")
            self.logger.debug(f" with: {call_kwargs}")
            result = self.fxn(*args, **call_kwargs)

            # for tformer in self.transformers:
            #     if tformer.match(call_kwargs):
            #         result = tformer.transform(result, **call_kwargs)
            # for handler in self.handlers:
            #     if handler.match(call_kwargs):
            #         self.logger.debug(f"Handling with `{handler.__class__.__name__}`")
            #         handler.handle(result, **call_kwargs)
            from pynchon.util.text import to_json

            print(to_json(result))
            return result

        return newf

    def __call__(self, fxn: typing.Callable):
        """ """
        self.fxn = fxn
        assert fxn, 'function cannot be None!'
        f = self.cmd(self.wrapper())

        f.help = ' '.join(
            [x.strip() for x in (f.help or fxn.__doc__ or "").split('\n')]
        ).lstrip()

        for opt in self.options:
            f = opt(f)
        for arg in self.arguments:
            f = arg(f)
        # import IPython; IPython.embed()
        # for opt_or_arg in click_params:
        #     f=opt_or_arg(f)
        return f


class groop(kommand):
    is_group = True
