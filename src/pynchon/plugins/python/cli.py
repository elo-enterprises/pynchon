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
                    path=f,
                    main_entrypoint=f.endswith("__main__.py"),
                    package_entrypoint=False,
                    resource=self.root / f"{dotpath}.md",
                ),
            }
        return list(matches.values())


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
        tmp = []
        for meta in entrypoints:
            tmp.append({**meta, **dict(src_url=meta["path"])})
        entrypoints = tmp
        cfg = {**self.config.dict(), **dict(entrypoints=entrypoints)}
        cfg = {**api.project.get_config().dict(), **{self.config_class.config_key: cfg}}
        templatef = self.plugin_templates_root / "TOC.md.j2"
        tmpl = api.render.get_template(templatef)
        result = tmpl.render(
            # package_entrypoints=python_cli.entrypoints,
            package_entrypoints=[e for e in entrypoints if e["package_entrypoint"]],
            main_entrypoints=[e for e in entrypoints if e["main_entrypoint"]],
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
                        f"python -m{v['invocation_sample']} --help", strict=True
                    ).stdout,
                    src_url=abcs.Path(path)
                    .absolute()
                    .relative_to(abcs.Path(git_root).absolute()),
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
        # entrypoints = dict([
        #     [abcs.Path(k),v] for k,v in self['entrypoints'].items()
        #     ])
        # self["entrypoints"].copy()
        found = False
        file = abcs.Path(file)
        for metadata in self.config["entrypoints"]:
            LOGGER.critical(f"processing: {metadata}")
            if str(metadata["path"]) == str(file):
                dotpath = metadata["dotpath"]
                module = (
                    f"{dotpath}.__main__"
                    if str(file).endswith("__main__.py")
                    else dotpath
                )
                try:
                    sub_entrypoints = self._click_recursive_help(
                        module=module,
                        name="entry",
                        resource=self.root / f"{dotpath}.md",
                        dotpath=dotpath,
                        path=file.absolute(),
                    )
                except (AttributeError,) as exc:
                    LOGGER.critical(
                        f"exception retrieving help programmatically: {exc}"
                    )
                    cmd = f"python -m{dotpath} --help"
                    LOGGER.critical(f"error retrieving help via system CLI {cmd}")
                    cmd = invoke(cmd)
                    help = cmd.succeeded and cmd.stdout.strip()
                    metadata.update(click=False, help=help, entrypoints=[])
                else:
                    metadata.update(
                        click=True,
                        help=None,
                        resource=self.root / f"{dotpath}.md",
                        entrypoints=sub_entrypoints,
                    )
                    # raise Exception(sub_entrypoints)
                metadata.update(src_url="relf")
                found = True
                break
        if not found:
            LOGGER.critical(f"missing {file}")
            return {}
        return metadata

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
            entrypoint_metadata = self.get_entrypoint_metadata(
                entrypoint_metadata["path"]
            )
            inp = entrypoint_metadata["path"]
            rsrc = entrypoint_metadata["resource"]
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
