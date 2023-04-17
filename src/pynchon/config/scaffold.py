""" pynchon.config.scaffold
"""
from pynchon import abcs
from pynchon.util import lme

LOGGER = lme.get_logger(__name__)

# from . import initialized


class ScaffoldConfig(abcs.Config):
    """ """

    config_key = "scaffold"


#    @property
#    def includes(self) -> typing.List:
#        docs_root = initialized["pynchon"].get("docs_root", None)
#        docs_root = docs_root and abcs.Path(docs_root)
#        if docs_root:
#            extra = [abcs.Path(docs_root.joinpath("templates"))]
#        else:
#            LOGGER.warning("`docs_root` is not set; cannot guess `scaffold.includes`")
#            extra = []
#        return extra + self._base.get("includes", [])
