""" pynchon.plugins.python.cli
"""
import glob

import importlib
import shimport

from fleks import cli
from fleks.util.click import click_recursive_help

from pynchon import abcs, models
from pynchon import api 
from pynchon.api import project
from pynchon.util.os import invoke
from pynchon.util import lme, tagging, typing  # noqa

config_mod = shimport.lazy(
    "pynchon.config",
)
LOGGER = lme.get_logger(__name__)


class PythonCliConfig(abcs.Config):
    """ """
    
    config_key: typing.ClassVar[str] = "python_cli"
    src_root:str = typing.Field(help='')
    entrypoints:typing.List[typing.Dict] = typing.Field(help='')
    
    @property
    def src_root(self) -> abcs.Path:
        """ """
        src_root = config_mod.src["root"]
        # FIXME: support for subprojects
        # # src_root = abcs.Path(
        # # config_mod.project.get(
        # #     "src_root", config_mod.pynchon.get("src_root")
        # # )).absolute()
        return abcs.Path(src_root)
    
    def is_click(self,path:str=None) -> bool:
        with open(str(path),'r') as fhandle:
            return 'click' in fhandle.read()
        
    @property
    def entrypoints(self) -> typing.List[typing.Dict]:
        """ """
        src_root = self.src_root
        pat = src_root / "**" / "__main__.py"
        excludes = config_mod.src["exclude_patterns"]
        matches = glob.glob(str(pat), recursive=True)
        LOGGER.info(f"{len(matches)} matches for `entrypoints` filter")
        # LOGGER.info(f"filtering with `excludes`: {excludes}")
        matches = list(
            filter(lambda x: not abcs.Path(x).match_any_glob(excludes), matches)
        )
        # LOGGER.critical(f"{len(matches)} matches survived filter")
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
                    click=self.is_click(path=f),
                    dotpath=dotpath,
                    path=f,
                ),
            }
        return list(matches.values())


