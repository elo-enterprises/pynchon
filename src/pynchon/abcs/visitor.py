""" pynchon.abcs.visitor
"""
# import sys
import pydash

from pynchon import abcs
from pynchon.util import lme

LOGGER = lme.get_logger(__name__)


class Visitor:
    def __init__(
        self,
        filter_path=lambda _: True,
        filter_value=lambda _: True,
        # trigger=lambda p, v: [print(f"[{p}: {v}]", file=sys.stderr)],
        trigger=lambda p, v: (p, v),
        paths=[],
        obj=None,
        **kwargs,
    ):
        """ """
        self.conf = kwargs
        self.filter_path = filter_path
        self.filter_value = filter_value
        self.trigger = trigger

    def __call__(
        self,
        path=None,
        value=None,
    ):
        if all([self.filter_path(path), self.filter_value(value)]):
            return self.matched(path=path, value=value)

    def matched(self, path=None, value=None):
        default = self.trigger(path, value)
        if 'accumulate_paths' in self.conf:
            return path
        elif 'accumulate_values' in self.conf:
            return value
        else:
            return default


def traverse(obj, visitor=None, visitor_kls=None, visitor_kwargs={}):
    """example `visitor`:

    def visit(value=None, path=None):
        print(f"[{path}: {value}]")
        return value
    """
    assert bool(visitor) ^ bool(visitor_kls) ^ bool(visitor_kwargs)
    paths = []

    def travel(arg=obj, path='', paths=[]):
        if isinstance(arg, (list, tuple)):
            for i, item in enumerate(arg):
                path_key = f"{path}.{i}"
                paths += [path_key]
                travel(item, path=path_key)
        if isinstance(arg, (dict,)):
            for k, v in arg.items():
                path_key = f"{path}.{k}"
                paths += [path_key]
                travel(v, path=path_key)
        paths = sorted(list(set(paths)))
        return paths

    paths = travel()
    result = dict(paths=paths, obj=obj)
    if visitor_kwargs and not visitor_kls:
        visitor_kls = Visitor
    if visitor_kls:
        assert not visitor
        visitor = visitor_kls(**{**result, **visitor_kwargs})
    visits = []
    if visitor is not None:
        for path in paths:
            visitation = visitor(path=path, value=pydash.get(obj, path))
            visitation and visits.append(visitation)
    result.update(
        # visitor=visitor,
        visits=visits
    )
    result = abcs.AttrDict(**result)
    return result


class TemplatedDict(dict):
    def get_path(self, path):
        return pydash.get(self, path)

    def set_path(self, path, val):
        return pydash.set_with(self, path, val)

    @property
    def traversal(self):
        traversed = traverse(
            self,
            visitor_kwargs=dict(filter_value=self.is_templated, accumulate_paths=True),
        )
        return traversed

    @property
    def unresolved(self):
        return self.traversal.visits


import jinja2


class JinjaDict(TemplatedDict):
    """ """

    def render(self, ctx={}):
        while self.unresolved:
            templated = self.unresolved
            LOGGER.debug(f"resolving: {templated}")
            LOGGER.debug(f"remaining unresolved: {templated}")
            for i, path in enumerate(templated):
                templated.pop(i)
                val = self.get_path(path)
                # if any([path.startswith(r) for r in ignore]):
                #     LOGGER.debug(f"resolution for {path} skipped")
                try:
                    x = self.render_path(path, ctx=ctx)
                    LOGGER.debug(f"resolution for `{val}` @ {path} succeeded ({x})")
                except (jinja2.exceptions.UndefinedError,) as exc:
                    LOGGER.debug(f"resolution for `{val}` @{path} failed ({exc})")
                    LOGGER.debug(f"self: {self}")
                    LOGGER.debug(f"ctx: {ctx}")
                    # move it to the end
                    templated.append(path)
                else:
                    # templated = templated
                    break
            else:
                break
        return dict(self)

    def render_path(self, path, ctx={}, strict=False):
        """ """
        from pynchon.api import render

        strict and True
        value = self.get_path(path)
        resolved = render.j2_loads(
            text=value,
            context={**self, **ctx},
            templates=[],
        )
        self.set_path(path, resolved)
        LOGGER.debug(f"resolved `{value}`@`{path}` as {resolved}")
        return resolved

    def is_templated(self, v):
        return isinstance(v, (str,)) and '{{' in v
