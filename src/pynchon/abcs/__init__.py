""" pynchon.abcs
"""
import json

from pynchon.util import lme, typing

from .attrdict import AttrDict  # noqa
from .config import Config  # noqa
from .path import Path

LOGGER = lme.get_logger(__name__)


class JSONEncoder(json.JSONEncoder):
    """ """

    def default(self, obj) -> typing.Any:
        if isinstance(obj, Path):
            return str(obj)
        return json.JSONEncoder.default(self, obj)


# from .config import Config
