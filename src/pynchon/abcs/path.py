""" pynchon.abcs.path
"""
import os
from pathlib import Path as BasePath

from pynchon.util import lme, typing

LOGGER = lme.get_logger(__name__)


class Path(type(BasePath())):
    """ """

    def has_file(self, fname) -> bool:
        """ """
        return self.absolute() in [p.absolute() for p in Path(fname).parents]

    def list(self) -> typing.List[str]:
        return [x for x in os.listdir(str(self))]
