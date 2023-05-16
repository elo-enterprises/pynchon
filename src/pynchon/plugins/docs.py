""" pynchon.plugins.docs
"""
import webbrowser

from memoized_property import memoized_property

from pynchon.util.os import invoke

from pynchon import abcs, api, cli, events, models, shimport  # noqa
from pynchon.util import lme, tagging, typing  # noqa

grip = shimport.lazy("pynchon.gripe")
LOGGER = lme.get_logger(__name__)


class OpenerMixin:
    """
    Helper for opening project documentation-files
    inside a webbrowser.  We use a modified version
    of `grip`[1] for this which is called `gripe`[2].

    How this actually works depends on the file-types
    involved, because whereas `grip` works natively to
    render markdown as github-flavored markdown, it
    ignores other types by default.  The `gripe` tool
    adds a special /__raw__ endpoint for other kinds of
    static content.

    (In the future other file-types like `.dot` for raw
    graphviz might be supported, but for now you'll still
    have to render those to png to see a picture.)
    """

    def _open_grip(self, file: str = None):
        """

        :param file: str:  (Default value = None)
        :param file: str:  (Default value = None)

        """
        pfile = abcs.Path(file).absolute()
        relf = pfile.relative_to(abcs.Path(self.git_root))
        grip_url = f"http://localhost:{self.server.port}/{relf}"
        LOGGER.warning(f"opening {grip_url}")
        return dict(url=grip_url, browser=webbrowser.open(grip_url))

    _open__md = _open_grip

    def _open_raw(self, file: str = None, server=None):
        """
        :param file: str:  (Default value = None)
        :param server: Default value = None)
        """
        relf = file.absolute().relative_to(abcs.Path(self.git_root))
        return self._open_grip(abcs.Path("__raw__") / relf)

    _open__html = _open_raw
    _open__png = _open_raw
    _open__jpg = _open_raw
    _open__jpeg = _open_raw
    _open__gif = _open_raw
    _open__htm = _open__html


@tagging.tags(click_aliases=["d"])
class DocsMan(models.ResourceManager, OpenerMixin):
    """
    Management tool for project docs
    """

    class config_class(abcs.Config):
        config_key = "docs"
        defaults = dict()

        @property
        def root(self):
            from pynchon.config import git, pynchon

            tmp = git.get("root")
            return tmp or pynchon["working_dir"]

    name = "docs"
    cli_name = "docs"
    cli_label = "Manager"
    priority = 0
    serving = None

    @property
    def server_pid(self):
        return self.server.proc.pid

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

    @cli.options.output
    @cli.options.should_print
    @gen.command("version-file")
    def version_file(self, output, should_print):
        """Creates {docs.root}/VERSION.md file
        :param output: param should_print:
        :param should_print:
        """
        from pynchon.api import render

        tmpl = render.get_template("pynchon/plugins/core/VERSIONS.md.j2")
        result = tmpl.render(**self.project_config)
        print(result, file=open(output, "w"))
        if should_print and output != "/dev/stdout":
            print(result)
        return True

    @cli.click.option("--background", is_flag=True, default=True)
    @cli.click.option("--force", is_flag=True, default=False)
    def serve(
        self,
        background: bool = True,
        force: bool = False,
    ):
        """
        Runs a `grip` server for this project

        :param background: bool:  (Default value = True)
        :param force: bool:  (Default value = False)
        """
        args = "--force" if force else ""
        if not self.server.live or force:
            assert invoke(f"python -m pynchon.gripe start {args}").succeeded
        return dict(url=self.server_url, pid=self.server_pid)

    @tagging.tags(click_aliases=["op", "opn"])
    @cli.click.argument(
        "file",
    )
    def open(self, file, server=None):
        """Open a docs-artifact (based on file type)
        :param file: param server:  (Default value = None)
        :param server:  (Default value = None)
        """
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

    def open_changes(self):
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
        """Creates a plan for this plugin

        :param config: Default value = None)

        """
        plan = super(self.__class__, self).plan(config=config)
        rsrc = self.config["root"]
        if not abcs.Path(rsrc).exists():
            plan.append(
                self.goal(resource=rsrc, type="mkdir", command=f"mkdir -p {rsrc}")
            )
        cmd_t = "pynchon docs gen version-file"
        rsrc = abcs.Path(rsrc) / "VERSION.md"
        plan.append(
            self.goal(
                resource=rsrc, type="gen", command=f"{cmd_t} --output {rsrc} --print"
            )
        )
        return plan
