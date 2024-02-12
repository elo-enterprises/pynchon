""" pynchon.plugins.mkdocs
"""

from pathlib import Path

from pynchon.plugins import util as plugin_util
from pynchon.util.text import loadf

from pynchon import abcs, api, events, models  # noqa
from pynchon.util import lme, typing  # noqa

LOGGER = lme.get_logger(__name__)


class MkdocsPluginConfig(abcs.Config):
    config_key: typing.ClassVar[str] = "mkdocs"
    config_file: str = typing.Field(default=None)

    @property
    def site_dir(self):
        return self.config.get("site_dir", "site")

    @property
    def config(self) -> typing.Dict:
        """
        returns a dictionary with the current mkdocs configuration
        """
        fname = self.config_file
        if fname is None:
            return {}

        return loadf.yaml(fname)

    @property
    def config_file(self) -> typing.StringMaybe:
        """returns the path to the mkdocs config-file, if applicable"""
        docs = plugin_util.get_plugin("docs", strict=False)
        docs = docs and docs.get_current_config()
        subproject = plugin_util.get_plugin("subproject", strict=False)
        subproject = subproject and subproject.get_current_config()
        project = plugin_util.get_plugin("project", strict=False)
        project = project and project.get_current_config()
        candidates = filter(
            None,
            [
                abcs.Path(".").absolute(),
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

    def open(self):
        """
        Opens `site_dir` in a webbrowser
        """
        import webbrowser

        index_f = Path(self.site_dir).absolute() / "index.html"
        url = f"file://{index_f}"
        return webbrowser.open(url)

    @property
    def site_dir(self) -> str:
        """
        Returns mkdocs `site_dir` if present in config, or guesses what it should be
        """
        plugin_cfg = self.config
        mkdocs_config = plugin_cfg.config
        result = str(mkdocs_config.get("site_dir", self.working_dir / "site"))
        self.logger.warning(f"returning {result}")
        return result

    # def _hook_open_after_apply(self, result) -> bool:
    #     raise Exception(result)

    def plan(self):
        """
        Runs a plan for this plugin
        """
        plan = super(self.__class__, self).plan()
        config_file = self["config_file"]
        plan.append(
            self.goal(
                type="render",
                resource=self.site_dir,
                command=f"mkdocs build --config-file {config_file}",
            )
        )
        return plan
