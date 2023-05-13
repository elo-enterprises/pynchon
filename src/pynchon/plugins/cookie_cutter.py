""" pynchon.plugins.cookie_cutter
"""
from pynchon import abcs, cli, events, models  # noqa
from pynchon.util import lme, tagging, typing  # noqa

LOGGER = lme.get_logger(__name__)


# https://cookiecutter.readthedocs.io/en/stable/tutorials/tutorial2.html
# mkdir -p ~/.cookie-cutter')
# mkdir cookiecutter-website-simple
# cd cookiecutter-website-simple/
#
# Step 2: Create project_slug Directory
#
#  Create a directory called {{ cookiecutter.project_slug }}.
#
# This value will be replaced with the repo name of projects that you generate from this cookiecutter.
# Step 3: Create Files
#
from pynchon import constants

ETR = abcs.Path(constants.PYNCHON_EMBEDDED_TEMPLATES_ROOT)


class Pattern(models.ResourceManager):
    """Tools for working with file/directory patterns"""

    class config_class(abcs.Config):
        config_key = "cookie-cutter"
        defaults = dict(include_patterns=["*/", "*/*/"])

        @property
        def root(self):
            tmp = ETR
            tmp /= self.config_key.replace("-", "_")
            assert tmp.exists()
            return tmp

    name = "cookie-cutter"
    cli_name = "cut"

    def list(self) -> typing.Dict:
        """Describe templates we can cut patterns from"""
        tmp = [
            [str(x.relative_to(self.config.root)), x.glob("**/*")]
            for x in super(self.__class__, self).list()
        ]
        tmp = dict(tmp)
        keep = [x for x in tmp if not any([k.startswith(f"{x}/") for k in tmp])]
        tmp = dict(list([[k, list(v)] for k, v in tmp.items() if k in keep]))
        return tmp

    @cli.click.argument("kind", nargs=1)
    @cli.click.argument("dest", nargs=1)
    def sync(self, dest: str = None, kind: str = None):
        """Synchronize DEST from KIND"""
        # https://github.com/cookiecutter/cookiecutter/issues/784

    @cli.click.argument("dest", nargs=1)
    def render(self, dest):
        """Renders content in DEST"""
        folder = abcs.Path(dest)
        if not folder.exists():
            self.logger.critical(f"folder @ {folder} does not exist!")
        else:
            plan = super(self.__class__, self).plan()
            name = folder.stem
            dirs = list([x for x in folder.glob("**/") if x.is_dir()])
            files = list([x for x in folder.glob("*") if not x.is_dir()])
            from pynchon.api import render

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
            results = self.apply(plan)
            files = list([x for x in folder.glob("*") if not x.is_dir()])
            for f in files:
                LOGGER.warning(f"rendering {f} in-place")
                tmpl = render.get_template_from_file(f)
                assert tmpl
                rendered = tmpl.render(name=name, **self.project_config)
                with open(f, "w") as fhandle:
                    fhandle.write(rendered)
            return dict(rendered=files)

    @cli.click.argument("dest", nargs=1)
    @cli.click.argument("kind", nargs=1)
    def clone(self, kind: str = None, name: str = None):
        """Clones PATTERN to DEST"""
        raise NotImplementedError()

    @property
    def pattern_folder(self):
        return ETR / self.name.replace("-", "_")

    @cli.click.argument("name", nargs=1)
    @cli.click.argument("kind", nargs=1)
    # @cli.click.option("--overwrite",is_flag=True, default=False)
    def new(self, kind, name, overwrite: bool = False):
        """Instantiates PATTERN to NAME"""
        pfolder = self.pattern_folder / kind
        if not pfolder.exists():
            choices = set(self.list().keys())
            tmp = pfolder.relative_to(abcs.Path(".").absolute())
            LOGGER.critical(
                f'Kind @ "{name}" suggests pattern-folder @ "{tmp}", but folder does not exist!'
            )
            LOGGER.critical(f"Choices are: {choices}")
        else:
            plan = super(self.__class__, self).plan()
            dest = abcs.Path(name).absolute()
            if dest.exists():
                LOGGER.critical(f"{dest} already exists!")
                return False
            plan.append(
                self.goal(
                    command=f"cp -rfv {pfolder} {dest}",
                    resource=dest,
                    type="copy",
                )
            )
            plan.append(
                self.goal(
                    # callable=lambda: self.render(name)
                    command=f"{self.click_entry.name} {self.cli_name} render {name}",
                    resource=dest,
                    type="recursive-render",
                )
            )
            result = self.apply(plan)
            return result.ok
