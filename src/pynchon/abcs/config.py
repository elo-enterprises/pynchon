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

    @typing.classproperty
    def _logging_name(kls):
        return f"{kls.__name__}@{kls.config_key}"

    @typing.classproperty
    def logger(kls):
        """ """
        return lme.get_logger(f"{kls._logging_name}")

    def __repr__(self):
        return f"<{self.__class__._logging_name}>"

    __str__ = __repr__

    def __init__(self, **this_config):
        """ """
        # LOGGER.critical(f"initializing {self}")
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

    def resolve_conflicts(self, conflicts):
        """ """
        conflicts and LOGGER.info(f"'{self.config_key}' is resolving conflicts..")
        for pname in conflicts:
            prop = getattr(self.__class__, pname)
            strategy = tags.get(prop, {}).get('conflict_strategy', 'user_wins')
            if strategy == 'user_wins':
                self.logger.info(
                    f"'{self.config_key}.{pname}' has prop-def,"
                    " but provided kwargs overrides them"
                )
            elif strategy == 'override':
                val = getattr(self, pname)
                self[pname] = val
            else:
                LOGGER.critical(f'unsupported conflict-strategy! {strategy}')
                raise SystemExit(1)
