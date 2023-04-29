""" pynchon.util.text CLI
"""
from pynchon.cli import click
from pynchon.util import text as THIS
from pynchon.util import lme, typing, importing

LOGGER = lme.get_logger(__name__)


def entry() -> typing.NoneType:
    pass


entry.__doc__ = __doc__ or ""

# FIXM: use THIS = importing.cli_builder(..)
THIS = importing.module_builder(
    __name__,
    assign_objects=True,
    # import_main_entry = [
    #     f'{THIS.__name__}.loadf',
    # ],
    import_names=[
        # FIXME:
        # f'.loadf.__main__.entry as loadf',
        f'{THIS.__name__}.loadf.__main__.entry as loadf',
        f'{THIS.__name__}.render.__main__.entry as render',
    ],
)

entry = click.group()(entry)

if __name__ == '__main__':
    click.group_copy(THIS.render, entry)
    click.group_copy(THIS.loadf, entry)
    entry()
