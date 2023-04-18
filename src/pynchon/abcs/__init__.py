""" pynchon.abcs
"""
import json

from pynchon.util import lme, typing

from .path import Path
from .config import Config  # noqa
from .attrdict import AttrDict  # noqa

LOGGER = lme.get_logger(__name__)


class JSONEncoder(json.JSONEncoder):
    """ """

    def default(self, obj) -> typing.Any:
        if isinstance(obj, Path):
            return str(obj)
        return json.JSONEncoder.default(self, obj)


# from .config import Config
