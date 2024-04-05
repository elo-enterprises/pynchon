""" pynchon.plugins.plugins
"""

from fleks import tagging

from pynchon import abcs, cli, models
from pynchon.util.os import invoke

from pynchon.util import lme, typing  # noqa

LOGGER = lme.get_logger(__name__)


class PluginsMan(models.Provider):
    """Meta-plugin for managing plugins"""

    name = "plugins"
    cli_name = "plugins"

    @cli.click.argument("plugin_name")
    @cli.click.option("--json-schema", "-s", is_flag=True, default=False)
    @cli.click.option("--markdown", "-m", is_flag=True, default=False)
    def schema(
        self, plugin_name, markdown: bool = False, json_schema: bool = True
    ) -> str:
        """Retrieve config schema for given plugin"""
        if not any([markdown, json_schema]):
            json_schema = True
        LOGGER.critical(locals())
        plugin = self.siblings[plugin_name]
        cfg = plugin.config
        model = cfg.__class__
        if json_schema:
            schema_json = model.schema()
            from pynchon.util.text import dumps

            schema_json.update(title=plugin_name)
            print(dumps.json(schema_json, indent=2))
        elif markdown:
            from pynchon.api import render

            t = render.get_template(
                from_string="""\n{%for field in fields%}\n**{{plugin_name}}.{{field}}:** `{{fields[field]}}`{%endfor%}\n""",
                template_name="asdasdsa",
            )
            fields = {k: v for k, v in plugin.config.__class__.__fields__.items()}
            fields = {
                k: str(v).replace(f"name='{k}'", "").lstrip() for k, v in fields.items()
            }
            # import IPython; IPython.embed()
            print(t.render(plugin_name=plugin_name, fields=fields))
            # md = """{%for field in fields%}{{field}}{%endfor%}"""
        else:
            raise SystemExit(1)

    @cli.click.option("--name")
    @cli.click.option("--template-skeleton", "-t", is_flag=True, default=False)
    def new(self, name: str = None, template_skeleton: bool = False) -> None:
        """
        Create new plugin from template (for devs)
        """
        # FIXME: use pattern?
        plugins_d = abcs.Path(__file__).parents[0]
        template_plugin_f = plugins_d / "__template__.py"
        new_plugin_file = plugins_d / f"{name}.py"
        cmd = f"ls {new_plugin_file} || cp {template_plugin_f} {new_plugin_file} && git status"
        result = invoke(cmd, system=True)
        if template_skeleton:
            raise NotImplementedError()
        return result.succeeded

    @tagging.tags(click_aliases=["ls"])
    def list(self, **kwargs):
        """List all plugins"""
        return list(self.status()["plugins"].keys())

    @tagging.tags(click_aliases=["st", "stat"])
    def status(self) -> typing.Dict:
        """Returns details about all known plugins"""
        result = typing.OrderedDict()
        for name, p in self.siblings.items():
            result[name] = dict(priority=p.priority, key=p.get_config_key())
        return dict(plugins=result)
