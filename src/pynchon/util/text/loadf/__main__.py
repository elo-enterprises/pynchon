""" pynchon.util.text.loadf CLI
"""
from pynchon.util import typing, lme  # noqa
from pynchon.cli import click, common, options  # noqa
from pynchon.util.tagging import tags

LOGGER = lme.get_logger(__name__)

entry = common.entry_for(__name__)


from pynchon import shimport

tmp = (
    shimport.wrapper('pynchon.util.text.loadf')
    .prune(
        filter_instances=typing.FunctionType,
        filter_module_origin='pynchon.util.text.loadf',
    )
    .map_ns(
        lambda _name, fxn: [fxn, tags[fxn].get('click_aliases', []) + [fxn.__name__]]
    )
    .starmap(
        lambda fxn, aliases: [
            common.kommand(
                name=alias,
                parent=entry,
                help=fxn.__doc__
                if alias == fxn.__name__
                else f'alias for {fxn.__name__}',
            )(fxn)
            for alias in aliases
        ],
        logger=LOGGER,
    )
)
LOGGER.debug(tmp)

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
