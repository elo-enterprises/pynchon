""" pynchon.util.makefile CLI
"""
# from fleks.cli import click, options  # noqa
from pynchon.cli import common
from pynchon.util.tagging import tags
import shimport
from pynchon.util import lme, typing  # noqa

LOGGER = lme.get_logger(__name__)
entry = common.entry_for(__name__)

tmp = (
    shimport.wrapper(
        "pynchon.util.makefile",
    )
    .prune(
        exclude_private=True,
        filter_instances=typing.FunctionType,
        filter_module_origin="pynchon.util.makefile",
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
