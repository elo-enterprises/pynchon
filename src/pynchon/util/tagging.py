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

from collections import defaultdict

from pynchon.util import typing, lme

LOGGER = lme.get_logger(__name__)

#         # if inspect.iscoroutinefunction(func):
#         #     @functools.wraps(func)
#         #     async def async_wrapped(*args: Any, **kwargs: Any) -> Awaitable:
#         #         return await func(*args, **kwargs)
#         #     return async_wrapped
#         # else:
#         #     @functools.wraps(func)
#         #     def sync_wrapped(*args: Any, **kwargs: Any) -> Any:
#         #         return func(*args, **kwargs)
#         #     return sync_wrapped
#
#     return decorator
#
#
def tag_factory(*args) -> typing.Any:
    """ """

    class tagger(dict):
        # def tag(self, **tags):
        #     self.tags = tags
        # tag = staticmethod(
        #     functools.partial(
        #         tag,
        #         ))
        # __call__ = tag
        #

        def get_tags(self, obj: typing.Any) -> dict:
            return GLOBAL_TAG_REGISTRY[obj]

        def __getitem__(self, obj: typing.Any) -> dict:
            return self.get_tags(obj)

    return tagger()


#
#
# class TaggerFactory(dict):
#     """
#     NB: not intended to be used directly- because this is
#         effectively singleton you probably want to use
#         `util.functools.taggers` directly
#     """
#
#     registry: typing.Dict[str, typing.Any] = {}
#
#     def __getitem__(self, name: str) -> typing.Any:
#         tmp = self.registry.get(name, tag_factory(name))
#         self.registry[name] = tmp
#         return tmp
#
#     def __getattr__(self, name: str) -> typing.Any:
#         return self[name]
#
#
# taggers = TAGGERS = TaggerFactory()
GLOBAL_TAG_REGISTRY = defaultdict(dict)


class tagsM:
    GLOBAL_TAG_REGISTRY.__iter__

    def __call__(self, **tags):
        def decorator(func: typing.Callable) -> typing.Callable:
            merged = {**GLOBAL_TAG_REGISTRY.get(func, {}), **tags}
            # LOGGER.debug(f"tagging {func} with {merged}")
            GLOBAL_TAG_REGISTRY[func] = merged
            return func

        return decorator

    def __getitem__(self, name: str) -> typing.Any:
        # LOGGER.critical(f"requested {name}")
        tmp = GLOBAL_TAG_REGISTRY.get(name)
        tmp = tmp or tag_factory(name)
        GLOBAL_TAG_REGISTRY[name] = tmp
        return tmp

    def __getattr__(self, name: str) -> typing.Any:
        if name in 'get'.split():
            return getattr(GLOBAL_TAG_REGISTRY, name)
        return self[name]


tags = tagsM()
