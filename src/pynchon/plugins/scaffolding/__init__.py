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
        scaffold = Plugin.init_cli(kls)
        from pynchon.bin import common

        for method_name in dir(kls):
            fxn = getattr(kls, method_name)
            FORBIDDEN = 'init_cli plan apply'.split()
            test = hasattr(fxn, '__name__') and all(
                [
                    callable(fxn),
                    not fxn.__name__.startswith('__'),
                    type(fxn).__name__ == 'function',
                    fxn.__name__ not in FORBIDDEN,
                ]
            )
            if test:
                LOGGER.debug(f"wrapping {fxn} for CLI..")
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
