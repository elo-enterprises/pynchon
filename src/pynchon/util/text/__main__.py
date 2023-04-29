""" pynchon.util.text CLI
"""
from pynchon.cli import click
from pynchon.util import text as THIS
from pynchon.util import lme, typing
from pynchon.util.importing import module_builder

LOGGER = lme.get_logger(__name__)


def entry() -> typing.NoneType:
    pass


entry.__doc__ = __doc__ or ""
this = module_builder(
    __name__,
    import_names=[
        f'{THIS.__name__}.loadf.__main__.entry as loadf',
        f'{THIS.__name__}.render.__main__.entry as render',
    ],
)

entry = click.group()(entry)

if __name__ == '__main__':
    click.group_copy(this.render, entry)
    click.group_copy(this.loadf, entry)
    entry()
