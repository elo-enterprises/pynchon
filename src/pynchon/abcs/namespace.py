""" {{pkg}}.abcs.namespace
"""

import typing

# import collections


def namespace(name, bases, namespace):
    """ """

    @property
    def _dict(self):
        """ """
        return self._asdict()

    def items(self):
        """ """
        return self._dict.items()

    def keys(self):
        """ """
        return self._dict.keys()

    def values(self):
        """ """
        return self._dict.values()

    # @classmethod
    # def __instancecheck__(cls, instance):
    #     if return isinstance(instance, User)

    def toJSON(self, *args):
        """ """
        from pynchon.util import text

        return text.to_json(self._dict, *args)

    for k, v in dict(
        values=values,
        keys=keys,
        items=items,
        _dict=_dict,
        toJSON=toJSON,
        __repr__=namespace.get(
            '__repr__', namespace.get('__str__', lambda hisself: str(hisself))
        ),
    ).items():
        if k not in namespace:
            namespace[k] = v

    return type(name, bases, namespace)


class Namespace(typing.NamedTuple, metaclass=namespace):
    """ """
