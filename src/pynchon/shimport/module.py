""" shimport.module
"""
from pynchon.util import typing

from . import models

MODULE_REGISTRY = dict()


class ModuleBuilder(models.ModulesWrapper):
    @typing.validate_arguments
    def __init__(
        self,
        name: str = '',
        init_hooks: typing.List = [],
        assign_objects: bool = True,
        **kwargs,
    ):
        models.ModulesWrapper.__init__(self, name=name, **kwargs)
        self.init_hooks = init_hooks
        self.assign_objects = assign_objects

    def initialize(self, **filters):
        """ """
        # FIXME: leaky abstraction
        msg = f"Building module-registry for {self.name}.."
        [h(msg) for h in self.init_hooks]
        return self.filter(**filters)

    def namespace_modified_hook(self, assignment, val):
        if self.assign_objects:
            self.validate_assignment(assignment)
            setattr(self.module, assignment, val)

    def filter(self, **filter):
        """ """
        models.ModulesWrapper.filter(self, **filter)
        self.logger.info(f"imported {len(self.namespace)} items to {self.name}")


def module_builder(
    name: str,
    return_objects=False,
    assign_objects: bool = True,
    sort_objects: typing.Dict = {},
    **kwargs,
) -> None:
    """ """
    if name not in MODULE_REGISTRY:
        MODULE_REGISTRY[name] = ModuleBuilder(name=name, **kwargs)
    builder = MODULE_REGISTRY[name]
    builder.initialize()
    result = builder.namespace
    result = result.values() if return_objects else result
    result = sorted(result, **sort_objects) if sort_objects else result
    return result


builder = module_builder
build = builder


def wrap(name, **kwargs):
    # from types import ModuleType
    if isinstance(name, (typing.ModuleType)):
        mod = name
        name = mod.__name__
        # kwargs['import_mods'] = list(set(kwargs.pop('import_mods',[])+[name]))
    result = models.ModulesWrapper(name, import_names=[f'{name}.*'], **kwargs)
    return result


wrapper = wrap


def registry_builder(
    name,
    # itemizer=None,
    **kargs,
):
    """ """
    wrapped = wrap(
        name,
    )
    return wrapped
    # return dict(itemizer(obj) for obj in built)


registry = registry_builder
build_registry = registry_builder


def lazy_import(
    module_name: str,
) -> models.LazyModule:
    """ """
    assert module_name
    return models.LazyModule(module_name)
