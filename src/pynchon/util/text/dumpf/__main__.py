from pynchon.cli import click, common, options  # noqa
from pynchon.util import lme, typing  # noqa
from pynchon.util.tagging import tags

LOGGER = lme.get_logger(__name__)

entry = common.entry_for(__name__)


from pynchon import shimport

tmp = (
    shimport.wrapper("pynchon.util.text.dumpf")
    .prune(
        filter_instances=typing.FunctionType,
        filter_module_origin="pynchon.util.text.dumpf",
    )
    .map_ns(
        lambda _name, fxn: [fxn, tags[fxn].get("click_aliases", []) + [fxn.__name__]]
    )
    .starmap(
        lambda fxn, aliases: [
            common.kommand(
                name=alias.replace("_", "-"),
                parent=entry,
                help=(
                    fxn.__doc__
                    if alias == fxn.__name__
                    else f"alias for `{fxn.__name__}`"
                ),
            )(fxn)
            for alias in aliases
        ],
        logger=LOGGER,
    )
)
LOGGER.debug(tmp)

if __name__ == "__main__":
    entry()