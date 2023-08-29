""" pynchon.abcs
"""

import typing

from .attrdict import AttrDict  # noqa
from .config import Config  # noqa
from .path import Path  # noqa

ResourceType = typing.Union[str, Path]
