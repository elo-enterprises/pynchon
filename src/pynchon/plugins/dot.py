""" pynchon.plugins.dot
"""
import os

import click

from pynchon.bin import options
from pynchon.util import lme
from pynchon.util.os import invoke
from pynchon.bin.common import kommand
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
from pynchon import abcs, models
from pynchon.util import files, lme, typing

LOGGER = lme.get_logger(__name__)

class Dot(models.Planner):
    """Tools for rendering graphviz dot files"""

    name = "dot"

    class config_kls(abcs.Config):
        config_key = 'dot'

    defaults = dict()

    def plan(self, config) -> typing.List[str]:
        plan = super(self.__class__, self).plan(config)
        # render_instructions = self.render_instructions
        # if "dot" in render_instructions:
        self.logger.debug("planning for rendering for .dot graph files..")
        dot_root = config.project["root"]
        for line in files.find_suffix(root=dot_root, suffix="dot"):
            line = line.strip()
            if not line:
                continue
            plan += [f"pynchon render dot {line} --in-place"]
        # if "dot" in self.gen_instructions:
        self.logger.debug("planning generation for .dot graph files..")
        dot_config = config["pynchon"].get("dot", {})
        script = dot_config.get("script")
        # # assert script, '`"dot" in pynchon.generate` but pynchon.dot.script is not set!'
        # from pynchon.api import render
        #
        # # FIXME: do this substition everywhere!
        # script = render._render(text=script, context=config)
        cmd = "pynchon gen dot files --script {script}"
        plan += [cmd]
        return plan

    @staticmethod
    def init_cli(kls):
        """
        Option parsing for the `dot` subcommands
        """
        gen_dot = plugin_sub = models.CliPlugin.init_cli(kls)

        LOGGER = lme.get_logger(__name__)
        files_arg = click.argument("files", nargs=-1)

        @kommand(
            name="files",
            parent=gen_dot,
            # formatters=dict(),
            options=[
                # options.file,
                # options.stdout,
                options.script,
                options.templates,
                click.option(
                    "--script",
                    default=None,
                    help=("generates .dot files using script"),
                ),
                click.option(
                    "--in-place",
                    is_flag=True,
                    default=False,
                    help=(
                        "if true, writes to {file}.json (dropping any other extensions)"
                    ),
                ),
            ],
            arguments=[files_arg],
        )
        def gen_dot_files(files, in_place, templates, script):
            """
            Render .dot files for this project.
            This creates the .dot files themselves; use `pynchon render dot` to convert those to an image.
            """
            assert os.path.exists(script), f"script file @`{script}` is missing!"
            invoke(f"python {script}")
