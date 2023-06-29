""" pynchon.abcs.config
"""
import json 
import collections

from pynchon.util import lme, text, typing
from pynchon.fleks.meta import Meta
from pynchon.util.tagging import tags

LOGGER = lme.get_logger(__name__)

from pydantic import BaseModel, Field,main #ModelMetaclass
##########################
class BaseConfig(BaseModel):
    config_key:str = Field(required=True, default=None)

class Config(
    BaseModel,
    # metaclass=type('MetaD', tuple([main.ModelMetaclass,Meta]), {})
    # metaclass=Meta,
):
    """ """
    # __hash__ = object.__hash__
    config_key: typing.ClassVar[str] = None
    
    class Config:
        arbitrary_types_allowed = True
        #https://github.com/pydantic/pydantic/discussions/5159
        frozen = True
    # debug = False
    # parent = None
    # priority = 100
    # config_key: typing.ClassVar[str] =  None
    # override_from_base = True
    @classmethod
    def get_properties(cls):
        return [prop for prop in dir(cls) if isinstance(getattr(cls, prop), property) and prop not in ("__values__", "fields")]

    def dict(
        self,
        *,
        include= None,
        exclude = None,
        by_alias: bool = False,
        skip_defaults: bool = None,
        exclude_unset: bool = False,
        exclude_defaults: bool = False,
        exclude_none: bool = False,
    ) -> 'DictStrAny':
        attribs = super().dict(
            include=include,
            exclude=exclude,
            by_alias=by_alias,
            skip_defaults=skip_defaults,
            exclude_unset=exclude_unset,
            exclude_defaults=exclude_defaults,
            exclude_none=exclude_none
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
        return attribs
    
    def __getitem__(self, key, ):
        if isinstance(key, (slice,)):
            start, stop, step = key.start, key.stop, key.step
            raise Exception('niy')
        try:
            return self.dict(
                # exclude_unset=True, 
                by_alias=True)[key]
        except (KeyError,TypeError) as exc:
            # import IPython; IPython.embed()
            raise
    
    def as_dict(self, **kwargs):
        kwargs.update(
            # exclude_unset=True, 
            by_alias=True)
        return self.dict(**kwargs)
    
    def json(self, **kwargs):
        return text.to_json(self.as_dict(**kwargs))
    
    # def get(self, k, default=None):
    #     """ """
    #     return self.as_dict().get(k,default)
    
    def items(self):
        return self.as_dict().items()
    
    def __init__(self, **this_config) -> None:
        """
        """
        called_defaults = this_config
        kls_defaults = getattr(self.__class__, "defaults", {})
        super().__init__(**{**kls_defaults, **called_defaults})
        # conflicts = []
        # for pname in self.__class__.__properties__:
        #     if pname in called_defaults or pname in kls_defaults:
        #         conflicts.append(pname)
        #         continue
        #     else:
        #         self[pname] = getattr(self, pname)
        # self.resolve_conflicts(conflicts)

    # @typing.classproperty
    # def _logging_name(kls):

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
