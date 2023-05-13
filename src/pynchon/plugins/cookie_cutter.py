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

    def list(self):
        tmp = [
            [str(x.relative_to(self.config.root)), x.glob("**/*")]
            for x in super(CookierCutter, self).list()
        ]
        tmp = dict(tmp)
        keep = [x for x in tmp if not any([k.startswith(f"{x}/") for k in tmp])]
        tmp = dict(list([[k, list(v)] for k, v in tmp.items() if k in keep]))
        return tmp

    def sync(self):
        """ """
        # https://github.com/cookiecutter/cookiecutter/issues/784

    # @cli.click.option('--name','-n',default='',help='name to use',)
    @cli.click.argument("name", nargs=1)
    @cli.click.argument("kind", nargs=1)
    # @cli.click.option('--out','-o',default='',help='output ',)
    def new(self, kind, name):
        """start new cookie-cutter"""
        # tpl=self//kind
        # tmp /= kind
        # assert tmp.exists()
        plan = super(self.__class__, self).plan()
        dest = abcs.Path(name)
        assert not dest.exists()
        plan.append(
            self.goal(
                command=f"cp -rfv {tmp} {name}",
                resource=dest.absolute(),
                type="copy",
            )
        )
        # return list(tmp.glob('*'))
        return plan
