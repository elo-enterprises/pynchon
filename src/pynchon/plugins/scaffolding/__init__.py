""" pynchon.plugins.scaffolding
"""
from pynchon.util import lme, typing  # , files
from pynchon.models import Plugin
from .config import ScaffoldingConfig

LOGGER = lme.get_logger(__name__)


class Scaffolding(Plugin):
    """ """

    priority = 0
    name = "scaffolding"
    cli_name='scaffold'
    defaults = dict()
    config_kls = ScaffoldingConfig

    def list(self):
        """list available scaffolds"""
        return self.config.items()

    def stat(self):
        """status of current scaffolding"""

    def diff(self):
        """diff with known scaffolding"""

    @staticmethod
    def init_cli(kls):
        """pynchon.bin.scaffold:
        Option parsing for the `scaffold` subcommand
        """
        from pynchon.plugins import registry as plugins_registry
        if 'obj' not in plugins_registry[kls.name]:
            from pynchon.api import project
            project.get_config()
        obj = plugins_registry[kls.name]['obj']
        from pynchon.bin import common
        scaffold = Plugin.init_cli(kls)
        FORBIDDEN = 'defaults logger init_cli plan apply'.split()
        for method_name in dir(obj):
            if method_name.startswith('_') or method_name in FORBIDDEN:
                continue
            fxn = getattr(obj, method_name)
            if type(fxn).__name__!='method':
                continue
            LOGGER.critical(f"wrapping {[method_name, type(fxn)]} for CLI..")
            tmp = common.kommand(
                fxn.__name__,
                parent=scaffold,
            )(fxn)

    def plan(self, config) -> typing.List[str]:
        """ """
        plan = super(Scaffolding, self).plan(config)
        plan += [
            f"mkdir -p {self.state.pynchon.docs_root}",
            f"pynchon project version --output {self.state.pynchon.docs_root}/VERSIONS.md",
        ]
        return plan
