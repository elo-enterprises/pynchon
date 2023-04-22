""" pynchon.plugins.scaffolding
"""
from pynchon import abcs
from pynchon.util import lme, typing  # , files
from pynchon.abcs.plugin import Plugin

LOGGER = lme.get_logger(__name__)


class Scaffolding(Plugin):
    """ """

    priority = 0
    name = "scaffolding"
    # config = ScaffoldConfig
    defaults = dict()

    class config(abcs.Config):
        """ """

        config_key = "scaffold"

    def plan(self, config) -> typing.List[str]:
        """ """
        plan = super(Scaffolding, self).plan(config)
        plan += [
            f"mkdir -p {self.state.pynchon.docs_root}",
            f"pynchon project version --output {self.state.pynchon.docs_root}/VERSIONS.md",
        ]
        return plan
