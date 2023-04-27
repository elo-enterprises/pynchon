""" pynchon.plugins.jinja
"""
from pynchon import abcs, models
from pynchon.util import files, lme, typing
from pynchon.api import project

LOGGER = lme.get_logger(__name__)


class JinjaConfig(abcs.Config):

    config_key = "jinja"
    defaults = dict()
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
    """ tools for rendering jinja2 files """

    name = "jinja"
    defaults = dict()
    config_kls = JinjaConfig

    def plan(self, config=None) -> typing.List:
        """ """
        config = config or project.get_config()
        plan = super(self.__class__, self).plan(config)
        templates = config.jinja['includes']
        templates = [t for t in templates]
        templates = [f"--templates {t}" for t in templates]
        templates = " ".join(templates)
        self.logger.warning(f"found j2 templates: {templates}")
        exclude_patterns = list(set(config.jinja['exclude_patterns']+config.globals['exclude_patterns']))
        proj_conf = config.project.get("subproject", config.project)
        project_root = proj_conf.get("root", config.git["root"])
        search = [
            abcs.Path(project_root).joinpath("**/*.j2"),
        ]
        self.logger.debug(f"search pattern is {search}")
        j2s = files.find_j2s(search)
        self.logger.debug("found {len(j2s)} j2 files (pre-filter)")
        j2s = [p for p in j2s if not p.match_any_glob(exclude_patterns)]
        self.logger.debug("found {len(j2s)} j2 files (post-filter)")
        if j2s:
            plan += [
                f"pynchon render jinja {templates} --in-place {fname} " for fname in j2s
            ]
        else:
            err = "jinja-plugin is included in this config, but found no .j2 files!"
            self.logger.warning(err)
        return plan
