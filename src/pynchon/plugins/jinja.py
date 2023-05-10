""" pynchon.plugins.jinja
"""
from pynchon.util import lme, typing, tagging  # noqa
from pynchon import abcs, models
from pynchon.api import project
from pynchon.util import files, text

LOGGER = lme.get_logger(__name__)

# from pynchon.util.text.render import __main__ as render_main

# @property
# def template_includes(self) -> typing.List:
#     docs_root = initialized["pynchon"].get("docs_root", None)
#     docs_root = docs_root and abcs.Path(docs_root)
#     if docs_root:
#         extra = [abcs.Path(docs_root.joinpath("templates"))]
#     else:
#         LOGGER.warning("`docs_root` is not set; cannot guess `jinja.template_includes`")
#         extra = []
#     return extra + self._base.get("template_includes", [])

from pynchon import cli, api
from pynchon.plugins import util as plugin_util


@tagging.tags(click_aliases=['j'])
class Jinja(models.Planner):
    """Renders files with {jinja.template_includes}"""

    name = "jinja"
    priority = 9
    COMMAND_TEMPLATE = (
        "python -mpynchon.util.text render jinja "
        "{resource} --context-file {context_file} "
        "--in-place {template_args}"
    )

    cli_subsumes: typing.List[typing.Callable] = [
        # render_main.j2cli,
        # render_main.jinja_file,
    ]
    # diff --color --minimal -w --side-by-side /etc/bash.bashrc <(bash --pretty-print /etc/bash.bashrc )

    class config_class(abcs.Config):

        config_key = "jinja"
        defaults = dict(
            template_includes=[],
        )

        @tagging.tagged_property(conflict_strategy='override')
        def exclude_patterns(self):
            globals = plugin_util.get_plugin('globals').get_current_config()
            global_ex = globals['exclude_patterns']
            my_ex = self.get('exclude_patterns', [])
            return list(set(global_ex + my_ex + ["**/pynchon/templates/includes/**"]))

    def _get_jinja_context(self):
        """ """
        fname = ".tmp.jinja.ctx.json"
        with open(fname, 'w') as fhandle:
            fhandle.write(text.to_json(self.config))
        return f"{fname}"

    @property
    def _include_folders(self):
        includes = self.project_config.jinja['template_includes']
        from pynchon import api

        includes = api.render.get_jinja_includes(*includes)
        return includes

    @cli.click.option('--local', default=False, is_flag=True)
    def list_includes(
        self,
        local: bool = False,
    ):
        """Lists full path of each include-file"""
        includes = self._include_folders
        if local:
            includes.remove(api.render.PYNCHON_CORE_INCLUDES)
        includes = [abcs.Path(t) / '**/*.j2' for t in includes]
        LOGGER.warning(includes)
        matches = files.find_globs(includes)
        return matches

    @cli.click.option('--local', default=False, is_flag=True)
    def list_include_args(
        self,
        local: bool = False,
    ):
        """Lists all usable {% include ... %} values"""
        includes = self.list_includes(local=local)
        out = []
        for fname in includes:
            fname = abcs.Path(fname)
            for inc in self._include_folders:
                try:
                    fname = fname.relative_to(inc)
                except ValueError:
                    continue
                else:
                    out.append(fname)
                break
            else:
                pass
        return out

    def list(self, changes=False):
        """Lists affected resources in this project"""
        default = self[:'project']
        proj_conf = self[:'project.subproject':default]
        default = self[:'git.root']
        project_root = proj_conf.get("root", default)
        globs = [
            abcs.Path(project_root).joinpath("**/*.j2"),
        ]
        self.logger.debug(f"search patterns are {globs}")
        result = files.find_globs(globs)
        self.logger.debug(f"found {len(result)} j2 files (pre-filter)")
        excludes = self['exclude_patterns']
        self.logger.debug(f"filtering search with {len(excludes)} excludes")
        result = [p for p in result if not p.match_any_glob(excludes)]
        self.logger.debug(f"found {len(result)} j2 files (post-filter)")
        if not result:
            err = f"{self.__class__.__name__} is active, but found no .j2 files!"
            self.logger.critical(err)
        return result

    def plan(
        self,
        config=None,
    ) -> typing.List:
        """Creates a plan for this plugin"""

        def _get_template_args():
            """ """
            templates = self['template_includes']
            templates = [t for t in templates]
            templates = [f"--include {t}" for t in templates]
            templates = " ".join(templates)
            return templates

        plan = super(self.__class__, self).plan()
        jctx = self._get_jinja_context()
        templates = _get_template_args()
        # self.logger.info("using `templates` argument(s):")
        # self.logger.info(f"  {templates}")
        for rsrc in self.list():
            plan.append(
                self.goal(
                    type='render',
                    resource=rsrc,
                    command=self.COMMAND_TEMPLATE.format(
                        resource=rsrc, context_file=jctx, template_args=templates
                    ),
                )
            )
        return plan
