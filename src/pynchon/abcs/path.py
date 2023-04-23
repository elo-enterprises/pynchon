""" pynchon.abcs.path
"""
import os
import json
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


from types import MappingProxyType
class JSONEncoder(json.JSONEncoder):
    """ """

    def default(self, obj):
        if isinstance(obj, Path):
            return str(obj)
        if isinstance(obj,MappingProxyType):
            return dict(obj)
        return json.JSONEncoder.default(self, obj)
