""" pynchon.plugins.cookie_cutter
"""
from pynchon import abcs, cli, events, models  # noqa
from pynchon.util import lme, typing, tagging  # noqa

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
# Inside of {{ cookiecutter.project_slug }}, create index.html, site.css, and site.js.
class CookierCutter(models.ToolPlugin):
    """Tools for working with cookie-cutter"""

    name = "cookie-cutter"
    cli_name = 'cut'

    class config_class(abcs.Config):
        config_key = 'cookie-cutter'

    def sync(self):
        """ """
        # https://github.com/cookiecutter/cookiecutter/issues/784

    def new(self):
        """start new cookie-cutter"""
