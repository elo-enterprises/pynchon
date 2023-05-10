""" pynchon.plugins.docs
"""
from pynchon import abcs, api, cli, events, models  # noqa
from pynchon.util import lme, typing, tagging  # noqa
from pynchon.util import files, grip

# from pynchon.util.os import invoke, filter_pids

LOGGER = lme.get_logger(__name__)


class DocsMan(models.Planner):
    """Management tool for project source"""

    name = "docs"
    cli_name = 'docs'
    priority = 0
    serving = None

    class config_class(abcs.Config):

        config_key = 'docs'

        # @tagging.tagged_property(conflict_strategy='override')
        # def exclude_patterns(self):
        #     globals = plugin_util.get_plugin('globals').get_current_config()
        #     global_ex = globals['exclude_patterns']
        #     my_ex = self.get('exclude_patterns', [])
        #     return list(set( global_ex+my_ex))

    def list(self):
        """Lists resources associated with this plugin"""
        include_patterns = self.config.get('include_patterns', ["**.j2"])
        root = abcs.Path(self.config['root'])
        proot = self.project_config['pynchon']['root']
        tmp = [p for p in include_patterns if abcs.Path(p).is_absolute()]
        tmp += [root / p for p in include_patterns if not abcs.Path(p).is_absolute()]
        tmp += [proot / p for p in include_patterns if not abcs.Path(p).is_absolute()]
        return files.find_globs(tmp)

    @cli.click.group('gen', hidden=True)
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

    def _open_md(self, file: str = None, server=None):
        """ """
        import webbrowser

        pfile = abcs.Path(file).absolute()
        groot = self.project_config['git']['root']
        relf = pfile.relative_to(abcs.Path(groot))
        grip_url = f'http://localhost:{self.server.port}/{relf}'
        LOGGER.warning(f'opening {grip_url}')
        return dict(url=grip_url, browser=webbrowser.open(grip_url))

    @cli.click.argument(
        'file',
    )
    def open(self, file, server=None):
        """Open a docs-artifact (based on file type)"""
        file = abcs.Path(file)
        if not file.exists():
            raise ValueError(f'File @ `{file}` does not exist')
        if file.endswith('.md'):
            return self._open_md(file, server=server)
        else:
            raise NotImplementedError(f'dont know how to open {file}')

    def open_changes(self, server=None):
        """Open changed files"""
        result = []
        changes = self.changes
        if not self.changes:
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
