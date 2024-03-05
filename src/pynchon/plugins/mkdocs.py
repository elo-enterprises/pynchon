""" pynchon.plugins.mkdocs
"""

from pathlib import Path

import yaml

from pynchon.plugins import util as plugin_util
from pynchon.util.text import loadf

from pynchon import abcs, api, events, models  # noqa
from pynchon.util import lme, typing  # noqa

LOGGER = lme.get_logger(__name__)


class MkdocsPluginConfig(abcs.Config):
    config_key: typing.ClassVar[str] = "mkdocs"
    config_file: str = typing.Field(default=None)

    @property
    def tags(self) -> typing.List:
        """ """
        tags = set()
        for p in self.pages:
            tags = tags.union(set(p.get("tags", [])))
        # NB: removes empty-string
        return list(filter(None, tags))

    @property
    def pages(self) -> typing.List:
        """ """
        mconf = self.config
        if mconf:
            ddir = abcs.Path(mconf.get("docs_dir", "docs"))
            from mkdocs.config.defaults import MkDocsConfig
            from mkdocs.structure.files import File
            from mkdocs.structure.pages import Page

            cfg = MkDocsConfig()

            data = yaml.load(open(self.config_file).read(), yaml.FullLoader)
            cfg.load_dict(data)
            cfg.validate()
            # fl = File(
            #     'heredoc/ambient-calculus-1.md',
            #     cfg.docs_dir, cfg.site_dir, cfg.use_directory_urls)
            # config_file
            # pconf = mconf['plugins'] if 'plugins' in mconf else {}
            # bconf = [conf for conf in pconf if 'blogging' in list(conf.keys())]
            # bconf = bconf[0]['blogging'] if bconf else {}
            pfiles = ddir.glob("**/*.md")
            # pfiles = [p.relative_to(ddir) for p in pfiles]
            pages = []
            for pfile in pfiles:
                rel_pfile = pfile.relative_to(ddir)
                mfile = File(
                    str(rel_pfile), cfg.docs_dir, cfg.site_dir, cfg.use_directory_urls
                )
                pg = Page(
                    file=mfile,
                    config=cfg,
                    title=None,
                )
                pg.read_source(cfg)
                tags = pg.meta.get("tags", [])
                pmeta = dict(
                    title=pg.title,
                    relative_url=pg.url,
                    path=pfile.absolute(),
                    tags=tags,
                )
                pages.append(pmeta)
            return pages

    @property
    def blog_posts(self) -> list:
        """
        returns blog posts, iff blogging plugin is installed.
        resulting files, if any, will not include index and
        will be sorted by modification time
        """
        mconf = self.config
        if mconf:
            pconf = mconf["plugins"] if "plugins" in mconf else {}
            ddir = abcs.Path(mconf.get("docs_dir", "docs"))
            bconf = [conf for conf in pconf if "blogging" in list(conf.keys())]
            bconf = bconf[0]["blogging"] if bconf else {}
            blog_dirs = [ddir / bdir for bdir in bconf.get("dirs", [])]
            result = []
            for bdir in blog_dirs:
                result += [g for g in bdir.glob("**/*.md") if g.name != "index.md"]
            result = reversed(sorted(result, key=lambda p: p.lstat().st_mtime))
            result = [str(p) for p in result]
            return result

    @property
    def site_relative_url(self):
        import urllib

        site_url = self.config["site_url"] if "site_url" in self.config else None
        if site_url:
            return urllib.parse.urlparse(site_url).path

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


DEFAULT_LOG_FILE = ".tmp.mkdocs.log"


class Mkdocs(models.Planner):
    """Mkdocs helper"""

    priority = 8  # before mermaid
    name = "mkdocs"
    cli_name = "mkdocs"
    cli_label = "Docs"
    config_class = MkdocsPluginConfig

    @property
    def config_file(self) -> str:
        return self["config_file"]

    def serve(self, background: bool = True):
        """
        Wrapper for `mkdocs serve`
        """
        from pynchon.util.os import invoke

        bg = "&" if background else ""
        cmd = f"mkdocs serve --config-file {self.config_file} >> {DEFAULT_LOG_FILE} 2>&1 {bg}"
        result = invoke(cmd)
        return result

    def open(self):
        """
        Opens `dev_addr` in a webbrowser
        """
        import webbrowser

        # index_f = Path(self.site_dir).absolute() / "index.html"
        # url = f"file://{index_f}"
        mconfig = self.config.config
        url = mconfig["dev_addr"]
        assert url
        self.logger.warning(f"opening {url}")
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
        plan.append(
            self.goal(
                type="render",
                resource=self.site_dir,
                command=f"mkdocs build --config-file {self.config_file}",
            )
        )
        return plan
