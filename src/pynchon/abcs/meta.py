""" pynchon.abcs.meta
"""
import collections

from pynchon.util import typing, lme

LOGGER = lme.get_logger(__name__)

type_spec = collections.namedtuple('type_spec', 'name bases namespace')


class Meta(type):
    """ """

    NAMES = []

    def __new__(mcls: type, name: str, bases: typing.List, namespace: typing.Dict):
        """ """
        tspec = type_spec(name=name, bases=bases, namespace=namespace)
        mcls.register(tspec)
        namespace = mcls.annotate(tspec)
        return super().__new__(mcls, name, bases, namespace)

    @staticmethod
    def aggregate_across_bases(
        var: str = '',
        tspec: type_spec = None,
    ):
        """
        aggregates values at `var` across all bases
        """
        tracked = tspec.namespace.get(var, [])
        for b in tspec.bases:
            bval = getattr(b, var, [])
            assert isinstance(bval, list), bval
            tracked += bval
        return tracked

    @classmethod
    def register(
        mcls: type,
        tspec: type_spec = None,
    ) -> None:
        """ """
        name, bases, namespace = tspec.name, tspec.bases, tspec.namespace
        this_name = namespace.get('name', None)
        this_name and Meta.NAMES.append(this_name)

    @classmethod
    def annotate(
        mcls: type,
        tspec: type_spec = None,
    ) -> typing.Dict:
        """ """
        name, bases, namespace = tspec.name, tspec.bases, tspec.namespace
        class_props = mcls.aggregate_across_bases(
            var='__class_properties__',
            tspec=tspec,
        )
        class_props += [
            k for k, v in namespace.items() if isinstance(v, typing.classproperty)
        ]
        class_props = list(set(class_props))
        namespace.update({'__class_properties__': class_props})
        instance_methods = mcls.aggregate_across_bases(var='__methods__', tspec=tspec)
        instance_methods += [
            k
            for k, v in namespace.items()
            if not k.startswith('_') and isinstance(v, typing.FunctionType)
        ]
        instance_methods = list(set(instance_methods))
        namespace.update({'__methods__': instance_methods})
        instance_properties = mcls.aggregate_across_bases(
            var='__properties__',
            tspec=tspec,
        )
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
