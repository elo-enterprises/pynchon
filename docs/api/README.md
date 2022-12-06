## API for 'pynchon' package

---------------------------------------------------------------------------------------------------------------------------------------------------------------
### pynchon
* Overview:  [source code](/src/pynchon/__init__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (0 total)
* Functions: (1 total)
  * [`pynchon.get_logger`](/src/pynchon/__init__.py#L37-L63) with signature `(name)`
-------------------------------------------------------------------------------
### pynchon._version
* Overview:  [source code](/src/pynchon/_version.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
-------------------------------------------------------------------------------
### pynchon.annotate
* Overview:  [source code](/src/pynchon/annotate.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Functions: (3 total)
  * [`pynchon.annotate.klass`](/src/pynchon/annotate.py#L10-L61) with signature `(name, kls) -> None`
    * with admonitions:  [🐉 Complex](/src/pynchon/annotate.py#L1 "score 8 / 7") 
  * [`pynchon.annotate.module`](/src/pynchon/annotate.py#L63-L67) with signature `(name, module, working_dir=None) -> None`
  * [`pynchon.annotate.function`](/src/pynchon/annotate.py#L69-L99) with signature `(name, fxn) -> None`
-------------------------------------------------------------------------------
### pynchon.util
* Overview:  [source code](/src/pynchon/util.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (1 total)
  * [`pynchon.util.Checker`](/src/pynchon/util.py#L142-L154)
    * with bases ([McCabeChecker](#mccabe),)
* Functions: (8 total)
  * [`pynchon.util.load_setupcfg`](/src/pynchon/util.py#L18-L27) with signature `(file: str = 'setup.cfg')`
  * [`pynchon.util.load_entrypoints`](/src/pynchon/util.py#L29-L45) with signature `(config=None)`
  * [`pynchon.util.click_recursive_help`](/src/pynchon/util.py#L47-L70)
    * with signature `(cmd, parent=None, out={}, file=<_io.TextIOWrapper name='<stdout>' mode='w' encoding='utf-8'>)`
  * [`pynchon.util.get_module`](/src/pynchon/util.py#L72-L90) with signature `(package: str = '', file: str = '')`
  * [`pynchon.util.get_refs`](/src/pynchon/util.py#L92-L105) with signature `(working_dir=None, module=None) -> dict`
  * [`pynchon.util.visit_module`](/src/pynchon/util.py#L107-L134)
    * with signature `(output=['-------------------------------------------------------------------------------\n### pynchon\n* Overview:  [source code](/src/pynchon/__init__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)\n* Classes: (0 total)\n* Functions: (1 total)\n  * [`pynchon.get_logger`](/src/pynchon/__init__.py#L37-L63) with signature `(name)`', '-------------------------------------------------------------------------------\n### pynchon._version\n* Overview:  [source code](/src/pynchon/_version.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)', '-------------------------------------------------------------------------------\n### pynchon.annotate\n* Overview:  [source code](/src/pynchon/annotate.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)\n* Functions: (3 total)\n  * [`pynchon.annotate.klass`](/src/pynchon/annotate.py#L10-L61) with signature `(name, kls) -> None`\n    * with admonitions:  [🐉 Complex](/src/pynchon/annotate.py#L1 "score 8 / 7") \n  * [`pynchon.annotate.module`](/src/pynchon/annotate.py#L63-L67) with signature `(name, module, working_dir=None) -> None`\n  * [`pynchon.annotate.function`](/src/pynchon/annotate.py#L69-L99) with signature `(name, fxn) -> None`'], stats={}, module=None, template=<Template 'api/TOC.md.j2'>, visited=[], exclude: list = [], module_name=None, working_dir='/home/matt/code/elo/pynchon')`
  * [`pynchon.util.clean_text`](/src/pynchon/util.py#L137-L140) with signature `(txt: str) -> str`
  * [`pynchon.util.complexity`](/src/pynchon/util.py#L156-L178) with signature `(code: str = None, fname: str = None, threshold: int = 7)`
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
  * [`pynchon.bin.cli.toc`](/src/pynchon/bin/cli.py#L12-L26) with signature `(*args: Any, **kwargs: Any) -> Any`
  * [`pynchon.bin.cli._all`](/src/pynchon/bin/cli.py#L28-L62) with signature `(*args: Any, **kwargs: Any) -> Any`
  * [`pynchon.bin.cli.entrypoint_docs`](/src/pynchon/bin/cli.py#L64-L80) with signature `(*args: Any, **kwargs: Any) -> Any`
  * [`pynchon.bin.cli._entrypoint_docs`](/src/pynchon/bin/cli.py#L82-L103) with signature `(module=None, name=None)`
-------------------------------------------------------------------------------
### pynchon.bin.project
* Overview:  [source code](/src/pynchon/bin/project.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Functions: (2 total)
  * [`pynchon.bin.project.project_entrypoints`](/src/pynchon/bin/project.py#L9-L19) with signature `(*args: Any, **kwargs: Any) -> Any`
  * [`pynchon.bin.project.version`](/src/pynchon/bin/project.py#L22-L36) with signature `(*args: Any, **kwargs: Any) -> Any`
-------------------------------------------------------------------------------
### pynchon.bin.render
* Overview:  [source code](/src/pynchon/bin/render.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Functions: (6 total)
  * [`pynchon.bin.render._rj5`](/src/pynchon/bin/render.py#L17-L30) with signature `(file, output='', in_place=False)`
  * [`pynchon.bin.render._render`](/src/pynchon/bin/render.py#L32-L35) with signature `(text: str = '', context: dict = {})`
  * [`pynchon.bin.render._rj2`](/src/pynchon/bin/render.py#L37-L62) with signature `(file, output='', in_place=False, ctx={})`
  * [`pynchon.bin.render.render_json5`](/src/pynchon/bin/render.py#L64-L88) with signature `(*args: Any, **kwargs: Any) -> Any`
  * [`pynchon.bin.render.render_any`](/src/pynchon/bin/render.py#L90-L104) with signature `(*args: Any, **kwargs: Any) -> Any`
  * [`pynchon.bin.render.render_j2`](/src/pynchon/bin/render.py#L106-L149) with signature `(*args: Any, **kwargs: Any) -> Any`
-------------------------------------------------------------------------------
### pynchon.bin.options
* Overview:  [source code](/src/pynchon/bin/options.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
-------------------------------------------------------------------------------
### pynchon.bin.common
* Overview:  [source code](/src/pynchon/bin/common.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (5 total)
  * [`pynchon.bin.common.handler`](/src/pynchon/bin/common.py#L14-L29)
    * with bases ([`__builtin__.object`](https://docs.python.org/3/library/functions.html#func-object),)
  * [`pynchon.bin.common.stdout_handler`](/src/pynchon/bin/common.py#L31-L41)
    * with bases ([handler](#pynchonbincommon),)
  * [`pynchon.bin.common.output_handler`](/src/pynchon/bin/common.py#L43-L56)
    * with bases ([handler](#pynchonbincommon),)
  * [`pynchon.bin.common.format_handler`](/src/pynchon/bin/common.py#L58-L84)
    * with bases ([handler](#pynchonbincommon),)
  * [`pynchon.bin.common.kommand`](/src/pynchon/bin/common.py#L86-L142)
    * with bases ([`__builtin__.object`](https://docs.python.org/3/library/functions.html#func-object),)
-------------------------------------------------------------------------------
### pynchon.bin.groups
* Overview:  [source code](/src/pynchon/bin/groups.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (1 total)
  * [`pynchon.bin.groups.group`](/src/pynchon/bin/groups.py#L5-L19)
    * with bases ([`__builtin__.object`](https://docs.python.org/3/library/functions.html#func-object),)
* Functions: (7 total)
  * [`pynchon.bin.groups.entry`](/src/pynchon/bin/groups.py#L21-L24) with signature `(*args: Any, **kwargs: Any) -> Any`
  * [`pynchon.bin.groups.gen`](/src/pynchon/bin/groups.py#L29-L31) with signature `(*args: Any, **kwargs: Any) -> Any`
  * [`pynchon.bin.groups.render`](/src/pynchon/bin/groups.py#L33-L35) with signature `(*args: Any, **kwargs: Any) -> Any`
  * [`pynchon.bin.groups.gen_api`](/src/pynchon/bin/groups.py#L37-L41) with signature `(*args: Any, **kwargs: Any) -> Any`
  * [`pynchon.bin.groups.gen_cli`](/src/pynchon/bin/groups.py#L43-L45) with signature `(*args: Any, **kwargs: Any) -> Any`
  * [`pynchon.bin.groups.project`](/src/pynchon/bin/groups.py#L47-L49) with signature `(*args: Any, **kwargs: Any) -> Any`
  * [`pynchon.bin.groups.ast`](/src/pynchon/bin/groups.py#L51-L53) with signature `(*args: Any, **kwargs: Any) -> Any`