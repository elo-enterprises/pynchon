""" pynchon.plugins.jinja
"""
from pynchon import abcs
from pynchon.util import files, lme, typing
from pynchon.abcs.plugin import Plugin

LOGGER = lme.get_logger(__name__)


class Jinja(Plugin):
    """ """

    name = "jinja"
    defaults = dict()

    class config(abcs.Config):
        """ """

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

    def plan(self, config) -> typing.List:
        plan = super(self.__class__, self).plan(config)
        # render_instructions = self.render_instructions
        # self.logger.debug(f"parsed render-instructions: {render_instructions}")
        templates = config.jinja['includes']
        templates = [t for t in templates]
        # import IPython; IPython.embed()
        templates = [f"--templates {t}" for t in templates]
        templates = " ".join(templates)
        self.logger.warning(f"j2 templates: {templates}")
        # import IPython; IPython.embed()
        from pynchon import abcs #config
        # import IPython; IPython.embed()
        project = config.project.get("subproject", config.project)
        project_root = project.get("root", config.git["root"])
        globs = [
            abcs.Path(project_root).joinpath("**/*.j2"),
        ]

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
