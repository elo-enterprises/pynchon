""" pynchon.plugins.plugins
"""
from pynchon import models

from pynchon.util import lme, typing  # noqa

LOGGER = lme.get_logger(__name__)

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
    cli_name = 'plugins'

    # def plan(self, config=None) -> typing.List:
    #     """Creates a plan for this plugin"""
    #     config = config or project.get_config()
    #     plan = super(self.__class__, self).plan(config)
    #     return plan
