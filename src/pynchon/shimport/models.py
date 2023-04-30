""" shimport.models
"""
import importlib
import collections

from pynchon.abcs.attrdict import AttrDict

import_spec = collections.namedtuple(
    'importSpec', 'assignment var star package relative'
)


def get_namespace(name):
    """
    FIXME: use FakeModule?
    """

    class ModuleNamespace(AttrDict):
        """ """

        def __str__(self):
            return f'<{self.__class__.__name__}[{self.__class__.name}]>'

        __repr__ = __str__

        @property
        def module(self):
            result = importlib.import_module(self.__class__.name)
            return result

    ModuleNamespace.name = name
    return ModuleNamespace()


class LazyModule:
    """ """

    class LazyImportError(ImportError):
        pass

    class LazyResolutionError(LazyImportError):
        pass

    def __init__(self, module_name: str = ''):
        """ """
        assert module_name
        self.module_name = module_name
        self.module = None

    def resolve(self):
        """ """
        if self.module is None:
            try:
                self.module = importlib.import_module(self.module_name)
            except (ImportError,) as exc:
                raise LazyModule.LazyResolutionError(exc)

    def __repr__(self):
        return f"<LazyModule[{self.module_name}]>"

    __str__ = __repr__

    def __getattr__(self, var_name):
        """ """
        self.resolve()
        return getattr(self.module, var_name)
