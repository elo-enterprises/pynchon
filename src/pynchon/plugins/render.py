""" pynchon.plugins.render
"""
from pynchon import models
from pynchon.util import lme, typing

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


class Renderers(models.CliAliases):
    """
    Namespace for rendering commands from other plugins
    """

    name = cli_name = 'render'
    defaults = dict()
    config_kls = None
    cli_includes: typing.List[typing.Callable] = []


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
#     name="dot",
#     parent=PARENT,
#     options=[
#         options.output,
#         click.option(
#             "--open",
#             "open_after",
#             is_flag=True,
#             default=False,
#             help=(f"if true, opens the created file using {DEFAULT_OPENER}"),
#         ),
#         click.option(
#             "--in-place",
#             is_flag=True,
#             default=False,
#             help=("if true, writes to {file}.png (dropping any other extensions)"),
#         ),
#     ],
#     arguments=[files_arg],
# )
# def render_dot(files, output, in_place, open_after):
#     """
#     Render dot file (graphviz) -> PNG
#     """
#     assert files, "expected files would be provided"
#     # if file:
#     #     return render.j5(file, output=output, in_place=in_place)
#     # elif files:
#     # files = files.split(' ')
#     LOGGER.debug(f"Running with many: {files}")
#     file = files[0]
#     files = files[1:]
#     result = render.dot(file, output=output, in_place=in_place)
#     output = result["output"]
#     if open_after:
#         LOGGER.debug(f"opening {output} with {DEFAULT_OPENER}")
#         invoke(f"{DEFAULT_OPENER} {output}")
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
#
#
# @kommand(
#     name="jinja",
#     parent=PARENT,
#     options=[
#         # options.file,
#         options.ctx,
#         options.output,
#         options.template,
#         click.option(
#             "--in-place",
#             is_flag=True,
#             default=False,
#             help=(
#                 "if true, writes to {file}.{ext} "
#                 "(dropping any .j2 extension if present)"
#             ),
#         ),
#     ],
#     arguments=[files_arg],
# )
# def render_j2(files, ctx, output, in_place, templates):
#     """
#     Render J2 files with given context
#     """
#     templates = templates.split(",")
#     assert isinstance(templates, (list, tuple)), f"expected list got {type(templates)}"
#     # assert (file or files) and not (file and files), 'expected files would be provided'
#     from pynchon import config
#
#     templates = templates + config.jinja.includes
#     if ctx:
#         if "{" in ctx:
#             LOGGER.debug("context is inlined JSON")
#             ctx = json.loads(ctx)
#         elif "=" in ctx:
#             LOGGER.debug("context is inlined (comma-separed k=v format)")
#             ctx = dict([kv.split("=") for kv in ctx.split(",")])
#         else:
#             with open(ctx, "r") as fhandle:
#                 content = fhandle.read()
#             if ctx.endswith(".json"):
#                 LOGGER.debug("context is JSON file")
#                 ctx = json.loads(content)
#             elif ctx.endswith(".json5"):
#                 LOGGER.debug("context is JSON-5 file")
#                 ctx = pyjson5.loads(content)
#             elif ctx.endswith(".yml") or ctx.endswith(".yaml"):
#                 LOGGER.debug("context is yaml file")
#                 ctx = yaml.loads(content)
#             else:
#                 raise TypeError(f"not sure how to load: {ctx}")
#     else:
#         ctx = {}
#     LOGGER.debug("user-defined context: ")
#     LOGGER.debug(json.dumps(ctx, cls=abcs.JSONEncoder))
#     if files:
#         return [
#             render.j2(
#                 file, ctx=ctx, output=output, in_place=in_place, templates=templates
#             )
#             for file in files
#         ]
#     # elif files:
#     #     LOGGER.debug(f"Running with many: {files}")
#     #     return [
#     #         render.j2(file, output=output, in_place=in_place, templates=templates)
#     #         for file in files ]
