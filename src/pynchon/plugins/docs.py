""" pynchon.plugins.docs
"""
from pynchon import abcs, api, cli, events, models  # noqa
from pynchon.util import lme, typing, tagging  # noqa
from pynchon.util import files

LOGGER = lme.get_logger(__name__)


class DocsMan(models.Planner):
    """Management tool for project source"""

    name = "docs"
    cli_name = 'docs'
    priority = 0

    class config_class(abcs.Config):

        config_key = 'docs'

        # @tagging.tagged_property(conflict_strategy='override')
        # def exclude_patterns(self):
        #     globals = plugin_util.get_plugin('globals').get_current_config()
        #     global_ex = globals['exclude_patterns']
        #     my_ex = self.get('exclude_patterns', [])
        #     return list(set( global_ex+my_ex))

    def list(self):
        """ """
        # config = api.project.get_config()
        # src_root = config.pynchon['src_root']
        include_patterns = self.config.get('include_patterns', ["**"])
        return files.find_globs(include_patterns)

    @cli.options.output
    @cli.options.should_print
    def gen_version_file(self, output, should_print):
        """creates {docs.root}/VERSION.md file"""
        raise NotImplementedError()

    def plan(self, config=None):
        """ """
        plan = super(self.__class__, self).plan(config=config)
        rsrc = self.config['root']
        plan.append(self.goal(resource=rsrc, type='mkdir', command=f'mkdir -p {rsrc}'))
        cmd_t = 'pynchon docs gen-version-file'
        rsrc = abcs.Path(rsrc) / 'VERSION.md'
        plan.append(
            self.goal(
                resource=rsrc, type='gen', command=f"{cmd_t} --output {rsrc} --print"
            )
        )
        return plan
