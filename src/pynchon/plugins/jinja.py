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

    def _get_exclude_patterns(self, config):
        """ """
        return list(
            set(config.jinja.get('exclude_patterns',[]) + config.globals['exclude_patterns'])
        )

    def _get_templates(self, config):
        """ """
        templates = config.jinja['template_includes']
        templates = [t for t in templates]
        templates = [f"--include {t}" for t in templates]
        templates = " ".join(templates)
        self.logger.warning(f"found j2 templates: {templates}")
        return templates

    def _find_j2s(self, config):
        """ """
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

    def list(self, config=None):
        """ """
        return self._find_j2s(config or project.get_config())

    def _get_jinja_context(self, config):
        """ """
        fname = f".tmp.{id(self)}"
        with open(fname, 'w') as fhandle:
            fhandle.write(text.to_json(config))
        return f"--context-file {fname}"

    def plan(
        self,
        config=None,
        # relative_paths: bool = True,
    ) -> typing.List:
        """Creates a plan for this plugin"""
        config = config or project.get_config()
        plan = super(self.__class__, self).plan(config)
        jctx = self._get_jinja_context(config)
        self.logger.info("using `context` argument:")
        self.logger.info(f"  {jctx}")
        templates = self._get_templates(config)
        self.logger.info("using `templates` argument:")
        self.logger.info(f"  {templates}")
        j2s = self.list(config)
        self.logger.warning(f"plan covers: {text.to_json(j2s)}")
        cmd_t = "python -mpynchon.util.text render jinja"
        plan += [f"{cmd_t} {fname} {jctx} {templates} --in-place" for fname in j2s]
        return plan


# @kommand(
#     name="jinja",
#     parent=PARENT,
#     options=[
#         # options.file,
#         options.ctx,
#         options.output,
#         options.template,
#         click.option(
#             "--in-place",
#             is_flag=True,
#             default=False,
#             help=(
#                 "if true, writes to {file}.{ext} "
#                 "(dropping any .j2 extension if present)"
#             ),
#         ),
#     ],
#     arguments=[files_arg],
# )
# def render_j2(files, ctx, output, in_place, templates):
#     """
#     Render J2 files with given context
#     """
#     templates = templates.split(",")
#     assert isinstance(templates, (list, tuple)), f"expected list got {type(templates)}"
#     # assert (file or files) and not (file and files), 'expected files would be provided'
#     from pynchon import config
#
#     templates = templates + config.jinja.template_includes
#     if ctx:
#         if "{" in ctx:
#             LOGGER.debug("context is inlined JSON")
#             ctx = json.loads(ctx)
#         elif "=" in ctx:
#             LOGGER.debug("context is inlined (comma-separed k=v format)")
#             ctx = dict([kv.split("=") for kv in ctx.split(",")])
#         else:
#             with open(ctx, "r") as fhandle:
#                 content = fhandle.read()
#             if ctx.endswith(".json"):
#                 LOGGER.debug("context is JSON file")
#                 ctx = json.loads(content)
#             elif ctx.endswith(".json5"):
#                 LOGGER.debug("context is JSON-5 file")
#                 ctx = pyjson5.loads(content)
#             elif ctx.endswith(".yml") or ctx.endswith(".yaml"):
#                 LOGGER.debug("context is yaml file")
#                 ctx = yaml.loads(content)
#             else:
#                 raise TypeError(f"not sure how to load: {ctx}")
#     else:
#         ctx = {}
#     LOGGER.debug("user-defined context: ")
#     LOGGER.debug(json.dumps(ctx, cls=abcs.JSONEncoder))
#     if files:
#         return [
#             render.j2(
#                 file, ctx=ctx, output=output, in_place=in_place, templates=templates
#             )
#             for file in files
#         ]
#     # elif files:
#     #     LOGGER.debug(f"Running with many: {files}")
#     #     return [
#     #         render.j2(file, output=output, in_place=in_place, templates=templates)
#     #         for file in files ]
