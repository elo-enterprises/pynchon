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

from pynchon.abcs.path import Path

MODULE_REGISTRY = dict()
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


class ModuleBuilderError(ImportError):
    pass


import_spec = collections.namedtuple(
    'importSpec', 'assignment var star package relative'
)


class ModuleBuilder(collections.UserDict):
    def normalize_import(self, name):
        """ """
        # .pkg.mod.name as bar
        # .mod
        # .mod.name
        assignment = None
        if ' as ' in name:
            name, assignment = name.split(' as ')
        relative = name.startswith('.')
        name = name if not relative else name[1:]
        bits = name.split(".")
        if len(bits) == 1:
            package = var = bits.pop(0)
        else:
            var = bits.pop(-1)
            package = '.'.join(bits)
        if relative:
            package = f"{self.name}.{package}"
        # assert var, f'variable must not be empty'
        # assert pkg, f'pkg must not be empty {bits}'
        result = import_spec(
            assignment=assignment,
            var=var,
            star='*' in var,
            package=package,
            relative=relative,
        )
        LOGGER.critical(result)
        return result

    def __init__(
        self,
        name: str = '',
        events: object = None,
        import_children: bool = False,
        name_validators: typing.List[typing.Callable] = [],
        val_validators: typing.List[typing.Callable] = [],
        import_mods: typing.List[str] = [],
        import_names: typing.List[str] = [],
        import_subs: typing.List[str] = [],
    ):
        assert name
        self.name = name
        self.events = events
        self.import_mods = import_mods
        self.import_names = import_names
        self.import_subs = import_subs
        self.import_children = import_children
        self.name_validators = [
            lambda name: not name.startswith('__')
        ] + name_validators
        self.val_validators = val_validators
        # assert 'namespace' not in kwargs
        self.namespace = ModuleNamespace(name)
        super().__init__(name=name)

    def __str__(self):
        return f'<{self.__class__.__name__}[{self["name"]}]>'

    __repr__ = __str__

    @property
    def module(self):
        result = importlib.import_module(self.name)
        return result

    def run_import_statements(self, import_statements):
        pass

    def initialize(self):

        # FIXME: leaky abstraction
        msg = f"Building module-registry for {self.name}.."
        LOGGER.critical(msg)
        self.events.status.update(stage=msg) if self.events is not None else None
        # if builder_kwargs:
        #     raise ModuleBuilderError(f"unused builder_kwargs {builder_kwargs}")

        module = self.module
        import_statements = []
        for name in self.import_mods:
            spec = self.normalize_import(name)
            assignment = spec.assignment or spec.var
            submod = importlib.import_module(spec.package)
            # for v in self.mod_validators ...
            setattr(module, assignment, submod)
            self.namespace[assignment] = submod

        for name in self.import_names:
            import_statements.append(self.normalize_import(name))

        if self.import_children:
            children = []
            for child in Path(self.module.__file__).parents[0].list():
                child = Path(child).stem
                if not child.startswith('__'):
                    self.import_subs.append(child)

        for name in self.import_subs:
            import_statements.append(self.normalize_import(f".{name}.*"))

        import_statements = list(set(import_statements))

        for st in import_statements:
            pkg = st.package
            # LOGGER.critical(f'imp: `{st.var}` from `{pkg}` to `{self.name}`')
            submod = importlib.import_module(pkg)
            vars = dir(submod) if st.star else [st.var]
            for var in vars:
                assert isinstance(var, str), var
                for validator in self.name_validators:
                    if not validator(var):
                        break
                else:
                    val = getattr(submod, var)
                    for validator in self.val_validators:
                        if not validator(val):
                            break
                    else:
                        assignment = st.assignment or var
                        if assignment in dir(module):
                            msg = f'refusing to override existing value in target module: {assignment}'
                            LOGGER.critical(msg)
                            err = f'cannot assign name `{assignment}` to {module}; already exists!'
                            raise ModuleBuilderError(err)
                        setattr(module, assignment, val)
                        self.namespace[assignment] = val
        LOGGER.debug(f"imported {len(self.namespace)} items to {self.name}")


def module_builder(name: str, **kwargs) -> None:
    """ """
    if name not in MODULE_REGISTRY:
        MODULE_REGISTRY[name] = ModuleBuilder(name=name, **kwargs)
    builder = MODULE_REGISTRY[name]
    builder.initialize()
    return builder.namespace


def lazy_import(
    module_name: str,
    # var:str=None,
) -> LazyModule:
    """ """
    assert module_name
    return LazyModule(module_name)