@tagging.tags(click_aliases=["pc"])
class PythonCLI(models.ShyPlanner):
    """Generators for Python CLI docs"""

    name = "python-cli"
    cli_name = 'python-cli'
    config_class = PythonCliConfig
    
    @cli.click.group
    def gen(self):
        """Generates CLI docs for python packages"""

    @gen.command("toc")
    @cli.options.header
    @cli.click.option(
        "--output-dir",
        "-o",
        default=None,
        help=("Directory to write output to"),
    )
    def toc(self, 
        # format, file, stdout, 
        output_dir, header) -> None:
        """
        Generate table-of-contents for project entrypoints
        """
        output_dir = output_dir or abcs.Path(self.siblings['docs']['root']) / "cli"
        output_file=abcs.Path(output_dir)/'README.md'
        LOGGER.warning(f"writing toc to file: {output_file}")
        entrypoints = self.config.entrypoints
        tmp=[]
        for meta in entrypoints:
            # LOGGER.warning([fname, meta])
            tmp.append(
                {   **meta, 
                    **dict(
                        url = meta['path'])})
        entrypoints=tmp
        cfg = {**self.config.dict(), **dict(entrypoints=entrypoints)}
        cfg = {**api.project.get_config().dict(), **{self.config_class.config_key: cfg}}
        templatef = self.plugin_templates_root / "TOC.md.j2"
        tmpl = api.render.get_template(templatef)
        result = tmpl.render(**cfg)
        with open(str(output_file), 'w') as fhandle:
            fhandle.write(result)

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
    #         docs[fname] = {**_click_recursive_help(name=e["setuptools_entrypoint"]), **e}
    #
    #     for fname in docs:
    #         with open(fname, "w") as fhandle:
    #             fhandle.write(constants.T_DETAIL_CLI.render(docs[fname]))
    #         LOGGER.debug(f"wrote: {fname}")
    #     return list(docs.keys())
    def get_entrypoint_metadata(self, file):
        """
        """
        LOGGER.critical(f"looking up metadata for {file}")
        # entrypoints = dict([
        #     [abcs.Path(k),v] for k,v in self['entrypoints'].items()
        #     ])
        # self["entrypoints"].copy()
        found = False 
        file = abcs.Path(file)
        for metadata in self.config['entrypoints']:
            # raise Exception([metadata,file])
            # raise Exception(metadata)
            # LOGGER.critical([fname,file,fname==file])
            if str(metadata['path']) == str(file):
                dotpath = metadata["dotpath"]
                module = f"{dotpath}.__main__" if str(file).endswith('__main__.py') else dotpath
                try:
                    sub_entrypoints = self._click_recursive_help(
                        module=module, name='entry', 
                        dotpath=dotpath, path=file.absolute(),
                        )
                except (AttributeError,) as exc:
                    LOGGER.critical(f"exception retrieving help programmatically: {exc}")
                    cmd = f"python -m{dotpath} --help"
                    LOGGER.critical(f"retrieving help via system CLI {cmd}")
                    cmd = invoke(cmd)
                    help = cmd.succeeded and cmd.stdout.strip()
                    metadata.update(
                        click=False, help=help, entrypoints=[])
                else:
                    metadata.update(
                        click=True, help=None, 
                        entrypoints=sub_entrypoints)
                    # raise Exception(sub_entrypoints)
                metadata.update(url='relf')
                found = True 
                break
        if not found:
            LOGGER.critical(f"missing {fname} in {list(entrypoints.keys())}")
            return {}
        return metadata

    @gen.command("main")
    @cli.options.stdout
    @cli.options.file
    @cli.options.header
    @cli.options.output_dir
    # @cli.click.flag('--click', help='treat as click')
    def main_docs(self, 
        # module, name ,format, 
        file, output_dir, stdout, 
        header,):  # noqa
        """
        Autogenenerate docs for py modules using `__main__`
        """
        assert abcs.Path(file).exists(), f'file @ {file} does not exist'
        output_dir = abcs.Path(output_dir) 
        assert output_dir.exists(), f"{output_dir} does not exist"
        metadata = self.get_entrypoint_metadata(file)
        tmpl = api.render.get_template(self.plugin_templates_root / "main.module.md.j2")
        config = {
            **api.project.get_config().dict(), 
            **{ self.config_class.config_key: {
                **self.config.dict(), **dict() } }
            }
        result = tmpl.render(
            entrypoints = [metadata], 
            **config,
            )
        LOGGER.critical(result)
        p = output_dir / f"{metadata['dotpath']}.md"
        LOGGER.critical(f"Writing output to: {p}")
        with open(str(p),'w') as fhandle:
            fhandle.write(result)

    def _click_recursive_help(self, path=None, module=None, dotpath=None, name=None, **kwargs):
        """ """    
        result = []
        if name and not module:
            module, name = name.split(":")
        if module and name:
            mod = importlib.import_module(module)
            entrypoint = getattr(mod, name)
        else:
            msg = "No entrypoint found"
            LOGGER.warning(msg)
            return dict(error=msg)
        LOGGER.debug(f"Recursive help for `{module}:{name}`")
        result = click_recursive_help(
            entrypoint, parent=None, 
            path=path, dotpath=dotpath, 
            **kwargs)
        result = result.values()
        git_root=self.siblings['git']['root']
        result = [
            {
                **v,
                **dict(
                    module=module,
                    entrypoint=name,
                    dotpath=dotpath,
                    help='....',
                    url=abcs.Path(path).absolute().relative_to(
                        abcs.Path(git_root).absolute()))
            } for v in result ]
        # raise Exception(result[0])
        return result
        # package = module.split(".")[0]
        # import IPython; IPython.embed()
        # return dict(
        #     package=module.split(".")[0],
        #     module=module,
        #     entrypoint=name,
        #     commands=result,
        # )

    def plan(self):
        """ Describe plan for this plugin """
        plan = super(self.__class__, self).plan()
        # droot = config.pynchon["docs_root"]
        droot = self[:"docs.root":]
        cli_root = f"{droot}/cli"

        plan.append(
            self.goal(command=f"mkdir -p {cli_root}", type="mkdir", resource=cli_root)
        )
        plan.append(
            self.goal(
                command=(
                    f"{self.click_entry.name} {self.cli_name} toc "
                    f"--output-dir {cli_root}"),
                type="gen", resource=cli_root)
        )
        # plan.append(
        #     self.goal(
        #         command=f"{self.click_entry.name} {self.cli_name} cli all --output-dir {cli_root}",
        #         type="gen", resource=cli_root,))

        [
            plan.append(
                self.goal(
                    command=(
                        f"{self.click_entry.name} {self.click_group.name} "
                        f"main --file {entrypoint_metadata['path']} "
                        f"--output-dir {cli_root}"),
                    type="gen",
                    resource=entrypoint_metadata['path'],
                )
            )
            for entrypoint_metadata in self.config.entrypoints
        ]

        return plan
