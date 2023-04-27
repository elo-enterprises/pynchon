""" pynchon.abcs.path
"""
import os
import json

# from glob import glob
from fnmatch import fnmatch
from pathlib import Path as BasePath

from pynchon.util import lme, typing

LOGGER = lme.get_logger(__name__)


class Path(type(BasePath())):
    """ """

    def match_any_glob(self, exclude_patterns: typing.List[str]):
        for exclude in exclude_patterns:
            match = self.match_glob(exclude)
            if match:
                LOGGER.debug(f"{self} matches exclude @{match}")
                return match

    def match_glob(self, pattern):
        """ """
        return fnmatch(str(self), str(pattern)) and pattern

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
        if isinstance(obj, MappingProxyType):
            return dict(obj)
        return json.JSONEncoder.default(self, obj)
