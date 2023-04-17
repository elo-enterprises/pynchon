""" pynchon.abcs.config
"""
# from memoized_property import memoized_property

from pynchon.util import lme, typing

LOGGER = lme.get_logger(__name__)


class Config(dict):
    """ """

    parent = None
    priority = 100
    config_key = None
    override_from_base = True

    @typing.classproperty
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
