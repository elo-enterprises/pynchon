""" pynchon.plugins.python.cli
"""

import glob
import importlib

import shimport
from fleks import cli, tagging
from fleks.util.click import click_recursive_help

from pynchon import abcs, api, models
from pynchon.util.os import invoke

from pynchon.util import lme, typing  # noqa

config_mod = shimport.lazy(
    "pynchon.config",
)
LOGGER = lme.get_logger(__name__)

# class EntryPoint(abcs.Config):
#     is_click:bool = typing.Field(default=False)
#     module:str = typing.Field(default=None)
#     package:str = typing.Field(default=None)
#     subcommands:typing.List = typing.Field(default=[])

from fleks.models import BaseModel


class EntryMetadata(BaseModel):
    is_click: bool = typing.Field(help="", required=False, default=False)
    is_package: bool = typing.Field(help="", required=False, default=False)
    is_module: bool = typing.Field(help="", required=False, default=True)
    dotpath: str = typing.Field(
        help="",
        required=True,
    )
    file: str = typing.Field(
        help="",
        required=True,
    )
    resource: abcs.Path = typing.Field(help="", required=True)
    path: abcs.Path = typing.Field(help="", required=True)
    entrypoints: typing.List = typing.Field(help="", required=False, default=[])
    src_root: abcs.Path = typing.Field(required=True)

    @property
    def src_url(self) -> str:
        return "/" + str(self.path.relative_to(self.src_root.parent))
        # return abcs.Path(path).absolute().relative_to(abcs.Path(git_root).absolute())

    @property
    def help_invocation(self):
        if self.is_module:
            return f"python -m{self.dotpath} --help"

    @property
    def help_output(self):
        if self.help_invocation:
            cmd = invoke(self.help_invocation)
            if cmd.succeeded:
                help = cmd.stdout.lstrip().strip()
                help = f"$ {self.help_invocation}\n\n{help}"
            else:
                LOGGER.critical(
                    f"ERROR: failure executing command (cannot extract help!)\n\ncommand='{help_invocation}'\n\nerror follows:\n\n{cmd.stderr}"
                )
                help = f"Failed to capture help from command `{help_invocation}`"
            return help
        else:
            import IPython

            IPython.embed()
            raise Exception(self)

    @property
    def module(self):
        return (
            f"{self.dotpath}.__main__"
            if str(self.file).endswith("__main__.py")
            else self.dotpath
        )


class PythonCliConfig(abcs.Config):
    """ """

    config_key: typing.ClassVar[str] = "python_cli"
    src_root: str = typing.Field(help="")
    entrypoints: typing.List[typing.Dict] = typing.Field(help="")
    hooks: typing.List[str] = typing.Field(
        help="applicable hook names",
        default=["open-after-apply"],
    )

    @property
    def root(self):
        tmp = self.__dict__.get("root")
        if tmp:
            return tmp
        else:
            from pynchon import config

            return abcs.Path(config.docs.root) / "cli"

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

    def is_click(self, path: str = None) -> bool:
        with open(str(path)) as fhandle:
            return "click" in fhandle.read()

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
        # LOGGER.info(f"{len(matches)} matches survived filter")
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
                    click=self.is_click(path=f),
                    dotpath=dotpath,
                    file=f,
                    path=abcs.Path(f),
                    main_entrypoint=f.endswith("__main__.py"),
                    # package_entrypoint=False,
                    resource=self.root / f"{dotpath}.md",
                ),
            }
        result = list(matches.values())
        result = [EntryMetadata(src_root=self.src_root, **x) for x in result]
        # raise Exception(result[0])
        return result


