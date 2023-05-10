""" pynchon.plugins.docs
"""
import webbrowser

from pynchon.util import files, grip

from pynchon import abcs, api, cli, events, models  # noqa
from pynchon.util import lme, typing, tagging  # noqa

# from pynchon.util.os import invoke, filter_pids

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

    @cli.click.group('gen')
    def gen(self):
        """Generator subcommands"""

    @cli.click.option('--background', is_flag=True, default=True)
    @cli.click.option('--force', is_flag=True, default=False)
    def serve(
        self,
        background: bool = True,
        force: bool = False,
        logfile: str = '.tmp.grip.log',
    ):
        """Runs a `grip` server for this project"""
        self.serving = grip.serve(background=background, force=force, logfile=logfile)
        return self.serving

    @cli.options.output
    @cli.options.should_print
    @gen.command('version-file')
    def version_file(self, output, should_print):
        """Creates {docs.root}/VERSION.md file"""
        raise NotImplementedError()

    # @property
    # def server(self):
    #     return grip.server()

    def _open_grip(self, file: str = None, server=None):
        """ """
        pfile = abcs.Path(file).absolute()
        groot = self.project_config['git']['root']
        relf = pfile.relative_to(abcs.Path(groot))
        grip_url = f'http://localhost:{server.port}/{relf}'
        LOGGER.warning(f'opening {grip_url}')
        return dict(url=grip_url, browser=webbrowser.open(grip_url))

    _open__md = _open_grip
    _open__html = _open_grip

    @cli.click.argument(
        'file',
    )
    def open(self, file, server=None):
        """Open a docs-artifact (based on file type)"""
        server = server or self.serving
        if not server and not grip.serving():
            grip.serve()
        self.serving = server = grip.server()
        file = abcs.Path(file)
        if not file.exists():
            raise ValueError(f'File @ `{file}` does not exist')
        ext = file.full_extension().replace('.', '_')
        name = f'_open_{ext}'
        try:
            fxn = getattr(self, name)
            # return self._open_md(file, server=server)
        except (AttributeError,) as exc:
            raise NotImplementedError(
                f'dont know how to open `{file}`, method `{name}` is missing'
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
        if not server and not grip.serving():
            grip.serve()
        self.server = grip.server()
        self.server.port = grip.port()
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
