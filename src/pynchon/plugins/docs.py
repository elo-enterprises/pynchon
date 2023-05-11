""" pynchon.plugins.docs
"""
import webbrowser

from memoized_property import memoized_property

from pynchon import shimport
from pynchon.util import files, grip

from pynchon import abcs, api, cli, events, models  # noqa
from pynchon.util import lme, typing, tagging  # noqa

grip = shimport.lazy('pynchon.util.grip')
LOGGER = lme.get_logger(__name__)


@tagging.tags(click_aliases=['d'])
class DocsMan(models.Planner):
    """Management tool for project docs"""

    name = "docs"
    cli_name = 'docs'
    cli_label = 'Manager'
    priority = 0
    serving = None

    class config_class(abcs.Config):
        config_key = 'docs'

    @property
    def server_pid(self):
        return self.server.proc.pid

    @property
    def server_url(self):
        return f'http://localhost:{self.server.port}'

    @property
    def git_root(self):
        return self[: 'git.root' : self[:'pynchon.working_dir']]

    @memoized_property
    def server(self):
        return grip.server

    @cli.click.group('gen')
    def gen(self):
        """Generator subcommands"""

    @cli.click.option('--background', is_flag=True, default=True)
    @cli.click.option('--force', is_flag=True, default=False)
    def serve(
        self,
        background: bool = True,
        force: bool = False,
    ):
        """Runs a `grip` server for this project"""
        args = '--force' if force else ''
        if not self.server.live or force:
            from pynchon.util.os import invoke

            invoke(f'python -m pynchon.util.grip serve {args}').succeeded
        return dict(url=self.server_url, pid=self.server_pid)

    @cli.options.output
    @cli.options.should_print
    @gen.command('version-file')
    def version_file(self, output, should_print):
        """Creates {docs.root}/VERSION.md file"""
        raise NotImplementedError()

    def _open_grip(self, file: str = None):
        """ """
        pfile = abcs.Path(file).absolute()
        relf = pfile.relative_to(abcs.Path(self.git_root))
        grip_url = f'http://localhost:{self.server.port}/{relf}'
        LOGGER.warning(f'opening {grip_url}')
        return dict(url=grip_url, browser=webbrowser.open(grip_url))

    _open__md = _open_grip

    def _open__html(self, file: str = None, server=None):
        """ """
        relf = file.absolute().relative_to(abcs.Path(self.git_root))
        return self._open_grip(abcs.Path('__raw__') / relf)

    @tagging.tags(click_aliases=['op', 'opn'])
    @cli.click.argument(
        'file',
    )
    def open(self, file, server=None):
        """Open a docs-artifact (based on file type)"""
        self.serve()
        file = abcs.Path(file)
        if not file.exists():
            raise ValueError(f'File @ `{file}` does not exist')
        ext = file.full_extension().replace('.', '_')
        opener = f'_open_{ext}'
        try:
            fxn = getattr(self, opener)
        except (AttributeError,) as exc:
            raise NotImplementedError(
                f'dont know how to open `{file}`, ' f'method `{opener}` is missing'
            )
        else:
            return fxn(file, server=server)

    def open_changes(self, server=None):
        """Open changed files"""
        result = []
        changes = self.list(changes=True)
        if not changes:
            LOGGER.warning("No changes to open")
            return []
        LOGGER.warning(f"opening {len(changes)} changed files..")
        if len(changes) > 10:
            LOGGER.critical('10+ changes; refusing to open this many.')
            return result
        for ch in changes:
            LOGGER.warning(f'opening {ch}')
            result.append(self.open(ch, server=server))
        return result

    def plan(self, config=None):
        """Creates a plan for this plugin"""
        plan = super(self.__class__, self).plan(config=config)
        rsrc = self.config['root']
        if not abcs.Path(rsrc).exists():
            plan.append(
                self.goal(resource=rsrc, type='mkdir', command=f'mkdir -p {rsrc}')
            )
        cmd_t = 'pynchon docs gen version-file'
        rsrc = abcs.Path(rsrc) / 'VERSION.md'
        plan.append(
            self.goal(
                resource=rsrc, type='gen', command=f"{cmd_t} --output {rsrc} --print"
            )
        )
        return plan
