""" pynchon.plugins.jinja
"""
from pynchon.util import lme, typing  # noqa
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


class Jinja(models.Planner):
    """Renders files with {jinja.template_includes}"""

    name = "jinja"
    cli_subsumes: typing.List[typing.Callable] = [
        # render_main.j2cli,
        # render_main.jinja_file,
    ]

    class config_class(abcs.Config):

        config_key = "jinja"
        defaults = dict(
            # exclude_patterns=src/pynchon/templates/
        )

    def _get_jinja_context(self, config):
        """ """
        fname = f".tmp.ctx.{id(self)}.json"
        with open(fname, 'w') as fhandle:
            fhandle.write(text.to_json(config))
        return f"{fname}"

    def _get_exclude_patterns(self, config):
        """ """
        return list(
            set(
                config.jinja.get('exclude_patterns', [])
                + config.globals['exclude_patterns']
            )
        )

    def list(self, config=None):
        """Lists affected resources in this project"""
        config = config or project.get_config()
        proj_conf = config.project.get("subproject", config.project)
        project_root = proj_conf.get("root", config.git["root"])
        search = [
            abcs.Path(project_root).joinpath("**/*.j2"),
        ]
        self.logger.debug(f"search pattern is {search}")
        result = files.find_globs(search)
        self.logger.debug(f"found {len(result)} j2 files (pre-filter)")
        excludes = self._get_exclude_patterns(config)
        self.logger.debug(f"filtering search with {len(excludes)} excludes")
        result = [p for p in result if not p.match_any_glob(excludes)]
        self.logger.debug(f"found {len(result)} j2 files (post-filter)")
        if not result:
            err = "jinja-plugin is included in this config, but found no .j2 files!"
            self.logger.critical(err)
        return result

    def plan(
        self,
        config=None,
    ) -> typing.List:
        """Creates a plan for this plugin"""

        def _get_templates(config):
            """ """
            templates = config.jinja['template_includes']
            templates = [t for t in templates]
            templates = [f"--include {t}" for t in templates]
            templates = " ".join(templates)
            self.logger.warning(f"found j2 templates: {templates}")
            return templates

        config = config or project.get_config()
        plan = super(self.__class__, self).plan(config)
        jctx = self._get_jinja_context(config)
        templates = _get_templates(config)
        self.logger.info("using `templates` argument(s):")
        self.logger.info(f"  {templates}")
        # j2s = self.list(config)
        cmd_t = "python -mpynchon.util.text render jinja "
        cmd_t += "{resource} --context-file {context_file} "
        cmd_t += "--in-place {template_args}"
        for rsrc in self.list():
            plan.append(
                models.Goal(
                    type='render',
                    resource=rsrc,
                    command=cmd_t.format(
                        resource=rsrc, context_file=jctx, template_args=templates
                    ),
                )
            )
        return plan
