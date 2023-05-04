""" pynchon.plugins.Core
"""
from pynchon import api, cli, models
from pynchon.bin import entry
from pynchon.core import Config as CoreConfig
from pynchon.util import lme, typing

LOGGER = lme.get_logger(__name__)


class Core(models.Planner):
    """Core Plugin"""

    name = "core"
    priority = -1
    config_class = CoreConfig

    # NB: prevents recursion when `pynchon plan` is used!
    contribute_plan_apply = False

    @typing.classproperty
    def click_group(kls):
        kls._finalized_click_groups[kls] = entry.entry
        return kls._finalized_click_groups[kls]

    @classmethod
    def get_current_config(kls):
        """ """
        from pynchon import config as config_mod

        result = getattr(config_mod, kls.get_config_key())
        return result

    @property
    def config(self):
        return self.cfg()

    def plan(self, config=None) -> typing.List:
        """Creates a plan for all plugins"""
        raise NotImplementedError()

    def apply(self, config=None) -> None:
        """Executes the result returned by planner"""
        raise NotImplementedError()

    def cfg(self):
        """Show current project config (with templating/interpolation)"""
        return self.project_config

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

    def plan(
        self,
        config=None,
    ) -> models.Plan:
        """ Runs plan for all plugins """

        config = config or self.project_config
        plan = super(self.__class__, self).plan(config)
        plugins = self.active_plugins
        plugins = [p for p in plugins if isinstance(p, models.AbstractPlanner)]
        self.logger.critical(f"Planning on behalf of: {[p.name for p in plugins]}")
        for plugin_obj in plugins:
            if not plugin_obj.contribute_plan_apply:
                continue
            self.logger.critical("=" * 20 + plugin_obj.name)
            subplan = plugin_obj.plan()
            if not subplan:
                self.logger.warning(f'subplan for {plugin_obj} is empty!')
            else:
                for g in subplan:
                    self.logger.info(f'{plugin_obj} contributes {g}')
                    plan.append(g)
        return plan
