""" pynchon.abcs.config
"""
import collections

from pynchon.fleks.meta import Meta
from pynchon.util import lme, text, typing
from pynchon.util.tagging import tags

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

    def __init__(self, **this_config) -> None:
        """

        :param **this_config:

        """
        called_defaults = this_config
        kls_defaults = getattr(self.__class__, "defaults", {})
        super().__init__(**{**kls_defaults, **called_defaults})
        conflicts = []
        for pname in self.__class__.__properties__:
            if pname in called_defaults or pname in kls_defaults:
                conflicts.append(pname)
                continue
            else:
                self[pname] = getattr(self, pname)
        self.resolve_conflicts(conflicts)

    @typing.classproperty
    def _logging_name(kls):
        return f"<{kls.__name__}['{kls.config_key}']"

    @typing.classproperty
    def logger(kls):
        """

        :param kls:

        """
        return lme.get_logger(f"{kls._logging_name}")

    def resolve_conflicts(self, conflicts: typing.List) -> None:
        """

        :param conflicts: typing.List:
        :param conflicts: typing.List:

        """
        conflicts and LOGGER.info(
            f"'{self.config_key}' is resolving {len(conflicts)} conflicts.."
        )

        record = collections.defaultdict(list)
        for pname in conflicts:
            prop = getattr(self.__class__, pname)
            strategy = tags.get(prop, {}).get("conflict_strategy", "user_wins")
            if strategy == "user_wins":
                record[strategy].append(f"{self.config_key}.{pname}")
            elif strategy == "override":
                val = getattr(self, pname)
                self[pname] = val
                record[strategy] += [pname]
            else:
                LOGGER.critical(f"unsupported conflict-strategy! {strategy}")
                raise SystemExit(1)

        overrides = record["override"]
        if overrides:
            pass

        user_wins = record["user_wins"]
        if user_wins:
            msg = "these keys have defaults, but user-provided config wins: "
            tmp = text.to_json(user_wins)
            self.logger.info(f"{msg}\n  {tmp}")

    def __repr__(self):
        return f"<{self.__class__._logging_name}>"

    __str__ = __repr__
