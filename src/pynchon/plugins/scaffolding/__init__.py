""" pynchon.plugins.scaffolding
"""
from pynchon import abcs
from pynchon.util import lme, typing  # , files
from pynchon.abcs.plugin import Plugin

from .config import ScaffoldingConfig

LOGGER = lme.get_logger(__name__)


class Scaffolding(Plugin):
    """ """

    priority = 0
    name = "scaffolding"
    defaults = dict()
    config_kls = ScaffoldingConfig

    @classmethod
    def init_cli(kls):
        """pynchon.bin.scaffold:
        Option parsing for the `scaffold` subcommand
        """
        from pynchon.bin import groups
        from pynchon.bin.common import groop

        @groop("scaffold", parent=groups.entry)
        def scaffold():
            """
            Scaffolding Automation
            (Creates folder layouts and other boilerplate)
            """

        @scaffold.command("list")
        def scaffold_list():
            """list available scaffolds"""

        @scaffold.command("stat")
        def scaffold_stat():
            """status of current scaffolding"""

        @scaffold.command("diff")
        def scaffold_diff():
            """diff with known scaffolding"""

        @scaffold.command("apply")
        def scaffold_apply():
            """apply results of scaffold-plan"""

        @scaffold.command("plan")
        def scaffold_plan():
            """plan application of scaffolding"""

    def plan(self, config) -> typing.List[str]:
        """ """
        plan = super(Scaffolding, self).plan(config)
        plan += [
            f"mkdir -p {self.state.pynchon.docs_root}",
            f"pynchon project version --output {self.state.pynchon.docs_root}/VERSIONS.md",
        ]
        return plan
