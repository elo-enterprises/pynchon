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
from pynchon.util.tagging import tags
from pynchon.util.text import __main__ as text_main


class Json(models.ToolPlugin):
    """
    Tools for working with JSON & JSON5
    """
    priority=-1
    name = cli_name = 'json'
    defaults = dict()
    config_kls = None

    @classmethod
    def cli_merge(kls, fxn):
        """ """
        parent = kls.cli_group
        import click
        if isinstance(fxn, click.Command):
            cmd=fxn
            LOGGER.debug(f"attaching command: {fxn}")
            parent.add_command(cmd)
            # LOGGER.debug(f"{parent.commands}")
            return parent
        if isinstance(fxn, click.Group):
            LOGGER.debug(f"attaching group: {fxn}")
            # parent.add_group(fxn)
            raise NotImplementedError("groups are not supported yet")

    @classmethod
    def init_cli(kls):
        """
        """
        import click
        fxns = [
            # NB: these are groups
            # text_main.json5,
            # text_main.json,
            # text_main.j2,

            text_main.json5_load,
            # text_main.json_load,
            text_main.j2_render,
        ]
        for fxn in fxns:
            parent = kls.cli_merge(fxn)
            LOGGER.debug(f"{parent.commands}")
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
