""" pynchon.plugins.dot
"""
from pynchon.util import files, lme, typing
from pynchon.abcs.plugin import Plugin

LOGGER = lme.get_logger(__name__)


class Dot(Plugin):
    """ """

    name = "dot"
    # config= DotConfig
    config = dict
    defaults = dict()

    def plan(self, config) -> typing.List[str]:
        plan = super(self.__class__, self).plan(config)
        # render_instructions = self.render_instructions
        # if "dot" in render_instructions:
        self.logger.debug("planning for rendering for .dot graph files..")
        dot_root = config.project["root"]
        for line in files.find_suffix(root=dot_root, suffix="dot"):
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
