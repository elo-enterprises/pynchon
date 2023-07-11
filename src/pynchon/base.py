"""
"""
import pydantic

Field = pydantic.Field
import typing

from pynchon.util import text


class BaseModel(pydantic.BaseModel):
    """ """

    class Config:
        arbitrary_types_allowed = True
        # https://github.com/pydantic/pydantic/discussions/5159
        frozen = True
        include: typing.Set[str] = set()
        exclude: typing.Set[str] = set()

    def json(self, **kwargs):
        return text.to_json(self.dict(**kwargs))

    def items(self):
        return self.dict().items()

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
        # Include and exclude properties
        include = include or set()
        include = include.union(getattr(self.Config, "include", set()))
        if len(include) == 0:
            include = None

        exclude = exclude or set()
        exclude = exclude.union(getattr(self.Config, "exclude", set()))
        if len(exclude) == 0:
            exclude = None
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

    def __repr__(self):
        return f"<{self.__class__.__name__}[..]>"

    __str__ = __repr__
