""" pynchon.plugins.Core
"""
from pynchon import models, cli
from pynchon.api import project
from pynchon.bin import entry
from pynchon.core import Config as CoreConfig
from pynchon.util import lme, typing

LOGGER = lme.get_logger(__name__)


class Core(models.Planner):
    """Core Plugin"""

    name = "core"
    config_class = CoreConfig
    contribute_plan_apply = False

    @typing.classproperty
    def click_group(kls):
        kls._finalized_click_groups[kls] = entry.entry
        return kls._finalized_click_groups[kls]

    @classmethod
    def get_current_config(kls):
        """ """
        from pynchon import config as config_mod

        result = getattr(config_mod, getattr(kls.config_class, 'config_key', kls.name))
        return result

    def plan(self, config=None) -> typing.List:
        """Creates a plan for all plugins"""
        raise NotImplementedError()

    def apply(self, config=None) -> None:
        """Executes the result returned by planner"""
        raise NotImplementedError()

    def cfg(self):
        """Show current project config (with templating/interpolation)"""
        return project.get_config()

    @property
    def config(self):
        return self.cfg()

    @cli.click.option('--bash', default=False, is_flag=True, help='bootstrap bash')
    @cli.click.option('--tox', default=False, is_flag=True, help='bootstrap tox')
    def bootstrap(
        self,
        bash: bool = False,
        tox: bool = False,
    ) -> None:
        """
        Bootstrap for shell integration, etc
        """
        from pynchon.api import render

        if bash:
            LOGGER.warning("This is intended to be run through a pipe, as in:")
            LOGGER.critical("pynchon bootstrap --bash | bash")
            result = render.get_template('pynchon/bootstrap/bash.sh').render(
                self.config
            )
            fname = '.tmp.pynchon.completions.sh'
            with open(fname, 'w') as fhandle:
                fhandle.write(result)
            LOGGER.debug(f"Wrote {fname}.")
            LOGGER.debug(
                "To use completion hints every time they are present "
                "in a folder add this to .bashrc:"
            )
            LOGGER.info(render.get_template('pynchon/bootstrap/bashrc.sh').render({}))

            # print(f"source /dev/stdin < <(cat {fname})")
        elif tox:
            result = render.get_template('pynchon/tox.ini')
            print(result)

    def raw(self) -> None:
        """
        Returns (almost) raw config,
        without interpolation
        """
        from pynchon.config import RAW

        return RAW
