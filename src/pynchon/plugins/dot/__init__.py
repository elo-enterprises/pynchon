""" pynchon.plugins.dot
"""
from pynchon.util import files, lme, typing
from pynchon.abcs.plugin import Plugin

LOGGER = lme.get_logger(__name__)


class Dot(Plugin):
    """ """

    name = "dot"
    # config= DotConfig
    config_kls = dict
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

    @classmethod
    def init_cli(kls):
        """pynchon.bin.dot:
        Option parsing for the `dot` subcommands
        """
        import os

        import click

        from pynchon.bin import options, groups
        from pynchon.util import lme
        from pynchon.util.os import invoke
        from pynchon.bin.common import groop, kommand

        # from pynchon.plugins.base import Base

        @groop("dot", parent=groups.gen)
        def gen_dot():
            """
            Generate .dot files
            """

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
