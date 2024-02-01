""" pynchon.plugins.docs.main
"""

import fleks
import shimport
from fleks import cli, tagging
from memoized_property import memoized_property

from pynchon.util.os import invoke
from pynchon.plugins.docs.opener import OpenerMixin

from pynchon import abcs, api, events, models  # noqa
from pynchon.util import files, lme, typing  # noqa

grip = shimport.lazy("pynchon.gripe")
LOGGER = lme.get_logger(__name__)


@tagging.tags(click_aliases=["d"])
class DocsMan(models.ResourceManager, OpenerMixin):
    """
    Management tool for project docs
    """

    class config_class(abcs.Config):
        config_key: typing.ClassVar[str] = "docs"
        include_patterns: typing.List[str] = typing.Field(default=[])
        root: typing.Union[str, abcs.Path, None] = typing.Field()
        exclude_patterns: typing.List[str] = typing.Field(default=[])

    name = "docs"
    cli_name = "docs"
    cli_label = "Manager"
    priority = 0
    serving = None

    # @property
    # def root(self):
    #     if "root" not in self.__dict__:
    #         from pynchon.config import GIT, pynchon
    #         tmp = GIT.root
    #         self.__dict__.update(root=tmp or pynchon["working_dir"])
    #     return self.__dict__["root"]

    @property
    def server_pid(self):
        tmp = self.server.proc
        return tmp and tmp.pid

    @property
    def server_url(self):
        return f"http://localhost:{self.server.port}"

    @property
    def git_root(self):
        return self[: "git.root" : self[:"pynchon.working_dir"]]

    @memoized_property
    def server(self):
        return grip.server

    @cli.click.group("gen")
    def gen(self):
        """Generator subcommands"""

    # @cli.click.option('--output',default=None)
    @cli.options.should_print
    @gen.command("version-file")
    def version_file(
        self,
        should_print: bool,
        # output:str=None,
    ):
        """
        Creates {docs.root}/VERSION.md file
        """
        output = abcs.Path(self[:"docs.root":]) / "VERSION.md"
        tmpl = api.render.get_template("pynchon/plugins/core/VERSIONS.md.j2")
        result = tmpl.render(**self.project_config.dict())
        files.dumps(
            content=result, file=output, quiet=False, logger=self.logger.warning
        )
        if should_print and output != "/dev/stdout":
            print(result)
        return True

    @cli.click.option("--background", is_flag=True, default=True)
    @cli.click.option("--force", is_flag=True, default=False)
    def serve(
        self,
        background: bool = True,
        force: bool = False,
    ) -> typing.Dict[str, str]:
        """
        Runs a `grip` server for this project
        """
        LOGGER.critical("running serve")
        args = "--force" if force else ""
        if not self.server.live or force:
            cmd = f"python -m pynchon.gripe start {args}"
            LOGGER.critical(cmd)
            assert invoke(cmd).succeeded
        return dict(url=self.server_url, pid=self.server_pid)

    @tagging.tags(click_aliases=["op", "opn"])
    @fleks.cli.arguments.file
    def open(self, file, server=None):
        """Open a docs-artifact (based on file type)"""
        self.serve()
        file = abcs.Path(file)
        if not file.exists():
            raise ValueError(f"File @ `{file}` does not exist")
        ext = file.full_extension().replace(".", "_")
        opener = f"_open_{ext}"
        try:
            fxn = getattr(self, opener)
        except (AttributeError,) as exc:
            raise NotImplementedError(
                f"dont know how to open `{file}`, " f"method `{opener}` is missing"
            )
        else:
            return fxn(file)

    def open_changes(self) -> typing.List[str]:
        """Open changed files"""
        result = []
        changes = self.list(changes=True)
        if not changes:
            LOGGER.warning("No changes to open")
            return []
        LOGGER.warning(f"opening {len(changes)} changed files..")
        if len(changes) > 10:
            LOGGER.critical("10+ changes; refusing to open this many.")
            return result
        for ch in changes:
            LOGGER.warning(f"opening {ch}")
            result.append(self.open(ch))
        return result

    def plan(self, config=None):
        """Creates a plan for this plugin"""
        plan = super(self.__class__, self).plan(config=config)
        rsrc = self.config["root"]
        if not abcs.Path(rsrc).exists():
            plan.append(
                self.goal(resource=rsrc, type="mkdir", command=f"mkdir -p {rsrc}")
            )
        cmd_t = f"{self.cli_path} gen version-file"
        rsrc = abcs.Path(rsrc) / "VERSION.md"
        plan.append(self.goal(resource=rsrc, type="gen", command=f"{cmd_t}"))
        return plan