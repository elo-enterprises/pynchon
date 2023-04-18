""" pynchon.abcs
"""
import json
import os

from pynchon.util import lme, typing

from .attrdict import AttrDict  # noqa
from .config import Config  # noqa
from .path import Path
LOGGER = lme.get_logger(__name__)


class JSONEncoder(json.JSONEncoder):
    """ """

    def default(self, obj):
        if isinstance(obj, Path):
            return str(obj)
        return json.JSONEncoder.default(self, obj)

# from .config import Config
