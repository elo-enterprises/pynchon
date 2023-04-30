""" pynchon.util.text.loadf CLI
"""
from pynchon import shimport
from pynchon.cli import click, common, options
from pynchon.util import text, typing, lme
from pynchon.util.text import loadf as THIS

LOGGER = lme.get_logger(__name__)

entry = common.entry_for(__name__)


# fxns = shimport.wrap(THIS.__name__,).filter(
#     exclude_private=True,  # default
#     filter_instances=typing.FunctionType,
#     filter_module_origin=THIS.__name__,
#     # return_values=True,
# ).values()
# for fxn in fxns:
#     common.kommand(fxn.__name__, parent=entry)(fxn)

if __name__ == '__main__':
    entry()

# @options.strict
# @click.argument("files", nargs=-1)
# def json_load(
#     files: typing.List[str] = [],
#     strict: bool = True,
# ) -> None:
#     """
#     loads json5 file(s) and outputs json.
#     if multiple files are provided, files will
#     be merged with overwrites in the order provided
#     """
#     out: typing.Dict[str, typing.Any] = {}
#     for file in files:
#         obj = THIS.json(file=file, strict=strict)
#         out = {**out, **obj}
#     print(text.to_json(out))
# json = entry.command('json')(json_load)


# json5 = common.kommand('json5',parent=entry)(THIS.json5)
# j5 = entry.command('j5')(THIS.json5)
