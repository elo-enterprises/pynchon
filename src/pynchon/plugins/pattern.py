""" pynchon.plugins.pattern
"""

from pynchon import abcs, cli, constants, events, models  # noqa
from pynchon.util import lme, tagging, typing  # noqa
from pynchon.util.os import invoke
from pynchon.util import text
from pynchon.api import render

LOGGER = lme.get_logger(__name__)

PETR = abcs.Path(constants.PYNCHON_EMBEDDED_TEMPLATES_ROOT)


@tagging.tags(click_aliases=["pat"])
class Pattern(models.ResourceManager):
    """
    Tools for working with file/directory patterns
    """

    name = "pattern"
    cli_name = "pattern"

    class config_class(abcs.Config):
        config_key: typing.ClassVar[str] =  "pattern"
        defaults = dict(include_patterns=["*/", "*/*/"])

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

    @cli.click.argument("kind", nargs=1)
    @cli.click.argument("dest", nargs=1)
    @cli.options.plan
    def sync(self, should_plan: bool = False, dest: str = None, kind: str = None):
        """ Synchronize DEST from KIND """
        # https://github.com/cookiecutter/cookiecutter/issues/784
        LOGGER.critical(f'Synchronizing "{dest}" from `{kind}`')
        tmp = self.pattern_names
        if kind not in tmp:
            LOGGER.critical(f"unrecognized pattern `{kind}`; expected one of {tmp}")
            raise SystemExit(1)
        plan = []
        destp = abcs.Path(dest)
        folder = abcs.Path(dest).absolute()
        for f in self._get_template_files(destp):
            after = self._render_file(dest=f)
            with open(f,'r') as fhandle:
                before = fhandle.read()
            if before!=after:
                # LOGGER.critical('rendering {f} creates changes!')
                fabs = f.absolute()
                plan.append(self.goal(
                    type='sync',
                    command=f'cp {destp} {fabs}',
                    resource=f,
                    ))
        if should_plan:
            LOGGER.critical( plan )
            return plan
        else:
            return plan.apply() #return dict(changes=changes)
    
    def _get_template_files(self, folder) -> typing.List:
        return list([x for x in folder.glob("*") if not x.is_dir()])
    
    def _get_template_dirs(self, folder) -> typing.List:
        return list([x for x in folder.glob("**/") if x.is_dir()])
    
    @cli.options.plan
    @cli.click.argument("dest", nargs=1)
    def render(self, dest, should_plan:bool=False):
        """ Renders content inside folder @ DEST """
        folder = abcs.Path(dest).absolute()
        name = folder.name
        if not folder.exists():
            self.logger.critical(f"Folder @ {folder} does not exist!")
        else:
            plan = super(self.__class__, self).plan()
            dirs = self._get_template_dirs(folder)
            files = self._get_template_files(folder)

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
                with open(f, "r") as fhandle:
                    if render.is_templated(fhandle.read()):
                        plan.append(self.goal(
                            resource=f, 
                            command=f"pynchon pattern render-file {f} --name {name}",
                            type="render",
                        ))

            if should_plan:
                return plan
            else:
                return self.apply(plan)

    @cli.click.option("--name", required=True)
    @cli.click.argument("dest", nargs=1)
    def render_file(self, dest=None, name='') -> bool:
        """ """
        f = abcs.Path(dest)
        assert f.exists()
        rendered = self._render_file(dest=dest,name=name)
        if rendered is None:
            raise SystemExit(1)
        else:
            with open(f, "w") as fhandle:
                fhandle.write(rendered)
            return True

    def _render_file(self, dest=None, name='') -> str:
        """ """
        f = abcs.Path(dest)
        LOGGER.warning(f"rendering `{f}` in-place")
        try:
            tmpl = render.get_template_from_file(f)
        except (Exception,) as exc:
            LOGGER.critical(f'failed to get_template_from_file @ {f}: {exc}')
            return None
        else:
            assert tmpl
            rendered = tmpl.render(
                name=name, 
                **self.project_config)            
            return rendered 

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
            fadvice = pfolder / ".scaffold.advice.json5"
            if fadvice.exists():

                advice = text.loadf.json5(file=fadvice)
                inherits = advice.get("inherits", [])
                inherits = [self.pattern_folder / p for p in inherits]
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
