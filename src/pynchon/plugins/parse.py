""" pynchon.plugins.parse
"""

import shimport
from fleks import cli

from pynchon import abcs, events, models  # noqa
from pynchon.util import lme, typing  # noqa

LOGGER = lme.get_logger(__name__)
config = shimport.lazy("pynchon.config")


class Parse(models.ToolPlugin):
    """
    Misc tools for parsing
    """

    class config_class(abcs.Config):
        config_key: typing.ClassVar[str] = "parse"

    name = "parse"
    cli_name = "parse"
    cli_aliases = ["parser"]

    @cli.click.flag("-c", "--codeblocks", help="only codeblocks")
    @cli.click.argument("file")
    def markdown(self, file: str = None, codeblocks: bool = True):
        """ """

        assert file
        with open(file) as fhandle:
            content = fhandle.read()
        from marko import Markdown
        from marko.ast_renderer import ASTRenderer

        result = Markdown(renderer=ASTRenderer)(content)
        result = result["children"]
        if codeblocks:
            result = [x for x in result if x["element"] == "fenced_code"]
        return result
