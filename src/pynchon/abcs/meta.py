""" pynchon.abcs.meta
"""
from pynchon.util import typing, lme

LOGGER = lme.get_logger(__name__)


class Meta(type):
    """ """

    NAMES = []

    def __new__(mcls: type, name, bases, namespace):
        """ """
        mcls.register(name=name, bases=bases, namespace=namespace)
        namespace = mcls.annotate(name=name, bases=bases, namespace=namespace)
        return super().__new__(mcls, name, bases, namespace)

    @classmethod
    def aggr(
        mcls: type,
        attr: str = '',
        bases: typing.List = [],
        namespace: typing.Dict = {},
    ):
        """ """
        class_props = namespace.get(attr, [])
        for b in bases:
            class_props += getattr(b, attr, [])
        return class_props

    @classmethod
    def register(
        mcls: type,
        name: str = '',
        bases: typing.List = [],
        namespace: typing.Dict = {},
    ) -> None:
        """ """
        this_name = namespace.get('name', None)
        this_name and Meta.NAMES.append(this_name)

    @classmethod
    def annotate(
        mcls: type,
        name: str = '',
        bases: typing.List = [],
        namespace: typing.Dict = {},
    ) -> typing.Dict:
        """ """
        class_props = mcls.aggr('__class_properties__', bases, namespace)
        class_props += [
            k for k, v in namespace.items() if isinstance(v, typing.classproperty)
        ]
        class_props = list(set(class_props))
        namespace.update({'__class_properties__': class_props})
        instance_methods = mcls.aggr('__methods__', bases, namespace)
        instance_methods += [
            k
            for k, v in namespace.items()
            if not k.startswith('_') and isinstance(v, typing.FunctionType)
        ]
        instance_methods = list(set(instance_methods))
        namespace.update({'__methods__': instance_methods})
        instance_properties = mcls.aggr('__properties__', bases, namespace)
        instance_properties += [
            k
            for k, v in namespace.items()
            if not k.startswith('_') and isinstance(v, property)
        ]
        namespace.update({'__properties__': instance_properties})
        # namespace.update({'__method_tags__':dict(
        #     [[mname, tagging.TAGGER[mname]],
        #     for mname in instance_methods])})
        # namespace.update({'__class_tags__': .. })
        # namespace.update({'__static_methods__': .. })
        # namespace.update({'__properties__': .. })
        # LOGGER.debug(f'mcls for {name} returns')
        return namespace