@tagging.tags(click_aliases=["pc"])
class PythonCLI(models.Planner):
    """Generators for Python CLI docs"""

    name = "python-cli"
    cli_name = "python-cli"
    config_class = PythonCliConfig

    @cli.click.group
    def gen(self):
        """Generates CLI docs for python packages"""

    @cli.click.flag("--changes")
    def list(self, changes: bool = False) -> typing.List[str]:
        """list related targets/resources"""
        if changes:
            out = []
            git = self.siblings["git"]
            git_changes = git.list(changes=True)
            for emeta in self.config.entrypoints:
                p = abcs.Path(emeta["path"]).absolute()
                if p in git_changes:
                    out.append(p)
            return out
        else:
            return [
                abcs.Path(emeta["path"]).absolute() for emeta in self.config.entrypoints
            ]

    @gen.command("toc")
    @cli.options.header
    @cli.options.output
    def toc(
        self,
        # format, file, stdout,
        output,
        header,
    ) -> None:
        """
        Generate table-of-contents for project entrypoints
        """
        output = output or self.root / "README.md"
        LOGGER.warning(f"writing toc to file: {output}")
        entrypoints = self.config.entrypoints
        # tmp = []
        # for meta in entrypoints:
        #     tmp.append({**meta.dict(), **dict(
        #         # src_url=meta["path"])}
        #         src_url='????',
        #         #self.get_src_url(meta['path'])
        #         )})
        # entrypoints = tmp
        cfg = {**self.config.dict(), **dict(entrypoints=entrypoints)}
        cfg = {**api.project.get_config().dict(), **{self.config_class.config_key: cfg}}
        templatef = self.plugin_templates_root / "TOC.md.j2"
        tmpl = api.render.get_template(templatef)
        result = tmpl.render(
            # package_entrypoints=python_cli.entrypoints,
            package_entrypoints=[e for e in entrypoints if e.is_package],
            main_entrypoints=[e for e in entrypoints if e.is_module],
            **cfg,
        )
        with open(str(output), "w") as fhandle:
            fhandle.write(result)

    def _click_recursive_help(
        self, resource=None, path=None, module=None, dotpath=None, name=None, **kwargs
    ):
        """ """
        import shil

        result = []
        if name and not module:
            module, name = name.split(":")
        if module and name:
            try:
                mod = importlib.import_module(module)
                entrypoint = getattr(mod, name)
            except (Exception,) as exc:
                LOGGER.critical(exc)
                return []
        else:
            msg = "No entrypoint found"
            LOGGER.warning(msg)
            # return dict(error=msg)
            raise Exception(msg)
        LOGGER.debug(f"Recursive help for `{module}:{name}`")
        result = click_recursive_help(
            entrypoint, parent=None, path=path, dotpath=dotpath, **kwargs
        ).values()
        git_root = self.siblings["git"]["root"]
        result = [
            {
                **v,
                **dict(
                    module=module,
                    resource=resource or self.root / f"{v['dotpath']}.md",
                    package=module.split(".")[0],
                    entrypoint=name,
                    dotpath=dotpath,
                    help=shil.invoke(
                        f"python -m{v['help_invocation']} --help", strict=True
                    ).stdout,
                    # src_url=self.get_src_url(path),
                ),
            }
            for v in result
        ]
        return result

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
        """ """
        LOGGER.critical(f"looking up metadata for '{file}'")
        found = False
        file = abcs.Path(file)

        for metadata in self.config["entrypoints"]:
            # path=metadata.pop('path')
            # raise Exception(type(path))
            # emd = EntryMetadata(**metadata)
            if str(metadata.path) == str(file):
                dotpath = metadata.dotpath  # metadata["dotpath"]
                module = metadata.module
                help_invocation = metadata.help_invocation
                # metadata.update(help_invocation=help_invocation)
                try:
                    metadata.update(
                        entrypoints=self._click_recursive_help(
                            module=module,
                            name="entry",
                            resource=self.root / f"{metadata.dotpath}.md",
                            dotpath=metadata.dotpath,
                            path=file.absolute(),
                        )
                    )
                except (AttributeError,) as exc:
                    LOGGER.critical(
                        f"exception retrieving help programmatically: {exc}"
                    )
                    LOGGER.critical(
                        f"error retrieving help via system CLI: {metadata.help_invocation}"
                    )
                else:
                    rsrc = self.root / f"{dotpath}.md"
                    # src_url = metadata.src_url #self.get_src_url(file)
                    # raise Exception(file)
                    docs_url = rsrc.relative_to(self.docs_root.parent)
                    metadata.update(
                        click=True,
                        help_invocation=help_invocation,
                        docs_url=docs_url,
                        # src_url='/'+str(src_url),
                        # src_url=src_url,
                        resource=rsrc,
                        entrypoints=sub_entrypoints,
                    )
                    # metadata.update(**get_cmd_output(help_invocation))
                    # import IPython; IPython.embed()
                    # raise Exception(sub_entrypoints)
                found = True
                break
        if not found:
            LOGGER.critical(f"missing {file}")
            return {}
        return metadata

    @property
    def docs_root(self):
        return abcs.Path(self[:"docs.root":])

    @property
    def src_root(self):
        return abcs.Path(self[:"src.root":])

    @property
    def root(self):
        return self.config.root

    @gen.command("main")
    @cli.options.stdout
    @cli.options.file
    @cli.options.header
    @cli.options.output_file
    # @cli.click.flag('--click', help='treat as click')
    def main_docs(
        self,
        file,
        output,
        stdout,
        header,
    ):  # noqa
        """
        Autogenenerate docs for py modules using `__main__`
        """
        assert abcs.Path(file).exists(), f"input file @ {file} does not exist"
        metadata = self.get_entrypoint_metadata(file)
        output = (
            abcs.Path(output) if output else self.root / f"{metadata['dotpath']}.md"
        )
        output_dir = output.parents[0]
        assert output_dir.exists(), f"{output_dir} does not exist"
        tmpl = api.render.get_template(self.plugin_templates_root / "main.module.md.j2")
        config = {
            **api.project.get_config().dict(),
            **{self.config_class.config_key: {**self.config.dict(), **dict()}},
        }
        result = tmpl.render(
            entrypoints=[metadata],
            **config,
        )
        LOGGER.critical(result)
        LOGGER.critical(f"Writing output to: {output}")
        with open(str(output), "w") as fhandle:
            fhandle.write(result)

    def plan(self):
        """Describe plan for this plugin"""
        plan = super(self.__class__, self).plan()

        plan.append(
            self.goal(command=f"mkdir -p {self.root}", type="mkdir", resource=self.root)
        )

        rsrc = self.root / "README.md"
        cmd = f"{self.click_entry.name} {self.cli_name} toc " f"--output {rsrc}"
        plan.append(self.goal(command=cmd, type="gen", resource=rsrc))

        # plan.append(
        #     self.goal(
        #         command=f"{self.click_entry.name} {self.cli_name} cli all --output ..",
        #         type="gen", resource=cli_root,))

        for entrypoint_metadata in self.config.entrypoints:
            entrypoint_metadata = self.get_entrypoint_metadata(entrypoint_metadata.path)
            inp = entrypoint_metadata.path
            rsrc = entrypoint_metadata.resource
            if not rsrc:
                raise Exception(entrypoint_metadata)
            plan.append(
                self.goal(
                    command=(
                        f"{self.click_entry.name} {self.click_group.name} "
                        f"main --file {inp} --output {rsrc}"
                    ),
                    type="gen",
                    resource=rsrc,
                )
            )

        return plan
