""" pynchon.abcs
"""
import os
import json

from extended_pathlib import Path as BasePath

import pynchon

LOGGER = pynchon.get_logger(__name__)

class JSONEncoder(json.JSONEncoder):
    def default(self, obj):
        # Match all the types you want to handle in your converter
        if isinstance(obj, Path):
            return str(obj)
        return json.JSONEncoder.default(self, obj)

class Path(type(BasePath())):
    def list(self):
        return os.listdir(str(self))

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
            # LOGGER.debug(f'initializing property: {p}')
            if p in kwargs:
                LOGGER.warning(
                    f"property '{p}' exists, but provided kwargs overrides it"
                )
                continue
            self[p] = getattr(self, p)

    # @property
    # def _pynchon_conf(self):
    #     from pynchon.api.pynchon import PynchonConfig
    #     return PynchonConfig()
