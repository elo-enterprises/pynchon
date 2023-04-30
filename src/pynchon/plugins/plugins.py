""" pynchon.plugins.plugins
"""
from pynchon import abcs, models
from pynchon.api import project
from pynchon.util import files, lme, typing

LOGGER = lme.get_logger(__name__)

from pynchon.util.text.render import __main__ as render_main

# class PluginsConfig(abcs.Config):
#
#     config_key = "plugins"
#     defaults = dict()
# @property
# def _base(self) -> abcs.AttrDict:
#     return abcs.AttrDict(**initialized["pynchon"].get("jinja", {}))

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


class PluginsMan(models.Provider):
    """meta-plugin for managing plugins"""

    name = "plugins"
    cli_name = 'cut'
    defaults = dict()
    # config_class = PluginsConfig
    cli_subsumes: typing.List[typing.Callable] = [
        # render_main.j2cli,
        # render_main.jinja_file,
    ]

    # def plan(self, config=None) -> typing.List:
    #     """Creates a plan for this plugin"""
    #     config = config or project.get_config()
    #     plan = super(self.__class__, self).plan(config)
    #     return plan
