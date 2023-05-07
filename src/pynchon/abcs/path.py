""" {{pkg}}.abcs.path
"""
import os
import json
from types import MappingProxyType
from fnmatch import fnmatch

from pynchon.util import lme, typing

LOGGER = lme.get_logger(__name__)


class Path(typing.PathType):
    """ """

    def path_truncated(self):
        """ """
        return self.parents[0] / self.stem_truncated()

    def full_extension(self):
        """
        no extension truncation, i.e. `.tar.gz`
        """
        return self.name[self.name.find('.') :]

    def stem_truncated(self):
        """truncated stem"""
        return self.name[: self.name.rfind(self.full_extension())]

    def siblings(self):
        return self.parents[0].list()

    def match_any_glob(self, exclude_patterns: typing.List[str], quiet: bool = True):
        for exclude in exclude_patterns:
            match = self.match_glob(exclude)
            if match:
                quiet or LOGGER.info(f"{self} matches exclude @{match}")
                return match

    def match_glob(self, pattern):
        """ """
        return fnmatch(str(self), str(pattern)) and pattern

    def has_file(self, fname) -> bool:
        """ """
        return self.absolute() in [p.absolute() for p in Path(fname).parents]

    def list(self) -> typing.List[str]:
        return [x for x in os.listdir(str(self))]


class JSONEncoder(json.JSONEncoder):
    """ """

    def encode(self, obj):
        """ """
        result = None

        def default():
            return super(JSONEncoder, self).encode(obj)

        try:
            toJSON = getattr(obj, 'toJSON', default) or default
        except (Exception,) as exc:
            toJSON = default
        return toJSON()

    # FIXME: use multimethod
    def default(self, obj):
        toJSON = getattr(obj, 'toJSON', None)
        if toJSON is not None:
            LOGGER.debug(f'{type(object)} brings custom toJSON')
            return obj.toJSON()
        if isinstance(obj, Path):
            return str(obj)
        if isinstance(obj, MappingProxyType):
            return dict(obj)
        if isinstance(obj, map):
            return list(obj)
        return super(JSONEncoder, self).default(obj)
