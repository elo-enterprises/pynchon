"""
"""
import re

from pynchon.util import typing


def snake_case(name: str) -> str:
    """ """
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()


DEFAULT_NORMALIZATION_RULES = {' ': '_', '/': '_', '-': '_'}


def normalize(
    txt: str = "",
    post: typing.List[typing.Callable] = [
        lambda _: _.lower(),
        lambda _: re.sub('_+', '_', _),
    ],
    rules: typing.List[typing.Callable] = DEFAULT_NORMALIZATION_RULES,
) -> str:
    """
    normalizes input text, with support for parametric rules/post-processing
    """
    tmp = txt
    for k, v in rules.items():
        tmp = tmp.replace(k, v)
    for fxn in post:
        tmp = fxn(tmp)
    return tmp
