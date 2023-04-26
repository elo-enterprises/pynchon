""" pynchon.abcs.config
"""
from pynchon.util import typing, lme

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
        conflicts = []
        for pname in props:
            if pname in kwargs:
                conflicts.append(pname)
                continue
            self[pname] = getattr(self, pname)
        if conflicts:
            from pynchon.util import tagging
            LOGGER.debug("resolving conflicts..")
            for pname in conflicts:
                prop = getattr(self.__class__, pname)
                strategy = tagging.tags.get(prop,{}).get('conflict_strategy','user_wins')
                if strategy=='user_wins':
                    self.logger.info(
                        f"property for {pname} exists,"
                        " but provided kwargs overrides them")
                elif strategy=='override':
                    self[pname] = getattr(self, pname)
                else:
                    LOGGER.critical('unsupported strategy!')
                    raise SystemExit(1)
