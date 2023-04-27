""" pynchon.abcs.config
"""
from pynchon.util import typing, lme
from pynchon.util.tagging import tags

from .meta import Meta

LOGGER = lme.get_logger(__name__)


class Config(
    dict,
    metaclass=Meta,
):
    """ """

    debug = False
    parent = None
    priority = 100
    config_key = None
    override_from_base = True

    def __str__(self):
        return repr(self)

    def __repr__(self):
        return self.__class__._logging_name

    @typing.classproperty
    def _logging_name(kls):
        return f"{kls.__name__}@{kls.config_key}"

    @typing.classproperty
    def logger(kls):
        """ """
        return lme.get_logger(f"{kls._logging_name}")

    def resolve_conflicts(self, conflicts):
        conflicts and LOGGER.debug("resolving conflicts..")
        for pname in conflicts:
            prop = getattr(self.__class__, pname)
            strategy = tags.get(prop, {}).get('conflict_strategy', 'user_wins')
            if strategy == 'user_wins':
                self.logger.info(
                    f"property for {pname} exists,"
                    " but provided kwargs overrides them"
                )
            elif strategy == 'override':
                val = getattr(self, pname)
                self[pname] = val
                # setattr(self, pname, val)
            else:
                LOGGER.critical('unsupported strategy!')
                raise SystemExit(1)

    def __init__(self, **this_config):
        """ """
        LOGGER.critical(f"initializing {self}")
        # def get_props():
        #     return [
        #         pname
        #         for pname in dir(self.__class__)
        #         if all(
        #             [
        #                 not pname.startswith("_"),
        #                 isinstance(getattr(self.__class__, pname), property),
        #             ]
        #         )
        #     ]

        called_defaults = this_config
        kls_defaults = getattr(self.__class__, 'defaults', {})
        super(Config, self).__init__(**{**kls_defaults, **called_defaults})
        conflicts = []
        for pname in self.__class__.__properties__:
            if pname in called_defaults or pname in kls_defaults:
                conflicts.append(pname)
                continue
            else:
                self[pname] = getattr(self, pname)
        self.resolve_conflicts(conflicts)
