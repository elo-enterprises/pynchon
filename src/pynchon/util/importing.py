""" {{pkg}}.util.importing
"""
import importlib

from . import lme, typing

LOGGER = lme.get_logger(__name__)


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


import_spec = collections.namedtuple(
    'importSpec', 'assignment var star package relative'
)


class ModuleBuilder(object):
    class Error(ImportError):
        pass

    def __str__(self):
        return f'<{self.__class__.__name__}[{self["name"]}]>'

    __repr__ = __str__

    def normalize_import(self, name):
        """ """
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
        result = import_spec(
            assignment=assignment,
            var=var,
            star='*' in var,
            package=package,
            relative=relative,
        )
        return result

    @typing.validate_arguments
    def __init__(
        self,
        name: str = '',
        init_hooks: typing.List = [],
        import_children: bool = False,
        assign_objects: bool = True,
        filter_failure_raises: bool = True,
        exclude_private: bool = True,
        name_filters: typing.List[typing.Callable] = [],
        fitler_vals: typing.List[typing.Callable] = [],
        import_mods: typing.List[str] = [],
        import_names: typing.List[str] = [],
        import_subs: typing.List[str] = [],
        filter_types: typing.List[type(type)] = [],
        exclude_names: typing.List[str] = [],
    ):
        assert name
        self.name = name
        self.init_hooks = init_hooks
        self.import_mods = import_mods
        self.import_names = import_names
        self.import_subs = import_subs
        self.import_children = import_children
        self.filter_failure_raises = filter_failure_raises
        self.exclude_private = exclude_private
        self.exclude_names = exclude_names
        self.filter_types = filter_types
        if self.exclude_private:
            self.name_filters = [lambda name: not name.startswith('__')] + name_filters
        if self.exclude_names:
            self.name_filters = [
                lambda n: n not in self.exclude_names,
            ] + name_filters

        self.fitler_vals = fitler_vals
        if self.filter_types:
            self.fitler_vals = [
                lambda val: any(
                    [typing.is_subclass(val, ty) for ty in self.filter_types]
                )
            ] + fitler_vals
        self.namespace = get_namespace(name)
        self.assign_objects = assign_objects

    @property
    def module(self):
        result = importlib.import_module(self.name)
        return result

    def run_filter(self, validator, arg):
        """
        wrapper to honor `filter_failure_raises`
        """
        test = False
        try:
            test = validator(arg)
        except:
            if self.filter_failure_raises:
                raise
        return test

    def do_import(self, package):
        """ """
        return importlib.import_module(package)

    def initialize(self):

        # FIXME: leaky abstraction
        msg = f"Building module-registry for {self.name}.."
        [h(msg) for h in self.init_hooks]

        module = self.module
        import_statements = []
        for name in self.import_mods:
            spec = self.normalize_import(name)
            assignment = spec.assignment or spec.var
            submod = importlib.import_module(spec.package)
            self.namespace[assignment] = submod
            if self.assign_objects:
                setattr(module, assignment, submod)

        for name in self.import_names:
            import_statements.append(self.normalize_import(name))

        if self.import_children:
            mod_file = self.module.__file__
            children = []
            for child in Path(mod_file).siblings():
                child = Path(child).stem
                if not child.startswith('__'):
                    self.import_subs.append(child)

        for name in self.import_subs:
            import_statements.append(self.normalize_import(f".{name}.*"))

        import_statements = list(set(import_statements))

        for st in import_statements:
            submod = self.do_import(st.package)
            vars = dir(submod) if st.star else [st.var]
            for var in vars:
                assert isinstance(var, str), var
                for validator in self.name_filters:
                    if not self.run_filter(validator, var):
                        break
                else:  # name is ok
                    val = getattr(submod, var)
                    for validator in self.fitler_vals:
                        if not self.run_filter(validator, val):
                            break
                    else:  # name/val is ok
                        assignment = st.assignment or var
                        self.validate_assignment(assignment)
                        self.namespace[assignment] = val
                        if self.assign_objects:
                            getattr(module, assignment, val)
        LOGGER.info(f"imported {len(self.namespace)} items to {self.name}")

    def validate_assignment(self, assignment):
        """ """
        if assignment in dir(self.module):
            msg = f'refusing to override existing value in target module: {assignment}'
            LOGGER.critical(msg)
            err = f'cannot assign name `{assignment}` to {module}; already exists!'
            raise ModuleBuilder.Error(err)


def module_builder(
    name: str,
    return_objects=False,
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


def registry_builder(name, itemizer=None, **kargs):
    """ """
    built = module_builder(name, **kargs)
    return dict(itemizer(obj) for obj in built)


def lazy_import(
    module_name: str,
    # var:str=None,
) -> LazyModule:
    """ """
    assert module_name
    return LazyModule(module_name)
