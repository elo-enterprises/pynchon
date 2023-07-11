""" pynchon.abcs.config
"""

from pynchon.util import lme, text, typing

LOGGER = lme.get_logger(__name__)

from pydantic import BaseModel, Field


##########################
class BaseConfig(BaseModel):
    config_key: str = Field(required=True, default=None)


class Config(
    BaseModel,
):
    """ """

    config_key: typing.ClassVar[str] = None

    class Config:
        arbitrary_types_allowed = True
        # https://github.com/pydantic/pydantic/discussions/5159
        frozen = True

    def __init__(self, **this_config) -> None:
        """ """
        kls_defaults = getattr(self.__class__, "defaults", {})
        super().__init__(**{**kls_defaults, **this_config})
        # conflicts = []
        # for pname in self.__class__.__properties__:
        #     if pname in called_defaults or pname in kls_defaults:
        #         conflicts.append(pname)
        #         continue
        #     else:
        #         self[pname] = getattr(self, pname)
        # self.resolve_conflicts(conflicts)

    # debug = False
    # parent = None
    # priority = 100
    # override_from_base = True

    @classmethod
    def get_properties(cls):
        return [
            prop
            for prop in dir(cls)
            if isinstance(getattr(cls, prop), property)
            and prop not in ("__values__", "fields")
        ]

    def dict(self, *args, **kwargs):
        return self._dict(*args, **kwargs)

    def _dict(
        self,
        *,
        include=None,
        exclude=None,
        by_alias: bool = True,
        skip_defaults: bool = None,
        exclude_unset: bool = False,
        exclude_defaults: bool = False,
        exclude_none: bool = False,
    ):
        # -> "DictStrAny":
        attribs = super().dict(
            include=include,
            exclude=exclude,
            by_alias=by_alias,
            skip_defaults=skip_defaults,
            exclude_unset=exclude_unset,
            exclude_defaults=exclude_defaults,
            exclude_none=exclude_none,
        )
        props = self.get_properties()
        # Include and exclude properties
        if include:
            props = [prop for prop in props if prop in include]
        if exclude:
            props = [prop for prop in props if prop not in exclude]

        # Update the attribute dict with the properties
        if props:
            attribs.update({prop: getattr(self, prop) for prop in props})
        for key, val in attribs.items():
            if isinstance(val, (BaseModel,)):
                attribs[key] = val.dict(
                    include=include,
                    exclude=exclude,
                    by_alias=by_alias,
                    skip_defaults=skip_defaults,
                    exclude_unset=exclude_unset,
                    exclude_defaults=exclude_defaults,
                    exclude_none=exclude_none,
                )
        return attribs

    def __getitem__(
        self,
        key,
    ):
        if isinstance(key, (slice,)):
            start, stop, step = key.start, key.stop, key.step
            raise Exception("niy")
        try:
            return self.dict(
                # exclude_unset=True,
                by_alias=True
            )[key]
        except (KeyError, TypeError) as exc:
            # import IPython; IPython.embed()
            raise

    # def as_dict(self, **kwargs):
    #     kwargs.update(
    #         # exclude_unset=True,
    #         by_alias=True
    #     )
    #     return self.dict(**kwargs)

    def json(self, **kwargs):
        return text.to_json(self.dict(**kwargs))

    def items(self):
        return self.dict().items()

    # @typing.classproperty
    # def logger(kls):
    #     """
    #
    #     :param kls:
    #
    #     """
    #     return lme.get_logger(f"{kls._logging_name}")

    # def resolve_conflicts(self, conflicts: typing.List) -> None:
    #     """
    #
    #     :param conflicts: typing.List:
    #     :param conflicts: typing.List:
    #
    #     """
    #     conflicts and LOGGER.info(
    #         f"'{self.config_key}' is resolving {len(conflicts)} conflicts.."
    #     )
    #
    #     record = collections.defaultdict(list)
    #     for pname in conflicts:
    #         prop = getattr(self.__class__, pname)
    #         strategy = tags.get(prop, {}).get("conflict_strategy", "user_wins")
    #         if strategy == "user_wins":
    #             record[strategy].append(f"{self.config_key}.{pname}")
    #         elif strategy == "override":
    #             val = getattr(self, pname)
    #             self[pname] = val
    #             record[strategy] += [pname]
    #         else:
    #             LOGGER.critical(f"unsupported conflict-strategy! {strategy}")
    #             raise SystemExit(1)
    #
    #     overrides = record["override"]
    #     if overrides:
    #         pass
    #
    #     user_wins = record["user_wins"]
    #     if user_wins:
    #         msg = "these keys have defaults, but user-provided config wins: "
    #         tmp = text.to_json(user_wins)
    #         self.logger.info(f"{msg}\n  {tmp}")
    # def __iter__(self):
    #     return iter(self.as_dict())
    # def __rich__(self):
    #     return self.as_dict()

    def __repr__(self):
        return f"<{self.__class__.__name__}['{self.__class__.config_key}']>"

    __str__ = __repr__


from pynchon.util.text import dumps

dumps.JSONEncoder.register_encoder(type=Config, fxn=lambda x: dumps.json(x.dict()))
