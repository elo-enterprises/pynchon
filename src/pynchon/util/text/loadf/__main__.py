""" pynchon.util.text.loadf CLI
"""
from pynchon import click
from pynchon.cli import options
from pynchon.util import text, typing, lme
from pynchon.util.text import loadf as THIS

LOGGER = lme.get_logger(__name__)


def entry() -> typing.NoneType:
    pass


entry.__doc__ = __doc__ or ""


@options.strict
@click.argument("files", nargs=-1)
def json_load(
    files: typing.List[str] = [],
    strict: bool = True,
) -> None:
    """
    loads json5 file(s) and outputs json.
    if multiple files are provided, files will
    be merged with overwrites in the order provided
    """
    out: typing.Dict[str, typing.Any] = {}
    for file in files:
        obj = THIS.json(file=file, strict=strict)
        out = {**out, **obj}
    print(text.to_json(out))


entry = click.group('loadf')(entry)
entry.command('json')(json_load)
entry.command('json5')(THIS.json5)
entry.command('j5')(THIS.json5)

if __name__ == '__main__':
    entry()
