""" pynchon.abcs.visitor
"""
import pydash

from pynchon import abcs


class Visitor:
    def __init__(
        self,
        filter_path=lambda _: True,
        filter_value=lambda _: True,
        trigger=lambda p, v: [print(f"[{p}: {v}]")],
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
