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


class CookierCutter(models.ResourceManager):
    """Tools for working with cookie-cutter"""

    name = "cookie-cutter"
    cli_name = "cut"

    class config_class(abcs.Config):
        config_key = "cookie-cutter"
        defaults = dict(include_patterns=["*/", "*/*/"])

        @property
        def root(self):
            tmp = ETR
            tmp /= self.config_key.replace("-", "_")
            assert tmp.exists()
            return tmp

    def list(self) -> typing.Dict:
        """ Describe templates we can cut patterns from """
        tmp = [
            [str(x.relative_to(self.config.root)), x.glob("**/*")]
            for x in super(CookierCutter, self).list()
        ]
        tmp = dict(tmp)
        keep = [x for x in tmp if not any([k.startswith(f"{x}/") for k in tmp])]
        tmp = dict(list([[k, list(v)] for k, v in tmp.items() if k in keep]))
        return tmp

    # def sync(self):
    #     """ """
    #     # https://github.com/cookiecutter/cookiecutter/issues/784

    @cli.click.argument("name", nargs=1)
    def render(self, name):
        """ Renders a cookiecutter-copy in-place """
        folder = abcs.Path(name)
        if not folder.exists():
            logger.critical(f"folder @ {folder} does not exist!")
        else:
            plan = super(self.__class__, self).plan()
            dirs = list([x for x in folder.glob('**/') if x.is_dir()])
            files = list([x for x in folder.glob('*') if not x.is_dir()])
            from pynchon.api import render
            # struct=dict(files=files, dirs=dirs)
            for d in dirs:
                d = str(d.absolute())
                if '{{name}}' in d:
                    newname=d.replace('{{name}}', name)
                    plan.append(self.goal(
                        resource=newname,
                        command=f"mv '{d}' {newname}",
                        type='move',
                    ))
            for f in files:
                f = str(f.absolute())
                if '{{name}}' in f:
                    newname=f.replace('{{name}}', name)
                    plan.append(self.goal(
                        resource=newname,
                        command=f"mv '{f}' {newname}",
                        type='move',
                    ))
            results = self.apply(plan)
            # plan = super(self.__class__, self).plan()
            # dirs = list([x for x in folder.glob('**/') if x.is_dir()])
            files = list([x for x in folder.glob('*') if not x.is_dir()])
            for f in files:
                LOGGER.warning(f'rendering {f} in-place')
                # with open(f,'r') as fhandle:
                #     content=fhandle.read()
                tmpl = render.get_template_from_file(f)
                assert tmpl
                rendered = tmpl.render(name=name,**self.project_config)
                with open(f,'w') as fhandle:
                    fhandle.write(rendered)
            return dict(rendered=files)
    # @cli.click.option('--name','-n',default='',help='name to use',)
    @cli.click.argument("name", nargs=1)
    @cli.click.argument("kind", nargs=1)
    def new(self, kind, name): # -> typing.PlanMaybe:
        """start new cookie-cutter"""
        # tpl=self//kind
        # tmp /= kind
        # assert tmp.exists()
        tmp = ETR/self.name.replace('-','_')/kind
        if not tmp.exists():
            choices=set(self.list().keys())
            tmp = tmp.relative_to(abcs.Path('.').absolute())
            LOGGER.critical(f'Kind @ "{name}" suggests pattern-folder @ "{tmp}", but folder does not exist!')
            LOGGER.critical(f"Choices are: {choices}")
        else:
            plan = super(self.__class__, self).plan()
            dest = abcs.Path(name)
            assert not dest.exists(), f'{dest} already exists'
            plan.append(
                self.goal(
                    command=f"cp -rfv {tmp} {name}",
                    resource=dest.absolute(),
                    type="copy",
                )
            )
            plan.append(
                self.goal(
                    command=f"pynchon {self.cli_name} render {name}",
                    resource=dest.absolute(),
                    type="render",
                )
            )
            return self.apply(plan)
