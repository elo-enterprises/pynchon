""" pynchon.plugins.python.cli
"""
# import os
import glob

from pynchon import abcs, models, shimport

from pynchon.util import typing, lme  # noqa

config_mod = shimport.lazy(
    'pynchon.config',
)
LOGGER = lme.get_logger(__name__)


class PythonCliConfig(abcs.Config):
    config_key = "python-cli"

    @property
    def src_root(self):
        """ """
        # src_root = abcs.Path(
        # config_mod.project.get(
        #     "src_root", config_mod.pynchon.get("src_root")
        # )).absolute()
        src_root = abcs.Path("./src").absolute()
        if not src_root:
            msg = "`src_root` not set for pynchon or project config; cannot enumerate entrypoints"
            LOGGER.critical(msg)
            return []
        return src_root

    @property
    def entrypoints(self) -> dict:
        """ """
        src_root = self.src_root
        pat = src_root / "**" / "__main__.py"
        matches = [[x, {}] for x in glob.glob(str(pat), recursive=True)]
        matches = dict(matches)
        pkg_name = config_mod.python['package']["name"] or "unknown"
        for f, meta in matches.items():
            LOGGER.info(f'found entry-point: {f}')
            dotpath = abcs.Path(f).relative_to(src_root)
            dotpath = '.'.join(str(dotpath).split('/')[:-1])
            matches[f] = {
                **matches[f],
                **dict(
                    # src_root=src_root,
                    dotpath=dotpath,
                ),
            }
        return matches


class PythonCLI(models.ShyPlanner):
    """Tools for generating CLI docs"""

    name = "python-cli"
    config_class = PythonCliConfig

    # @common.kommand(
    #     name="toc",
    #     parent=Core.gen_cli,
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
    #     parent=Core.gen_cli,
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
    #     parent=Core.gen_cli,
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
    #     parent=Core.gen_cli,
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

    def plan(self, config=None):
        from pynchon import api

        config = config or api.project.get_config()
        plan = super(self.__class__, self).plan(config)
        droot = config.pynchon['docs_root']
        cli_root = f"{droot}/cli"

        plan.append(
            self.goal(command=f"mkdir -p {cli_root}", type='mkdir', resource=cli_root)
        )
        plan.append(
            self.goal(
                command=f"pynchon gen cli toc --output {cli_root}/README.md",
                type='gen',
                resource=cli_root,
            )
        )

        plan.append(
            self.goal(
                command=f"pynchon gen cli all --output-dir {cli_root}",
                type='gen',
                resource=cli_root,
            )
        )

        [
            plan.append(
                self.goal(
                    command=f"pynchon gen cli main --file {fname} --output-dir {cli_root}",
                    type='gen',
                    resource=fname,
                )
            )
            for fname in config['python-cli'].entrypoints
        ]

        return plan
