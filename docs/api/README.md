## API for 'pynchon' package

---------------------------------------------------------------------------------------------------------------------------------------------------------------
### pynchon
* Overview:  [source code](/src/pynchon/__init__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (0 total)
* Functions: (1 total)
  * [`pynchon.get_logger`](/src/pynchon/__init__.py#L37-L63) with signature `(name)`
-------------------------------------------------------------------------------
### pynchon.config
* Overview:  [source code](/src/pynchon/config.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Functions: (2 total)
  * [`pynchon.config.read_config`](/src/pynchon/config.py#L4-L5) with signature `(file: str = '.pynchon_conf.json5') -> dict`
  * [`pynchon.config.detect_config`](/src/pynchon/config.py#L7-L8) with signature `() -> dict`
-------------------------------------------------------------------------------
### pynchon.util
* Overview:  [source code](/src/pynchon/util.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (1 total)
  * [`pynchon.util.Checker`](/src/pynchon/util.py#L185-L197)
    * with bases ([McCabeChecker](#mccabe),)
* Functions: (15 total)
  * [`pynchon.util.project_version`](/src/pynchon/util.py#L18-L22) with signature `() -> str`
  * [`pynchon.util.pynchon_version`](/src/pynchon/util.py#L24-L27) with signature `() -> str`
  * [`pynchon.util.is_python_project`](/src/pynchon/util.py#L29-L31) with signature `() -> bool`
  * [`pynchon.util.find_git_root`](/src/pynchon/util.py#L33-L41) with signature `(path: str = '.') -> str`
  * [`pynchon.util.get_git_hash`](/src/pynchon/util.py#L43-L46) with signature `() -> str`
  * [`pynchon.util.find_src_root`](/src/pynchon/util.py#L48-L52) with signature `(config: dict) -> str`
  * [`pynchon.util.load_setupcfg`](/src/pynchon/util.py#L54-L70) with signature `(file: str = 'setup.cfg')`
  * [`pynchon.util.load_entrypoints`](/src/pynchon/util.py#L72-L88) with signature `(config=None)`
  * [`pynchon.util.click_recursive_help`](/src/pynchon/util.py#L90-L113)
    * with signature `(cmd, parent=None, out={}, file=<_io.TextIOWrapper name='<stdout>' mode='w' encoding='utf-8'>)`
  * [`pynchon.util.get_module`](/src/pynchon/util.py#L115-L133) with signature `(package: str = '', file: str = '')`
  * [`pynchon.util.get_refs`](/src/pynchon/util.py#L135-L148) with signature `(working_dir=None, module=None) -> dict`
  * [`pynchon.util.visit_module`](/src/pynchon/util.py#L150-L177)
    * with signature `(output=['-------------------------------------------------------------------------------\n### pynchon\n* Overview:  [source code](/src/pynchon/__init__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)\n* Classes: (0 total)\n* Functions: (1 total)\n  * [`pynchon.get_logger`](/src/pynchon/__init__.py#L37-L63) with signature `(name)`', "-------------------------------------------------------------------------------\n### pynchon.config\n* Overview:  [source code](/src/pynchon/config.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)\n* Functions: (2 total)\n  * [`pynchon.config.read_config`](/src/pynchon/config.py#L4-L5) with signature `(file: str = '.pynchon_conf.json5') -> dict`\n  * [`pynchon.config.detect_config`](/src/pynchon/config.py#L7-L8) with signature `() -> dict`"], stats={}, module=None, template=<Template 'api/TOC.md.j2'>, visited=[], exclude: list = [], module_name=None, working_dir='/Users/mattanderson-admin/code/elo/pynchon')`
  * [`pynchon.util.clean_text`](/src/pynchon/util.py#L180-L183) with signature `(txt: str) -> str`
  * [`pynchon.util.complexity`](/src/pynchon/util.py#L199-L221) with signature `(code: str = None, fname: str = None, threshold: int = 7)`
  * [`pynchon.util.invoke`](/src/pynchon/util.py#L225-L285)
    * with signature `(cmd=None, stdin='', interactive: bool = False, large_output: bool = False, log_command: bool = True, environment: dict = {}, log_stdin: bool = True, system: bool = False)`
-------------------------------------------------------------------------------
### pynchon.annotate
* Overview:  [source code](/src/pynchon/annotate.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Functions: (3 total)
  * [`pynchon.annotate.klass`](/src/pynchon/annotate.py#L10-L61) with signature `(name, kls) -> None`
    * with admonitions:  [🐉 Complex](/src/pynchon/annotate.py#L1 "score 8 / 7") 
  * [`pynchon.annotate.module`](/src/pynchon/annotate.py#L63-L67) with signature `(name, module, working_dir=None) -> None`
  * [`pynchon.annotate.function`](/src/pynchon/annotate.py#L69-L99) with signature `(name, fxn) -> None`
-------------------------------------------------------------------------------
### pynchon.bin
* Overview:  [source code](/src/pynchon/bin/__init__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (0 total)
-------------------------------------------------------------------------------
### pynchon.bin.api
* Overview:  [source code](/src/pynchon/bin/api.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Functions: (2 total)
  * [`pynchon.bin.api.markdown`](/src/pynchon/bin/api.py#L10-L11) with signature `(**result)`
  * [`pynchon.bin.api.toc`](/src/pynchon/bin/api.py#L13-L35) with signature `(*args: Any, **kwargs: Any) -> Any`
-------------------------------------------------------------------------------
### pynchon.bin.cli
* Overview:  [source code](/src/pynchon/bin/cli.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Functions: (4 total)
  * [`pynchon.bin.cli.toc`](/src/pynchon/bin/cli.py#L13-L27) with signature `(*args: Any, **kwargs: Any) -> Any`
  * [`pynchon.bin.cli._all`](/src/pynchon/bin/cli.py#L29-L63) with signature `(*args: Any, **kwargs: Any) -> Any`
  * [`pynchon.bin.cli.entrypoint_docs`](/src/pynchon/bin/cli.py#L65-L81) with signature `(*args: Any, **kwargs: Any) -> Any`
  * [`pynchon.bin.cli._entrypoint_docs`](/src/pynchon/bin/cli.py#L83-L104) with signature `(module=None, name=None)`
-------------------------------------------------------------------------------
### pynchon.bin.project
* Overview:  [source code](/src/pynchon/bin/project.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Functions: (3 total)
  * [`pynchon.bin.project.project_entrypoints`](/src/pynchon/bin/project.py#L10-L20) with signature `(*args: Any, **kwargs: Any) -> Any`
  * [`pynchon.bin.project.project_version`](/src/pynchon/bin/project.py#L22-L36) with signature `(*args: Any, **kwargs: Any) -> Any`
  * [`pynchon.bin.project.project_plan`](/src/pynchon/bin/project.py#L51-L99) with signature `(*args: Any, **kwargs: Any) -> Any`
-------------------------------------------------------------------------------
### pynchon.bin.render
* Overview:  [source code](/src/pynchon/bin/render.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Functions: (3 total)
  * [`pynchon.bin.render.render_json5`](/src/pynchon/bin/render.py#L20-L45) with signature `(*args: Any, **kwargs: Any) -> Any`
  * [`pynchon.bin.render.render_any`](/src/pynchon/bin/render.py#L47-L62) with signature `(*args: Any, **kwargs: Any) -> Any`
  * [`pynchon.bin.render.render_j2`](/src/pynchon/bin/render.py#L64-L110) with signature `(*args: Any, **kwargs: Any) -> Any`
-------------------------------------------------------------------------------
### pynchon.bin.options
* Overview:  [source code](/src/pynchon/bin/options.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
-------------------------------------------------------------------------------
### pynchon.bin.groups
* Overview:  [source code](/src/pynchon/bin/groups.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (1 total)
  * [`pynchon.bin.groups.group`](/src/pynchon/bin/groups.py#L6-L20)
    * with bases ([`__builtin__.object`](https://docs.python.org/3/library/functions.html#func-object),)
* Functions: (7 total)
  * [`pynchon.bin.groups.entry`](/src/pynchon/bin/groups.py#L22-L25) with signature `(*args: Any, **kwargs: Any) -> Any`
  * [`pynchon.bin.groups.gen`](/src/pynchon/bin/groups.py#L30-L32) with signature `(*args: Any, **kwargs: Any) -> Any`
  * [`pynchon.bin.groups.render`](/src/pynchon/bin/groups.py#L40-L42) with signature `(*args: Any, **kwargs: Any) -> Any`
  * [`pynchon.bin.groups.gen_api`](/src/pynchon/bin/groups.py#L44-L48) with signature `(*args: Any, **kwargs: Any) -> Any`
  * [`pynchon.bin.groups.gen_cli`](/src/pynchon/bin/groups.py#L50-L52) with signature `(*args: Any, **kwargs: Any) -> Any`
  * [`pynchon.bin.groups.project`](/src/pynchon/bin/groups.py#L54-L56) with signature `(*args: Any, **kwargs: Any) -> Any`
  * [`pynchon.bin.groups.ast`](/src/pynchon/bin/groups.py#L58-L60) with signature `(*args: Any, **kwargs: Any) -> Any`
-------------------------------------------------------------------------------
### pynchon.bin.common
* Overview:  [source code](/src/pynchon/bin/common.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (5 total)
  * [`pynchon.bin.common.handler`](/src/pynchon/bin/common.py#L15-L30)
    * with bases ([`__builtin__.object`](https://docs.python.org/3/library/functions.html#func-object),)
  * [`pynchon.bin.common.stdout_handler`](/src/pynchon/bin/common.py#L32-L42)
    * with bases ([handler](#pynchonbincommon),)
  * [`pynchon.bin.common.output_handler`](/src/pynchon/bin/common.py#L44-L60)
    * with bases ([handler](#pynchonbincommon),)
  * [`pynchon.bin.common.format_handler`](/src/pynchon/bin/common.py#L62-L88)
    * with bases ([handler](#pynchonbincommon),)
  * [`pynchon.bin.common.kommand`](/src/pynchon/bin/common.py#L90-L146)
    * with bases ([`__builtin__.object`](https://docs.python.org/3/library/functions.html#func-object),)
-------------------------------------------------------------------------------
### pynchon.api
* Overview:  [source code](/src/pynchon/api/__init__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (0 total)
-------------------------------------------------------------------------------
### pynchon.api.render
* Overview:  [source code](/src/pynchon/api/render.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Functions: (3 total)
  * [`pynchon.api.render.rj5`](/src/pynchon/api/render.py#L17-L30) with signature `(file, output='', in_place=False)`
  * [`pynchon.api.render.rj2`](/src/pynchon/api/render.py#L32-L65)
    * with signature `(file, output='', in_place=False, ctx={}, templates='.', strict: bool = True)`
  * [`pynchon.api.render._render`](/src/pynchon/api/render.py#L67-L83)
    * with signature `(text: str = '', context: dict = {}, templates='.', strict: bool = True)`