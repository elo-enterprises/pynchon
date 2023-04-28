""" {{pkg}}.util.importing
"""
import importlib


def lazy_import(
    importer_name,
):
    """Return the importing module and a callable for lazy importing.

    The module named by importer_name represents the module performing the
    import to help facilitate resolving relative imports.

    to_import is an iterable of the modules to be potentially imported (absolute
    or relative). The `as` form of importing is also supported,
    e.g. `pkg.mod as spam`.

    This function returns a tuple of two items. The first is the importer
    module for easy reference within itself. The second item is a callable to be
    set to `__getattr__`.
    """

    class fakemod:
        """ """

        def __init__(self, name):
            self.name = name

        def __getattr__(self, name):
            module = importlib.import_module(self.name)
            return getattr(module, name)

    return fakemod(importer_name)
