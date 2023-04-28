""" pynchon.plugins.jinja
"""
from pynchon import abcs, models
from pynchon.api import project
from pynchon.util import files, lme, typing

LOGGER = lme.get_logger(__name__)

from pynchon.util.text.render import __main__ as render_main


class JinjaConfig(abcs.Config):

    config_key = "jinja"
    defaults = dict()
    # @property
    # def _base(self) -> abcs.AttrDict:
    #     return abcs.AttrDict(**initialized["pynchon"].get("jinja", {}))

    # @property
    # def includes(self) -> typing.List:
    #     docs_root = initialized["pynchon"].get("docs_root", None)
    #     docs_root = docs_root and abcs.Path(docs_root)
    #     if docs_root:
    #         extra = [abcs.Path(docs_root.joinpath("templates"))]
    #     else:
    #         LOGGER.warning("`docs_root` is not set; cannot guess `jinja.includes`")
    #         extra = []
    #     return extra + self._base.get("includes", [])


class Jinja(models.Planner):
    """tools for rendering jinja2 files"""

    name = "jinja"
    defaults = dict()
    config_kls = JinjaConfig
    cli_includes: typing.List[typing.Callable] = [
        render_main.j2cli,
        render_main.jinja_file,
    ]

    def _get_exclude_patterns(self, config):
        """ """
        return list(
            set(config.jinja['exclude_patterns'] + config.globals['exclude_patterns'])
        )

    def _find_j2s(self, config):
        """ """
        proj_conf = config.project.get("subproject", config.project)
        project_root = proj_conf.get("root", config.git["root"])
        search = [
            abcs.Path(project_root).joinpath("**/*.j2"),
        ]
        self.logger.debug(f"search pattern is {search}")
        j2s = files.find_j2s(search)
        self.logger.debug(f"found {len(j2s)} j2 files (pre-filter)")
        excludes = self._get_exclude_patterns(config)
        j2s = [p for p in j2s if not p.match_any_glob(excludes)]
        self.logger.debug(f"found {len(j2s)} j2 files (post-filter)")
        return j2s

    def _get_templates(self, config):
        """ """
        templates = config.jinja['includes']
        templates = [t for t in templates]
        templates = [f"--templates {t}" for t in templates]
        templates = " ".join(templates)
        self.logger.warning(f"found j2 templates: {templates}")
        return templates

    def plan(self, config=None) -> typing.List:
        """Creates a plan for this plugin"""
        config = config or project.get_config()
        plan = super(self.__class__, self).plan(config)
        templates = self._get_templates(config)
        j2s = self._find_j2s(config)
        if j2s:
            plan += [
                f"python -mpynchon.util.text render jinja {templates} --in-place {fname} "
                for fname in j2s
            ]
        else:
            err = "jinja-plugin is included in this config, but found no .j2 files!"
            self.logger.warning(err)
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
#     templates = templates + config.jinja.includes
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
