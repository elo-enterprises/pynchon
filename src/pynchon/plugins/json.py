""" pynchon.plugins.render
"""
from pynchon.util import lme, typing  # noqa

from pynchon import models, abcs

# from pynchon.util.os import invoke

LOGGER = lme.get_logger(__name__)
# from pynchon.util import tagging


# import yaml
# import click
# import pyjson5
# from pynchon import abcs
# from pynchon.api import render
# from pynchon.bin import groups, options
# from pynchon.util import lme
# from pynchon.util.os import invoke
# from .common import kommand
# LOGGER = lme.get_logger(__name__)
# PARENT = groups.render
# files_arg = click.argument("files", nargs=-1)
# from pynchon.util.tagging import tags


# def j5(
#     file,
#     output="",
#     in_place=False,
# ) -> typing.StringMaybe:
#     """renders json5 file"""
#     LOGGER.debug(f"Running with one file: {file}")
#     with open(file, "r") as fhandle:
#         data = text.json5_loads(content=fhandle.read())
#     if in_place:
#         assert not output, "cannot use --in-place and --output at the same time"
#         output = os.path.splitext(file)[0]
#         output = f"{output}.json"
#     if output:
#         with open(output, "w") as fhandle:
#             content = text.to_json(data)
#             fhandle.write(f"{content}\n")
#     return data

# from pynchon.util.text.loadf import __main__ as loadf_main


class Json(models.ToolPlugin):
    """
    Tools for working with JSON & JSON5
    """

    name = 'json'
    priority = -1
    config_class = None
    cli_name = name
    # cli_subsumes: typing.List[typing.Callable] = [
    #     loadf_main.json5,
    #     loadf_main.json,
    #     loadf_main.j5,
    #     # loadf_main.json,
    # ]

    class config_class(abcs.Config):
        config_key = 'json'

    # @tags(click_aliases=['loads',])
    # def json_loads(self):
    #     """ loads JSON from string-input (strict) """

    # @tags(click_aliases=['loadf',])
    # def json_loadf(self):
    #     """ loads JSON from file-input (strict) """
    #     pass

    # def load_json5(self):
    #     """ loads JSON-5 from string-input """
    #     pass
    #
    # def loadf_json5(self):
    #     """ loads JSON-5 from file-input """
    #     pass


# @kommand(
#     name="json5",
#     parent=PARENT,
#     # formatters=dict(),
#     options=[
#         # options.file,
#         # options.stdout,
#         options.output,
#         options.templates,
#         click.option(
#             "--in-place",
#             is_flag=True,
#             default=False,
#             help=("if true, writes to {file}.json (dropping any other extensions)"),
#         ),
#     ],
#     arguments=[files_arg],
# )
# def render_json5(files, output, in_place, templates):
#     """
#     Render JSON5 files -> JSON
#     """
#     assert files, "expected files would be provided"
#     # if file:
#     #     return render.j5(file, output=output, in_place=in_place)
#     # elif files:
#     # files = files.split(' ')
#     LOGGER.debug(f"Running with many: {files}")
#     file = files[0]
#     files = files[1:]
#     return render.j5(file, output=output, in_place=in_place, templates=templates)
#
#
# DEFAULT_OPENER = "open"
#
#
# @kommand(
#     name="any",
#     parent=PARENT,
#     formatters=dict(
#         # markdown=pynchon.T_TOC_CLI,
#     ),
#     options=[
#         # options.file,
#         options.format,
#         # options.stdout,
#         options.output,
#     ],
# )
# def render_any(format, file, stdout, output):
#     """
#     Render files with given renderer
#     """
#     raise NotImplementedError()
