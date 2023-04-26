""" pynchon.util.tagging:

    helpers for tagging things with decorators.  this stuff is simple but
    pretty abstract; to understand this it's probably better to just look
    at how it's used.  you might want to start by just checking out the
    tests[1] or the use-cases[2,3] instead.

    [1]: tests/units/test_util_tagging.py
    [2]: pynchon.tagging
    [3]: utility-airflow.git/utility/dags/frontier-bronze-etl.py
"""
from __future__ import annotations

import inspect
import functools

from pynchon.util import typing, lme

LOGGER = lme.get_logger(__name__)


def tag(tag_storage_var: str = '_tags', **tags: typing.OptionalAny) -> typing.Callable:
    """ """

    def decorator(func: typing.Callable) -> typing.Callable:
        merged = {**getattr(func, tag_storage_var, {}), **tags}
        LOGGER.debug(f"tagging {func} with {merged}")
        setattr(func, tag_storage_var, merged)
        return func
        # if inspect.iscoroutinefunction(func):
        #     @functools.wraps(func)
        #     async def async_wrapped(*args: Any, **kwargs: Any) -> Awaitable:
        #         return await func(*args, **kwargs)
        #     return async_wrapped
        # else:
        #     @functools.wraps(func)
        #     def sync_wrapped(*args: Any, **kwargs: Any) -> Any:
        #         return func(*args, **kwargs)
        #     return sync_wrapped

    return decorator


def tag_factory(tag_storage_var: str) -> typing.Any:
    """ """

    class tagger(dict):
        tag = staticmethod(functools.partial(tag, tag_storage_var=tag_storage_var))
        __call__ = tag

        def get_tags(self, obj: typing.Any) -> dict:
            return getattr(obj, tag_storage_var, {})

        def __getitem__(self, obj: typing.Any) -> dict:
            return self.get_tags(obj)

    return tagger()


class TaggerFactory(dict):
    """
    NB: not intended to be used directly- because this is
        effectively singleton you probably want to use
        `util.functools.taggers` directly
    """

    registry: typing.Dict[str, typing.Any] = {}

    def __getitem__(self, name: str) -> typing.Any:
        tmp = self.registry.get(name, tag_factory(name))
        self.registry[name] = tmp
        return tmp

    def __getattr__(self, name: str) -> typing.Any:
        return self[name]


taggers = TAGGERS = TaggerFactory()
