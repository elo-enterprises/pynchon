""" {{pkg}}.util.importing
"""
import importlib

from . import lme, typing

LOGGER = lme.get_logger(__name__)


class LazyImportError(ImportError):
    pass


class LazyResolutionError(LazyImportError):
    pass


class LazyModule:
    """ """

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
                raise LazyResolutionError(exc)

    def __repr__(self):
        return f"<LazyModule[{self.module_name}]>"

    __str__ = __repr__

    def __getattr__(self, var_name):
        """ """
        self.resolve()
        return getattr(self.module, var_name)


#####
import collections

MODULE_REGISTRY = dict()  # collections.defaultdict(dict)
from pynchon.abcs.attrdict import AttrDict


class ModuleNamespace(AttrDict):
    """ """

    def __init__(self, name: str = '', **kwargs):
        assert name
        assert 'namespace' not in kwargs
        self.namespace = {}
        super().__init__(name=name, **kwargs)

    def __str__(self):
        return f'<{self.__class__.__name__}[{self["name"]}]>'

    __repr__ = __str__

    @property
    def module(self):
        result = importlib.import_module(self.name)
        return result


class ModuleBuilder(ModuleNamespace):
    def run_import_statements(self, import_statements):
        pass

    def initialize(
        self,
        events=None,
        import_names: typing.List[str] = [],
        import_subs: typing.List[str] = [],
        **builder_kwargs,
    ):
        # FIXME: leaky abstraction
        msg = f"Building module-registry for {self.name}.."
        LOGGER.critical(msg)
        events.status.update(stage=msg)
        if builder_kwargs:
            raise Exception(f"unused builder_kwargs {builder_kwargs}")

        module = self.module
        namespace = {}
        import_statements = []
        if import_names:
            for name in import_names:
                bits = name.split(".")
                var = bits[-1]
                pkg = '.'.join(bits[:-1])
                assert var, 'variable must not be empty'
                assert pkg, 'pkg must not be empty'
                LOGGER.critical(f'imp: `{var}` from `{pkg}` to `{self.name}`')
                import_statements.append((pkg, var))

        if self.import_children:
            from pynchon import abcs

            children = []
            for child in abcs.Path(self.module.__file__).parents[0].list():
                child = abcs.Path(child).stem
                if not child.startswith('__'):
                    import_subs.append(child)

        if import_subs:
            for name in import_subs:
                import_statements.append((f".{name}", "*"))

        import_statements = list(set(import_statements))
        # self.run_import_statements(import_statements)
        for pkg, var in import_statements:
            pkg = f'{self.name}' + pkg if pkg.startswith('.') else pkg
            submod = importlib.import_module(pkg)
            if var == '*':
                vars = [v for v in dir(submod)]
            else:
                vars = [var]
            tmp = []  # v for v in vars if self.validate_name(var)]
            for var in vars:
                for validator in self.name_validators:
                    if not validator(var):
                        break
                else:
                    tmp.append(var)
            vars = tmp
            for var in vars:
                val = getattr(submod, var)
                for validator in self.val_validators:
                    if not validator(val):
                        break
                else:
                    if var in dir(module):
                        msg = f'refusing to override existing value in target module: {var}'
                        LOGGER.critical(msg)
                        raise NameError(var)
                    else:
                        setattr(module, var, val)
                        namespace[var] = val
        LOGGER.debug(f"imported {len(namespace)} items to {self.name}")
        self.namespace = namespace


def module_builder(name: str, **kwargs) -> None:
    """ """
    if name not in MODULE_REGISTRY:
        MODULE_REGISTRY[name] = ModuleBuilder(name=name, **kwargs)
    return MODULE_REGISTRY[name]


def lazy_import(
    module_name: str,
    # var:str=None,
) -> LazyModule:
    """ """
    assert module_name
    return LazyModule(module_name)
