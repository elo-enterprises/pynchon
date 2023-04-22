""" pynchon.plugins.fixme
"""
from pynchon.abcs.plugin import Plugin


class FixMe(Plugin):
    """ """

    name = "fixme"
    config = dict
    defaults = dict()

    def plan(self, config):
        plan = super(self.__class__, self).plan(config)
        plan += [f"pynchon gen fixme --output {config.pynchon.docs_root}/FIXME.md"]
        return plan
