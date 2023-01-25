## API for 'pynchon' package

---------------------------------------------------------------------------------------------------------------------------------------------------------------
### pynchon
* Overview:  [source code](/src/pynchon/__init__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (0 total)
* Functions: (1 total)
  * [`pynchon.get_logger`](/src/pynchon/__init__.py#L39-L64) with signature `(name)`
-------------------------------------------------------------------------------
### pynchon.config
* Overview:  [source code](/src/pynchon/config.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Functions: (2 total)
  * [`pynchon.config.detect_config`](/src/pynchon/config.py#L9-L10) with signature `() -> dict`
  * [`pynchon.config.read_config`](/src/pynchon/config.py#L5-L6) with signature `(file: str = '.pynchon_conf.json5') -> dict`
-------------------------------------------------------------------------------
### pynchon.util
* Overview:  [source code](/src/pynchon/util.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (1 total)
  * [`pynchon.util.Checker`](/src/pynchon/util.py#L279-L291)
    * with bases ([McCabeChecker](#mccabe),)
* Functions: (16 total)
  * [`pynchon.util.clean_text`](/src/pynchon/util.py#L274-L276) with signature `(txt: str) -> str`
  * [`pynchon.util.click_recursive_help`](/src/pynchon/util.py#L150-L174)
    * with signature `(cmd, parent=None, out={}, file=<_io.TextIOWrapper name='<stdout>' mode='w' encoding='utf-8'>)`
  * [`pynchon.util.complexity`](/src/pynchon/util.py#L294-L323) with signature `(code: str = None, fname: str = None, threshold: int = 7)`
  * [`pynchon.util.find_git_root`](/src/pynchon/util.py#L75-L83) with signature `(path: str = '.') -> str`
  * [`pynchon.util.find_src_root`](/src/pynchon/util.py#L92-L98) with signature `(config: dict) -> str`
  * [`pynchon.util.get_git_hash`](/src/pynchon/util.py#L86-L89) with signature `() -> str`
  * [`pynchon.util.get_module`](/src/pynchon/util.py#L177-L195) with signature `(package: str = '', file: str = '')`
  * [`pynchon.util.get_refs`](/src/pynchon/util.py#L198-L229) with signature `(working_dir=None, module=None) -> dict`
  * [`pynchon.util.invoke`](/src/pynchon/util.py#L329-L392)
    * with signature `(cmd=None, stdin='', interactive: bool = False, large_output: bool = False, log_command: bool = True, environment: dict = {}, log_stdin: bool = True, system: bool = False)`
  * [`pynchon.util.is_python_project`](/src/pynchon/util.py#L70-L72) with signature `() -> bool`
  * [`pynchon.util.load_entrypoints`](/src/pynchon/util.py#L119-L147) with signature `(config=None) -> dict`
  * [`pynchon.util.load_setupcfg`](/src/pynchon/util.py#L101-L116) with signature `(file: str = '')`
  * [`pynchon.util.project_config`](/src/pynchon/util.py#L25-L54) with signature `() -> dict`
  * [`pynchon.util.project_version`](/src/pynchon/util.py#L57-L60) with signature `() -> str`
  * [`pynchon.util.pynchon_version`](/src/pynchon/util.py#L63-L67) with signature `() -> str`
  * [`pynchon.util.visit_module`](/src/pynchon/util.py#L232-L271)
    * with signature `(output=['-------------------------------------------------------------------------------\n### pynchon\n* Overview:  [source code](/src/pynchon/__init__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)\n* Classes: (0 total)\n* Functions: (1 total)\n  * [`pynchon.get_logger`](/src/pynchon/__init__.py#L39-L64) with signature `(name)`', "-------------------------------------------------------------------------------\n### pynchon.config\n* Overview:  [source code](/src/pynchon/config.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)\n* Functions: (2 total)\n  * [`pynchon.config.detect_config`](/src/pynchon/config.py#L9-L10) with signature `() -> dict`\n  * [`pynchon.config.read_config`](/src/pynchon/config.py#L5-L6) with signature `(file: str = '.pynchon_conf.json5') -> dict`"], stats={}, module=None, template=<Template 'api/TOC.md.j2'>, visited=[], exclude: list = [], module_name=None, working_dir='/Users/mattanderson-admin/code/elo/pynchon')`
-------------------------------------------------------------------------------
### pynchon.annotate
* Overview:  [source code](/src/pynchon/annotate.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Functions: (3 total)
  * [`pynchon.annotate.function`](/src/pynchon/annotate.py#L80-L120) with signature `(name, fxn) -> None`
  * [`pynchon.annotate.klass`](/src/pynchon/annotate.py#L12-L71) with signature `(name, kls) -> None`
    * with admonitions:  [🐉 Complex](/src/pynchon/annotate.py#L1 "score 8 / 7") 
  * [`pynchon.annotate.module`](/src/pynchon/annotate.py#L74-L77) with signature `(name, module, working_dir=None) -> None`
-------------------------------------------------------------------------------
### pynchon.__main__
* Overview: (entrypoint) | [source code](/src/pynchon/__main__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
-------------------------------------------------------------------------------
### pynchon.bin
* Overview:  [source code](/src/pynchon/bin/__init__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (0 total)
-------------------------------------------------------------------------------
### pynchon.bin.api
* Overview:  [source code](/src/pynchon/bin/api.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Functions: (2 total)
  * [`pynchon.bin.api.markdown`](/src/pynchon/bin/api.py#L14-L15) with signature `(**result)`
  * [`pynchon.bin.api.toc`](/src/pynchon/bin/api.py#L18-L54) with signature `(*args: Any, **kwargs: Any) -> Any`
-------------------------------------------------------------------------------
### pynchon.bin.cli
* Overview:  [source code](/src/pynchon/bin/cli.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Functions: (5 total)
  * [`pynchon.bin.cli._all`](/src/pynchon/bin/cli.py#L46-L83) with signature `(*args: Any, **kwargs: Any) -> Any`
  * [`pynchon.bin.cli._entrypoint_docs`](/src/pynchon/bin/cli.py#L136-L157) with signature `(module=None, name=None)`
  * [`pynchon.bin.cli.entrypoint_docs`](/src/pynchon/bin/cli.py#L114-L133) with signature `(*args: Any, **kwargs: Any) -> Any`
  * [`pynchon.bin.cli.main_docs`](/src/pynchon/bin/cli.py#L85-L112) with signature `(*args: Any, **kwargs: Any) -> Any`
  * [`pynchon.bin.cli.toc`](/src/pynchon/bin/cli.py#L20-L43) with signature `(*args: Any, **kwargs: Any) -> Any`
-------------------------------------------------------------------------------
### pynchon.bin.project
* Overview:  [source code](/src/pynchon/bin/project.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Functions: (5 total)
  * [`pynchon.bin.project._project_plan`](/src/pynchon/bin/project.py#L76-L118) with signature `(config: dict = {}) -> dict`
  * [`pynchon.bin.project.project_apply`](/src/pynchon/bin/project.py#L61-L73) with signature `(*args: Any, **kwargs: Any) -> Any`
  * [`pynchon.bin.project.project_entrypoints`](/src/pynchon/bin/project.py#L16-L36) with signature `(*args: Any, **kwargs: Any) -> Any`
  * [`pynchon.bin.project.project_plan`](/src/pynchon/bin/project.py#L121-L134) with signature `(*args: Any, **kwargs: Any) -> Any`
  * [`pynchon.bin.project.project_version`](/src/pynchon/bin/project.py#L39-L58) with signature `(*args: Any, **kwargs: Any) -> Any`
-------------------------------------------------------------------------------
### pynchon.bin.render
* Overview:  [source code](/src/pynchon/bin/render.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Functions: (3 total)
  * [`pynchon.bin.render.render_any`](/src/pynchon/bin/render.py#L56-L73) with signature `(*args: Any, **kwargs: Any) -> Any`
  * [`pynchon.bin.render.render_j2`](/src/pynchon/bin/render.py#L76-L134) with signature `(*args: Any, **kwargs: Any) -> Any`
  * [`pynchon.bin.render.render_json5`](/src/pynchon/bin/render.py#L23-L53) with signature `(*args: Any, **kwargs: Any) -> Any`
-------------------------------------------------------------------------------
### pynchon.bin.parse
* Overview:  [source code](/src/pynchon/bin/parse.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Functions: (1 total)
  * [`pynchon.bin.parse.parse_pyright`](/src/pynchon/bin/parse.py#L16-L32) with signature `(*args: Any, **kwargs: Any) -> Any`
-------------------------------------------------------------------------------
### pynchon.bin.options
* Overview:  [source code](/src/pynchon/bin/options.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
-------------------------------------------------------------------------------
### pynchon.bin.groups
* Overview:  [source code](/src/pynchon/bin/groups.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (1 total)
  * [`pynchon.bin.groups.group`](/src/pynchon/bin/groups.py#L8-L27)
    * with bases ([`__builtin__.object`](https://docs.python.org/3/library/functions.html#func-object),)
* Functions: (8 total)
  * [`pynchon.bin.groups.ast`](/src/pynchon/bin/groups.py#L77-L79) with signature `(*args: Any, **kwargs: Any) -> Any`
  * [`pynchon.bin.groups.entry`](/src/pynchon/bin/groups.py#L30-L33) with signature `(*args: Any, **kwargs: Any) -> Any`
  * [`pynchon.bin.groups.gen`](/src/pynchon/bin/groups.py#L39-L41) with signature `(*args: Any, **kwargs: Any) -> Any`
  * [`pynchon.bin.groups.gen_api`](/src/pynchon/bin/groups.py#L55-L59) with signature `(*args: Any, **kwargs: Any) -> Any`
  * [`pynchon.bin.groups.gen_cli`](/src/pynchon/bin/groups.py#L62-L64) with signature `(*args: Any, **kwargs: Any) -> Any`
  * [`pynchon.bin.groups.parse`](/src/pynchon/bin/groups.py#L72-L74) with signature `(*args: Any, **kwargs: Any) -> Any`
  * [`pynchon.bin.groups.project`](/src/pynchon/bin/groups.py#L67-L69) with signature `(*args: Any, **kwargs: Any) -> Any`
  * [`pynchon.bin.groups.render`](/src/pynchon/bin/groups.py#L50-L52) with signature `(*args: Any, **kwargs: Any) -> Any`
-------------------------------------------------------------------------------
### pynchon.bin.common
* Overview:  [source code](/src/pynchon/bin/common.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (5 total)
  * [`pynchon.bin.common.handler`](/src/pynchon/bin/common.py#L16-L31)
    * with bases ([`__builtin__.object`](https://docs.python.org/3/library/functions.html#func-object),)
  * [`pynchon.bin.common.stdout_handler`](/src/pynchon/bin/common.py#L34-L45)
    * with bases ([handler](#pynchonbincommon),)
  * [`pynchon.bin.common.output_handler`](/src/pynchon/bin/common.py#L48-L66)
    * with bases ([handler](#pynchonbincommon),)
  * [`pynchon.bin.common.format_handler`](/src/pynchon/bin/common.py#L69-L99)
    * with bases ([handler](#pynchonbincommon),)
  * [`pynchon.bin.common.kommand`](/src/pynchon/bin/common.py#L102-L172)
    * with bases ([`__builtin__.object`](https://docs.python.org/3/library/functions.html#func-object),)
-------------------------------------------------------------------------------
### pynchon.api
* Overview:  [source code](/src/pynchon/api/__init__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (0 total)
-------------------------------------------------------------------------------
### pynchon.api.render
* Overview:  [source code](/src/pynchon/api/render.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Functions: (3 total)
  * [`pynchon.api.render._render`](/src/pynchon/api/render.py#L82-L103)
    * with signature `(text: str = '', context: dict = {}, templates='.', strict: bool = True)`
  * [`pynchon.api.render.rj2`](/src/pynchon/api/render.py#L42-L79)
    * with signature `(file, output='', in_place=False, ctx={}, templates='.', strict: bool = True)`
  * [`pynchon.api.render.rj5`](/src/pynchon/api/render.py#L22-L39) with signature `(file, output='', in_place=False)`