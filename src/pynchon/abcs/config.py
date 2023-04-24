""" pynchon.abcs.config
"""
from pynchon.util import lme, typing

LOGGER = lme.get_logger(__name__)


class Config(dict):
    """ """

    debug = False
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
        overridden = []
        for p in props:
            if p in kwargs:
                overridden.append(p)
                continue
            self[p] = getattr(self, p)
        msg=f"properties for {overridden} exist, but provided kwargs overrides them"
        self.logger.info(msg)
