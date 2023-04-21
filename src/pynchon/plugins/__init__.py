""" pynchon.plugins
"""
from pynchon import abcs
from pynchon.util import files, lme, typing
from pynchon.util.os import invoke
from pynchon.abcs.plugin import Plugin
from pynchon.config.jinja import JinjaConfig
from pynchon.config.python import PyPiConfig, PythonConfig, PackageConfig
# from pynchon.config.scaffold import ScaffoldConfig

LOGGER = lme.get_logger(__name__)


class PythonCLI(Plugin):
    """ """

    name = "python-cli"
    config = dict
    defaults = dict()

    def plan(self, config):
        plan = super(self.__class__, self).plan(config)
        cli_root = f"{config.pynchon.docs_root}/cli"
        plan += [f"mkdir -p {cli_root}"]
        plan += [f"pynchon gen cli toc --output {cli_root}/README.md"]
        plan += [f"pynchon gen cli all --output-dir {cli_root}"]
        plan += [
            f"pynchon gen cli main --file {fname} --output-dir {cli_root}"
            for fname in config["python"]["entrypoints"]
        ]
        return plan


class PythonAPI(Plugin):
    """ """
    name = "python-api"
    config = dict
    defaults = dict()
    def plan(self, config) -> typing.List:
        plan = super(self.__class__, self).plan(config)
        # self.logger.debug("planning for API docs..")
        api_root = f"{config.pynchon['docs_root']}/api"
        plan += [f"mkdir -p {api_root}"]
        plan += [
            "pynchon gen api toc"
            f' --package {config["python"]["package"]["name"]}'
            f" --output {api_root}/README.md"
        ]
        return plan

class Pypi(Plugin):
    """
    """
    name="pypi"
    config = PyPiConfig
    defaults=dict()


class Jinja(Plugin):
    """ """

    name = "jinja"
    config = JinjaConfig
    defaults = dict()

    def plan(self, config) -> typing.List:
        plan = super(self.__class__, self).plan(config)
        # render_instructions = self.render_instructions
        # self.logger.debug(f"parsed render-instructions: {render_instructions}")
        templates = config["jinja"].includes
        templates = [t for t in templates]
        # import IPython; IPython.embed()
        templates = [f"--templates {t}" for t in templates]
        templates = " ".join(templates)
        self.logger.warning(f"j2 templates: {templates}")
        j2s = files.find_j2s(config)
        j2s = [p for p in j2s if not abcs.Path(config.pynchon["src_root"]).has_file(p)]
        if j2s:
            plan += [
                f"pynchon render jinja {templates} --in-place {fname} " for fname in j2s
            ]
        else:
            err = "`j2` is present in `render` instructions, but found no .j2 files!"
            self.logger.critical(err)
        return plan


class FixMe(Plugin):
    """ """

    name = "fixme"
    config = dict
    defaults = dict()

    def plan(self, config):
        plan = super(self.__class__, self).plan(config)
        plan += [f"pynchon gen fixme --output {config.pynchon.docs_root}/FIXME.md"]
        return plan


class Dot(Plugin):
    """ """

    name = "dot"
    # config= DotConfig
    config = dict
    defaults = dict()


    def plan(self, config):
        plan = super(self.__class__, self).plan(config)
        # render_instructions = self.render_instructions
        # if "dot" in render_instructions:
        self.logger.debug("planning for rendering for .dot graph files..")
        dot_root = config.project["root"]
        for line in invoke(f"find {dot_root} -type f -name *.dot").stdout.split("\n"):
            line = line.strip()
            if not line:
                continue
            plan += [f"pynchon render dot {line} --in-place"]
        # if "dot" in self.gen_instructions:
        self.logger.debug("planning generation for .dot graph files..")
        dot_config = config["pynchon"].get("dot", {})
        script = dot_config.get("script")
        # # assert script, '`"dot" in pynchon.generate` but pynchon.dot.script is not set!'
        # from pynchon.api import render
        #
        # # FIXME: do this substition everywhere!
        # script = render._render(text=script, context=config)
        cmd = "pynchon gen dot files --script {script}"
        plan += [cmd]
        return plan


# """ pynchon.config.scaffold
# """
# from pynchon import abcs
# from pynchon.util import lme
#
# LOGGER = lme.get_logger(__name__)
# from . import initialized
class ScaffoldConfig(abcs.Config):
    """ """

    config_key = "scaffold"


#    @property
#    def includes(self) -> typing.List:
#        docs_root = initialized["pynchon"].get("docs_root", None)
#        docs_root = docs_root and abcs.Path(docs_root)
#        if docs_root:
#            extra = [abcs.Path(docs_root.joinpath("templates"))]
#        else:
#            LOGGER.warning("`docs_root` is not set; cannot guess `scaffold.includes`")
#            extra = []
#        return extra + self._base.get("includes", [])

class Scaffolding(Plugin):
    """ """

    priority = 0
    name = "scaffolding"
    config = dict
    defaults = dict()

    def plan(self, config):
        """ """
        plan = super(Scaffolding, self).plan(config)
        plan += [
            f"mkdir -p {self.state.pynchon.docs_root}",
            f"pynchon project version --output {self.state.pynchon.docs_root}/VERSIONS.md",
        ]
        return plan


registry = [eval(name) for name in dir()]
registry = [kls for kls in registry if typing.is_subclass(kls, Plugin)]
# registry = [kls() for kls in registry]
registry = sorted(registry, key=lambda plugin: plugin.priority)
registry = dict([plugin.name, plugin] for plugin in registry)
LOGGER.info(f"prioritized plugin-registry: {registry}")
for k,v in registry.items():
    print(k)

    # assert isinstance(v.config,(dict,)), [type(v), type(v.config), v.config,]
    # assert isinstance(v.config,(dict,)), [type(v), type(v.config), v.config, v.__class__.config]
# raise Exception(registry)
