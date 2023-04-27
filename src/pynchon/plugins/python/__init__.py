""" pynchon.config.python
"""
import os

import click

from pynchon import constants, util, models
from pynchon.bin import options, common
from pynchon.util import lme, typing
from pynchon.plugins.base import Base

from .config import PythonConfig, PyPiConfig, PythonCliConfig

LOGGER = lme.get_logger(__name__)


class Python(models.ContextPlugin):
    """context-provider: python-platform"""

    priority = 2
    name = 'python'
    defaults = dict()
    config_kls = PythonConfig


class PythonCLI(models.Planner):
    """tools for generating CLI docs"""

    name = "python-cli"
    defaults = dict()
    config_kls = PythonCliConfig

    @staticmethod
    def init_cli(kls):
        """pynchon.bin.cli:
        Option parsing for the `cli` subcommand
        """

        # @common.kommand(
        #     name="toc",
        #     parent=Base.gen_cli,
        #     formatters=dict(markdown=constants.T_TOC_CLI),
        #     options=[
        #         options.file_setupcfg,
        #         options.format_markdown,
        #         click.option(
        #             "--output",
        #             "-o",
        #             default="docs/cli/README.md",
        #             help=("output file to write.  (optional)"),
        #         ),
        #         options.stdout,
        #         options.header,
        #     ],
        # )
        # def toc(format, file, stdout, output, header):
        #     """
        #     Describe entrypoints for this project (parses setup.cfg)
        #     """
        #     from pynchon.api import project
        #
        #     config, plan = project.plan()
        #     return config
        #
        # @common.kommand(
        #     name="all",
        #     parent=Base.gen_cli,
        #     options=[
        #         options.file_setupcfg,
        #         options.output_dir,
        #         options.stdout,
        #     ],
        # )
        # def _all(
        #     file,
        #     stdout,
        #     output_dir,
        # ) -> list:
        #     """
        #     Generates help for every entrypoint
        #     """
        #     conf = util.python.load_entrypoints(util.python.load_setupcfg(path=file))
        #     entrypoints = conf.get("entrypoints", {})
        #     if not entrypoints:
        #         LOGGER.warning(f"failed loading entrypoints from {file}")
        #         return []
        #     docs = {}
        #     for e in entrypoints:
        #         bin_name = str(e["bin_name"])
        #         epoint = e["setuptools_entrypoint"]
        #         fname = os.path.join(output_dir, bin_name)
        #         fname = f"{fname}.md"
        #         LOGGER.debug(f"{epoint}: -> `{fname}`")
        #         docs[fname] = {**_entrypoint_docs(name=e["setuptools_entrypoint"]), **e}
        #
        #     for fname in docs:
        #         with open(fname, "w") as fhandle:
        #             fhandle.write(constants.T_DETAIL_CLI.render(docs[fname]))
        #         LOGGER.debug(f"wrote: {fname}")
        #     return list(docs.keys())
        #
        # @common.kommand(
        #     name="main",
        #     parent=Base.gen_cli,
        #     formatters=dict(markdown=constants.T_CLI_MAIN_MODULE),
        #     options=[
        #         options.format_markdown,
        #         options.stdout,
        #         options.header,
        #         options.file,
        #         options.output_dir,
        #         options.name,
        #         options.module,
        #     ],
        # )
        # def main_docs(format, module, file, output_dir, stdout, header, name):
        #     """
        #     Autogenenerate docs for python modules using __main__
        #     """
        #     from pynchon.api import project
        #     from pynchon.util.os import invoke
        #
        #     config, plan = project.plan()
        #     for fname, metadata in config["python"]["entrypoints"].items():
        #         if fname == file:
        #             dotpath = metadata["dotpath"]
        #             cmd = invoke(f"python -m{dotpath} --help")
        #             help = cmd.succeeded and cmd.stdout.strip()
        #             config["python"]["entrypoints"][fname] = {
        #                 **metadata,
        #                 **dict(help=help),
        #             }
        #             return config
        #
        # @common.kommand(
        #     name="entrypoint",
        #     parent=Base.gen_cli,
        #     formatters=dict(markdown=constants.T_DETAIL_CLI),
        #     options=[
        #         options.format_markdown,
        #         options.stdout,
        #         options.header,
        #         options.file,
        #         options.output,
        #         options.name,
        #         options.module,
        #     ],
        # )
        # def entrypoint_docs(format, module, file, output, stdout, header, name):
        #     """
        #     Autogenenerate docs for python CLIs using click
        #     """
        #     tmp = _entrypoint_docs(module=module, name=name)
        #     return tmp
        #
        # def _entrypoint_docs(module=None, name=None):
        #     """ """
        #     import importlib
        #
        #     result = []
        #     if name and not module:
        #         module, name = name.split(":")
        #     if module and name:
        #         mod = importlib.import_module(module)
        #         entrypoint = getattr(mod, name)
        #     else:
        #         msg = "No entrypoint found"
        #         LOGGER.warning(msg)
        #         return dict(error=msg)
        #     LOGGER.debug(f"Recursive help for `{module}:{name}`")
        #     result = util.click_recursive_help(entrypoint, parent=None)
        #     package = module.split(".")[0]
        #     return dict(
        #         package=module.split(".")[0],
        #         module=module,
        #         entrypoint=name,
        #         commands=result,
        #     )

    def plan(self, config):
        plan = super(self.__class__, self).plan(config)
        droot = config.pynchon['docs_root']
        cli_root = f"{droot}/cli"
        plan += [f"mkdir -p {cli_root}"]
        plan += [f"pynchon gen cli toc --output {cli_root}/README.md"]
        plan += [f"pynchon gen cli all --output-dir {cli_root}"]
        plan += [
            f"pynchon gen cli main --file {fname} --output-dir {cli_root}"
            for fname in config.python_cli.entrypoints
        ]
        return plan


