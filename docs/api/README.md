## API for 'pynchon' package

---------------------------------------------------------------------------------------------------------------------------------------------------------------
### pynchon
* Overview:  [source code](/src/pynchon/__init__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (0 total)
-------------------------------------------------------------------------------
### pynchon.__main__
* Overview: (entrypoint) | [source code](/src/pynchon/__main__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
-------------------------------------------------------------------------------
### pynchon.testing
* Overview:  [source code](/src/pynchon/testing.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
-------------------------------------------------------------------------------
### pynchon._version
* Overview:  [source code](/src/pynchon/_version.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
-------------------------------------------------------------------------------
### pynchon.annotate
* Overview:  [source code](/src/pynchon/annotate.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Functions: (4 total)
  * [`pynchon.annotate.function`](/src/pynchon/annotate.py#L114-L157) with signature `(name, fxn) -> None`
  * [`pynchon.annotate.klass`](/src/pynchon/annotate.py#L13-L90) with signature `(name, kls) -> None`
    * with admonitions:  [🐉 Complex](/src/pynchon/annotate.py#L1 "score 16 / 7") 
  * [`pynchon.annotate.module`](/src/pynchon/annotate.py#L93-L99) with signature `(name, module, working_dir=None) -> None`
  * [`pynchon.annotate.should_skip`](/src/pynchon/annotate.py#L102-L111) with signature `(name: str)`
-------------------------------------------------------------------------------
### pynchon.tagging
* Overview:  [source code](/src/pynchon/tagging.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
-------------------------------------------------------------------------------
### pynchon.app
* Overview:  [source code](/src/pynchon/app.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (5 total)
  * [`pynchon.app.AppBase`](/src/pynchon/app.py#L29-L30)
    * with bases ([`__builtin__.object`](https://docs.python.org/3/library/functions.html#object),)
  * [`pynchon.app.AppConsole`](/src/pynchon/app.py#L33-L92)
    * with bases ([AppBase](#pynchonapp),)
    * with properties: (2 total)
      *  [`manager`](/src/pynchon/app.py#L37) -> inspect._empty
      *  [`status_bar`](/src/pynchon/app.py#L37) -> inspect._empty
  * [`pynchon.app.AppExitHooks`](/src/pynchon/app.py#L95-L142)
    * with bases ([AppBase](#pynchonapp),)
  * [`pynchon.app.AppEvents`](/src/pynchon/app.py#L145-L148)
    * with bases ([AppBase](#pynchonapp),)
  * [`pynchon.app.App`](/src/pynchon/app.py#L151-L158)
    * with bases ([AppConsole](#pynchonapp),[AppEvents](#pynchonapp),[AppExitHooks](#pynchonapp),)
    * with properties: (2 total)
      *  [`manager`](/src/pynchon/app.py#L37) -> inspect._empty
      *  [`status_bar`](/src/pynchon/app.py#L37) -> inspect._empty
-------------------------------------------------------------------------------
### pynchon.constants
* Overview:  [source code](/src/pynchon/constants.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
-------------------------------------------------------------------------------
### pynchon.core
* Overview:  [source code](/src/pynchon/core.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (1 total)
  * [`pynchon.core.Config`](/src/pynchon/core.py#L11-L91)
    * with bases ([Config](#pynchonabcsconfig),)
    * with properties: (3 total)
      *  [`plugins`](/src/pynchon/core.py#L31) -> inspect._empty
      *  [`root`](/src/pynchon/core.py#L56) -> str
      *  [`working_dir`](/src/pynchon/core.py#L86) -> inspect._empty
-------------------------------------------------------------------------------
### pynchon.events
* Overview:  [source code](/src/pynchon/events.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Functions: (6 total)
  * [`pynchon.events._lifecycle`](/src/pynchon/events.py#L53-L59) with signature ``
  * [`pynchon.events.lifecycle_applying`](/src/pynchon/events.py#L29-L34) with signature `(sender, applying=None, **kwargs)`
  * [`pynchon.events.lifecycle_config`](/src/pynchon/events.py#L21-L26) with signature `(sender, config)`
  * [`pynchon.events.lifecycle_msg`](/src/pynchon/events.py#L46-L50) with signature `(sender, msg=None, **kwargs)`
  * [`pynchon.events.lifecycle_plugin`](/src/pynchon/events.py#L13-L18) with signature `(sender, plugin)`
  * [`pynchon.events.lifecycle_stage`](/src/pynchon/events.py#L37-L43) with signature `(sender, stage=None, **kwargs)`
-------------------------------------------------------------------------------
### pynchon.fleks
* Overview:  [source code](/src/pynchon/fleks/__init__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (0 total)
-------------------------------------------------------------------------------
### pynchon.fleks.plugin
* Overview:  [source code](/src/pynchon/fleks/plugin.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (1 total)
  * [`pynchon.fleks.plugin.Plugin`](/src/pynchon/fleks/plugin.py#L12-L33)
    * with bases ([`__builtin__.object`](https://docs.python.org/3/library/functions.html#object),)
    * with properties: (1 total)
      *  [`logger`](/src/pynchon/fleks/plugin.py#L37) -> inspect._empty
-------------------------------------------------------------------------------
### pynchon.fleks.typing
* Overview:  [source code](/src/pynchon/fleks/typing.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Functions: (1 total)
  * [`pynchon.fleks.typing.validate`](/src/pynchon/fleks/typing.py#L28-L29)
    * with signature `(func: Union[ForwardRef('AnyCallableT'), NoneType] = None, *, config: 'ConfigType' = None) -> Any`
-------------------------------------------------------------------------------
### pynchon.fleks.meta
* Overview:  [source code](/src/pynchon/fleks/meta/__init__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (0 total)
-------------------------------------------------------------------------------
### pynchon.fleks.meta.namespace
* Overview:  [source code](/src/pynchon/fleks/meta/namespace.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (1 total)
  * [`pynchon.fleks.meta.namespace.Namespace`](/src/pynchon/fleks/meta/namespace.py#L7-L35)
    * with bases ([`__builtin__.object`](https://docs.python.org/3/library/functions.html#object),)
* Functions: (1 total)
  * [`pynchon.fleks.meta.namespace.namespace`](/src/pynchon/fleks/meta/namespace.py#L38-L46) with signature `(name, bases, namespace)`
-------------------------------------------------------------------------------
### pynchon.fleks.meta.oop
* Overview:  [source code](/src/pynchon/fleks/meta/oop.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (2 total)
  * [`pynchon.fleks.meta.oop.ClassMalformed`](/src/pynchon/fleks/meta/oop.py#L10-L11)
    * with bases ([`__builtin__.TypeError`](https://docs.python.org/3/library/functions.html#TypeError),)
  * [`pynchon.fleks.meta.oop.Meta`](/src/pynchon/fleks/meta/oop.py#L14-L176)
    * with bases ([`__builtin__.type`](https://docs.python.org/3/library/functions.html#type),)
    * with admonitions:  [🐉 Complex](/src/pynchon/fleks/meta/oop.py#L42 "score 9 / 7") 
-------------------------------------------------------------------------------
### pynchon.shimport
* Overview:  [source code](/src/pynchon/shimport/__init__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (0 total)
-------------------------------------------------------------------------------
### pynchon.shimport.util
* Overview:  [source code](/src/pynchon/shimport/util.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Functions: (1 total)
  /src/pynchon/shimport/util.py#L6-L26 "")
  * [`pynchon.shimport.util.get_namespace`](/src/pynchon/shimport/util.py#L6-L26) with signature `(name)`
    * with admonitions:  [ 🚩has FIXMEs ](/src/pynchon/shimport/util.py#L7 "on lines [7]") 
-------------------------------------------------------------------------------
### pynchon.shimport.module
* Overview:  [source code](/src/pynchon/shimport/module.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (1 total)
  * [`pynchon.shimport.module.ModuleBuilder`](/src/pynchon/shimport/module.py#L10-L38)
    * with bases ([ModulesWrapper](#pynchonshimportmodels),)
    * with properties: (3 total)
      *  [`module`](/src/pynchon/shimport/module.py#L101) -> inspect._empty
      *  [`parent`](/src/pynchon/shimport/module.py#L116) -> inspect._empty
      *  [`parent_folder`](/src/pynchon/shimport/module.py#L111) -> inspect._empty
* Functions: (3 total)
  * [`pynchon.shimport.module.lazy`](/src/pynchon/shimport/module.py#L76-L81) with signature `(module_name: str) -> pynchon.shimport.models.LazyModule`
  * [`pynchon.shimport.module.module_builder`](/src/pynchon/shimport/module.py#L41-L56)
    * with signature `(name: str, return_objects=False, assign_objects: bool = True, sort_objects: Dict = {}, **kwargs) -> None`
  * [`pynchon.shimport.module.wrap`](/src/pynchon/shimport/module.py#L63-L70) with signature `(name, **kwargs)`
-------------------------------------------------------------------------------
### pynchon.shimport.models
* Overview:  [source code](/src/pynchon/shimport/models.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (3 total)
  * [`pynchon.shimport.models.Base`](/src/pynchon/shimport/models.py#L19-L28)
    * with bases ([`__builtin__.object`](https://docs.python.org/3/library/functions.html#object),)
  * [`pynchon.shimport.models.ModulesWrapper`](/src/pynchon/shimport/models.py#L31-L366)
    * with bases ([Base](#pynchonshimportmodels),)
    * with admonitions:  [🐉 Complex](/src/pynchon/shimport/models.py#L302 "score 8 / 7") 
    * with properties: (3 total)
      *  [`module`](/src/pynchon/shimport/models.py#L101) -> inspect._empty
      *  [`parent`](/src/pynchon/shimport/models.py#L116) -> inspect._empty
      *  [`parent_folder`](/src/pynchon/shimport/models.py#L111) -> inspect._empty
  * [`pynchon.shimport.models.LazyModule`](/src/pynchon/shimport/models.py#L369-L400)
    * with bases ([`__builtin__.object`](https://docs.python.org/3/library/functions.html#object),)
-------------------------------------------------------------------------------
### pynchon.shimport.abcs
* Overview:  [source code](/src/pynchon/shimport/abcs.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (1 total)
  * [`pynchon.shimport.abcs.FilterResult`](/src/pynchon/shimport/abcs.py#L10-L32)
    * with bases ([`__builtin__.list`](https://docs.python.org/3/library/functions.html#list),[Generic](#typing),)
-------------------------------------------------------------------------------
### pynchon.shimport.types
* Overview:  [source code](/src/pynchon/shimport/types.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
-------------------------------------------------------------------------------
### pynchon.shimport.registry
* Overview:  [source code](/src/pynchon/shimport/registry.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
-------------------------------------------------------------------------------
### pynchon.shimport.hooks
* Overview:  [source code](/src/pynchon/shimport/hooks.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
-------------------------------------------------------------------------------
### pynchon.shimport.importing
* Overview:  [source code](/src/pynchon/shimport/importing.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
-------------------------------------------------------------------------------
### pynchon.bin
* Overview:  [source code](/src/pynchon/bin/__init__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (0 total)
-------------------------------------------------------------------------------
### pynchon.bin.entry
* Overview:  [source code](/src/pynchon/bin/entry.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (1 total)
  * [`pynchon.bin.entry.RootGroup`](/src/pynchon/bin/entry.py#L17-L85)
    * with bases ([Group](#clickcore),)
    * with admonitions:  [🐉 Complex](/src/pynchon/bin/entry.py#L4 "score 13 / 7") 
* Functions: (1 total)
  * [`pynchon.bin.entry.entry`](/src/pynchon/bin/entry.py#L88-L98) with signature `(*args: Any, **kwargs: Any) -> Any`
-------------------------------------------------------------------------------
### pynchon.bin.parse
* Overview:  [source code](/src/pynchon/bin/parse.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
-------------------------------------------------------------------------------
### pynchon.bin.options
* Overview:  [source code](/src/pynchon/bin/options.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
-------------------------------------------------------------------------------
### pynchon.bin.render
* Overview:  [source code](/src/pynchon/bin/render.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
-------------------------------------------------------------------------------
### pynchon.bin.cli
* Overview:  [source code](/src/pynchon/bin/cli.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
-------------------------------------------------------------------------------
### pynchon.bin.dot
* Overview:  [source code](/src/pynchon/bin/dot.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
-------------------------------------------------------------------------------
### pynchon.bin.groups
* Overview:  [source code](/src/pynchon/bin/groups.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
-------------------------------------------------------------------------------
### pynchon.plugins
* Overview:  [source code](/src/pynchon/plugins/__init__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (0 total)
-------------------------------------------------------------------------------
### pynchon.plugins.json
* Overview:  [source code](/src/pynchon/plugins/json.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (1 total)
  * [`pynchon.plugins.json.Json`](/src/pynchon/plugins/json.py#L50-L67)
    * with bases ([ToolPlugin](#pynchonmodelsplugin_types),)
    * with properties: (4 total)
      *  [`config`](/src/pynchon/plugins/json.py#L92) -> inspect._empty
      *  [`logger`](/src/pynchon/plugins/json.py#L37) -> inspect._empty
      *  [`plugin_config`](/src/pynchon/plugins/json.py#L64) -> inspect._empty
      *  [`siblings`](/src/pynchon/plugins/json.py#L69) -> inspect._empty
-------------------------------------------------------------------------------
### pynchon.plugins.src
* Overview:  [source code](/src/pynchon/plugins/src.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (1 total)
  * [`pynchon.plugins.src.SourceMan`](/src/pynchon/plugins/src.py#L29-L148)
    * with bases ([Manager](#pynchonmodelsplanner),)
    * with properties: (5 total)
      *  [`changes`](/src/pynchon/plugins/src.py#L27) -> inspect._empty
      *  [`config`](/src/pynchon/plugins/src.py#L92) -> inspect._empty
      *  [`logger`](/src/pynchon/plugins/src.py#L37) -> inspect._empty
      *  [`plugin_config`](/src/pynchon/plugins/src.py#L64) -> inspect._empty
      *  [`siblings`](/src/pynchon/plugins/src.py#L69) -> inspect._empty
-------------------------------------------------------------------------------
### pynchon.plugins.parse
* Overview:  [source code](/src/pynchon/plugins/parse.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
-------------------------------------------------------------------------------
### pynchon.plugins.cookie_cutter
* Overview:  [source code](/src/pynchon/plugins/cookie_cutter.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (1 total)
  * [`pynchon.plugins.cookie_cutter.CookierCutter`](/src/pynchon/plugins/cookie_cutter.py#L22-L36)
    * with bases ([ToolPlugin](#pynchonmodelsplugin_types),)
    * with properties: (4 total)
      *  [`config`](/src/pynchon/plugins/cookie_cutter.py#L92) -> inspect._empty
      *  [`logger`](/src/pynchon/plugins/cookie_cutter.py#L37) -> inspect._empty
      *  [`plugin_config`](/src/pynchon/plugins/cookie_cutter.py#L64) -> inspect._empty
      *  [`siblings`](/src/pynchon/plugins/cookie_cutter.py#L69) -> inspect._empty
-------------------------------------------------------------------------------
### pynchon.plugins.tox
* Overview:  [source code](/src/pynchon/plugins/tox.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (1 total)
  * [`pynchon.plugins.tox.PluginTemplate`](/src/pynchon/plugins/tox.py#L9-L17)
    * with bases ([Provider](#pynchonmodelsplugin_types),)
    * with properties: (4 total)
      *  [`config`](/src/pynchon/plugins/tox.py#L92) -> inspect._empty
      *  [`logger`](/src/pynchon/plugins/tox.py#L37) -> inspect._empty
      *  [`plugin_config`](/src/pynchon/plugins/tox.py#L64) -> inspect._empty
      *  [`siblings`](/src/pynchon/plugins/tox.py#L69) -> inspect._empty
-------------------------------------------------------------------------------
### pynchon.plugins.cicd
* Overview:  [source code](/src/pynchon/plugins/cicd.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (1 total)
  * [`pynchon.plugins.cicd.CiCd`](/src/pynchon/plugins/cicd.py#L15-L40)
    * with bases ([Provider](#pynchonmodelsplugin_types),)
    * with properties: (4 total)
      *  [`config`](/src/pynchon/plugins/cicd.py#L92) -> inspect._empty
      *  [`logger`](/src/pynchon/plugins/cicd.py#L37) -> inspect._empty
      *  [`plugin_config`](/src/pynchon/plugins/cicd.py#L64) -> inspect._empty
      *  [`siblings`](/src/pynchon/plugins/cicd.py#L69) -> inspect._empty
-------------------------------------------------------------------------------
### pynchon.plugins.util
* Overview:  [source code](/src/pynchon/plugins/util.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (3 total)
  * [`pynchon.plugins.util.PluginNotInitialized`](/src/pynchon/plugins/util.py#L11-L12)
    * with bases ([`__builtin__.RuntimeError`](https://docs.python.org/3/library/functions.html#RuntimeError),)
  * [`pynchon.plugins.util.PluginNotRegistered`](/src/pynchon/plugins/util.py#L15-L16)
    * with bases ([`__builtin__.RuntimeError`](https://docs.python.org/3/library/functions.html#RuntimeError),)
  * [`pynchon.plugins.util.PluginNotConfigured`](/src/pynchon/plugins/util.py#L19-L20)
    * with bases ([`__builtin__.RuntimeError`](https://docs.python.org/3/library/functions.html#RuntimeError),)
* Functions: (3 total)
  * [`pynchon.plugins.util.get_plugin_class`](/src/pynchon/plugins/util.py#L33-L39) with signature `(plugin_name: str) -> Type`
  * [`pynchon.plugins.util.get_plugin_meta`](/src/pynchon/plugins/util.py#L23-L30) with signature `(plugin_name: str) -> Dict`
  * [`pynchon.plugins.util.get_plugin_obj`](/src/pynchon/plugins/util.py#L45-L53) with signature `(plugin_name: str) -> object`
-------------------------------------------------------------------------------
### pynchon.plugins.git
* Overview:  [source code](/src/pynchon/plugins/git.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (2 total)
  * [`pynchon.plugins.git.GitConfig`](/src/pynchon/plugins/git.py#L11-L84)
    * with bases ([Config](#pynchonabcsconfig),)
    * with properties: (9 total)
      *  [`branch_name`](/src/pynchon/plugins/git.py#L74) -> inspect._empty
      *  [`default_remote_branch`](/src/pynchon/plugins/git.py#L37) -> typing.Union[str, NoneType]
      *  [`github_org`](/src/pynchon/plugins/git.py#L48) -> inspect._empty
      *  [`hash`](/src/pynchon/plugins/git.py#L80) -> str
      *  [`is_github`](/src/pynchon/plugins/git.py#L42) -> inspect._empty
      *  [`repo`](/src/pynchon/plugins/git.py#L37) -> typing.Union[str, NoneType]
      *  [`repo_name`](/src/pynchon/plugins/git.py#L56) -> typing.Union[str, NoneType]
      *  [`repo_url`](/src/pynchon/plugins/git.py#L68) -> inspect._empty
      *  [`root`](/src/pynchon/plugins/git.py#L28) -> typing.Union[str, NoneType]
  * [`pynchon.plugins.git.Git`](/src/pynchon/plugins/git.py#L87-L112)
    * with bases ([Provider](#pynchonmodelsplugin_types),)
    * with properties: (5 total)
      *  [`config`](/src/pynchon/plugins/git.py#L92) -> inspect._empty
      *  [`logger`](/src/pynchon/plugins/git.py#L37) -> inspect._empty
      *  [`modified`](/src/pynchon/plugins/git.py#L96) -> typing.List[pynchon.abcs.path.Path]
      *  [`plugin_config`](/src/pynchon/plugins/git.py#L64) -> inspect._empty
      *  [`siblings`](/src/pynchon/plugins/git.py#L69) -> inspect._empty
-------------------------------------------------------------------------------
### pynchon.plugins.docs
* Overview:  [source code](/src/pynchon/plugins/docs.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (1 total)
  * [`pynchon.plugins.docs.DocsMan`](/src/pynchon/plugins/docs.py#L15-L126)
    * with bases ([Planner](#pynchonmodelsplanner),)
    * with properties: (5 total)
      *  [`changes`](/src/pynchon/plugins/docs.py#L27) -> inspect._empty
      *  [`config`](/src/pynchon/plugins/docs.py#L92) -> inspect._empty
      *  [`logger`](/src/pynchon/plugins/docs.py#L37) -> inspect._empty
      *  [`plugin_config`](/src/pynchon/plugins/docs.py#L64) -> inspect._empty
      *  [`siblings`](/src/pynchon/plugins/docs.py#L69) -> inspect._empty
-------------------------------------------------------------------------------
### pynchon.plugins.jinja
* Overview:  [source code](/src/pynchon/plugins/jinja.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (1 total)
  * [`pynchon.plugins.jinja.Jinja`](/src/pynchon/plugins/jinja.py#L12-L145)
    * with bases ([Planner](#pynchonmodelsplanner),)
    * with properties: (5 total)
      *  [`changes`](/src/pynchon/plugins/jinja.py#L27) -> inspect._empty
      *  [`config`](/src/pynchon/plugins/jinja.py#L92) -> inspect._empty
      *  [`logger`](/src/pynchon/plugins/jinja.py#L37) -> inspect._empty
      *  [`plugin_config`](/src/pynchon/plugins/jinja.py#L64) -> inspect._empty
      *  [`siblings`](/src/pynchon/plugins/jinja.py#L69) -> inspect._empty
-------------------------------------------------------------------------------
### pynchon.plugins.rtd
* Overview:  [source code](/src/pynchon/plugins/rtd.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
-------------------------------------------------------------------------------
### pynchon.plugins.pandoc
* Overview:  [source code](/src/pynchon/plugins/pandoc.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (1 total)
  * [`pynchon.plugins.pandoc.PluginTemplate`](/src/pynchon/plugins/pandoc.py#L9-L17)
    * with bases ([Provider](#pynchonmodelsplugin_types),)
    * with properties: (4 total)
      *  [`config`](/src/pynchon/plugins/pandoc.py#L92) -> inspect._empty
      *  [`logger`](/src/pynchon/plugins/pandoc.py#L37) -> inspect._empty
      *  [`plugin_config`](/src/pynchon/plugins/pandoc.py#L64) -> inspect._empty
      *  [`siblings`](/src/pynchon/plugins/pandoc.py#L69) -> inspect._empty
-------------------------------------------------------------------------------
### pynchon.plugins.griffe
* Overview:  [source code](/src/pynchon/plugins/griffe.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (1 total)
  * [`pynchon.plugins.griffe.Griffe`](/src/pynchon/plugins/griffe.py#L9-L18)
    * with bases ([ToolPlugin](#pynchonmodelsplugin_types),)
    * with properties: (4 total)
      *  [`config`](/src/pynchon/plugins/griffe.py#L92) -> inspect._empty
      *  [`logger`](/src/pynchon/plugins/griffe.py#L37) -> inspect._empty
      *  [`plugin_config`](/src/pynchon/plugins/griffe.py#L64) -> inspect._empty
      *  [`siblings`](/src/pynchon/plugins/griffe.py#L69) -> inspect._empty
-------------------------------------------------------------------------------
### pynchon.plugins.github
* Overview:  [source code](/src/pynchon/plugins/github.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (1 total)
  * [`pynchon.plugins.github.GitHub`](/src/pynchon/plugins/github.py#L13-L56)
    * with bases ([ToolPlugin](#pynchonmodelsplugin_types),)
    * with properties: (4 total)
      *  [`config`](/src/pynchon/plugins/github.py#L92) -> inspect._empty
      *  [`logger`](/src/pynchon/plugins/github.py#L37) -> inspect._empty
      *  [`plugin_config`](/src/pynchon/plugins/github.py#L64) -> inspect._empty
      *  [`siblings`](/src/pynchon/plugins/github.py#L69) -> inspect._empty
-------------------------------------------------------------------------------
### pynchon.plugins.makefile
* Overview:  [source code](/src/pynchon/plugins/makefile/__init__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
-------------------------------------------------------------------------------
### pynchon.plugins.core
* Overview:  [source code](/src/pynchon/plugins/core.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (1 total)
  * [`pynchon.plugins.core.Core`](/src/pynchon/plugins/core.py#L11-L139)
    * with bases ([Planner](#pynchonmodelsplanner),)
    * with properties: (5 total)
      *  [`changes`](/src/pynchon/plugins/core.py#L27) -> inspect._empty
      *  [`config`](/src/pynchon/plugins/core.py#L92) -> inspect._empty
      *  [`logger`](/src/pynchon/plugins/core.py#L37) -> inspect._empty
      *  [`plugin_config`](/src/pynchon/plugins/core.py#L64) -> inspect._empty
      *  [`siblings`](/src/pynchon/plugins/core.py#L69) -> inspect._empty
-------------------------------------------------------------------------------
### pynchon.plugins.fixme
* Overview:  [source code](/src/pynchon/plugins/fixme.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (2 total)
  * [`pynchon.plugins.fixme.FixMeConfig`](/src/pynchon/plugins/fixme.py#L14-L15)
    * with bases ([Config](#pynchonabcsconfig),)
  * [`pynchon.plugins.fixme.FixMe`](/src/pynchon/plugins/fixme.py#L18-L104)
    * with bases ([Planner](#pynchonmodelsplanner),)
    * with properties: (5 total)
      *  [`changes`](/src/pynchon/plugins/fixme.py#L27) -> inspect._empty
      *  [`config`](/src/pynchon/plugins/fixme.py#L92) -> inspect._empty
      *  [`logger`](/src/pynchon/plugins/fixme.py#L37) -> inspect._empty
      *  [`plugin_config`](/src/pynchon/plugins/fixme.py#L64) -> inspect._empty
      *  [`siblings`](/src/pynchon/plugins/fixme.py#L69) -> inspect._empty
-------------------------------------------------------------------------------
### pynchon.plugins.release
* Overview:  [source code](/src/pynchon/plugins/release.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
-------------------------------------------------------------------------------
### pynchon.plugins.render
* Overview:  [source code](/src/pynchon/plugins/render.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (1 total)
  * [`pynchon.plugins.render.Renderers`](/src/pynchon/plugins/render.py#L10-L17)
    * with bases ([NameSpace](#pynchonmodelsplugin_types),)
    * with properties: (4 total)
      *  [`config`](/src/pynchon/plugins/render.py#L92) -> inspect._empty
      *  [`logger`](/src/pynchon/plugins/render.py#L37) -> inspect._empty
      *  [`plugin_config`](/src/pynchon/plugins/render.py#L64) -> inspect._empty
      *  [`siblings`](/src/pynchon/plugins/render.py#L69) -> inspect._empty
-------------------------------------------------------------------------------
### pynchon.plugins.gen
* Overview:  [source code](/src/pynchon/plugins/gen.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (1 total)
  * [`pynchon.plugins.gen.Generators`](/src/pynchon/plugins/gen.py#L9-L17)
    * with bases ([NameSpace](#pynchonmodelsplugin_types),)
    * with properties: (4 total)
      *  [`config`](/src/pynchon/plugins/gen.py#L92) -> inspect._empty
      *  [`logger`](/src/pynchon/plugins/gen.py#L37) -> inspect._empty
      *  [`plugin_config`](/src/pynchon/plugins/gen.py#L64) -> inspect._empty
      *  [`siblings`](/src/pynchon/plugins/gen.py#L69) -> inspect._empty
-------------------------------------------------------------------------------
### pynchon.plugins.plugins
* Overview:  [source code](/src/pynchon/plugins/plugins.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (1 total)
  * [`pynchon.plugins.plugins.PluginsMan`](/src/pynchon/plugins/plugins.py#L11-L41)
    * with bases ([Manager](#pynchonmodelsplanner),)
    * with properties: (5 total)
      *  [`changes`](/src/pynchon/plugins/plugins.py#L27) -> inspect._empty
      *  [`config`](/src/pynchon/plugins/plugins.py#L92) -> inspect._empty
      *  [`logger`](/src/pynchon/plugins/plugins.py#L37) -> inspect._empty
      *  [`plugin_config`](/src/pynchon/plugins/plugins.py#L64) -> inspect._empty
      *  [`siblings`](/src/pynchon/plugins/plugins.py#L69) -> inspect._empty
-------------------------------------------------------------------------------
### pynchon.plugins.api
* Overview:  [source code](/src/pynchon/plugins/api.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
-------------------------------------------------------------------------------
### pynchon.plugins.__template__
* Overview:  [source code](/src/pynchon/plugins/__template__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (1 total)
  * [`pynchon.plugins.__template__.PluginTemplate`](/src/pynchon/plugins/__template__.py#L9-L17)
    * with bases ([Provider](#pynchonmodelsplugin_types),)
    * with properties: (4 total)
      *  [`config`](/src/pynchon/plugins/__template__.py#L92) -> inspect._empty
      *  [`logger`](/src/pynchon/plugins/__template__.py#L37) -> inspect._empty
      *  [`plugin_config`](/src/pynchon/plugins/__template__.py#L64) -> inspect._empty
      *  [`siblings`](/src/pynchon/plugins/__template__.py#L69) -> inspect._empty
-------------------------------------------------------------------------------
### pynchon.plugins.load
* Overview:  [source code](/src/pynchon/plugins/load.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
-------------------------------------------------------------------------------
### pynchon.plugins.dot
* Overview:  [source code](/src/pynchon/plugins/dot.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (1 total)
  * [`pynchon.plugins.dot.Dot`](/src/pynchon/plugins/dot.py#L14-L126)
    * with bases ([Planner](#pynchonmodelsplanner),)
    * with properties: (5 total)
      *  [`changes`](/src/pynchon/plugins/dot.py#L27) -> inspect._empty
      *  [`config`](/src/pynchon/plugins/dot.py#L92) -> inspect._empty
      *  [`logger`](/src/pynchon/plugins/dot.py#L37) -> inspect._empty
      *  [`plugin_config`](/src/pynchon/plugins/dot.py#L64) -> inspect._empty
      *  [`siblings`](/src/pynchon/plugins/dot.py#L69) -> inspect._empty
-------------------------------------------------------------------------------
### pynchon.plugins.project
* Overview:  [source code](/src/pynchon/plugins/project.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (2 total)
  * [`pynchon.plugins.project.ProjectConfig`](/src/pynchon/plugins/project.py#L11-L46)
    * with bases ([Config](#pynchonabcsconfig),)
    * with properties: (3 total)
      *  [`name`](/src/pynchon/plugins/project.py#L18) -> typing.Union[str, NoneType]
      *  [`root`](/src/pynchon/plugins/project.py#L28) -> str
      *  [`subproject`](/src/pynchon/plugins/project.py#L34) -> typing.Dict
  * [`pynchon.plugins.project.Project`](/src/pynchon/plugins/project.py#L49-L54)
    * with bases ([Manager](#pynchonmodelsplanner),)
    * with properties: (5 total)
      *  [`changes`](/src/pynchon/plugins/project.py#L27) -> inspect._empty
      *  [`config`](/src/pynchon/plugins/project.py#L92) -> inspect._empty
      *  [`logger`](/src/pynchon/plugins/project.py#L37) -> inspect._empty
      *  [`plugin_config`](/src/pynchon/plugins/project.py#L64) -> inspect._empty
      *  [`siblings`](/src/pynchon/plugins/project.py#L69) -> inspect._empty
-------------------------------------------------------------------------------
### pynchon.plugins.globals
* Overview:  [source code](/src/pynchon/plugins/globals.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (2 total)
  * [`pynchon.plugins.globals.GlobalsConfig`](/src/pynchon/plugins/globals.py#L6-L10)
    * with bases ([Config](#pynchonabcsconfig),)
  * [`pynchon.plugins.globals.Globals`](/src/pynchon/plugins/globals.py#L13-L18)
    * with bases ([Provider](#pynchonmodelsplugin_types),)
    * with properties: (4 total)
      *  [`config`](/src/pynchon/plugins/globals.py#L92) -> inspect._empty
      *  [`logger`](/src/pynchon/plugins/globals.py#L37) -> inspect._empty
      *  [`plugin_config`](/src/pynchon/plugins/globals.py#L64) -> inspect._empty
      *  [`siblings`](/src/pynchon/plugins/globals.py#L69) -> inspect._empty
-------------------------------------------------------------------------------
### pynchon.plugins.tests
* Overview:  [source code](/src/pynchon/plugins/tests.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (1 total)
  * [`pynchon.plugins.tests.Tests`](/src/pynchon/plugins/tests.py#L9-L16)
    * with bases ([Planner](#pynchonmodelsplanner),)
    * with properties: (5 total)
      *  [`changes`](/src/pynchon/plugins/tests.py#L27) -> inspect._empty
      *  [`config`](/src/pynchon/plugins/tests.py#L92) -> inspect._empty
      *  [`logger`](/src/pynchon/plugins/tests.py#L37) -> inspect._empty
      *  [`plugin_config`](/src/pynchon/plugins/tests.py#L64) -> inspect._empty
      *  [`siblings`](/src/pynchon/plugins/tests.py#L69) -> inspect._empty
-------------------------------------------------------------------------------
### pynchon.plugins.ast
* Overview:  [source code](/src/pynchon/plugins/ast.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
-------------------------------------------------------------------------------
### pynchon.plugins.hooks
* Overview:  [source code](/src/pynchon/plugins/hooks.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
-------------------------------------------------------------------------------
### pynchon.plugins.terraform
* Overview:  [source code](/src/pynchon/plugins/terraform.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (1 total)
  * [`pynchon.plugins.terraform.PluginTemplate`](/src/pynchon/plugins/terraform.py#L9-L17)
    * with bases ([Provider](#pynchonmodelsplugin_types),)
    * with properties: (4 total)
      *  [`config`](/src/pynchon/plugins/terraform.py#L92) -> inspect._empty
      *  [`logger`](/src/pynchon/plugins/terraform.py#L37) -> inspect._empty
      *  [`plugin_config`](/src/pynchon/plugins/terraform.py#L64) -> inspect._empty
      *  [`siblings`](/src/pynchon/plugins/terraform.py#L69) -> inspect._empty
-------------------------------------------------------------------------------
### pynchon.plugins.scaffolding
* Overview:  [source code](/src/pynchon/plugins/scaffolding/__init__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (1 total)
  * [`pynchon.plugins.scaffolding.Scaffolding`](/src/pynchon/plugins/scaffolding/__init__.py#L13-L110)
    * with bases ([ShyPlanner](#pynchonmodelsplanner),)
    * with properties: (7 total)
      *  [`changes`](/src/pynchon/plugins/scaffolding/__init__.py#L27) -> inspect._empty
      *  [`config`](/src/pynchon/plugins/scaffolding/__init__.py#L92) -> inspect._empty
      *  [`logger`](/src/pynchon/plugins/scaffolding/__init__.py#L37) -> inspect._empty
      *  [`matches`](/src/pynchon/plugins/scaffolding/__init__.py#L42) -> inspect._empty
      *  [`plugin_config`](/src/pynchon/plugins/scaffolding/__init__.py#L64) -> inspect._empty
      *  [`scaffolds`](/src/pynchon/plugins/scaffolding/__init__.py#L57) -> inspect._empty
      *  [`siblings`](/src/pynchon/plugins/scaffolding/__init__.py#L69) -> inspect._empty
* Classes: (1 total)
  * [`pynchon.plugins.scaffolding.Scaffolding`](/src/pynchon/plugins/scaffolding/__init__.py#L13-L110)
    * with bases ([ShyPlanner](#pynchonmodelsplanner),)
    * with properties: (7 total)
      *  [`changes`](/src/pynchon/plugins/scaffolding/__init__.py#L27) -> inspect._empty
      *  [`config`](/src/pynchon/plugins/scaffolding/__init__.py#L92) -> inspect._empty
      *  [`logger`](/src/pynchon/plugins/scaffolding/__init__.py#L37) -> inspect._empty
      *  [`matches`](/src/pynchon/plugins/scaffolding/__init__.py#L42) -> inspect._empty
      *  [`plugin_config`](/src/pynchon/plugins/scaffolding/__init__.py#L64) -> inspect._empty
      *  [`scaffolds`](/src/pynchon/plugins/scaffolding/__init__.py#L57) -> inspect._empty
      *  [`siblings`](/src/pynchon/plugins/scaffolding/__init__.py#L69) -> inspect._empty
-------------------------------------------------------------------------------
### pynchon.plugins.scaffolding.config
* Overview:  [source code](/src/pynchon/plugins/scaffolding/config.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (2 total)
  * [`pynchon.plugins.scaffolding.config.ScaffoldingItem`](/src/pynchon/plugins/scaffolding/config.py#L11-L35)
    * with bases ([AttrDict](#pynchonabcsattrdict),)
    * with properties: (1 total)
      *  [`exists`](/src/pynchon/plugins/scaffolding/config.py#L14) -> bool
  * [`pynchon.plugins.scaffolding.config.ScaffoldingConfig`](/src/pynchon/plugins/scaffolding/config.py#L38-L41)
    * with bases ([Config](#pynchonabcsconfig),)
-------------------------------------------------------------------------------
### pynchon.plugins.doctor
* Overview:  [source code](/src/pynchon/plugins/doctor/__init__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
-------------------------------------------------------------------------------
### pynchon.plugins.python
* Overview:  [source code](/src/pynchon/plugins/python/__init__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (0 total)
-------------------------------------------------------------------------------
### pynchon.plugins.python.pypi
* Overview:  [source code](/src/pynchon/plugins/python/pypi.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (2 total)
  * [`pynchon.plugins.python.pypi.PyPiConfig`](/src/pynchon/plugins/python/pypi.py#L9-L15)
    * with bases ([Config](#pynchonabcsconfig),)
  * [`pynchon.plugins.python.pypi.PyPI`](/src/pynchon/plugins/python/pypi.py#L18-L22)
    * with bases ([Provider](#pynchonmodelsplugin_types),)
    * with properties: (4 total)
      *  [`config`](/src/pynchon/plugins/python/pypi.py#L92) -> inspect._empty
      *  [`logger`](/src/pynchon/plugins/python/pypi.py#L37) -> inspect._empty
      *  [`plugin_config`](/src/pynchon/plugins/python/pypi.py#L64) -> inspect._empty
      *  [`siblings`](/src/pynchon/plugins/python/pypi.py#L69) -> inspect._empty
-------------------------------------------------------------------------------
### pynchon.plugins.python.models
* Overview:  [source code](/src/pynchon/plugins/python/models.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
-------------------------------------------------------------------------------
### pynchon.plugins.python.config
* Overview:  [source code](/src/pynchon/plugins/python/config.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
-------------------------------------------------------------------------------
### pynchon.plugins.python.cli
* Overview:  [source code](/src/pynchon/plugins/python/cli.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (2 total)
  * [`pynchon.plugins.python.cli.PythonCliConfig`](/src/pynchon/plugins/python/cli.py#L14-L55)
    * with bases ([Config](#pynchonabcsconfig),)
    * with properties: (2 total)
      *  [`entrypoints`](/src/pynchon/plugins/python/cli.py#L32) -> dict
      *  [`src_root`](/src/pynchon/plugins/python/cli.py#L20) -> inspect._empty
  * [`pynchon.plugins.python.cli.PythonCLI`](/src/pynchon/plugins/python/cli.py#L58-L248)
    * with bases ([ShyPlanner](#pynchonmodelsplanner),)
    * with properties: (5 total)
      *  [`changes`](/src/pynchon/plugins/python/cli.py#L27) -> inspect._empty
      *  [`config`](/src/pynchon/plugins/python/cli.py#L92) -> inspect._empty
      *  [`logger`](/src/pynchon/plugins/python/cli.py#L37) -> inspect._empty
      *  [`plugin_config`](/src/pynchon/plugins/python/cli.py#L64) -> inspect._empty
      *  [`siblings`](/src/pynchon/plugins/python/cli.py#L69) -> inspect._empty
-------------------------------------------------------------------------------
### pynchon.plugins.python.platform
* Overview:  [source code](/src/pynchon/plugins/python/platform.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (2 total)
  * [`pynchon.plugins.python.platform.PythonPlatform`](/src/pynchon/plugins/python/platform.py#L14-L39)
    * with bases ([Provider](#pynchonmodelsplugin_types),)
    * with properties: (4 total)
      *  [`config`](/src/pynchon/plugins/python/platform.py#L92) -> inspect._empty
      *  [`logger`](/src/pynchon/plugins/python/platform.py#L37) -> inspect._empty
      *  [`plugin_config`](/src/pynchon/plugins/python/platform.py#L64) -> inspect._empty
      *  [`siblings`](/src/pynchon/plugins/python/platform.py#L69) -> inspect._empty
  * [`pynchon.plugins.python.platform.PackageConfig`](/src/pynchon/plugins/python/platform.py#L42-L62)
    * with bases ([Config](#pynchonabcsconfig),)
    * with properties: (2 total)
      *  [`name`](/src/pynchon/plugins/python/platform.py#L50) -> str
      *  [`version`](/src/pynchon/plugins/python/platform.py#L37) -> str
-------------------------------------------------------------------------------
### pynchon.plugins.python.api
* Overview:  [source code](/src/pynchon/plugins/python/api.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (2 total)
  * [`pynchon.plugins.python.api.PythonApiConfig`](/src/pynchon/plugins/python/api.py#L8-L13)
    * with bases ([Config](#pynchonabcsconfig),)
  * [`pynchon.plugins.python.api.PythonAPI`](/src/pynchon/plugins/python/api.py#L14-L96)
    * with bases ([ShyPlanner](#pynchonmodelsplanner),)
    * with properties: (5 total)
      *  [`changes`](/src/pynchon/plugins/python/api.py#L27) -> inspect._empty
      *  [`config`](/src/pynchon/plugins/python/api.py#L92) -> inspect._empty
      *  [`logger`](/src/pynchon/plugins/python/api.py#L37) -> inspect._empty
      *  [`plugin_config`](/src/pynchon/plugins/python/api.py#L64) -> inspect._empty
      *  [`siblings`](/src/pynchon/plugins/python/api.py#L69) -> inspect._empty
-------------------------------------------------------------------------------
### pynchon.plugins.python.ast
* Overview:  [source code](/src/pynchon/plugins/python/ast.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
-------------------------------------------------------------------------------
### pynchon.util
* Overview:  [source code](/src/pynchon/util/__init__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (0 total)
* Functions: (4 total)
  * [`pynchon.util.click_recursive_help`](/src/pynchon/util/__init__.py#L47-L71)
    * with signature `(cmd, parent=None, out={}, file=<_io.TextIOWrapper name='<stdout>' mode='w' encoding='utf-8'>)`
  * [`pynchon.util.find_src_root`](/src/pynchon/util/__init__.py#L36-L44) with signature `(config: dict) -> str`
  * [`pynchon.util.get_root`](/src/pynchon/util/__init__.py#L12-L24) with signature `(path: str = '.') -> str`
  * [`pynchon.util.is_python_project`](/src/pynchon/util/__init__.py#L27-L33) with signature `() -> bool`
-------------------------------------------------------------------------------
### pynchon.util.testing
* Overview:  [source code](/src/pynchon/util/testing.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Functions: (1 total)
  * [`pynchon.util.testing.get_test_info`](/src/pynchon/util/testing.py#L9-L17) with signature `(fname: str) -> dict`
-------------------------------------------------------------------------------
### pynchon.util.python
* Overview:  [source code](/src/pynchon/util/python.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Functions: (3 total)
  * [`pynchon.util.python.is_package`](/src/pynchon/util/python.py#L8-L18) with signature `(folder: str) -> bool`
  * [`pynchon.util.python.load_entrypoints`](/src/pynchon/util/python.py#L29-L57) with signature `(config=None) -> dict`
  * [`pynchon.util.python.load_setupcfg`](/src/pynchon/util/python.py#L21-L26) with signature `(file: str = '', folder: str = '')`
-------------------------------------------------------------------------------
### pynchon.util.tagging
* Overview:  [source code](/src/pynchon/util/tagging.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (1 total)
  * [`pynchon.util.tagging.tagsM`](/src/pynchon/util/tagging.py#L87-L109)
    * with bases ([`__builtin__.object`](https://docs.python.org/3/library/functions.html#object),)
* Functions: (2 total)
  * [`pynchon.util.tagging.tag_factory`](/src/pynchon/util/tagging.py#L41-L60) with signature `(*args) -> 'typing.Any'`
  * [`pynchon.util.tagging.tagged_property`](/src/pynchon/util/tagging.py#L21-L38) with signature `(**ftags)`
-------------------------------------------------------------------------------
### pynchon.util.click
* Overview:  [source code](/src/pynchon/util/click.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Functions: (1 total)
  * [`pynchon.util.click.click_recursive_help`](/src/pynchon/util/click.py#L8-L31)
    * with signature `(cmd, parent=None, out={}, file=<_io.TextIOWrapper name='<stdout>' mode='w' encoding='utf-8'>)`
-------------------------------------------------------------------------------
### pynchon.util.config
* Overview:  [source code](/src/pynchon/util/config.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
-------------------------------------------------------------------------------
### pynchon.util.complexity
* Overview:  [source code](/src/pynchon/util/complexity.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (1 total)
  * [`pynchon.util.complexity.Checker`](/src/pynchon/util/complexity.py#L123-L135)
    * with bases ([McCabeChecker](#mccabe),)
* Functions: (5 total)
  * [`pynchon.util.complexity.clean_text`](/src/pynchon/util/complexity.py#L21-L23) with signature `(txt: str) -> str`
  * [`pynchon.util.complexity.complexity`](/src/pynchon/util/complexity.py#L138-L167) with signature `(code: str = None, fname: str = None, threshold: int = 7)`
  * [`pynchon.util.complexity.get_module`](/src/pynchon/util/complexity.py#L26-L44) with signature `(package: str = '', file: str = '')`
  * [`pynchon.util.complexity.get_refs`](/src/pynchon/util/complexity.py#L47-L78) with signature `(working_dir=None, module=None) -> dict`
  * [`pynchon.util.complexity.visit_module`](/src/pynchon/util/complexity.py#L81-L120)
    * with signature `(output=['-------------------------------------------------------------------------------\n### pynchon\n* Overview:  [source code](/src/pynchon/__init__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)\n* Classes: (0 total)', '-------------------------------------------------------------------------------\n### pynchon.__main__\n* Overview: (entrypoint) | [source code](/src/pynchon/__main__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)', '-------------------------------------------------------------------------------\n### pynchon.testing\n* Overview:  [source code](/src/pynchon/testing.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)', '-------------------------------------------------------------------------------\n### pynchon._version\n* Overview:  [source code](/src/pynchon/_version.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)', '-------------------------------------------------------------------------------\n### pynchon.annotate\n* Overview:  [source code](/src/pynchon/annotate.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)\n* Functions: (4 total)\n  * [`pynchon.annotate.function`](/src/pynchon/annotate.py#L114-L157) with signature `(name, fxn) -> None`\n  * [`pynchon.annotate.klass`](/src/pynchon/annotate.py#L13-L90) with signature `(name, kls) -> None`\n    * with admonitions:  [🐉 Complex](/src/pynchon/annotate.py#L1 "score 16 / 7") \n  * [`pynchon.annotate.module`](/src/pynchon/annotate.py#L93-L99) with signature `(name, module, working_dir=None) -> None`\n  * [`pynchon.annotate.should_skip`](/src/pynchon/annotate.py#L102-L111) with signature `(name: str)`', '-------------------------------------------------------------------------------\n### pynchon.tagging\n* Overview:  [source code](/src/pynchon/tagging.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)', '-------------------------------------------------------------------------------\n### pynchon.app\n* Overview:  [source code](/src/pynchon/app.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)\n* Classes: (5 total)\n  * [`pynchon.app.AppBase`](/src/pynchon/app.py#L29-L30)\n    * with bases ([`__builtin__.object`](https://docs.python.org/3/library/functions.html#object),)\n  * [`pynchon.app.AppConsole`](/src/pynchon/app.py#L33-L92)\n    * with bases ([AppBase](#pynchonapp),)\n    * with properties: (2 total)\n      *  [`manager`](/src/pynchon/app.py#L37) -> inspect._empty\n      *  [`status_bar`](/src/pynchon/app.py#L37) -> inspect._empty\n  * [`pynchon.app.AppExitHooks`](/src/pynchon/app.py#L95-L142)\n    * with bases ([AppBase](#pynchonapp),)\n  * [`pynchon.app.AppEvents`](/src/pynchon/app.py#L145-L148)\n    * with bases ([AppBase](#pynchonapp),)\n  * [`pynchon.app.App`](/src/pynchon/app.py#L151-L158)\n    * with bases ([AppConsole](#pynchonapp),[AppEvents](#pynchonapp),[AppExitHooks](#pynchonapp),)\n    * with properties: (2 total)\n      *  [`manager`](/src/pynchon/app.py#L37) -> inspect._empty\n      *  [`status_bar`](/src/pynchon/app.py#L37) -> inspect._empty', '-------------------------------------------------------------------------------\n### pynchon.constants\n* Overview:  [source code](/src/pynchon/constants.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)', '-------------------------------------------------------------------------------\n### pynchon.core\n* Overview:  [source code](/src/pynchon/core.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)\n* Classes: (1 total)\n  * [`pynchon.core.Config`](/src/pynchon/core.py#L11-L91)\n    * with bases ([Config](#pynchonabcsconfig),)\n    * with properties: (3 total)\n      *  [`plugins`](/src/pynchon/core.py#L31) -> inspect._empty\n      *  [`root`](/src/pynchon/core.py#L56) -> str\n      *  [`working_dir`](/src/pynchon/core.py#L86) -> inspect._empty', '-------------------------------------------------------------------------------\n### pynchon.events\n* Overview:  [source code](/src/pynchon/events.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)\n* Functions: (6 total)\n  * [`pynchon.events._lifecycle`](/src/pynchon/events.py#L53-L59) with signature ``\n  * [`pynchon.events.lifecycle_applying`](/src/pynchon/events.py#L29-L34) with signature `(sender, applying=None, **kwargs)`\n  * [`pynchon.events.lifecycle_config`](/src/pynchon/events.py#L21-L26) with signature `(sender, config)`\n  * [`pynchon.events.lifecycle_msg`](/src/pynchon/events.py#L46-L50) with signature `(sender, msg=None, **kwargs)`\n  * [`pynchon.events.lifecycle_plugin`](/src/pynchon/events.py#L13-L18) with signature `(sender, plugin)`\n  * [`pynchon.events.lifecycle_stage`](/src/pynchon/events.py#L37-L43) with signature `(sender, stage=None, **kwargs)`', '-------------------------------------------------------------------------------\n### pynchon.fleks\n* Overview:  [source code](/src/pynchon/fleks/__init__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)\n* Classes: (0 total)', '-------------------------------------------------------------------------------\n### pynchon.fleks.plugin\n* Overview:  [source code](/src/pynchon/fleks/plugin.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)\n* Classes: (1 total)\n  * [`pynchon.fleks.plugin.Plugin`](/src/pynchon/fleks/plugin.py#L12-L33)\n    * with bases ([`__builtin__.object`](https://docs.python.org/3/library/functions.html#object),)\n    * with properties: (1 total)\n      *  [`logger`](/src/pynchon/fleks/plugin.py#L37) -> inspect._empty', "-------------------------------------------------------------------------------\n### pynchon.fleks.typing\n* Overview:  [source code](/src/pynchon/fleks/typing.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)\n* Functions: (1 total)\n  * [`pynchon.fleks.typing.validate`](/src/pynchon/fleks/typing.py#L28-L29)\n    * with signature `(func: Union[ForwardRef('AnyCallableT'), NoneType] = None, *, config: 'ConfigType' = None) -> Any`", '-------------------------------------------------------------------------------\n### pynchon.fleks.meta\n* Overview:  [source code](/src/pynchon/fleks/meta/__init__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)\n* Classes: (0 total)', '-------------------------------------------------------------------------------\n### pynchon.fleks.meta.namespace\n* Overview:  [source code](/src/pynchon/fleks/meta/namespace.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)\n* Classes: (1 total)\n  * [`pynchon.fleks.meta.namespace.Namespace`](/src/pynchon/fleks/meta/namespace.py#L7-L35)\n    * with bases ([`__builtin__.object`](https://docs.python.org/3/library/functions.html#object),)\n* Functions: (1 total)\n  * [`pynchon.fleks.meta.namespace.namespace`](/src/pynchon/fleks/meta/namespace.py#L38-L46) with signature `(name, bases, namespace)`', '-------------------------------------------------------------------------------\n### pynchon.fleks.meta.oop\n* Overview:  [source code](/src/pynchon/fleks/meta/oop.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)\n* Classes: (2 total)\n  * [`pynchon.fleks.meta.oop.ClassMalformed`](/src/pynchon/fleks/meta/oop.py#L10-L11)\n    * with bases ([`__builtin__.TypeError`](https://docs.python.org/3/library/functions.html#TypeError),)\n  * [`pynchon.fleks.meta.oop.Meta`](/src/pynchon/fleks/meta/oop.py#L14-L176)\n    * with bases ([`__builtin__.type`](https://docs.python.org/3/library/functions.html#type),)\n    * with admonitions:  [🐉 Complex](/src/pynchon/fleks/meta/oop.py#L42 "score 9 / 7") ', '-------------------------------------------------------------------------------\n### pynchon.shimport\n* Overview:  [source code](/src/pynchon/shimport/__init__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)\n* Classes: (0 total)', '-------------------------------------------------------------------------------\n### pynchon.shimport.util\n* Overview:  [source code](/src/pynchon/shimport/util.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)\n* Functions: (1 total)\n  /src/pynchon/shimport/util.py#L6-L26 "")\n  * [`pynchon.shimport.util.get_namespace`](/src/pynchon/shimport/util.py#L6-L26) with signature `(name)`\n    * with admonitions:  [ 🚩has FIXMEs ](/src/pynchon/shimport/util.py#L7 "on lines [7]") ', '-------------------------------------------------------------------------------\n### pynchon.shimport.module\n* Overview:  [source code](/src/pynchon/shimport/module.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)\n* Classes: (1 total)\n  * [`pynchon.shimport.module.ModuleBuilder`](/src/pynchon/shimport/module.py#L10-L38)\n    * with bases ([ModulesWrapper](#pynchonshimportmodels),)\n    * with properties: (3 total)\n      *  [`module`](/src/pynchon/shimport/module.py#L101) -> inspect._empty\n      *  [`parent`](/src/pynchon/shimport/module.py#L116) -> inspect._empty\n      *  [`parent_folder`](/src/pynchon/shimport/module.py#L111) -> inspect._empty\n* Functions: (3 total)\n  * [`pynchon.shimport.module.lazy`](/src/pynchon/shimport/module.py#L76-L81) with signature `(module_name: str) -> pynchon.shimport.models.LazyModule`\n  * [`pynchon.shimport.module.module_builder`](/src/pynchon/shimport/module.py#L41-L56)\n    * with signature `(name: str, return_objects=False, assign_objects: bool = True, sort_objects: Dict = {}, **kwargs) -> None`\n  * [`pynchon.shimport.module.wrap`](/src/pynchon/shimport/module.py#L63-L70) with signature `(name, **kwargs)`', '-------------------------------------------------------------------------------\n### pynchon.shimport.models\n* Overview:  [source code](/src/pynchon/shimport/models.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)\n* Classes: (3 total)\n  * [`pynchon.shimport.models.Base`](/src/pynchon/shimport/models.py#L19-L28)\n    * with bases ([`__builtin__.object`](https://docs.python.org/3/library/functions.html#object),)\n  * [`pynchon.shimport.models.ModulesWrapper`](/src/pynchon/shimport/models.py#L31-L366)\n    * with bases ([Base](#pynchonshimportmodels),)\n    * with admonitions:  [🐉 Complex](/src/pynchon/shimport/models.py#L302 "score 8 / 7") \n    * with properties: (3 total)\n      *  [`module`](/src/pynchon/shimport/models.py#L101) -> inspect._empty\n      *  [`parent`](/src/pynchon/shimport/models.py#L116) -> inspect._empty\n      *  [`parent_folder`](/src/pynchon/shimport/models.py#L111) -> inspect._empty\n  * [`pynchon.shimport.models.LazyModule`](/src/pynchon/shimport/models.py#L369-L400)\n    * with bases ([`__builtin__.object`](https://docs.python.org/3/library/functions.html#object),)', '-------------------------------------------------------------------------------\n### pynchon.shimport.abcs\n* Overview:  [source code](/src/pynchon/shimport/abcs.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)\n* Classes: (1 total)\n  * [`pynchon.shimport.abcs.FilterResult`](/src/pynchon/shimport/abcs.py#L10-L32)\n    * with bases ([`__builtin__.list`](https://docs.python.org/3/library/functions.html#list),[Generic](#typing),)', '-------------------------------------------------------------------------------\n### pynchon.shimport.types\n* Overview:  [source code](/src/pynchon/shimport/types.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)', '-------------------------------------------------------------------------------\n### pynchon.shimport.registry\n* Overview:  [source code](/src/pynchon/shimport/registry.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)', '-------------------------------------------------------------------------------\n### pynchon.shimport.hooks\n* Overview:  [source code](/src/pynchon/shimport/hooks.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)', '-------------------------------------------------------------------------------\n### pynchon.shimport.importing\n* Overview:  [source code](/src/pynchon/shimport/importing.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)', '-------------------------------------------------------------------------------\n### pynchon.bin\n* Overview:  [source code](/src/pynchon/bin/__init__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)\n* Classes: (0 total)', '-------------------------------------------------------------------------------\n### pynchon.bin.entry\n* Overview:  [source code](/src/pynchon/bin/entry.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)\n* Classes: (1 total)\n  * [`pynchon.bin.entry.RootGroup`](/src/pynchon/bin/entry.py#L17-L85)\n    * with bases ([Group](#clickcore),)\n    * with admonitions:  [🐉 Complex](/src/pynchon/bin/entry.py#L4 "score 13 / 7") \n* Functions: (1 total)\n  * [`pynchon.bin.entry.entry`](/src/pynchon/bin/entry.py#L88-L98) with signature `(*args: Any, **kwargs: Any) -> Any`', '-------------------------------------------------------------------------------\n### pynchon.bin.parse\n* Overview:  [source code](/src/pynchon/bin/parse.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)', '-------------------------------------------------------------------------------\n### pynchon.bin.options\n* Overview:  [source code](/src/pynchon/bin/options.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)', '-------------------------------------------------------------------------------\n### pynchon.bin.render\n* Overview:  [source code](/src/pynchon/bin/render.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)', '-------------------------------------------------------------------------------\n### pynchon.bin.cli\n* Overview:  [source code](/src/pynchon/bin/cli.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)', '-------------------------------------------------------------------------------\n### pynchon.bin.dot\n* Overview:  [source code](/src/pynchon/bin/dot.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)', '-------------------------------------------------------------------------------\n### pynchon.bin.groups\n* Overview:  [source code](/src/pynchon/bin/groups.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)', '-------------------------------------------------------------------------------\n### pynchon.plugins\n* Overview:  [source code](/src/pynchon/plugins/__init__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)\n* Classes: (0 total)', '-------------------------------------------------------------------------------\n### pynchon.plugins.json\n* Overview:  [source code](/src/pynchon/plugins/json.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)\n* Classes: (1 total)\n  * [`pynchon.plugins.json.Json`](/src/pynchon/plugins/json.py#L50-L67)\n    * with bases ([ToolPlugin](#pynchonmodelsplugin_types),)\n    * with properties: (4 total)\n      *  [`config`](/src/pynchon/plugins/json.py#L92) -> inspect._empty\n      *  [`logger`](/src/pynchon/plugins/json.py#L37) -> inspect._empty\n      *  [`plugin_config`](/src/pynchon/plugins/json.py#L64) -> inspect._empty\n      *  [`siblings`](/src/pynchon/plugins/json.py#L69) -> inspect._empty', '-------------------------------------------------------------------------------\n### pynchon.plugins.src\n* Overview:  [source code](/src/pynchon/plugins/src.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)\n* Classes: (1 total)\n  * [`pynchon.plugins.src.SourceMan`](/src/pynchon/plugins/src.py#L29-L148)\n    * with bases ([Manager](#pynchonmodelsplanner),)\n    * with properties: (5 total)\n      *  [`changes`](/src/pynchon/plugins/src.py#L27) -> inspect._empty\n      *  [`config`](/src/pynchon/plugins/src.py#L92) -> inspect._empty\n      *  [`logger`](/src/pynchon/plugins/src.py#L37) -> inspect._empty\n      *  [`plugin_config`](/src/pynchon/plugins/src.py#L64) -> inspect._empty\n      *  [`siblings`](/src/pynchon/plugins/src.py#L69) -> inspect._empty', '-------------------------------------------------------------------------------\n### pynchon.plugins.parse\n* Overview:  [source code](/src/pynchon/plugins/parse.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)', '-------------------------------------------------------------------------------\n### pynchon.plugins.cookie_cutter\n* Overview:  [source code](/src/pynchon/plugins/cookie_cutter.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)\n* Classes: (1 total)\n  * [`pynchon.plugins.cookie_cutter.CookierCutter`](/src/pynchon/plugins/cookie_cutter.py#L22-L36)\n    * with bases ([ToolPlugin](#pynchonmodelsplugin_types),)\n    * with properties: (4 total)\n      *  [`config`](/src/pynchon/plugins/cookie_cutter.py#L92) -> inspect._empty\n      *  [`logger`](/src/pynchon/plugins/cookie_cutter.py#L37) -> inspect._empty\n      *  [`plugin_config`](/src/pynchon/plugins/cookie_cutter.py#L64) -> inspect._empty\n      *  [`siblings`](/src/pynchon/plugins/cookie_cutter.py#L69) -> inspect._empty', '-------------------------------------------------------------------------------\n### pynchon.plugins.tox\n* Overview:  [source code](/src/pynchon/plugins/tox.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)\n* Classes: (1 total)\n  * [`pynchon.plugins.tox.PluginTemplate`](/src/pynchon/plugins/tox.py#L9-L17)\n    * with bases ([Provider](#pynchonmodelsplugin_types),)\n    * with properties: (4 total)\n      *  [`config`](/src/pynchon/plugins/tox.py#L92) -> inspect._empty\n      *  [`logger`](/src/pynchon/plugins/tox.py#L37) -> inspect._empty\n      *  [`plugin_config`](/src/pynchon/plugins/tox.py#L64) -> inspect._empty\n      *  [`siblings`](/src/pynchon/plugins/tox.py#L69) -> inspect._empty', '-------------------------------------------------------------------------------\n### pynchon.plugins.cicd\n* Overview:  [source code](/src/pynchon/plugins/cicd.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)\n* Classes: (1 total)\n  * [`pynchon.plugins.cicd.CiCd`](/src/pynchon/plugins/cicd.py#L15-L40)\n    * with bases ([Provider](#pynchonmodelsplugin_types),)\n    * with properties: (4 total)\n      *  [`config`](/src/pynchon/plugins/cicd.py#L92) -> inspect._empty\n      *  [`logger`](/src/pynchon/plugins/cicd.py#L37) -> inspect._empty\n      *  [`plugin_config`](/src/pynchon/plugins/cicd.py#L64) -> inspect._empty\n      *  [`siblings`](/src/pynchon/plugins/cicd.py#L69) -> inspect._empty', '-------------------------------------------------------------------------------\n### pynchon.plugins.util\n* Overview:  [source code](/src/pynchon/plugins/util.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)\n* Classes: (3 total)\n  * [`pynchon.plugins.util.PluginNotInitialized`](/src/pynchon/plugins/util.py#L11-L12)\n    * with bases ([`__builtin__.RuntimeError`](https://docs.python.org/3/library/functions.html#RuntimeError),)\n  * [`pynchon.plugins.util.PluginNotRegistered`](/src/pynchon/plugins/util.py#L15-L16)\n    * with bases ([`__builtin__.RuntimeError`](https://docs.python.org/3/library/functions.html#RuntimeError),)\n  * [`pynchon.plugins.util.PluginNotConfigured`](/src/pynchon/plugins/util.py#L19-L20)\n    * with bases ([`__builtin__.RuntimeError`](https://docs.python.org/3/library/functions.html#RuntimeError),)\n* Functions: (3 total)\n  * [`pynchon.plugins.util.get_plugin_class`](/src/pynchon/plugins/util.py#L33-L39) with signature `(plugin_name: str) -> Type`\n  * [`pynchon.plugins.util.get_plugin_meta`](/src/pynchon/plugins/util.py#L23-L30) with signature `(plugin_name: str) -> Dict`\n  * [`pynchon.plugins.util.get_plugin_obj`](/src/pynchon/plugins/util.py#L45-L53) with signature `(plugin_name: str) -> object`', '-------------------------------------------------------------------------------\n### pynchon.plugins.git\n* Overview:  [source code](/src/pynchon/plugins/git.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)\n* Classes: (2 total)\n  * [`pynchon.plugins.git.GitConfig`](/src/pynchon/plugins/git.py#L11-L84)\n    * with bases ([Config](#pynchonabcsconfig),)\n    * with properties: (9 total)\n      *  [`branch_name`](/src/pynchon/plugins/git.py#L74) -> inspect._empty\n      *  [`default_remote_branch`](/src/pynchon/plugins/git.py#L37) -> typing.Union[str, NoneType]\n      *  [`github_org`](/src/pynchon/plugins/git.py#L48) -> inspect._empty\n      *  [`hash`](/src/pynchon/plugins/git.py#L80) -> str\n      *  [`is_github`](/src/pynchon/plugins/git.py#L42) -> inspect._empty\n      *  [`repo`](/src/pynchon/plugins/git.py#L37) -> typing.Union[str, NoneType]\n      *  [`repo_name`](/src/pynchon/plugins/git.py#L56) -> typing.Union[str, NoneType]\n      *  [`repo_url`](/src/pynchon/plugins/git.py#L68) -> inspect._empty\n      *  [`root`](/src/pynchon/plugins/git.py#L28) -> typing.Union[str, NoneType]\n  * [`pynchon.plugins.git.Git`](/src/pynchon/plugins/git.py#L87-L112)\n    * with bases ([Provider](#pynchonmodelsplugin_types),)\n    * with properties: (5 total)\n      *  [`config`](/src/pynchon/plugins/git.py#L92) -> inspect._empty\n      *  [`logger`](/src/pynchon/plugins/git.py#L37) -> inspect._empty\n      *  [`modified`](/src/pynchon/plugins/git.py#L96) -> typing.List[pynchon.abcs.path.Path]\n      *  [`plugin_config`](/src/pynchon/plugins/git.py#L64) -> inspect._empty\n      *  [`siblings`](/src/pynchon/plugins/git.py#L69) -> inspect._empty', '-------------------------------------------------------------------------------\n### pynchon.plugins.docs\n* Overview:  [source code](/src/pynchon/plugins/docs.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)\n* Classes: (1 total)\n  * [`pynchon.plugins.docs.DocsMan`](/src/pynchon/plugins/docs.py#L15-L126)\n    * with bases ([Planner](#pynchonmodelsplanner),)\n    * with properties: (5 total)\n      *  [`changes`](/src/pynchon/plugins/docs.py#L27) -> inspect._empty\n      *  [`config`](/src/pynchon/plugins/docs.py#L92) -> inspect._empty\n      *  [`logger`](/src/pynchon/plugins/docs.py#L37) -> inspect._empty\n      *  [`plugin_config`](/src/pynchon/plugins/docs.py#L64) -> inspect._empty\n      *  [`siblings`](/src/pynchon/plugins/docs.py#L69) -> inspect._empty', '-------------------------------------------------------------------------------\n### pynchon.plugins.jinja\n* Overview:  [source code](/src/pynchon/plugins/jinja.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)\n* Classes: (1 total)\n  * [`pynchon.plugins.jinja.Jinja`](/src/pynchon/plugins/jinja.py#L12-L145)\n    * with bases ([Planner](#pynchonmodelsplanner),)\n    * with properties: (5 total)\n      *  [`changes`](/src/pynchon/plugins/jinja.py#L27) -> inspect._empty\n      *  [`config`](/src/pynchon/plugins/jinja.py#L92) -> inspect._empty\n      *  [`logger`](/src/pynchon/plugins/jinja.py#L37) -> inspect._empty\n      *  [`plugin_config`](/src/pynchon/plugins/jinja.py#L64) -> inspect._empty\n      *  [`siblings`](/src/pynchon/plugins/jinja.py#L69) -> inspect._empty', '-------------------------------------------------------------------------------\n### pynchon.plugins.rtd\n* Overview:  [source code](/src/pynchon/plugins/rtd.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)', '-------------------------------------------------------------------------------\n### pynchon.plugins.pandoc\n* Overview:  [source code](/src/pynchon/plugins/pandoc.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)\n* Classes: (1 total)\n  * [`pynchon.plugins.pandoc.PluginTemplate`](/src/pynchon/plugins/pandoc.py#L9-L17)\n    * with bases ([Provider](#pynchonmodelsplugin_types),)\n    * with properties: (4 total)\n      *  [`config`](/src/pynchon/plugins/pandoc.py#L92) -> inspect._empty\n      *  [`logger`](/src/pynchon/plugins/pandoc.py#L37) -> inspect._empty\n      *  [`plugin_config`](/src/pynchon/plugins/pandoc.py#L64) -> inspect._empty\n      *  [`siblings`](/src/pynchon/plugins/pandoc.py#L69) -> inspect._empty', '-------------------------------------------------------------------------------\n### pynchon.plugins.griffe\n* Overview:  [source code](/src/pynchon/plugins/griffe.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)\n* Classes: (1 total)\n  * [`pynchon.plugins.griffe.Griffe`](/src/pynchon/plugins/griffe.py#L9-L18)\n    * with bases ([ToolPlugin](#pynchonmodelsplugin_types),)\n    * with properties: (4 total)\n      *  [`config`](/src/pynchon/plugins/griffe.py#L92) -> inspect._empty\n      *  [`logger`](/src/pynchon/plugins/griffe.py#L37) -> inspect._empty\n      *  [`plugin_config`](/src/pynchon/plugins/griffe.py#L64) -> inspect._empty\n      *  [`siblings`](/src/pynchon/plugins/griffe.py#L69) -> inspect._empty', '-------------------------------------------------------------------------------\n### pynchon.plugins.github\n* Overview:  [source code](/src/pynchon/plugins/github.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)\n* Classes: (1 total)\n  * [`pynchon.plugins.github.GitHub`](/src/pynchon/plugins/github.py#L13-L56)\n    * with bases ([ToolPlugin](#pynchonmodelsplugin_types),)\n    * with properties: (4 total)\n      *  [`config`](/src/pynchon/plugins/github.py#L92) -> inspect._empty\n      *  [`logger`](/src/pynchon/plugins/github.py#L37) -> inspect._empty\n      *  [`plugin_config`](/src/pynchon/plugins/github.py#L64) -> inspect._empty\n      *  [`siblings`](/src/pynchon/plugins/github.py#L69) -> inspect._empty', '-------------------------------------------------------------------------------\n### pynchon.plugins.makefile\n* Overview:  [source code](/src/pynchon/plugins/makefile/__init__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)', '-------------------------------------------------------------------------------\n### pynchon.plugins.core\n* Overview:  [source code](/src/pynchon/plugins/core.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)\n* Classes: (1 total)\n  * [`pynchon.plugins.core.Core`](/src/pynchon/plugins/core.py#L11-L139)\n    * with bases ([Planner](#pynchonmodelsplanner),)\n    * with properties: (5 total)\n      *  [`changes`](/src/pynchon/plugins/core.py#L27) -> inspect._empty\n      *  [`config`](/src/pynchon/plugins/core.py#L92) -> inspect._empty\n      *  [`logger`](/src/pynchon/plugins/core.py#L37) -> inspect._empty\n      *  [`plugin_config`](/src/pynchon/plugins/core.py#L64) -> inspect._empty\n      *  [`siblings`](/src/pynchon/plugins/core.py#L69) -> inspect._empty', '-------------------------------------------------------------------------------\n### pynchon.plugins.fixme\n* Overview:  [source code](/src/pynchon/plugins/fixme.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)\n* Classes: (2 total)\n  * [`pynchon.plugins.fixme.FixMeConfig`](/src/pynchon/plugins/fixme.py#L14-L15)\n    * with bases ([Config](#pynchonabcsconfig),)\n  * [`pynchon.plugins.fixme.FixMe`](/src/pynchon/plugins/fixme.py#L18-L104)\n    * with bases ([Planner](#pynchonmodelsplanner),)\n    * with properties: (5 total)\n      *  [`changes`](/src/pynchon/plugins/fixme.py#L27) -> inspect._empty\n      *  [`config`](/src/pynchon/plugins/fixme.py#L92) -> inspect._empty\n      *  [`logger`](/src/pynchon/plugins/fixme.py#L37) -> inspect._empty\n      *  [`plugin_config`](/src/pynchon/plugins/fixme.py#L64) -> inspect._empty\n      *  [`siblings`](/src/pynchon/plugins/fixme.py#L69) -> inspect._empty', '-------------------------------------------------------------------------------\n### pynchon.plugins.release\n* Overview:  [source code](/src/pynchon/plugins/release.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)', '-------------------------------------------------------------------------------\n### pynchon.plugins.render\n* Overview:  [source code](/src/pynchon/plugins/render.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)\n* Classes: (1 total)\n  * [`pynchon.plugins.render.Renderers`](/src/pynchon/plugins/render.py#L10-L17)\n    * with bases ([NameSpace](#pynchonmodelsplugin_types),)\n    * with properties: (4 total)\n      *  [`config`](/src/pynchon/plugins/render.py#L92) -> inspect._empty\n      *  [`logger`](/src/pynchon/plugins/render.py#L37) -> inspect._empty\n      *  [`plugin_config`](/src/pynchon/plugins/render.py#L64) -> inspect._empty\n      *  [`siblings`](/src/pynchon/plugins/render.py#L69) -> inspect._empty', '-------------------------------------------------------------------------------\n### pynchon.plugins.gen\n* Overview:  [source code](/src/pynchon/plugins/gen.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)\n* Classes: (1 total)\n  * [`pynchon.plugins.gen.Generators`](/src/pynchon/plugins/gen.py#L9-L17)\n    * with bases ([NameSpace](#pynchonmodelsplugin_types),)\n    * with properties: (4 total)\n      *  [`config`](/src/pynchon/plugins/gen.py#L92) -> inspect._empty\n      *  [`logger`](/src/pynchon/plugins/gen.py#L37) -> inspect._empty\n      *  [`plugin_config`](/src/pynchon/plugins/gen.py#L64) -> inspect._empty\n      *  [`siblings`](/src/pynchon/plugins/gen.py#L69) -> inspect._empty', '-------------------------------------------------------------------------------\n### pynchon.plugins.plugins\n* Overview:  [source code](/src/pynchon/plugins/plugins.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)\n* Classes: (1 total)\n  * [`pynchon.plugins.plugins.PluginsMan`](/src/pynchon/plugins/plugins.py#L11-L41)\n    * with bases ([Manager](#pynchonmodelsplanner),)\n    * with properties: (5 total)\n      *  [`changes`](/src/pynchon/plugins/plugins.py#L27) -> inspect._empty\n      *  [`config`](/src/pynchon/plugins/plugins.py#L92) -> inspect._empty\n      *  [`logger`](/src/pynchon/plugins/plugins.py#L37) -> inspect._empty\n      *  [`plugin_config`](/src/pynchon/plugins/plugins.py#L64) -> inspect._empty\n      *  [`siblings`](/src/pynchon/plugins/plugins.py#L69) -> inspect._empty', '-------------------------------------------------------------------------------\n### pynchon.plugins.api\n* Overview:  [source code](/src/pynchon/plugins/api.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)', '-------------------------------------------------------------------------------\n### pynchon.plugins.__template__\n* Overview:  [source code](/src/pynchon/plugins/__template__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)\n* Classes: (1 total)\n  * [`pynchon.plugins.__template__.PluginTemplate`](/src/pynchon/plugins/__template__.py#L9-L17)\n    * with bases ([Provider](#pynchonmodelsplugin_types),)\n    * with properties: (4 total)\n      *  [`config`](/src/pynchon/plugins/__template__.py#L92) -> inspect._empty\n      *  [`logger`](/src/pynchon/plugins/__template__.py#L37) -> inspect._empty\n      *  [`plugin_config`](/src/pynchon/plugins/__template__.py#L64) -> inspect._empty\n      *  [`siblings`](/src/pynchon/plugins/__template__.py#L69) -> inspect._empty', '-------------------------------------------------------------------------------\n### pynchon.plugins.load\n* Overview:  [source code](/src/pynchon/plugins/load.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)', '-------------------------------------------------------------------------------\n### pynchon.plugins.dot\n* Overview:  [source code](/src/pynchon/plugins/dot.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)\n* Classes: (1 total)\n  * [`pynchon.plugins.dot.Dot`](/src/pynchon/plugins/dot.py#L14-L126)\n    * with bases ([Planner](#pynchonmodelsplanner),)\n    * with properties: (5 total)\n      *  [`changes`](/src/pynchon/plugins/dot.py#L27) -> inspect._empty\n      *  [`config`](/src/pynchon/plugins/dot.py#L92) -> inspect._empty\n      *  [`logger`](/src/pynchon/plugins/dot.py#L37) -> inspect._empty\n      *  [`plugin_config`](/src/pynchon/plugins/dot.py#L64) -> inspect._empty\n      *  [`siblings`](/src/pynchon/plugins/dot.py#L69) -> inspect._empty', '-------------------------------------------------------------------------------\n### pynchon.plugins.project\n* Overview:  [source code](/src/pynchon/plugins/project.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)\n* Classes: (2 total)\n  * [`pynchon.plugins.project.ProjectConfig`](/src/pynchon/plugins/project.py#L11-L46)\n    * with bases ([Config](#pynchonabcsconfig),)\n    * with properties: (3 total)\n      *  [`name`](/src/pynchon/plugins/project.py#L18) -> typing.Union[str, NoneType]\n      *  [`root`](/src/pynchon/plugins/project.py#L28) -> str\n      *  [`subproject`](/src/pynchon/plugins/project.py#L34) -> typing.Dict\n  * [`pynchon.plugins.project.Project`](/src/pynchon/plugins/project.py#L49-L54)\n    * with bases ([Manager](#pynchonmodelsplanner),)\n    * with properties: (5 total)\n      *  [`changes`](/src/pynchon/plugins/project.py#L27) -> inspect._empty\n      *  [`config`](/src/pynchon/plugins/project.py#L92) -> inspect._empty\n      *  [`logger`](/src/pynchon/plugins/project.py#L37) -> inspect._empty\n      *  [`plugin_config`](/src/pynchon/plugins/project.py#L64) -> inspect._empty\n      *  [`siblings`](/src/pynchon/plugins/project.py#L69) -> inspect._empty', '-------------------------------------------------------------------------------\n### pynchon.plugins.globals\n* Overview:  [source code](/src/pynchon/plugins/globals.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)\n* Classes: (2 total)\n  * [`pynchon.plugins.globals.GlobalsConfig`](/src/pynchon/plugins/globals.py#L6-L10)\n    * with bases ([Config](#pynchonabcsconfig),)\n  * [`pynchon.plugins.globals.Globals`](/src/pynchon/plugins/globals.py#L13-L18)\n    * with bases ([Provider](#pynchonmodelsplugin_types),)\n    * with properties: (4 total)\n      *  [`config`](/src/pynchon/plugins/globals.py#L92) -> inspect._empty\n      *  [`logger`](/src/pynchon/plugins/globals.py#L37) -> inspect._empty\n      *  [`plugin_config`](/src/pynchon/plugins/globals.py#L64) -> inspect._empty\n      *  [`siblings`](/src/pynchon/plugins/globals.py#L69) -> inspect._empty', '-------------------------------------------------------------------------------\n### pynchon.plugins.tests\n* Overview:  [source code](/src/pynchon/plugins/tests.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)\n* Classes: (1 total)\n  * [`pynchon.plugins.tests.Tests`](/src/pynchon/plugins/tests.py#L9-L16)\n    * with bases ([Planner](#pynchonmodelsplanner),)\n    * with properties: (5 total)\n      *  [`changes`](/src/pynchon/plugins/tests.py#L27) -> inspect._empty\n      *  [`config`](/src/pynchon/plugins/tests.py#L92) -> inspect._empty\n      *  [`logger`](/src/pynchon/plugins/tests.py#L37) -> inspect._empty\n      *  [`plugin_config`](/src/pynchon/plugins/tests.py#L64) -> inspect._empty\n      *  [`siblings`](/src/pynchon/plugins/tests.py#L69) -> inspect._empty', '-------------------------------------------------------------------------------\n### pynchon.plugins.ast\n* Overview:  [source code](/src/pynchon/plugins/ast.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)', '-------------------------------------------------------------------------------\n### pynchon.plugins.hooks\n* Overview:  [source code](/src/pynchon/plugins/hooks.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)', '-------------------------------------------------------------------------------\n### pynchon.plugins.terraform\n* Overview:  [source code](/src/pynchon/plugins/terraform.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)\n* Classes: (1 total)\n  * [`pynchon.plugins.terraform.PluginTemplate`](/src/pynchon/plugins/terraform.py#L9-L17)\n    * with bases ([Provider](#pynchonmodelsplugin_types),)\n    * with properties: (4 total)\n      *  [`config`](/src/pynchon/plugins/terraform.py#L92) -> inspect._empty\n      *  [`logger`](/src/pynchon/plugins/terraform.py#L37) -> inspect._empty\n      *  [`plugin_config`](/src/pynchon/plugins/terraform.py#L64) -> inspect._empty\n      *  [`siblings`](/src/pynchon/plugins/terraform.py#L69) -> inspect._empty', '-------------------------------------------------------------------------------\n### pynchon.plugins.scaffolding\n* Overview:  [source code](/src/pynchon/plugins/scaffolding/__init__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)\n* Classes: (1 total)\n  * [`pynchon.plugins.scaffolding.Scaffolding`](/src/pynchon/plugins/scaffolding/__init__.py#L13-L110)\n    * with bases ([ShyPlanner](#pynchonmodelsplanner),)\n    * with properties: (7 total)\n      *  [`changes`](/src/pynchon/plugins/scaffolding/__init__.py#L27) -> inspect._empty\n      *  [`config`](/src/pynchon/plugins/scaffolding/__init__.py#L92) -> inspect._empty\n      *  [`logger`](/src/pynchon/plugins/scaffolding/__init__.py#L37) -> inspect._empty\n      *  [`matches`](/src/pynchon/plugins/scaffolding/__init__.py#L42) -> inspect._empty\n      *  [`plugin_config`](/src/pynchon/plugins/scaffolding/__init__.py#L64) -> inspect._empty\n      *  [`scaffolds`](/src/pynchon/plugins/scaffolding/__init__.py#L57) -> inspect._empty\n      *  [`siblings`](/src/pynchon/plugins/scaffolding/__init__.py#L69) -> inspect._empty\n* Classes: (1 total)\n  * [`pynchon.plugins.scaffolding.Scaffolding`](/src/pynchon/plugins/scaffolding/__init__.py#L13-L110)\n    * with bases ([ShyPlanner](#pynchonmodelsplanner),)\n    * with properties: (7 total)\n      *  [`changes`](/src/pynchon/plugins/scaffolding/__init__.py#L27) -> inspect._empty\n      *  [`config`](/src/pynchon/plugins/scaffolding/__init__.py#L92) -> inspect._empty\n      *  [`logger`](/src/pynchon/plugins/scaffolding/__init__.py#L37) -> inspect._empty\n      *  [`matches`](/src/pynchon/plugins/scaffolding/__init__.py#L42) -> inspect._empty\n      *  [`plugin_config`](/src/pynchon/plugins/scaffolding/__init__.py#L64) -> inspect._empty\n      *  [`scaffolds`](/src/pynchon/plugins/scaffolding/__init__.py#L57) -> inspect._empty\n      *  [`siblings`](/src/pynchon/plugins/scaffolding/__init__.py#L69) -> inspect._empty', '-------------------------------------------------------------------------------\n### pynchon.plugins.scaffolding.config\n* Overview:  [source code](/src/pynchon/plugins/scaffolding/config.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)\n* Classes: (2 total)\n  * [`pynchon.plugins.scaffolding.config.ScaffoldingItem`](/src/pynchon/plugins/scaffolding/config.py#L11-L35)\n    * with bases ([AttrDict](#pynchonabcsattrdict),)\n    * with properties: (1 total)\n      *  [`exists`](/src/pynchon/plugins/scaffolding/config.py#L14) -> bool\n  * [`pynchon.plugins.scaffolding.config.ScaffoldingConfig`](/src/pynchon/plugins/scaffolding/config.py#L38-L41)\n    * with bases ([Config](#pynchonabcsconfig),)', '-------------------------------------------------------------------------------\n### pynchon.plugins.doctor\n* Overview:  [source code](/src/pynchon/plugins/doctor/__init__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)', '-------------------------------------------------------------------------------\n### pynchon.plugins.python\n* Overview:  [source code](/src/pynchon/plugins/python/__init__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)\n* Classes: (0 total)', '-------------------------------------------------------------------------------\n### pynchon.plugins.python.pypi\n* Overview:  [source code](/src/pynchon/plugins/python/pypi.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)\n* Classes: (2 total)\n  * [`pynchon.plugins.python.pypi.PyPiConfig`](/src/pynchon/plugins/python/pypi.py#L9-L15)\n    * with bases ([Config](#pynchonabcsconfig),)\n  * [`pynchon.plugins.python.pypi.PyPI`](/src/pynchon/plugins/python/pypi.py#L18-L22)\n    * with bases ([Provider](#pynchonmodelsplugin_types),)\n    * with properties: (4 total)\n      *  [`config`](/src/pynchon/plugins/python/pypi.py#L92) -> inspect._empty\n      *  [`logger`](/src/pynchon/plugins/python/pypi.py#L37) -> inspect._empty\n      *  [`plugin_config`](/src/pynchon/plugins/python/pypi.py#L64) -> inspect._empty\n      *  [`siblings`](/src/pynchon/plugins/python/pypi.py#L69) -> inspect._empty', '-------------------------------------------------------------------------------\n### pynchon.plugins.python.models\n* Overview:  [source code](/src/pynchon/plugins/python/models.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)', '-------------------------------------------------------------------------------\n### pynchon.plugins.python.config\n* Overview:  [source code](/src/pynchon/plugins/python/config.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)', '-------------------------------------------------------------------------------\n### pynchon.plugins.python.cli\n* Overview:  [source code](/src/pynchon/plugins/python/cli.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)\n* Classes: (2 total)\n  * [`pynchon.plugins.python.cli.PythonCliConfig`](/src/pynchon/plugins/python/cli.py#L14-L55)\n    * with bases ([Config](#pynchonabcsconfig),)\n    * with properties: (2 total)\n      *  [`entrypoints`](/src/pynchon/plugins/python/cli.py#L32) -> dict\n      *  [`src_root`](/src/pynchon/plugins/python/cli.py#L20) -> inspect._empty\n  * [`pynchon.plugins.python.cli.PythonCLI`](/src/pynchon/plugins/python/cli.py#L58-L248)\n    * with bases ([ShyPlanner](#pynchonmodelsplanner),)\n    * with properties: (5 total)\n      *  [`changes`](/src/pynchon/plugins/python/cli.py#L27) -> inspect._empty\n      *  [`config`](/src/pynchon/plugins/python/cli.py#L92) -> inspect._empty\n      *  [`logger`](/src/pynchon/plugins/python/cli.py#L37) -> inspect._empty\n      *  [`plugin_config`](/src/pynchon/plugins/python/cli.py#L64) -> inspect._empty\n      *  [`siblings`](/src/pynchon/plugins/python/cli.py#L69) -> inspect._empty', '-------------------------------------------------------------------------------\n### pynchon.plugins.python.platform\n* Overview:  [source code](/src/pynchon/plugins/python/platform.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)\n* Classes: (2 total)\n  * [`pynchon.plugins.python.platform.PythonPlatform`](/src/pynchon/plugins/python/platform.py#L14-L39)\n    * with bases ([Provider](#pynchonmodelsplugin_types),)\n    * with properties: (4 total)\n      *  [`config`](/src/pynchon/plugins/python/platform.py#L92) -> inspect._empty\n      *  [`logger`](/src/pynchon/plugins/python/platform.py#L37) -> inspect._empty\n      *  [`plugin_config`](/src/pynchon/plugins/python/platform.py#L64) -> inspect._empty\n      *  [`siblings`](/src/pynchon/plugins/python/platform.py#L69) -> inspect._empty\n  * [`pynchon.plugins.python.platform.PackageConfig`](/src/pynchon/plugins/python/platform.py#L42-L62)\n    * with bases ([Config](#pynchonabcsconfig),)\n    * with properties: (2 total)\n      *  [`name`](/src/pynchon/plugins/python/platform.py#L50) -> str\n      *  [`version`](/src/pynchon/plugins/python/platform.py#L37) -> str', '-------------------------------------------------------------------------------\n### pynchon.plugins.python.api\n* Overview:  [source code](/src/pynchon/plugins/python/api.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)\n* Classes: (2 total)\n  * [`pynchon.plugins.python.api.PythonApiConfig`](/src/pynchon/plugins/python/api.py#L8-L13)\n    * with bases ([Config](#pynchonabcsconfig),)\n  * [`pynchon.plugins.python.api.PythonAPI`](/src/pynchon/plugins/python/api.py#L14-L96)\n    * with bases ([ShyPlanner](#pynchonmodelsplanner),)\n    * with properties: (5 total)\n      *  [`changes`](/src/pynchon/plugins/python/api.py#L27) -> inspect._empty\n      *  [`config`](/src/pynchon/plugins/python/api.py#L92) -> inspect._empty\n      *  [`logger`](/src/pynchon/plugins/python/api.py#L37) -> inspect._empty\n      *  [`plugin_config`](/src/pynchon/plugins/python/api.py#L64) -> inspect._empty\n      *  [`siblings`](/src/pynchon/plugins/python/api.py#L69) -> inspect._empty', '-------------------------------------------------------------------------------\n### pynchon.plugins.python.ast\n* Overview:  [source code](/src/pynchon/plugins/python/ast.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)', "-------------------------------------------------------------------------------\n### pynchon.util\n* Overview:  [source code](/src/pynchon/util/__init__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)\n* Classes: (0 total)\n* Functions: (4 total)\n  * [`pynchon.util.click_recursive_help`](/src/pynchon/util/__init__.py#L47-L71)\n    * with signature `(cmd, parent=None, out={}, file=<_io.TextIOWrapper name='<stdout>' mode='w' encoding='utf-8'>)`\n  * [`pynchon.util.find_src_root`](/src/pynchon/util/__init__.py#L36-L44) with signature `(config: dict) -> str`\n  * [`pynchon.util.get_root`](/src/pynchon/util/__init__.py#L12-L24) with signature `(path: str = '.') -> str`\n  * [`pynchon.util.is_python_project`](/src/pynchon/util/__init__.py#L27-L33) with signature `() -> bool`", '-------------------------------------------------------------------------------\n### pynchon.util.testing\n* Overview:  [source code](/src/pynchon/util/testing.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)\n* Functions: (1 total)\n  * [`pynchon.util.testing.get_test_info`](/src/pynchon/util/testing.py#L9-L17) with signature `(fname: str) -> dict`', "-------------------------------------------------------------------------------\n### pynchon.util.python\n* Overview:  [source code](/src/pynchon/util/python.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)\n* Functions: (3 total)\n  * [`pynchon.util.python.is_package`](/src/pynchon/util/python.py#L8-L18) with signature `(folder: str) -> bool`\n  * [`pynchon.util.python.load_entrypoints`](/src/pynchon/util/python.py#L29-L57) with signature `(config=None) -> dict`\n  * [`pynchon.util.python.load_setupcfg`](/src/pynchon/util/python.py#L21-L26) with signature `(file: str = '', folder: str = '')`", "-------------------------------------------------------------------------------\n### pynchon.util.tagging\n* Overview:  [source code](/src/pynchon/util/tagging.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)\n* Classes: (1 total)\n  * [`pynchon.util.tagging.tagsM`](/src/pynchon/util/tagging.py#L87-L109)\n    * with bases ([`__builtin__.object`](https://docs.python.org/3/library/functions.html#object),)\n* Functions: (2 total)\n  * [`pynchon.util.tagging.tag_factory`](/src/pynchon/util/tagging.py#L41-L60) with signature `(*args) -> 'typing.Any'`\n  * [`pynchon.util.tagging.tagged_property`](/src/pynchon/util/tagging.py#L21-L38) with signature `(**ftags)`", "-------------------------------------------------------------------------------\n### pynchon.util.click\n* Overview:  [source code](/src/pynchon/util/click.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)\n* Functions: (1 total)\n  * [`pynchon.util.click.click_recursive_help`](/src/pynchon/util/click.py#L8-L31)\n    * with signature `(cmd, parent=None, out={}, file=<_io.TextIOWrapper name='<stdout>' mode='w' encoding='utf-8'>)`", '-------------------------------------------------------------------------------\n### pynchon.util.config\n* Overview:  [source code](/src/pynchon/util/config.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)'], stats={}, module=None, template=None, visited=[], exclude: list = [], module_name=None, working_dir=Path('.'))`
-------------------------------------------------------------------------------
### pynchon.util.typing
* Overview:  [source code](/src/pynchon/util/typing.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Functions: (1 total)
  * [`pynchon.util.typing.validate`](/src/pynchon/util/typing.py#L28-L29)
    * with signature `(func: Union[ForwardRef('AnyCallableT'), NoneType] = None, *, config: 'ConfigType' = None) -> Any`
-------------------------------------------------------------------------------
### pynchon.util.grip
* Overview:  [source code](/src/pynchon/util/grip.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Functions: (6 total)
  * [`pynchon.util.grip._current_grip_procs`](/src/pynchon/util/grip.py#L24-L26) with signature ``
  * [`pynchon.util.grip._is_my_grip`](/src/pynchon/util/grip.py#L38-L40) with signature ``
  * [`pynchon.util.grip.port`](/src/pynchon/util/grip.py#L13-L16) with signature `(conn=None)`
  * [`pynchon.util.grip.serve`](/src/pynchon/util/grip.py#L43-L69)
    * with signature `(background: bool = True, force: bool = False, logfile: str = '.tmp.grip.log') -> object`
  * [`pynchon.util.grip.server`](/src/pynchon/util/grip.py#L29-L35) with signature `() -> psutil.Process`
  * [`pynchon.util.grip.serving`](/src/pynchon/util/grip.py#L19-L21) with signature `()`
-------------------------------------------------------------------------------
### pynchon.util.lme
* Overview:  [source code](/src/pynchon/util/lme.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Functions: (2 total)
  * [`pynchon.util.lme.get_logger`](/src/pynchon/util/lme.py#L54-L85) with signature `(name, console=<console width=115 ColorSystem.TRUECOLOR>)`
  * [`pynchon.util.lme.set_global_level`](/src/pynchon/util/lme.py#L41-L48) with signature `(level)`
-------------------------------------------------------------------------------
### pynchon.util.oop
* Overview:  [source code](/src/pynchon/util/oop.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (2 total)
  * [`pynchon.util.oop.classproperty`](/src/pynchon/util/oop.py#L21-L28)
    * with bases ([`__builtin__.object`](https://docs.python.org/3/library/functions.html#object),)
  * [`pynchon.util.oop.classproperty_cached`](/src/pynchon/util/oop.py#L31-L39)
    * with bases ([classproperty](#pynchonutiloop),)
* Functions: (2 total)
  * [`pynchon.util.oop.is_subclass`](/src/pynchon/util/oop.py#L12-L18) with signature `(x, y, strict=True)`
  * [`pynchon.util.oop.new_in_class`](/src/pynchon/util/oop.py#L6-L9) with signature `(name: str, kls: Type)`
-------------------------------------------------------------------------------
### pynchon.util.events
* Overview:  [source code](/src/pynchon/util/events.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (1 total)
  * [`pynchon.util.events.Engine`](/src/pynchon/util/events.py#L12-L20)
    * with bases ([`__builtin__.object`](https://docs.python.org/3/library/functions.html#object),)
-------------------------------------------------------------------------------
### pynchon.util.os
* Overview:  [source code](/src/pynchon/util/os/__init__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (0 total)
* Functions: (2 total)
  * [`pynchon.util.os.filter_pids`](/src/pynchon/util/os/__init__.py#L6-L21) with signature `(**kwargs)`
  * [`pynchon.util.os.invoke`](/src/pynchon/util/os/__init__.py#L24-L32) with signature `(cmd: str, **kwargs)`
-------------------------------------------------------------------------------
### pynchon.util.os.models
* Overview:  [source code](/src/pynchon/util/os/models.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (2 total)
  * [`pynchon.util.os.models.Invocation`](/src/pynchon/util/os/models.py#L13-L102)
    * with bases ([`__builtin__.tuple`](https://docs.python.org/3/library/functions.html#tuple),)
  * [`pynchon.util.os.models.InvocationResult`](/src/pynchon/util/os/models.py#L105-L144)
    * with bases ([`__builtin__.tuple`](https://docs.python.org/3/library/functions.html#tuple),)
-------------------------------------------------------------------------------
### pynchon.util.os.pidfile
* Overview:  [source code](/src/pynchon/util/os/pidfile.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
-------------------------------------------------------------------------------
### pynchon.util.console
* Overview:  [source code](/src/pynchon/util/console/__init__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (0 total)
-------------------------------------------------------------------------------
### pynchon.util.console.__main__
* Overview: (entrypoint) | [source code](/src/pynchon/util/console/__main__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
-------------------------------------------------------------------------------
### pynchon.util.text
* Overview:  [source code](/src/pynchon/util/text/__init__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (0 total)
* Functions: (2 total)
  * [`pynchon.util.text.indent`](/src/pynchon/util/text/__init__.py#L28-L36) with signature `(txt: str, level: int = 2) -> str`
  * [`pynchon.util.text.to_json`](/src/pynchon/util/text/__init__.py#L20-L22)
    * with signature `(obj, cls=<class 'pynchon.abcs.path.JSONEncoder'>, indent: int = 2) -> str`
-------------------------------------------------------------------------------
### pynchon.util.text.loads
* Overview:  [source code](/src/pynchon/util/text/loads.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Functions: (5 total)
  * [`pynchon.util.text.loads.ini`](/src/pynchon/util/text/loads.py#L14-L18) with signature `(content: str) -> Union[str, NoneType]`
  * [`pynchon.util.text.loads.json`](/src/pynchon/util/text/loads.py#L35-L41) with signature `(content: str = '') -> Union[str, NoneType]`
  * [`pynchon.util.text.loads.json5`](/src/pynchon/util/text/loads.py#L44-L64) with signature `(content: str = '', quiet=True) -> Union[str, NoneType]`
  * [`pynchon.util.text.loads.toml`](/src/pynchon/util/text/loads.py#L28-L32) with signature `(content: str) -> Union[str, NoneType]`
  * [`pynchon.util.text.loads.yaml`](/src/pynchon/util/text/loads.py#L21-L25) with signature `(content: str) -> Union[str, NoneType]`
-------------------------------------------------------------------------------
### pynchon.util.text.__main__
* Overview: (entrypoint) | [source code](/src/pynchon/util/text/__main__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
-------------------------------------------------------------------------------
### pynchon.util.text.normalize
* Overview:  [source code](/src/pynchon/util/text/normalize/__init__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (0 total)
* Functions: (2 total)
  * [`pynchon.util.text.normalize.normalize`](/src/pynchon/util/text/normalize/__init__.py#L17-L33)
    * with signature `(txt: str = '', post: List[Callable] = [<function <lambda> at 0x7f8a5a86cee0>, <function <lambda> at 0x7f8a5a86cf70>], rules: List[Callable] = {' ': '_', '/': '_', '-': '_'}) -> str`
  * [`pynchon.util.text.normalize.snake_case`](/src/pynchon/util/text/normalize/__init__.py#L8-L11) with signature `(name: str) -> str`
-------------------------------------------------------------------------------
### pynchon.util.text.normalize.__main__
* Overview: (entrypoint) | [source code](/src/pynchon/util/text/normalize/__main__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
-------------------------------------------------------------------------------
### pynchon.util.text.loadf
* Overview:  [source code](/src/pynchon/util/text/loadf/__init__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (0 total)
* Functions: (5 total)
  * [`pynchon.util.text.loadf.ini`](/src/pynchon/util/text/loadf/__init__.py#L20-L28) with signature `(file)`
  * [`pynchon.util.text.loadf.json`](/src/pynchon/util/text/loadf/__init__.py#L173-L192) with signature `(file: str = '', content: str = '', strict: bool = True) -> dict`
  * [`pynchon.util.text.loadf.json5`](/src/pynchon/util/text/loadf/__init__.py#L71-L170)
    * with signature `(output: str = '', should_print: bool = False, file: str = '', files: List[str] = [], wrapper_key: str = '', pull: str = '', push_data: str = '', push_file_data: str = '', push_json_data: str = '', push_command_output: str = '', under_key: str = '') -> None`
    * with admonitions:  [🐉 Complex](/src/pynchon/util/text/loadf/__init__.py#L28 "score 12 / 7") 
  * [`pynchon.util.text.loadf.toml`](/src/pynchon/util/text/loadf/__init__.py#L36-L54) with signature `(file: str = None, strict: bool = True)`
  * [`pynchon.util.text.loadf.yaml`](/src/pynchon/util/text/loadf/__init__.py#L31-L33) with signature `(*args, **kwargs)`
-------------------------------------------------------------------------------
### pynchon.util.text.loadf.__main__
* Overview: (entrypoint) | [source code](/src/pynchon/util/text/loadf/__main__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
-------------------------------------------------------------------------------
### pynchon.util.text.render
* Overview:  [source code](/src/pynchon/util/text/render/__init__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (0 total)
* Functions: (4 total)
  * [`pynchon.util.text.render.j2cli`](/src/pynchon/util/text/render/__init__.py#L140-L172)
    * with signature `(output: str, should_print: bool, file: str, context: str, format: str = 'json') -> None`
  * [`pynchon.util.text.render.jinja`](/src/pynchon/util/text/render/__init__.py#L41-L72)
    * with signature `(text: str = '', context: dict = {}, includes: List[str] = [], strict: bool = True)`
  * [`pynchon.util.text.render.jinja_file`](/src/pynchon/util/text/render/__init__.py#L75-L137)
    * with signature `(file: str, output: Union[str, NoneType] = '', should_print: bool = False, in_place: bool = False, context: Dict = {}, context_file: Dict = {}, includes: List[str] = [], strict: bool = True) -> str`
  * [`pynchon.util.text.render.jinja_loadf`](/src/pynchon/util/text/render/__init__.py#L20-L38)
    * with signature `(file: str, context: Dict = {}, includes: List[str] = [], strict: bool = True, quiet: bool = False) -> str`
-------------------------------------------------------------------------------
### pynchon.util.text.render.__main__
* Overview: (entrypoint) | [source code](/src/pynchon/util/text/render/__main__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
-------------------------------------------------------------------------------
### pynchon.util.shfmt
* Overview:  [source code](/src/pynchon/util/shfmt/__init__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (1 total)
  * [`pynchon.util.shfmt.Semantics`](/src/pynchon/util/shfmt/__init__.py#L9-L95)
    * with bases ([`__builtin__.object`](https://docs.python.org/3/library/functions.html#object),)
* Classes: (1 total)
  * [`pynchon.util.shfmt.Semantics`](/src/pynchon/util/shfmt/__init__.py#L9-L95)
    * with bases ([`__builtin__.object`](https://docs.python.org/3/library/functions.html#object),)
* Functions: (1 total)
  * [`pynchon.util.shfmt.fmt`](/src/pynchon/util/shfmt/__init__.py#L98-L109) with signature `(text, filename='?')`
-------------------------------------------------------------------------------
### pynchon.util.shfmt.__main__
* Overview: (entrypoint) | [source code](/src/pynchon/util/shfmt/__main__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Functions: (1 total)
  * [`pynchon.util.shfmt.__main__.entry`](/src/pynchon/util/shfmt/__main__.py#L13-L30) with signature `(*args: Any, **kwargs: Any) -> Any`
-------------------------------------------------------------------------------
### pynchon.util.shfmt.grammar
* Overview:  [source code](/src/pynchon/util/shfmt/grammar.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
-------------------------------------------------------------------------------
### pynchon.util.files
* Overview:  [source code](/src/pynchon/util/files/__init__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (0 total)
* Functions: (8 total)
  * [`pynchon.util.files.ansible_docker`](/src/pynchon/util/files/__init__.py#L109-L139)
    * with signature `(local: bool = True, volumes: dict = {}, container: str = 'alpinelinux/ansible', entrypoint: str = 'ansible', e: dict = {}, module_name: str = None, extra: List[str] = []) -> List[str]`
  * [`pynchon.util.files.block_in_file`](/src/pynchon/util/files/__init__.py#L152-L196)
    * with signature `(target_file: str, block_file: str, create: str = 'no', insertbefore: str = 'BOF', backup: str = 'yes', marker: str = '# {mark} ANSIBLE MANAGED BLOCK - pynchon', dest='.tmp.ansible.blockinfile.out')`
  * [`pynchon.util.files.dumps`](/src/pynchon/util/files/__init__.py#L142-L149)
    * with signature `(content: str = None, file: str = None, quiet: bool = True, logger=<bound method Logger.info of <Logger pynchon.util.files (INFO)>>)`
  * [`pynchon.util.files.find_globs`](/src/pynchon/util/files/__init__.py#L85-L106)
    * with signature `(globs: List[pynchon.abcs.path.Path], includes=[], logger: object = None, quiet: bool = False) -> List[str]`
  * [`pynchon.util.files.find_src`](/src/pynchon/util/files/__init__.py#L64-L82) with signature `(src_root: str, exclude_patterns=[], quiet: bool = False) -> list`
  * [`pynchon.util.files.find_suffix`](/src/pynchon/util/files/__init__.py#L43-L46) with signature `(root: str = '', suffix: str = '') -> Union[str, NoneType]`
  * [`pynchon.util.files.get_git_root`](/src/pynchon/util/files/__init__.py#L49-L61) with signature `(path: str = '.') -> Union[str, NoneType]`
  * [`pynchon.util.files.prepend`](/src/pynchon/util/files/__init__.py#L16-L40)
    * with signature `(prepend_file: str = None, target_file: str = None, clean: bool = False)`
-------------------------------------------------------------------------------
### pynchon.util.files.diff
* Overview:  [source code](/src/pynchon/util/files/diff.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Functions: (3 total)
  * [`pynchon.util.files.diff.diff`](/src/pynchon/util/files/diff.py#L41-L57) with signature `(file1: str = None, file2: str = None)`
  * [`pynchon.util.files.diff.diff_percent`](/src/pynchon/util/files/diff.py#L27-L38) with signature `(file1: str = None, file2: str = None)`
  * [`pynchon.util.files.diff.diff_report`](/src/pynchon/util/files/diff.py#L12-L24)
    * with signature `(diff, logger=<bound method Logger.debug of <Logger pynchon.util.files.diff (INFO)>>)`
-------------------------------------------------------------------------------
### pynchon.util.files.__main__
* Overview: (entrypoint) | [source code](/src/pynchon/util/files/__main__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
-------------------------------------------------------------------------------
### pynchon.config
* Overview:  [source code](/src/pynchon/config/__init__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (0 total)
-------------------------------------------------------------------------------
### pynchon.config.util
* Overview:  [source code](/src/pynchon/config/util.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Functions: (4 total)
  * [`pynchon.config.util.config_folders`](/src/pynchon/config/util.py#L98-L102) with signature `()`
  * [`pynchon.config.util.finalize`](/src/pynchon/config/util.py#L16-L74) with signature `()`
  * [`pynchon.config.util.get_config_files`](/src/pynchon/config/util.py#L77-L95) with signature `()`
  * [`pynchon.config.util.load_config_from_files`](/src/pynchon/config/util.py#L105-L125) with signature `() -> Dict[str, str]`
-------------------------------------------------------------------------------
### pynchon.cli
* Overview:  [source code](/src/pynchon/cli/__init__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (0 total)
-------------------------------------------------------------------------------
### pynchon.cli.options
* Overview:  [source code](/src/pynchon/cli/options.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
-------------------------------------------------------------------------------
### pynchon.cli.click
* Overview:  [source code](/src/pynchon/cli/click.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Functions: (2 total)
  * [`pynchon.cli.click.group_merge`](/src/pynchon/cli/click.py#L37-L46) with signature `(g1: click.core.Group, g2: click.core.Group)`
  * [`pynchon.cli.click.walk_group`](/src/pynchon/cli/click.py#L21-L34) with signature `(parent, path='', tree={})`
-------------------------------------------------------------------------------
### pynchon.cli.common
* Overview:  [source code](/src/pynchon/cli/common.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (6 total)
  * [`pynchon.cli.common.handler`](/src/pynchon/cli/common.py#L37-L52)
    * with bases ([`__builtin__.object`](https://docs.python.org/3/library/functions.html#object),)
  * [`pynchon.cli.common.stdout_handler`](/src/pynchon/cli/common.py#L55-L66)
    * with bases ([handler](#pynchonclicommon),)
  * [`pynchon.cli.common.output_handler`](/src/pynchon/cli/common.py#L69-L87)
    * with bases ([handler](#pynchonclicommon),)
  * [`pynchon.cli.common.format_handler`](/src/pynchon/cli/common.py#L90-L119)
    * with bases ([handler](#pynchonclicommon),)
  * [`pynchon.cli.common.kommand`](/src/pynchon/cli/common.py#L143-L229)
    * with bases ([`__builtin__.object`](https://docs.python.org/3/library/functions.html#object),)
  * [`pynchon.cli.common.groop`](/src/pynchon/cli/common.py#L232-L247)
    * with bases ([kommand](#pynchonclicommon),)
* Functions: (2 total)
  * [`pynchon.cli.common.entry_for`](/src/pynchon/cli/common.py#L122-L140) with signature `(name)`
  * [`pynchon.cli.common.load_groups_from_children`](/src/pynchon/cli/common.py#L18-L34) with signature `(root=None, parent=None)`
-------------------------------------------------------------------------------
### pynchon.cli.arguments
* Overview:  [source code](/src/pynchon/cli/arguments.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
-------------------------------------------------------------------------------
### pynchon.models
* Overview:  [source code](/src/pynchon/models/__init__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (0 total)
-------------------------------------------------------------------------------
### pynchon.models.planner
* Overview:  [source code](/src/pynchon/models/planner.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (4 total)
  * [`pynchon.models.planner.AbstractPlanner`](/src/pynchon/models/planner.py#L19-L108)
    * with bases ([BasePlugin](#pynchonmodelsplugin_types),)
    * with properties: (5 total)
      *  [`changes`](/src/pynchon/models/planner.py#L27) -> inspect._empty
      *  [`config`](/src/pynchon/models/planner.py#L92) -> inspect._empty
      *  [`logger`](/src/pynchon/models/planner.py#L37) -> inspect._empty
      *  [`plugin_config`](/src/pynchon/models/planner.py#L64) -> inspect._empty
      *  [`siblings`](/src/pynchon/models/planner.py#L69) -> inspect._empty
  * [`pynchon.models.planner.ShyPlanner`](/src/pynchon/models/planner.py#L111-L118)
    * with bases ([AbstractPlanner](#pynchonmodelsplanner),)
    * with properties: (5 total)
      *  [`changes`](/src/pynchon/models/planner.py#L27) -> inspect._empty
      *  [`config`](/src/pynchon/models/planner.py#L92) -> inspect._empty
      *  [`logger`](/src/pynchon/models/planner.py#L37) -> inspect._empty
      *  [`plugin_config`](/src/pynchon/models/planner.py#L64) -> inspect._empty
      *  [`siblings`](/src/pynchon/models/planner.py#L69) -> inspect._empty
  * [`pynchon.models.planner.Manager`](/src/pynchon/models/planner.py#L121-L123)
    * with bases ([ShyPlanner](#pynchonmodelsplanner),)
    * with properties: (5 total)
      *  [`changes`](/src/pynchon/models/planner.py#L27) -> inspect._empty
      *  [`config`](/src/pynchon/models/planner.py#L92) -> inspect._empty
      *  [`logger`](/src/pynchon/models/planner.py#L37) -> inspect._empty
      *  [`plugin_config`](/src/pynchon/models/planner.py#L64) -> inspect._empty
      *  [`siblings`](/src/pynchon/models/planner.py#L69) -> inspect._empty
  * [`pynchon.models.planner.Planner`](/src/pynchon/models/planner.py#L126-L132)
    * with bases ([ShyPlanner](#pynchonmodelsplanner),)
    * with properties: (5 total)
      *  [`changes`](/src/pynchon/models/planner.py#L27) -> inspect._empty
      *  [`config`](/src/pynchon/models/planner.py#L92) -> inspect._empty
      *  [`logger`](/src/pynchon/models/planner.py#L37) -> inspect._empty
      *  [`plugin_config`](/src/pynchon/models/planner.py#L64) -> inspect._empty
      *  [`siblings`](/src/pynchon/models/planner.py#L69) -> inspect._empty
-------------------------------------------------------------------------------
### pynchon.models.planning
* Overview:  [source code](/src/pynchon/models/planning.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (4 total)
  * [`pynchon.models.planning.Goal`](/src/pynchon/models/planning.py#L15-L46)
    * with bases ([`__builtin__.tuple`](https://docs.python.org/3/library/functions.html#tuple),)
  * [`pynchon.models.planning.Action`](/src/pynchon/models/planning.py#L49-L58)
    * with bases ([`__builtin__.tuple`](https://docs.python.org/3/library/functions.html#tuple),)
  * [`pynchon.models.planning.Plan`](/src/pynchon/models/planning.py#L61-L140)
    * with bases ([`__builtin__.list`](https://docs.python.org/3/library/functions.html#list),[Generic](#typing),)
  * [`pynchon.models.planning.ApplyResults`](/src/pynchon/models/planning.py#L143-L162)
    * with bases ([`__builtin__.list`](https://docs.python.org/3/library/functions.html#list),[Generic](#typing),)
-------------------------------------------------------------------------------
### pynchon.models.plugin_types
* Overview:  [source code](/src/pynchon/models/plugin_types/__init__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (6 total)
  * [`pynchon.models.plugin_types.PynchonPlugin`](/src/pynchon/models/plugin_types/__init__.py#L24-L137)
    * with bases ([Plugin](#pynchonfleksplugin),)
    * with admonitions:  [🐉 Complex](/src/pynchon/models/plugin_types/__init__.py#L89 "score 10 / 7") 
    * with properties: (4 total)
      *  [`config`](/src/pynchon/models/plugin_types/__init__.py#L92) -> inspect._empty
      *  [`logger`](/src/pynchon/models/plugin_types/__init__.py#L37) -> inspect._empty
      *  [`plugin_config`](/src/pynchon/models/plugin_types/__init__.py#L64) -> inspect._empty
      *  [`siblings`](/src/pynchon/models/plugin_types/__init__.py#L69) -> inspect._empty
  * [`pynchon.models.plugin_types.CliPlugin`](/src/pynchon/models/plugin_types/__init__.py#L140-L326)
    * with bases ([PynchonPlugin](#pynchonmodelsplugin_types),)
    * with admonitions:  [🐉 Complex](/src/pynchon/models/plugin_types/__init__.py#L54 "score 13 / 7") 
    * with properties: (4 total)
      *  [`config`](/src/pynchon/models/plugin_types/__init__.py#L92) -> inspect._empty
      *  [`logger`](/src/pynchon/models/plugin_types/__init__.py#L37) -> inspect._empty
      *  [`plugin_config`](/src/pynchon/models/plugin_types/__init__.py#L64) -> inspect._empty
      *  [`siblings`](/src/pynchon/models/plugin_types/__init__.py#L69) -> inspect._empty
  * [`pynchon.models.plugin_types.Provider`](/src/pynchon/models/plugin_types/__init__.py#L329-L342)
    * with bases ([CliPlugin](#pynchonmodelsplugin_types),)
    * with properties: (4 total)
      *  [`config`](/src/pynchon/models/plugin_types/__init__.py#L92) -> inspect._empty
      *  [`logger`](/src/pynchon/models/plugin_types/__init__.py#L37) -> inspect._empty
      *  [`plugin_config`](/src/pynchon/models/plugin_types/__init__.py#L64) -> inspect._empty
      *  [`siblings`](/src/pynchon/models/plugin_types/__init__.py#L69) -> inspect._empty
  * [`pynchon.models.plugin_types.ToolPlugin`](/src/pynchon/models/plugin_types/__init__.py#L345-L357)
    * with bases ([CliPlugin](#pynchonmodelsplugin_types),)
    * with properties: (4 total)
      *  [`config`](/src/pynchon/models/plugin_types/__init__.py#L92) -> inspect._empty
      *  [`logger`](/src/pynchon/models/plugin_types/__init__.py#L37) -> inspect._empty
      *  [`plugin_config`](/src/pynchon/models/plugin_types/__init__.py#L64) -> inspect._empty
      *  [`siblings`](/src/pynchon/models/plugin_types/__init__.py#L69) -> inspect._empty
  * [`pynchon.models.plugin_types.BasePlugin`](/src/pynchon/models/plugin_types/__init__.py#L360-L365)
    * with bases ([CliPlugin](#pynchonmodelsplugin_types),)
    * with properties: (4 total)
      *  [`config`](/src/pynchon/models/plugin_types/__init__.py#L92) -> inspect._empty
      *  [`logger`](/src/pynchon/models/plugin_types/__init__.py#L37) -> inspect._empty
      *  [`plugin_config`](/src/pynchon/models/plugin_types/__init__.py#L64) -> inspect._empty
      *  [`siblings`](/src/pynchon/models/plugin_types/__init__.py#L69) -> inspect._empty
  * [`pynchon.models.plugin_types.NameSpace`](/src/pynchon/models/plugin_types/__init__.py#L368-L377)
    * with bases ([CliPlugin](#pynchonmodelsplugin_types),)
    * with properties: (4 total)
      *  [`config`](/src/pynchon/models/plugin_types/__init__.py#L92) -> inspect._empty
      *  [`logger`](/src/pynchon/models/plugin_types/__init__.py#L37) -> inspect._empty
      *  [`plugin_config`](/src/pynchon/models/plugin_types/__init__.py#L64) -> inspect._empty
      *  [`siblings`](/src/pynchon/models/plugin_types/__init__.py#L69) -> inspect._empty
* Classes: (6 total)
  * [`pynchon.models.plugin_types.PynchonPlugin`](/src/pynchon/models/plugin_types/__init__.py#L24-L137)
    * with bases ([Plugin](#pynchonfleksplugin),)
    * with admonitions:  [🐉 Complex](/src/pynchon/models/plugin_types/__init__.py#L89 "score 10 / 7") 
    * with properties: (4 total)
      *  [`config`](/src/pynchon/models/plugin_types/__init__.py#L92) -> inspect._empty
      *  [`logger`](/src/pynchon/models/plugin_types/__init__.py#L37) -> inspect._empty
      *  [`plugin_config`](/src/pynchon/models/plugin_types/__init__.py#L64) -> inspect._empty
      *  [`siblings`](/src/pynchon/models/plugin_types/__init__.py#L69) -> inspect._empty
  * [`pynchon.models.plugin_types.CliPlugin`](/src/pynchon/models/plugin_types/__init__.py#L140-L326)
    * with bases ([PynchonPlugin](#pynchonmodelsplugin_types),)
    * with admonitions:  [🐉 Complex](/src/pynchon/models/plugin_types/__init__.py#L54 "score 13 / 7") 
    * with properties: (4 total)
      *  [`config`](/src/pynchon/models/plugin_types/__init__.py#L92) -> inspect._empty
      *  [`logger`](/src/pynchon/models/plugin_types/__init__.py#L37) -> inspect._empty
      *  [`plugin_config`](/src/pynchon/models/plugin_types/__init__.py#L64) -> inspect._empty
      *  [`siblings`](/src/pynchon/models/plugin_types/__init__.py#L69) -> inspect._empty
  * [`pynchon.models.plugin_types.Provider`](/src/pynchon/models/plugin_types/__init__.py#L329-L342)
    * with bases ([CliPlugin](#pynchonmodelsplugin_types),)
    * with properties: (4 total)
      *  [`config`](/src/pynchon/models/plugin_types/__init__.py#L92) -> inspect._empty
      *  [`logger`](/src/pynchon/models/plugin_types/__init__.py#L37) -> inspect._empty
      *  [`plugin_config`](/src/pynchon/models/plugin_types/__init__.py#L64) -> inspect._empty
      *  [`siblings`](/src/pynchon/models/plugin_types/__init__.py#L69) -> inspect._empty
  * [`pynchon.models.plugin_types.ToolPlugin`](/src/pynchon/models/plugin_types/__init__.py#L345-L357)
    * with bases ([CliPlugin](#pynchonmodelsplugin_types),)
    * with properties: (4 total)
      *  [`config`](/src/pynchon/models/plugin_types/__init__.py#L92) -> inspect._empty
      *  [`logger`](/src/pynchon/models/plugin_types/__init__.py#L37) -> inspect._empty
      *  [`plugin_config`](/src/pynchon/models/plugin_types/__init__.py#L64) -> inspect._empty
      *  [`siblings`](/src/pynchon/models/plugin_types/__init__.py#L69) -> inspect._empty
  * [`pynchon.models.plugin_types.BasePlugin`](/src/pynchon/models/plugin_types/__init__.py#L360-L365)
    * with bases ([CliPlugin](#pynchonmodelsplugin_types),)
    * with properties: (4 total)
      *  [`config`](/src/pynchon/models/plugin_types/__init__.py#L92) -> inspect._empty
      *  [`logger`](/src/pynchon/models/plugin_types/__init__.py#L37) -> inspect._empty
      *  [`plugin_config`](/src/pynchon/models/plugin_types/__init__.py#L64) -> inspect._empty
      *  [`siblings`](/src/pynchon/models/plugin_types/__init__.py#L69) -> inspect._empty
  * [`pynchon.models.plugin_types.NameSpace`](/src/pynchon/models/plugin_types/__init__.py#L368-L377)
    * with bases ([CliPlugin](#pynchonmodelsplugin_types),)
    * with properties: (4 total)
      *  [`config`](/src/pynchon/models/plugin_types/__init__.py#L92) -> inspect._empty
      *  [`logger`](/src/pynchon/models/plugin_types/__init__.py#L37) -> inspect._empty
      *  [`plugin_config`](/src/pynchon/models/plugin_types/__init__.py#L64) -> inspect._empty
      *  [`siblings`](/src/pynchon/models/plugin_types/__init__.py#L69) -> inspect._empty
-------------------------------------------------------------------------------
### pynchon.models.plugin_types.validators
* Overview:  [source code](/src/pynchon/models/plugin_types/validators.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Functions: (2 total)
  * [`pynchon.models.plugin_types.validators.require_conf_key`](/src/pynchon/models/plugin_types/validators.py#L14-L23) with signature `(kls, strict=True, **vdata)`
  * [`pynchon.models.plugin_types.validators.warn_config_kls`](/src/pynchon/models/plugin_types/validators.py#L26-L31) with signature `(kls, warnings=defaultdict(<class 'list'>, {}), **vdata)`
-------------------------------------------------------------------------------
### pynchon.models.plugin_types.base
* Overview:  [source code](/src/pynchon/models/plugin_types/base.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
-------------------------------------------------------------------------------
### pynchon.abcs
* Overview:  [source code](/src/pynchon/abcs/__init__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (0 total)
-------------------------------------------------------------------------------
### pynchon.abcs.config
* Overview:  [source code](/src/pynchon/abcs/config.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (1 total)
  * [`pynchon.abcs.config.Config`](/src/pynchon/abcs/config.py#L10-L82)
    * with bases ([`__builtin__.dict`](https://docs.python.org/3/library/functions.html#dict),)
-------------------------------------------------------------------------------
### pynchon.abcs.attrdict
* Overview:  [source code](/src/pynchon/abcs/attrdict.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (2 total)
  * [`pynchon.abcs.attrdict.AttrDictBase`](/src/pynchon/abcs/attrdict.py#L9-L48)
    * with bases ([`__builtin__.object`](https://docs.python.org/3/library/functions.html#object),)
  * [`pynchon.abcs.attrdict.AttrDict`](/src/pynchon/abcs/attrdict.py#L51-L52)
    * with bases ([AttrDictBase](#pynchonabcsattrdict),[`__builtin__.dict`](https://docs.python.org/3/library/functions.html#dict),)
-------------------------------------------------------------------------------
### pynchon.abcs.path
* Overview:  [source code](/src/pynchon/abcs/path.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (2 total)
  * [`pynchon.abcs.path.Path`](/src/pynchon/abcs/path.py#L13-L55)
    * with bases ([PosixPath](#pathlib),)
    * with properties: (10 total)
      *  [`anchor`](/src/pynchon/abcs/path.py#L798) -> inspect._empty
      *  [`drive`](/src/pynchon/abcs/path.py#L13) -> None
      *  [`name`](/src/pynchon/abcs/path.py#L804) -> inspect._empty
      *  [`parent`](/src/pynchon/abcs/path.py#L945) -> inspect._empty
      *  [`parents`](/src/pynchon/abcs/path.py#L955) -> inspect._empty
      *  [`parts`](/src/pynchon/abcs/path.py#L913) -> inspect._empty
      *  [`root`](/src/pynchon/abcs/path.py#L13) -> None
      *  [`stem`](/src/pynchon/abcs/path.py#L839) -> inspect._empty
      *  [`suffix`](/src/pynchon/abcs/path.py#L812) -> inspect._empty
      *  [`suffixes`](/src/pynchon/abcs/path.py#L826) -> inspect._empty
  * [`pynchon.abcs.path.JSONEncoder`](/src/pynchon/abcs/path.py#L58-L86)
    * with bases ([JSONEncoder](#jsonencoder),)
-------------------------------------------------------------------------------
### pynchon.abcs.visitor
* Overview:  [source code](/src/pynchon/abcs/visitor.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (3 total)
  * [`pynchon.abcs.visitor.Visitor`](/src/pynchon/abcs/visitor.py#L14-L47)
    * with bases ([`__builtin__.object`](https://docs.python.org/3/library/functions.html#object),)
  * [`pynchon.abcs.visitor.TemplatedDict`](/src/pynchon/abcs/visitor.py#L95-L123)
    * with bases ([`__builtin__.dict`](https://docs.python.org/3/library/functions.html#dict),)
    * with properties: (2 total)
      *  [`traversal`](/src/pynchon/abcs/visitor.py#L111) -> inspect._empty
      *  [`unresolved`](/src/pynchon/abcs/visitor.py#L120) -> inspect._empty
  * [`pynchon.abcs.visitor.JinjaDict`](/src/pynchon/abcs/visitor.py#L131-L176)
    * with bases ([TemplatedDict](#pynchonabcsvisitor),)
    * with properties: (2 total)
      *  [`traversal`](/src/pynchon/abcs/visitor.py#L111) -> inspect._empty
      *  [`unresolved`](/src/pynchon/abcs/visitor.py#L120) -> inspect._empty
* Functions: (1 total)
  * [`pynchon.abcs.visitor.traverse`](/src/pynchon/abcs/visitor.py#L50-L92) with signature `(obj, visitor=None, visitor_kls=None, visitor_kwargs={})`
    * with admonitions:  [🐉 Complex](/src/pynchon/abcs/visitor.py#L1 "score 10 / 7") 
-------------------------------------------------------------------------------
### pynchon.api
* Overview:  [source code](/src/pynchon/api/__init__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (0 total)
-------------------------------------------------------------------------------
### pynchon.api.render
* Overview:  [source code](/src/pynchon/api/render.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Functions: (5 total)
  * [`pynchon.api.render.dictionary`](/src/pynchon/api/render.py#L22-L26) with signature `(input, context)`
  * [`pynchon.api.render.get_jinja_env`](/src/pynchon/api/render.py#L62-L88) with signature `(*includes, quiet: bool = False)`
  * [`pynchon.api.render.get_jinja_globals`](/src/pynchon/api/render.py#L29-L51) with signature `()`
  * [`pynchon.api.render.get_jinja_includes`](/src/pynchon/api/render.py#L55-L59) with signature `(*includes)`
  * [`pynchon.api.render.get_template`](/src/pynchon/api/render.py#L90-L103) with signature `(template_name: str, env=None)`
-------------------------------------------------------------------------------
### pynchon.api.pynchon
* Overview:  [source code](/src/pynchon/api/pynchon.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
-------------------------------------------------------------------------------
### pynchon.api.project
* Overview:  [source code](/src/pynchon/api/project/__init__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Functions: (2 total)
  * [`pynchon.api.project.get_config`](/src/pynchon/api/project/__init__.py#L8-L12) with signature `() -> dict`
  * [`pynchon.api.project.plan`](/src/pynchon/api/project/__init__.py#L15-L42) with signature `(config: dict = {}) -> dict`
-------------------------------------------------------------------------------
### pynchon.api.git
* Overview:  [source code](/src/pynchon/api/git/__init__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
