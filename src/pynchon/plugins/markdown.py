""" pynchon.plugins.markdown
"""

from pynchon import abcs, api, cli, events, models  # noqa
from pynchon.util import lme, typing  # noqa

LOGGER = lme.get_logger(__name__)
from fleks import tagging


class Markdown(models.CliPlugin):
    """Markdown"""

    class config_class(abcs.Config):
        config_key: typing.ClassVar[str] = "markdown"
        goals: typing.List[str] = typing.Field(default=[])
        include_patterns: typing.List[str] = typing.Field(default=[])
        exclude_patterns: typing.List[str] = typing.Field(default=[])
        root: typing.Union[str, abcs.Path, None] = typing.Field(default=None)

    name = "markdown"
    cli_name = "markdown"
    priority = 0

    @tagging.tags(click_aliases=["parse.markdown"])
    @cli.click.flag("-c", "--codeblocks", help="only codeblocks")
    @cli.click.argument("file")
    def parse(self, file: str = None, codeblocks: bool = True):
        """parses given markdown file into json"""

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

    # plan=None
    # def plan(self, config=None):
    #     """Describe plan for this plugin"""
    #     plan = super().plan(config=config)
    #     return plan
    # resources = [abcs.Path(fsrc) for fsrc in self.list()]
    # self.logger.warning("Adding user-provided goals")
    # for g in self["goals"]:
    #     plan.append(self.goal(command=g, resource="?", type="user-config"))
    #
    # self.logger.warning("Adding file-header related goals")
    # cmd_t = "python -mpynchon.util.files prepend --clean "
    # loop = self._get_missing_headers(resources)
    # for rsrc in loop["files"]:
    #     if rsrc.match_any_glob(self["exclude_patterns"::[]]):
    #         continue
    #     ext = rsrc.full_extension()
    #     ext = ext[1:] if ext.startswith(".") else ext
    #     # fhdr = header_files[ext]
    #     fhdr = self._render_header_file(rsrc)
    #     plan.append(
    #         self.goal(
    #             resource=rsrc,
    #             type="change",
    #             label=f"Adding file header for '{ext}'",
    #             command=f"{cmd_t} {fhdr} {rsrc}",
    #         )
    #     )
