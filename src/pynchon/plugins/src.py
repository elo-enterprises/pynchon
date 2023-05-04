""" pynchon.plugins.src
"""
from pynchon import abcs, api, cli, events, models  # noqa
from pynchon.util import lme, typing, tagging  # noqa
from pynchon.util import files

LOGGER = lme.get_logger(__name__)

ext_map = {
    '.sh': dict(
        template='includes/pynchon/src/header/sh.j2', pre=['#', '###'], post='###'
    ),
    '.ini': dict(
        template='includes/pynchon/src/header/ini.j2', pre=['#', '###'], post='###'
    ),
    '.j2': dict(template='includes/pynchon/src/jinja-header.j2', pre=["{#"], post='#}'),
    '.json5': dict(
        template='includes/pynchon/src/json5-header.j2', pre=['//', '///'], post='///'
    ),
    '.py': dict(
        template='includes/pynchon/src/python-header.j2',
        pre=['"""', '"', "'"],
        post='""""',
    ),
}


class SourceMan(models.Manager):
    """Management tool for project source"""

    name = "src"
    cli_name = 'src'

    class config_class(abcs.Config):

        config_key = 'src'

        # @tagging.tagged_property(conflict_strategy='override')
        # def exclude_patterns(self):
        #     globals = plugin_util.get_plugin('globals').get_current_config()
        #     global_ex = globals['exclude_patterns']
        #     my_ex = self.get('exclude_patterns', [])
        #     return list(set( global_ex+my_ex))

    def list(self):
        """ """
        config = api.project.get_config()
        src_root = config.pynchon['src_root']
        include_patterns = self.config.get('include_patterns', ["**"])
        return files.find_globs(include_patterns)

    def plan(self, config=None):
        """ """
        for fsrc in self.list():
            psrc = abcs.Path(fsrc)
            if not psrc.is_file() or not psrc.exists():
                continue
            full_ext, stem = (
                psrc.name[psrc.name.find('.') :],
                psrc.name[: psrc.name.find('.')],
            )
            mdata = ext_map[full_ext]
            with psrc.open('r') as fhandle:
                content = fhandle.read().lstrip()
                if any([content.startswith(pre) for pre in mdata['pre']]):
                    continue
                LOGGER.critical(f"{psrc} missing header!")

    def find(self):
        """file finder"""

    def header(self):
        """creates file headers for source in {src_root}"""

    def map(self):
        """file mapper"""
