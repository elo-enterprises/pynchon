""" pynchon.plugins.pattern
"""

from pynchon import abcs, cli, constants, events, models  # noqa
from pynchon.api import render
from pynchon.util.os import invoke
from pynchon.util.text import loads

from pynchon.util import lme, tagging, text, typing  # noqa

LOGGER = lme.get_logger(__name__)

PETR = abcs.Path(constants.PYNCHON_EMBEDDED_TEMPLATES_ROOT)

FNAME_ADVICE = ".scaffold.advice.json5"

from pynchon.util.files.diff import str_diff


class RenderResult(abcs.Config):
    before: typing.Optional[str] = typing.Field(default=None)
    after: typing.Optional[str] = typing.Field(default=None)
    diff: typing.Optional[str] = typing.Field(default=None)
    src: typing.Union[str, abcs.Path] = typing.Field(default=None)
    dest: typing.Union[str, abcs.Path] = typing.Field(default=None)

    def __str__(self):
        return f"<RenderResult>"

    @property
    def diff(self):
        return str_diff(self.before, self.after)


class ScaffoldAdvice(abcs.Config):
    file: typing.Union[str, abcs.Path] = typing.Field(required=True)
    loaded: bool = typing.Field(default=False)
    inherits: typing.List[str] = typing.Field(default=[])

    def __str__(self):
        return f"<ScaffoldAdvice>"

    @property
    def inherits(self):
        if self.loaded:
            return self.__dict__["inherits"]
        else:
            return self.load().inherits

    def exists(self):
        return abcs.Path(self.file).exists()

    def load(self):
        cadvice = abcs.Path(self.file).read()
        adv = loads.json5(cadvice)
        self.__dict__.update(loaded=True, **adv)
        return self


class Scaffold(abcs.Config):
    root: typing.Union[str, abcs.Path] = typing.Field(required=True)
    files: typing.List[str] = typing.Field(default=[])
    dirs: typing.List[str] = typing.Field(default=[])
    kind: str = typing.Field(required=True)

    def __str__(self):
        return f"<Scaffold@`{self.kind}`>"

    __repr__ = __str__

    def sync(self, dest=None, goals=[], context: dict = {}):
        """ """
        LOGGER.critical(f"sync: {dest}")
        self.sync_dirs(dest=dest, goals=goals, context=context)
        self.sync_files(dest=dest, goals=goals, context=context)
        for p in self.get_parents():
            p.sync(dest=dest, goals=goals, context=context)
        return goals

    def sync_dirs(self, dest=None, goals=[], context: dict = {}):
        """ """
        LOGGER.info(f"sync_dirs: {dest}")
        for pdir in self.dirs:
            # raise Exception(dest)
            tmp = pdir.relative_to(self.root)
            tmp = tmp.relative_to(dest)
            if render.is_templated(str(tmp)):
                msg = f"detected `{tmp}` is templated, "
                tmp = abcs.Path(
                    render.get_template_from_string(str(tmp)).render(**context)
                )
                msg += f"rendered it as {tmp}"
                LOGGER.critical(msg)
            LOGGER.critical(f"sync_dirs:: {dest} {tmp}")
            if tmp.exists():
                LOGGER.info(f"directory already exists @ `{tmp}`")
            else:
                goals.append(
                    models.Goal(
                        type="create",
                        label=f"dir-creation required by {self.kind}",
                        resource=tmp,
                        command=f"mkdir -p {tmp}",
                    )
                )

    def render_file(
        self, src=None, dest=None, should_plan=False, goals=[], context: dict = {}
    ) -> str:
        """ """
        assert context
        if src.exists():
            before = src.read()
            tmpl = render.get_template_from_file(src)
            # rendered = tmpl.render(name=name, **self.project_config)
            LOGGER.critical(f"render_file: {context}")
            after = tmpl.render(**context)
            tmp = RenderResult(before=before, after=after, src=src, dest=dest)
            if tmp.diff:
                LOGGER.critical(f"render_file: diff present")
                goals.append(
                    models.Goal(
                        type="sync",
                        label="sync existing file",
                        resource=dest,
                        command=f"cp '{src}' {dest}",
                    )
                )
            else:
                LOGGER.critical(f"render_file: no diff")
        else:
            raise NotImplementedError()
        # return rendered

    def sync_files(
        self, dest=None, goals=[], should_plan=False, context: dict = {}
    ) -> models.Plan:
        """ """
        for src in self.files:
            dst = src.relative_to(self.root)
            if not dst.exists():
                goals.append(
                    models.Goal(
                        type="create",
                        label=f"file-creation required by scaffold @ `{self.kind}`",
                        resource=dst,
                        command=f"cp {src} {dst}",
                    )
                )
            else:
                LOGGER.critical(f"modifies?: {dest}")
                goal_maybe = self.render_file(
                    src=src,
                    dest=dest,
                    should_plan=should_plan,
                    goals=goals,
                    context=context,
                )
            # after = self._render_file(dest=f)
            # with open(f) as fhandle:
            #     before = fhandle.read()
            # if before != after:
            #     # LOGGER.critical('rendering {f} creates changes!')
            #             type="sync",
            #             command=f"cp {destp} {fabs}",
            #             resource=f,
            #         )
            #     )

    def get_parents(self):
        out = []
        parents = self.advice.inherits if self.advice else []
        for kind in parents:
            pfolder = PETR / "scaffolds" / kind
            scaf = Scaffold(kind=kind, root=pfolder)
            out.append(scaf)
        return out

    def get_inherited_files(self):
        """ """
        out = []
        for scaf in self.get_parents():
            out += scaf.files
        return out

    def get_inherited_dirs(self):
        """ """
        out = []
        for scaf in self.get_parents():
            out += scaf.dirs
        return out

    @property
    def has_advice(self) -> bool:
        return self.advice is not None

    @property
    def advice(self):
        fadvice = ScaffoldAdvice(file=self.root / FNAME_ADVICE)
        if not fadvice.exists():
            return None
        else:
            return fadvice

    @property
    def files(self) -> typing.List[str]:
        folder = self.root
        base_files = list(
            {x for x in folder.glob("*") if not x.is_dir() and x.name != FNAME_ADVICE}
        )
        return base_files  # +self.get_inherited_files()

    @property
    def dirs(self) -> typing.List:
        base_dirs = list(
            [x for x in self.root.glob("**/") if x.is_dir() and not x == self.root]
        )
        return base_dirs  # +self.get_inherited_dirs()