class PythonAPI(models.Planner):
    """tools for generating python-api docs"""

    name = "python-api"
    config_kls = dict
    defaults = dict()

    @staticmethod
    def init_cli(kls):
        """pynchon.bin.api"""
        import click

        from pynchon import util
        from pynchon.plugins.base import Base

        LOGGER = lme.get_logger(__name__)

        def markdown(**result):
            return result["header"] + "\n".join(result["blocks"])

        # @common.kommand(
        #     name="toc",
        #     parent=Base.gen_api,
        #     formatters=dict(markdown=markdown),
        #     options=[
        #         options.format_markdown,
        #         options.package,
        #         click.option(
        #             "--output",
        #             "-o",
        #             default="docs/api/README.md",
        #             help=("output file to write.  (optional)"),
        #         ),
        #         click.option(
        #             "--exclude",
        #             default="",
        #             help=("comma-separated list of modules to exclude (optional)"),
        #         ),
        #         options.file,
        #         options.stdout,
        #         options.header,
        #     ],
        # )
        # def toc(package, file, exclude, output, format, stdout, header):
        #     """
        #     Generate table-of-contents
        #     """
        #     module = util.get_module(package=package, file=file)
        #     result = util.visit_module(
        #         module=module,
        #         module_name=package,
        #         exclude=exclude.split(","),
        #     )
        #     header = f"{header}\n\n" if header else ""
        #     return dict(
        #         header=f"## API for '{package}' package\n\n{header}" + "-" * 80,
        #         blocks=result,
        #     )

    def plan(self, config) -> typing.List:
        plan = super(self.__class__, self).plan(config)
        # self.logger.debug("planning for API docs..")
        api_root = f"{config.pynchon['docs_root']}/api"
        plan += [f"mkdir -p {api_root}"]
        import IPython

        # IPython.embed()
        tmp = config.python["package"]["name"]
        plan += [
            "pynchon gen api toc" f' --package {tmp}' f" --output {api_root}/README.md"
        ]
        return plan


class PyPI(models.ContextPlugin):
    """pypi-defaults"""

    name = "pypi"
    config_kls = PyPiConfig
    defaults = dict()
