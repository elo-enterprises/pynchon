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

    def endswith(self, other) -> bool:
        return str(self).endswith(other)

    def startswith(self, other) -> bool:
        return str(self).startswith(other)

    def path_truncated(self):
        """ """
        return self.parents[0] / self.stem_truncated()

    def full_extension(self):
        """no extension truncation, i.e. `.tar.gz`"""
        return self.name[self.name.find(".") :]

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
        """

        :param pattern:

        """
        return fnmatch(str(self), str(pattern)) and pattern

    def has_file(self, fname) -> bool:
        """

        :param fname:

        """
        return self.absolute() in [p.absolute() for p in Path(fname).parents]

    def list(self) -> typing.List[str]:
        return [x for x in os.listdir(str(self))]


class JSONEncoder(json.JSONEncoder):
    """ """

    def encode(self, obj):
        """

        :param obj:

        """
        result = None

        def default():
            return super(JSONEncoder, self).encode(obj)

        try:
            toJSON = getattr(obj, "toJSON", default) or default
        except (Exception,) as exc:
            toJSON = default
        return toJSON()

    # FIXME: use multimethod
    def default(self, obj):
        toJSON = getattr(obj, "toJSON", None)
        jsonify = getattr(obj, "json", None)
        as_dict = getattr(obj, "as_dict", None)
        if as_dict is not None and callable(as_dict):
            LOGGER.warning(f"{type(obj)} brings custom as_dict()")
            return obj.as_dict()
            
        elif jsonify is not None and callable(jsonify):
            LOGGER.warning(f"{type(obj)} brings custom json()")
            return obj.json()
            
        elif toJSON is not None:
            assert callable(toJSON)
            LOGGER.warning(f"{type(obj)} brings custom toJSON()")
            return obj.toJSON()
        elif isinstance(obj, Path):
            return str(obj)
        # if isinstance(obj, MappingProxyType):
        #     return dict(obj)
        elif isinstance(obj, map):
            return list(obj)
        # if typing.iscoroutine(obj):
        else:
            LOGGER.warning(f"coercing {obj} to string")
            # import IPython; IPython.embed()
            return str(obj)
        return super().default(obj)
