"""
"""
from memoized_property import memoized_property

from pynchon.util import lme

LOGGER = lme.get_logger(__name__)

class classproperty(object):
    def __init__(self, f):
        self.f = f
    def __get__(self, obj, owner):
        return self.f(owner)

class Config(dict):
    """ """

    parent = None
    priority = 100
    config_key = None
    override_from_base = True

    @classproperty
    def logger(kls):
        """ """
        return lme.get_logger(f"Config['{kls.config_key}']")

    def __init__(self, **kwargs):
        """ """
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
                self.logger.warning(
                    f"property '{p}' exists, but provided kwargs overrides it"
                )
                continue
            self[p] = getattr(self, p)
