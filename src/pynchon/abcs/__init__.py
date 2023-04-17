""" pynchon.abcs
"""
import json
import os
from pathlib import Path as BasePath

from memoized_property import memoized_property

from pynchon.util import lme, typing

from .attrdict import AttrDict

LOGGER = lme.get_logger(__name__)


class JSONEncoder(json.JSONEncoder):
    """ """

    def default(self, obj):
        if isinstance(obj, Path):
            return str(obj)
        return json.JSONEncoder.default(self, obj)


class Path(type(BasePath())):
    """ """

    def has_file(self, fname):
        """ """
        p = Path(fname)
        if not p.is_absolute():
            try:
                tmp = p.relative_to(self)
            except ValueError:
                tmp = p
            return self.joinpath(tmp).exists()
        else:
            return (
                Path(p.parent).absolute() == self.absolute() and p.name in self.list()
            )

    def list(self):
        return [x for x in os.listdir(str(self))]


from .config import Config
