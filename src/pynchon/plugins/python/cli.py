""" pynchon.plugins.python.cli
"""
import glob

import shimport
from fleks import cli

from pynchon import abcs, models
from pynchon.api import project
from pynchon.util.os import invoke
from pynchon.util import lme, tagging, typing  # noqa

config_mod = shimport.lazy(
    "pynchon.config",
)
# config = shimport.lazy("pynchon.config")
LOGGER = lme.get_logger(__name__)


class PythonCliConfig(abcs.Config):
    """ """
    
    config_key: typing.ClassVar[str] = "python_cli"
    src_root:str = typing.Field()
    entrypoints:typing.List[str]=typing.Field()
    
    @property
    def src_root(self):
        """ """
        src_root = config_mod.src["root"]
        # FIXME: support for subprojects
        # # src_root = abcs.Path(
        # # config_mod.project.get(
        # #     "src_root", config_mod.pynchon.get("src_root")
        # # )).absolute()
        return abcs.Path(src_root)

    @property
    def entrypoints(self) -> dict:
        """ """
        src_root = self.src_root
        pat = src_root / "**" / "__main__.py"
        excludes = config_mod.src["exclude_patterns"]
        matches = glob.glob(str(pat), recursive=True)
        LOGGER.info(f"{len(matches)} matches for `entrypoints` filter")
        LOGGER.info(f"filtering with `excludes`: {excludes}")
        matches = list(
            filter(lambda x: not abcs.Path(x).match_any_glob(excludes), matches)
        )
        LOGGER.critical(f"{len(matches)} matches survived filter")
        matches = [[x, {}] for x in matches]
        matches = dict(matches)
        pkg_name = (
            "unknown"  # self.siblings['python']['package'].get("name") or "unknown"
        )
        for f, meta in matches.items():
            LOGGER.info(f"found entry-point: {f}")
            dotpath = abcs.Path(f).relative_to(src_root)
            dotpath = ".".join(str(dotpath).split("/")[:-1])
            matches[f] = {
                **matches[f],
                **dict(
                    # src_root=src_root,
                    dotpath=dotpath,
                    path=f,
                ),
            }
        return matches


@tagging.tags(click_aliases=["pc"])
class PythonCLI(models.ShyPlanner):
    """Generators for Python CLI docs"""

    name = "python-cli"
    config_class = PythonCliConfig
    cli_name = 'python-cli'
    
    @cli.click.group
    def gen(self):
        """Generates CLI docs for python packages"""

    # formatters=dict(markdown=constants.T_TOC_CLI),
    @gen.command("toc")
    # @cli.options.stdout
    @cli.options.header
    # options.file_setupcfg,
    @cli.click.option(
        "--output",
        "-o",
        default=None,
        help=("output file to write.  ({docs_root}/cli/README.md)"),
    )
    def toc(self, 
        # format, file, stdout, 
        output, header) -> None:
        """
        Describe entrypoints for this project (parses setup.cfg)
        """
        output = output or abcs.Path(self.siblings['docs']['root']) / "cli" / "README.md"
        LOGGER.warning(f"toc-output: {output}")
        raise NotImplementedError()

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
    @gen.command("main")
    @cli.options.stdout
    @cli.options.file
    @cli.options.header
    @cli.options.output_dir
    # @cli.click.flag('--click',help='treat as click')
    def main_docs(self, 
        # module, name ,format, 
        file, output_dir, stdout, header,):  # noqa
        """
        Autogenenerate docs for py modules using `__main__`
        """
        # config, plan = project.plan()
        from pynchon import api 
        tmp = self.config.dict()
        entrypoints = self["entrypoints"]
        found=False 
        for fname, metadata in entrypoints.items():
            if fname == file:
                dotpath = metadata["dotpath"]
                cmd = invoke(f"python -m{dotpath} --help")
                help = cmd.succeeded and cmd.stdout.strip()
                entrypoints[fname] = {
                    **metadata,
                    **dict(help=help),
                }
                found=True 
                break
        assert found,f"missing {fname}"
        tmp['entrypoints']=entrypoints 
        templatef = "pynchon/plugins/python/cli/main.module.md.j2"
        tmpl = api.render.get_template(templatef)
        core = api.project.get_config().dict()
        core.update(**{self.config_class.config_key:tmp})
        result = tmpl.render(**core)
        LOGGER.critical(result)
        p = abcs.Path(output_dir) 
        assert p.exists()
        p = p / f"{dotpath}.md"
        LOGGER.critical(f"Writing output to: {p}")
        with open(str(p),'w') as fhandle:
            fhandle.write(result)
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

    def plan(self):
        # from pynchon import api
        # config = config or api.project.get_config()
        plan = super(self.__class__, self).plan()
        # droot = config.pynchon["docs_root"]
        droot = self[:"docs.root":]
        cli_root = f"{droot}/cli"

        plan.append(
            self.goal(command=f"mkdir -p {cli_root}", type="mkdir", resource=cli_root)
        )
        plan.append(
            self.goal(
                command=f"{self.click_entry.name} {self.cli_name} toc --output {cli_root}/README.md",
                type="gen",
                resource=cli_root,
            )
        )
        # plan.append(
        #     self.goal(
        #         command=f"{self.click_entry.name} {self.cli_name} cli all --output-dir {cli_root}",
        #         type="gen",
        #         resource=cli_root,
        #     )
        # )

        [
            plan.append(
                self.goal(
                    command=f"{self.click_entry.name} {self.click_group.name} main --file {fname} --output-dir {cli_root}",
                    type="gen",
                    resource=fname,
                )
            )
            for fname in self.config.entrypoints
        ]

        return plan
