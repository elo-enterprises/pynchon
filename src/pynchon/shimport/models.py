""" shimport.models
"""
import importlib
import collections

from pynchon.util import typing
from pynchon.abcs.path import Path
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

import logging

class ModulesWrapper(object):
    class Error(ImportError):
        pass

    def __str__(self):
        return f'<{self.__class__.__name__}[{self.name}]>'

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

    def __init__(
        self,
        name: str = '',
        import_mods: typing.List[str] = [],
        import_names: typing.List[str] = [],
        import_subs: typing.List[str] = [],
        import_children: bool = False,
        # lazy: bool = False,
        filter_failure_raises: bool = True,
        logger=None,
        **kwargs,
    ):
        assert name
        self.name = name
        self.import_mods = import_mods
        self.import_names = import_names
        self.logger = logger or logging.getLogger(__name__)
        self.import_subs = import_subs
        self.import_children = import_children
        self.namespace = get_namespace(name)
        self.filter_failure_raises = filter_failure_raises
        if kwargs:
            raise TypeError(f'extra kwargs: {kwargs}')
        # if not lazy:
        #     self.import_side_effects()

    @property
    def module(self):
        result = importlib.import_module(self.name)
        return result

    def do_import(self, package):
        """ """
        return importlib.import_module(package)
    @property
    def parent_folder(self):
        return Path(self.module.__file__).parents[0]

    @property
    def parent(self):
        return self.__class__(
            name='.'.join(
            self.name.split('.')[:-1]))

    def select(self, **filter_kwargs):
        tmp = list(self.filter(
            # return_values=True,
            **filter_kwargs))
        assert len(tmp)==1
        return tmp[0]

    def validate_assignment(self, assignment):
        """ """
        if assignment in dir(self.module):
            msg = f'refusing to override existing value in target module: {assignment}'
            self.logger.critical(msg)
            err = f'cannot assign name `{assignment}` to {self.module}; already exists!'
            raise ModulesWrapper.Error(err)

    def assign_back(self):
        for assignment in self.namespace:
            self.validate_assignment(assignment)
            setattr(self.module, assignment, self.namespace[assignment])

    def prune(self, **filters):
        self.namespace = self.filter(**filters)
        return self
    def filter_folder(
        self,
        include_main:str=True,
        exclude_private=True,
        filter:typing.Dict={},
        select:typing.Dict={},
        merge_filters=False,
        # rekey=None,
        # return_values=None,
    ):
        """
        """
        import glob, os
        p = self.parent_folder/'**/*.py'
        result = glob.glob(str(p))
        result = [Path(x) for x in result]
        main = [x for x in result if x.stem == '__main__']
        if exclude_private:
            result = [x for x in result if not x.stem.startswith('_')]
        if include_main:
            result += main
        children = []
        for p in result:
            rel = p.relative_to(self.parent_folder)
            rel = rel.parents[0]/rel.stem
            rel = str(rel).replace(os.path.sep, '.')
            dotpath = f"{self.name}.{rel}"
            child = ModulesWrapper(
                name=dotpath,
                import_mods=[dotpath])
            children.append(child)
        if not (filter or select):
            return children
        else:
            result = []
            assert bool(filter)^bool(select)
            filter_results = []
            for child in children:
                fxn = child.filter if filter else child.select
                kwargs = filter if filter else select
                matches = fxn(**kwargs)
                if matches:
                    import IPython; IPython.embed()
                    filter_results.append([child, matches])
                    result.append(child)
            if not merge_filters:
                return result
            else:
                out = {}
                for child, fres in filter_results:
                    out = {**out, **child.namespace}
                return out

        # if rekey is not None:
        #     return dict([rekey(ch) for ch in result])
        # if return_values:
        #     # raise Exception([ch.namespace.values() for ch in result])
        #     result = [child.namespace for child in result]
        return result

    def __items__(self):
        return self.namespace.__items__()

    def filter(
        self,
        exclude_private: bool = True,
        name_is: str = '',
        filter_names: typing.List[typing.Callable] = [],
        filter_vals: typing.List[typing.Callable] = [],
        filter_types: typing.List[type(type)] = [],
        filter_module_origin: str = '',
        filter_instances: typing.List[type(type)] = [],
        exclude_names: typing.List[str] = [],
        **kwargs,
    ):
        if name_is:
            filter_names = [lambda name: name == name_is] + filter_names
        if exclude_private:
            filter_names = [lambda name: not name.startswith('__')] + filter_names

        if exclude_names:
            filter_names = [
                lambda n: n not in exclude_names,
            ] + filter_names

        filter_vals = filter_vals
        if filter_types:
            filter_vals = [
                lambda val: any([typing.is_subclass(val, ty) for ty in filter_types])
            ] + filter_vals
        if filter_instances:
            filter_vals = [lambda val: isinstance(val, filter_instances)] + filter_vals
        if filter_module_origin:
            filter_vals = [
                lambda val: filter_module_origin == getattr(val, '__module__', None)
            ] + filter_vals
        return self._apply_filters(
            filter_vals=filter_vals,
            filter_names=filter_names,
            # return_values=return_values,
            **kwargs
        )

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

    def namespace_modified_hook(self, assignment, val):
        """ """

    def import_side_effects(self,):
        import_statements = []
        for name in self.import_mods:
            spec = self.normalize_import(name)
            assignment = spec.assignment or spec.var
            submod = importlib.import_module(spec.package)
            self.namespace[assignment] = submod
            self.namespace_modified_hook(assignment, submod)

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
        return import_statements

    def _apply_filters(
        self,
        # import_names=[], import_statements=[],
        filter_vals=[],
        filter_names=[],
        import_statements=[],
        # return_values=False,
        rekey: typing.Callable = None,
    ):
        """ """
        # if kwargs:
        #     raise ValueError(f'unused kwargs {kwargs}')
        module = self.module
        namespace = {}
        import_statements = import_statements or self.import_side_effects()
        for st in import_statements:
            submod = self.do_import(st.package)
            vars = dir(submod) if st.star else [st.var]
            for var in vars:
                assert isinstance(var, str), var
                for validator in filter_names:
                    if not self.run_filter(validator, var):
                        break
                else:  # name is ok
                    val = getattr(submod, var)
                    for validator in filter_vals:
                        if not self.run_filter(validator, val):
                            break
                    else:  # name/val is ok
                        assignment = st.assignment or var
                        namespace[assignment] = val
                        self.namespace_modified_hook(assignment, val)
        if rekey:
            return dict([ rekey(v) for v in namespace.values()])
        return namespace


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