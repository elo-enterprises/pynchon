""" pynchon.abcs
"""
import os
import json

from pathlib import Path as BasePath

import pynchon

LOGGER = pynchon.get_logger(__name__)


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


class Config(dict):
    """ """

    def __init__(self, **kwargs):
        super(Config, self).__init__(**kwargs)
        props = [
            p
            for p in dir(self.__class__)
            if all(
                [
                    not p.startswith("_"),
                    isinstance(getattr(self.__class__, p), property),
                ]
            )
        ]
        for p in props:
            if p in kwargs:
                LOGGER.warning(
                    f"property '{p}' exists, but provided kwargs overrides it"
                )
                continue
            self[p] = getattr(self, p)
