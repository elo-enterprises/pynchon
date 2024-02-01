""" pynchon.abcs
"""

import typing

from fleks.config import Config  # noqa

from .attrdict import AttrDict  # noqa
from .path import Path  # noqa

ResourceType = typing.Union[str, Path]
