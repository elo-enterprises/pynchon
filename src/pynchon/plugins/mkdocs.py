""" pynchon.plugins.mkdocs
"""
from pathlib import Path

from pynchon import abcs, api, events, models  # noqa
from pynchon.util import lme, typing  # noqa
from pynchon.util.text import loadf
from pynchon.plugins import util as plugin_util

LOGGER = lme.get_logger(__name__)

class MkdocsPluginConfig(abcs.Config):
    config_key: typing.ClassVar[str] = "mkdocs"
    config_file: str = typing.Field(default=None)

    @property
    def config(self) -> typing.Dict:
        fname = self.config_file
        if fname is None:
            return {}

        return loadf.yaml(fname)

    @property
    def config_file(self) -> typing.StringMaybe:

        docs = plugin_util.get_plugin("docs", strict=False)
        docs = docs and docs.get_current_config()
        subproject = plugin_util.get_plugin("subproject", strict=False)
        subproject = subproject and subproject.get_current_config()
        project = plugin_util.get_plugin("project", strict=False)
        project = project and project.get_current_config()
        candidates = filter(
            None,
            [
                docs and docs.root,
                subproject and subproject.root,
                project and project.root,
            ],
        )
        for folder in [Path(c) for c in candidates]:
            cand = folder / "mkdocs.yml"
            if cand.exists():
                return str(cand.absolute())

class Mkdocs(models.Planner):
    """Mkdocs helper"""

    priority = 6  # before mermaid
    name = "mkdocs"
    cli_name = "mkdocs"
    cli_label = "Docs"
    config_class = MkdocsPluginConfig


    def plan(self):
        """Runs a plan for this plugin"""
        plan = super(self.__class__, self).plan()
        config_file = self["config_file"]
        plugin_cfg = self.config
        mkdocs_config = plugin_cfg.config
        mkdocs_site_dir = mkdocs_config.get("site_dir", self.working_dir / "site")
        plan.append(
            self.goal(
                type="render",
                resource=mkdocs_site_dir,
                command=f"mkdocs build --config-file {config_file}",
            )
        )
        return plan
