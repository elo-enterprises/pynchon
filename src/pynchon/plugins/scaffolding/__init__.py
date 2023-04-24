""" pynchon.plugins.scaffolding
"""
from pynchon.util import lme, typing  # , files
from pynchon.models import Plugin
from .config import ScaffoldingConfig

LOGGER = lme.get_logger(__name__)

from pynchon.util import files

class Scaffolding(Plugin):
    """ """

    priority = 0
    name = "scaffolding"
    cli_name = 'scaffold'
    defaults = dict()
    config_kls = ScaffoldingConfig

    def match(self):
        """ returns files that match for all scaffolds """
        result={}
        for k in self.list():
            result[k]=files.find_globs([k])
        return result

    def list(self):
        """list available scaffolds"""
        return list(self.get_current_config().keys())

    def stat(self):
        """status of current scaffolding"""
        for pattern,file_list in self.match():
            for fname in file_list:
                return dict(NotImplementedError=True)
    def diff(self):
        """diff with known scaffolding"""

    def plan(self, config) -> typing.List[str]:
        """ """
        plan = super(Scaffolding, self).plan(config)
        plan += [
            f"mkdir -p {self.state.pynchon.docs_root}",
            f"pynchon project version --output {self.state.pynchon.docs_root}/VERSIONS.md",
        ]
        return plan
