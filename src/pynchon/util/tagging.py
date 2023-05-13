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

from pynchon.util import lme, typing

LOGGER = lme.get_logger(__name__)


# FIXME: avoid collisions by namespacing like this:
# https://multiple-dispatch.readthedocs.io/en/latest/design.html#namespaces-and-dispatch
GLOBAL_TAG_REGISTRY = defaultdict(dict)


def tag_factory(*args) -> typing.Any:
    """
    :param *args:
    """

    class tagger(dict):
        def get_tags(self, obj: typing.Any) -> dict:
            return GLOBAL_TAG_REGISTRY[obj]

        def __getitem__(self, obj: typing.Any) -> dict:
            return self.get_tags(obj)

    return tagger()


TagDict = typing.Dict[str, typing.Any]


class tagsM:
    def __call__(self, **tags: TagDict):
        def decorator(func: typing.Callable) -> typing.Callable:
            merged = {**GLOBAL_TAG_REGISTRY.get(func, {}), **tags}
            # LOGGER.debug(f"tagging {func} with {merged}")
            GLOBAL_TAG_REGISTRY[func] = merged
            return func

        return decorator

    def __getattr__(self, name: str) -> typing.Any:
        if name in "get".split():
            return getattr(GLOBAL_TAG_REGISTRY, name)
        return self[name]

    @typing.validate_arguments
    def __setitem__(self, item: typing.Any, tags: TagDict):
        assert tags is not None
        GLOBAL_TAG_REGISTRY[item] = tags

    # @typing.validate_arguments
    # -> dict[str, typing.Any]
    def __getitem__(self, item: typing.Any) -> TagDict:
        tmp = GLOBAL_TAG_REGISTRY.get(item, {})
        if not tmp and callable(item) and type(item) == typing.MethodType:
            fxn = item
            cfxn = getattr(fxn.__self__.__class__, fxn.__name__)
            tmp = GLOBAL_TAG_REGISTRY.get(cfxn, {})
            # if tmp:
            #     LOGGER.critical(
            #         f'missing tags for {item}; setting tags from parent @ {cfxn}'
            #     )
        tmp = tmp or tag_factory(item)
        self.__setitem__(item, tmp)
        return tmp or {}

    __iter__ = GLOBAL_TAG_REGISTRY.__iter__


tags = tagsM()


def tagged_property(**ftags):
    """Equivalent to:
    @tagging.tags(foo=bar)
    @property
    def method(self):
        ...
    """

    def dec(fxn):
        @tags(**ftags)
        @property
        def newf(*args, **kwargs):
            return fxn(*args, **kwargs)

        return newf

    return dec