@tagging.tags(click_aliases=["pat"])
class Pattern(models.ResourceManager):
    """
    Tools for working with file/directory patterns
    """

    name = "pattern"
    cli_name = "pattern"

    class config_class(abcs.Config):
        config_key: typing.ClassVar[str] = "pattern"
        include_patterns: typing.List[str] = typing.Field(default=["*/", "*/*/"])

        @property
        def root(self):
            tmp = PETR / "scaffolds"
            assert tmp.exists(), tmp
            return tmp

    @property
    def patterns(self) -> typing.Dict:
        tmp = super(self.__class__, self).list()
        tmp = [[str(x.relative_to(self.config.root)), x.glob("**/*")] for x in tmp]
        tmp = dict(tmp)
        keep = [x for x in tmp if not any([k.startswith(f"{x}/") for k in tmp])]
        tmp = dict(list([[k, list(v)] for k, v in tmp.items() if k in keep]))
        return tmp

    @property
    def pattern_folder(self):
        return self["root"]

    @property
    def pattern_names(self):
        tmp = self.patterns
        tmp = [abcs.Path(x) for x in tmp.keys()]
        tmp = [x.parents[0] if (self.config.root / x).is_file() else x for x in tmp]
        tmp = map(str, tmp)
        return list(tmp)

    def list(self) -> typing.List:
        """
        Describe templates we can cut patterns from
        """
        return self.pattern_names

    @cli.click.command("open")
    @cli.click.argument("kind", nargs=1)
    def _open(self, kind):
        """open pattern in editor"""
        pfolder = self.pattern_folder / kind
        ed = self[:"pynchon.editor":"atom"]
        invoke(f"{ed} {pfolder}&", system=True)

    @cli.click.option("--name", default=False)
    @cli.click.argument("kind", nargs=1)
    @cli.click.argument("dest", nargs=1)
    @cli.options.plan
    def sync(
        self,
        dest: str = None,
        kind: str = None,
        name: str = None,
        should_plan: bool = False,
    ):
        """Synchronizes DEST from scaffold KIND"""
        # https://github.com/cookiecutter/cookiecutter/issues/784

        LOGGER.critical(f'Synchronizing "{dest}" from `{kind}`')
        tmp = self.pattern_names
        if kind not in tmp:
            LOGGER.critical(f"Unrecognized pattern `{kind}`; expected one of {tmp}")
            raise SystemExit(1)
        plan = super(self.__class__, self).plan()
        destp = abcs.Path(dest)
        folder = abcs.Path(dest).absolute()

        pattern = Scaffold(kind=kind, root=self.pattern_folder / kind)

        LOGGER.warning(f"found pattern:\n\t{pattern}")
        LOGGER.warning(f"tentatively rendering {pattern} to `{destp}`")
        # import IPython; IPython.embed()
        patterns = [pattern] + pattern.get_parents()
        for pattern in patterns:
            LOGGER.critical(f"running sync for: {pattern}")
            goals = pattern.sync(
                dest=destp,
                goals=plan,
                context=dict(name=name, **self.project_config.dict()),
            )
        if should_plan:
            LOGGER.critical(plan)
            # import IPython; IPython.embed()
            return plan
        else:
            return plan.apply()  # return dict(changes=changes)

    @cli.options.plan
    @cli.click.argument("dest", nargs=1)
    def render(self, dest, should_plan: bool = False):
        """Renders content inside folder @ DEST"""
        folder = abcs.Path(dest).absolute()
        name = folder.name
        if not folder.exists():
            self.logger.critical(f"Folder @ {folder} does not exist!")
        else:
            plan = super(self.__class__, self).plan()
            # dirs = self._get_template_dirs(folder)
            # files = self._get_template_files(folder)

            # struct=dict(files=files, dirs=dirs)
            for d in dirs:
                d = str(d.absolute())
                if "{{name}}" in d:
                    newname = d.replace("{{name}}", name)
                    plan.append(
                        self.goal(
                            resource=newname,
                            command=f"mv '{d}' {newname}",
                            type="move",
                        )
                    )
            for f in files:
                f = str(f.absolute())
                if "{{name}}" in f:
                    newname = f.replace("{{name}}", name)
                    plan.append(
                        self.goal(
                            resource=newname,
                            command=f"mv '{f}' {newname}",
                            type="move",
                        )
                    )
            files = list([x for x in folder.glob("*") if not x.is_dir()])
            # rendered_files=[]

            for f in files:
                with open(f) as fhandle:
                    if render.is_templated(fhandle.read()):
                        plan.append(
                            self.goal(
                                resource=f,
                                command=f"pynchon pattern render-file {f} --name {name}",
                                type="render",
                            )
                        )

            if should_plan:
                return plan
            else:
                return self.apply(plan)

    # @cli.click.option("--name", required=True)
    # @cli.click.argument("dest", nargs=1)
    # def render_file(self, dest=None, name="") -> bool:
    #     """ """
    #     destp = abcs.Path(dest)
    # assert destp.exists()
    # rendered = self._render_file(dest=dest, name=name)
    # if rendered is None:
    #     raise SystemExit(1)
    # else:
    #     with open(f, "w") as fhandle:
    #         fhandle.write(rendered)
    #     return True

    # def _render_file(self, dest=None, name="") -> str:
    #     """ """
    #     f = abcs.Path(dest)
    #     LOGGER.warning(f"rendering `{f}` in-place")
    #     try:
    #         tmpl = render.get_template_from_file(f)
    #     except (Exception,) as exc:
    #         LOGGER.critical(f"failed to get_template_from_file @ {f}: {exc}")
    #         return None
    #     else:
    #         assert tmpl
    #         rendered = tmpl.render(name=name, **self.project_config)
    #         return rendered

    @cli.click.argument("dest", nargs=1)
    @cli.click.argument("kind", nargs=1)
    def clone(self, kind: str = None, name: str = None):
        """Clones PATTERN to DEST"""
        raise NotImplementedError()

    @cli.click.argument("name", nargs=1)
    @cli.click.argument("kind", nargs=1)
    @cli.options.plan
    def new(
        self,
        kind,
        name,
        should_plan: bool = False,
    ):
        """Instantiates PATTERN to NAME"""
        pfolder = self.pattern_folder / kind
        if not pfolder.exists():
            choices = set(self.list().keys())
            tmp = pfolder.relative_to(abcs.Path(".").absolute())
            LOGGER.critical(
                f'KIND @ "{name}" suggests pattern-folder @ "{tmp}", but folder does not exist!'
            )
            LOGGER.critical(f"Choices are: {choices}")
        else:
            plan = super(self.__class__, self).plan()
            dest = abcs.Path(name).absolute()
            if dest.exists():
                LOGGER.warning(f"{dest} already exists!")
            fadvice = ScaffoldAdvice(file=pfolder / ".scaffold.advice.json5")
            if fadvice.exists():
                fadvice.load()
                inherits = fadvice.inherits
            else:
                inherits = []
            inherits += [pfolder / "*"] if pfolder not in inherits else []
            LOGGER.warning(f"{kind} inherits {len(inherits)} patterns")
            dest = dest.relative_to(abcs.Path(".").absolute())
            for parent in inherits:
                # parent = parent.relative_to(abcs.Path(".").absolute())
                plan.append(
                    self.goal(
                        command=f"cp -rfv {parent} {dest}",
                        resource=dest,
                        type="copy",
                    )
                )

            plan.append(
                self.goal(
                    # callable=lambda: self.render(name)
                    command=f"{self.click_entry.name} {self.cli_name} render {dest}",
                    resource=dest.absolute(),
                    type="recursive-render",
                )
            )
            if should_plan:
                return plan
            else:
                result = self.apply(plan)
                return result.ok
