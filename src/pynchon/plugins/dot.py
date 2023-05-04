""" pynchon.plugins.dot
"""
import os

from pynchon import abcs, models, cli, api
from pynchon.util import files
from pynchon.util.os import invoke

from pynchon.util import lme, typing  # noqa

LOGGER = lme.get_logger(__name__)


class Dot(models.Planner):
    """Finds / Renders (graphviz) dot files for this project"""

    name = "dot"

    class config_class(abcs.Config):
        config_key = 'dot'

    def _get_exclude_patterns(self, config):
        """ """
        return list(
            set(
                config.dot.get('exclude_patterns', [])
                + config.globals['exclude_patterns']
            )
        )

    def list(self, config=None) -> typing.List[str]:
        """ """
        config = config or self.project_config
        proj_conf = config.project.get("subproject", config.project)
        project_root = proj_conf.get("root", config.git["root"])
        search = [
            abcs.Path(project_root).joinpath("**/*.dot"),
        ]
        self.logger.debug(f"search pattern is {search}")
        result = files.find_globs(search)
        self.logger.debug(f"found {len(result)} files (pre-filter)")
        excludes = self._get_exclude_patterns(config)
        self.logger.debug(f"filtering search with {len(excludes)} excludes")
        result = [p for p in result if not p.match_any_glob(excludes)]
        self.logger.debug(f"found {len(result)} files (post-filter)")
        if not result:
            err = "jinja-plugin is included in this config, but found no .j2 files!"
            self.logger.critical(err)
        return result

    # def render_dot(files, output, in_place, open_after):
    #     """
    #     Render dot file (graphviz) -> PNG
    #     """
    #     assert files, "expected files would be provided"
    #     # if file:
    #     #     return render.j5(file, output=output, in_place=in_place)
    #     # elif files:
    #     # files = files.split(' ')
    #     LOGGER.debug(f"Running with many: {files}")
    #     file = files[0]
    #     files = files[1:]
    #     result = render.dot(file, output=output, in_place=in_place)
    #     output = result["output"]
    #     if open_after:
    #         LOGGER.debug(f"opening {output} with {DEFAULT_OPENER}")
    #         invoke(f"{DEFAULT_OPENER} {output}")
    #

    # def _dot(
    #     file: str,  in_place: bool = False,
    # ) -> typing.Dict:
    #     """renders .dot file to png"""
    # Using https://github.com/nickshine/dot
    # invoke(
    #
    # )
    # return dict(output=output)

    @cli.options.in_place
    @cli.options.output
    @cli.click.option('--img', default="nshine/dot")
    @cli.click.option('--output-mode')
    @cli.click.argument("file", nargs=1)
    def render(
        self,
        img: str = '??',
        file: str = '',
        in_place: bool = True,
        output_mode: str = "png",
        output: str = "",
    ):
        if in_place:
            assert not output
            output = os.path.splitext(file)[0] + ".png"
        cmd = f"cat {file} | docker run --rm --entrypoint dot -i {img} -T{output_mode} > {output}"
        return invoke(cmd, system=True).succeeded

    def plan(
        self,
        config=None,
    ) -> models.Plan:
        config = config or api.project.get_config()
        plan = super(self.__class__, self).plan(config)
        self.logger.debug("planning for rendering for .dot graph files..")
        cmd_t = "pynchon dot render {resource} --in-place --output-mode png"
        for resource in self.list(config):
            plan.append(
                models.Goal(
                    resource=resource,
                    command=cmd_t.format(resource=resource),
                    type='render',
                )
            )
        return plan

    # @common.kommand(
    #     name="files",
    #     parent=parent,
    #     options=[
    #         options.script,
    #         options.includes,
    #         click.option(
    #             "--script",
    #             default=None,
    #             help=("generates .dot files using script"),
    #         ),
    #         cli.options.inplace,
    #     ],
    #     arguments=[files_arg],
    # )
    # def gen_dot_files(files, in_place, includes, templates, script):
    #     """
    #     Render .dot files for this project.
    #     This creates the .dot files themselves; use `pynchon render dot` to convert those to an image.
    #     """
    #     assert os.path.exists(script), f"script file @`{script}` is missing!"
    #     invoke(f"python {script}")


#     assert files, "expected files would be provided"
#     # if file:
#     #     return render.j5(file, output=output, in_place=in_place)
#     # elif files:
#     # files = files.split(' ')
#     LOGGER.debug(f"Running with many: {files}")
#     file = files[0]
#     files = files[1:]
#     result = render.dot(file, output=output, in_place=in_place)
#     output = result["output"]
#     if open_after:
#         LOGGER.debug(f"opening {output} with {DEFAULT_OPENER}")
#         invoke(f"{DEFAULT_OPENER} {output}")
#
