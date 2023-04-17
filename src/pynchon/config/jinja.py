""" pynchon.config.jinja
"""
from pynchon import abcs
from pynchon.util import lme, typing

LOGGER = lme.get_logger(__name__)

from . import initialized


class JinjaConfig(abcs.Config):
    """ """

    config_key = "jinja"

    @property
    def _base(self) -> abcs.AttrDict:
        return abcs.AttrDict(**initialized["pynchon"].get("jinja", {}))

    @property
    def includes(self) -> typing.List:
        docs_root = initialized["pynchon"].get("docs_root", None)
        docs_root = docs_root and abcs.Path(docs_root)
        if docs_root:
            extra = [abcs.Path(docs_root.joinpath("templates"))]
        else:
            LOGGER.warning("`docs_root` is not set; cannot guess `jinja.includes`")
            extra = []
        return extra + self._base.get("includes", [])
