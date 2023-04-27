""" pynchon.abcs.plugin
"""
from memoized_property import memoized_property

from pynchon.util import lme, typing

LOGGER = lme.get_logger(__name__)


class Meta(type):
    NAMES = []

    @staticmethod
    def aggr(
        attr,
        bases,
        namespace,
    ):
        class_props = namespace.get(attr, [])
        for b in bases:
            class_props += getattr(b, attr, [])
        return class_props

    def __new__(mcls, clsname, bases, namespace):
        this_name = namespace.get('name', None)
        this_name and mcls.NAMES.append(this_name)
        class_props = Meta.aggr('__class_properties__', bases, namespace)
        class_props += [
            k for k, v in namespace.items() if isinstance(v, typing.classproperty)
        ]
        class_props = list(set(class_props))
        namespace.update({'__class_properties__': class_props})
        instance_methods = Meta.aggr('__methods__', bases, namespace)
        instance_methods += [
            k
            for k, v in namespace.items()
            if not k.startswith('_') and isinstance(v, typing.FunctionType)
        ]
        instance_methods = list(set(instance_methods))
        namespace.update({'__methods__': instance_methods})
        # namespace.update({'__method_tags__':dict(
        #     [[mname, tagging.TAGGER[mname]],
        #     for mname in instance_methods])})
        # namespace.update({'__class_tags__': .. })
        # namespace.update({'__static_methods__': .. })
        # namespace.update({'__properties__': .. })
        return super().__new__(mcls, clsname, bases, namespace)


class Plugin(object, metaclass=Meta):
    priority = 0

    def __init__(self, final=None):
        """ """
        self.final = final
        # self.config = config
        # self.state = None

    @memoized_property
    def logger(self):
        return lme.get_logger(f"<{self.__class__.__name__} Plugin>")
