""" pynchon.plugins.scaffolding
"""
from pynchon import abcs
from pynchon.util import lme, typing, files  # , files
from pynchon.models import Plugin

from .config import ScaffoldingConfig

LOGGER = lme.get_logger(__name__)


class Scaffolding(Plugin):
    """ """

    priority = 0
    name = "scaffolding"
    cli_name = 'scaffold'
    defaults = dict()
    config_kls = ScaffoldingConfig

    @property
    def plugin_config(self):
        return self.get_current_config()

    def match(self, pattern=None):
        """returns files that match for all scaffolds"""
        if pattern:
            return files.find_globs([pattern], quiet=True)
        else:
            matches = {}
            for scaffold in self.scaffolds:
                LOGGER.debug(f"scaffold @ `{scaffold.pattern}` with scope {scaffold.scope}:")
                these_matches = self.match(pattern=scaffold.pattern)
                tmp={**scaffold,**dict(matches=these_matches)}
                tmp.pop('pattern') #NB: re-keying on this
                matches[scaffold.pattern] = tmp
            return matches

    @property
    def scaffolds(self):
        result = self.plugin_config.get('scaffolds',[])
        return [
            abcs.AttrDict(
                name=x.get('name','unnamed scaffold'),
                scope=x.get('scope','*'),
                pattern=x['pattern'],)
                for x in result]

    def list(self):
        """list available scaffolds"""
        return self.scaffolds

    def stat(self):
        """status of current scaffolding"""
        for pattern, file_list in self.match():
            for fname in file_list:
                return dict(NotImplementedError=True)

    def diff(self):
        """diff with known scaffolding"""
        return dict(NotImplementedError=True)

    def plan(self, config) -> typing.List[str]:
        """ """
        plan = super(Scaffolding, self).plan(config)
        plan += [
            f"mkdir -p {self.state.pynchon.docs_root}",
            f"pynchon project version --output {self.state.pynchon.docs_root}/VERSIONS.md",
        ]
        return plan
