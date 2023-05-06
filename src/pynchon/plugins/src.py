""" pynchon.plugins.src
"""
from pynchon import abcs, api, cli, events, models  # noqa
from pynchon.util import lme, typing, tagging  # noqa
from pynchon.util import files

LOGGER = lme.get_logger(__name__)

EXT_MAP = {
    '.ini': dict(
        template='pynchon/plugins/src/header/ini.j2', pre=['#', '###'], post='###'
    ),
    '.j2': dict(template='pynchon/plugins/src/header/jinja.j2', pre=["{#"], post='#}'),
    '.json5': dict(
        template='includes/pynchon/src/json5-header.j2', pre=['//', '///'], post='///'
    ),
    '.py': dict(
        # template='includes/pynchon/src/python-header.j2',
        template='pynchon/plugins/src/header/python.j2',
        pre=['"""', '"', "'"],
        post='""""',
    ),
    '.sh': dict(
        template='pynchon/plugins/src/header/sh.j2', pre=['#', '###'], post='###'
    ),
}


class SourceMan(models.Manager):
    """Management tool for project source"""

    name = "src"
    cli_name = 'src'
    priority = 0

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
        # config = api.project.get_config()
        # src_root = config.pynchon['src_root']
        include_patterns = self.config.get('include_patterns', ["**"])
        return files.find_globs(include_patterns)

    def _get_missing_headers(self, resources):
        """ """
        result = dict(extensions=set([]), files=[])
        for p_rsrc in resources:
            if not p_rsrc.is_file() or not p_rsrc.exists():
                continue
            # ext_info = self._rsrc_ext_info(p_rsrc)
            ext_meta = EXT_MAP[p_rsrc.full_extension()]
            preamble_patterns = ext_meta['pre']
            assert isinstance(preamble_patterns, (list,))
            with p_rsrc.open('r') as fhandle:
                content = fhandle.read().lstrip()
                if any([content.startswith(pre) for pre in preamble_patterns]):
                    # we detected expected comment at the top of the file,
                    # so the appropriate header *might* be present; skip it
                    continue
                else:
                    # no header at all
                    result['files'].append(p_rsrc)
                    result['extensions'] = result['extensions'].union(
                        set([p_rsrc.full_extension()])
                    )
        result.update(extensions=list(result['extensions']))
        return result

    def _plan_empties(self, resources):
        """ """
        result = []
        return result

    def _render_header_file(self, rsrc: abcs.Path = None):
        """ """
        ext = rsrc.full_extension()
        templatef = EXT_MAP[ext]['template']
        tpl = api.render.get_template(templatef)
        abs = rsrc.absolute()
        src_root = abcs.Path(self.config['root']).absolute()
        try:
            relf = abs.relative_to(src_root)
        except ValueError:
            relf = abs.relative_to(abcs.Path(".").absolute())
        relf = relf.path_truncated()
        module_dotpath = str(relf).replace('/', '.')
        tmp2 = __name__.replace('.', '-')
        fname = f'.tmp.src-header.{module_dotpath}{ext}'
        result = tpl.render(
            module_dotpath=module_dotpath,
            template=templatef,
            filename=str(abs),
            relative_filename=relf,
        )
        if not result:
            err = f'header for extension "{ext}" rendered to "{fname}" from {templatef}'
            raise Exception(err)
        with open(fname, 'w') as fhandle:
            fhandle.write(result)
        LOGGER.warning(f"wrote {fname}")
        return fname

    def plan(self, config=None):
        """ """
        plan = super(SourceMan, self).plan(config=config)
        resources = [abcs.Path(fsrc) for fsrc in self.list()]
        cmd_t = 'python -mpynchon.util.files prepend --clean '
        loop = self._get_missing_headers(resources)
        for rsrc in loop['files']:
            ext = rsrc.full_extension()
            ext = ext[1:] if ext.startswith('.') else ext
            # fhdr = header_files[ext]
            fhdr = self._render_header_file(rsrc)
            plan.append(
                self.goal(
                    resource=rsrc,
                    type='change',
                    command=f"{cmd_t} {fhdr} {rsrc}",
                )
            )
        for rsrc in self._plan_empties(resources):
            plan.append(
                self.goal(
                    resource=rsrc,
                    type='delete',
                    command=f'rm {rsrc}',
                )
            )
        return plan

    def find(self):
        """file finder"""

    def header(self):
        """creates file headers for source in {src_root}"""

    def map(self):
        """file mapper"""
