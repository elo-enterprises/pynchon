## API for 'pynchon' package

---------------------------------------------------------------------------------------------------------------------------------------------------------------
### pynchon
* Overview:  [source code](/src/pynchon/__init__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (0 total)
* Functions: (1 total)
  * [`pynchon.get_logger`](/src/pynchon/__init__.py#L40-L65) with signature `(name)`
-------------------------------------------------------------------------------
### pynchon.abcs
* Overview:  [source code](/src/pynchon/abcs.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (3 total)
  * [`pynchon.abcs.JSONEncoder`](/src/pynchon/abcs.py#L13-L19)
    * with bases ([JSONEncoder](#jsonencoder),)
  * [`pynchon.abcs.Path`](/src/pynchon/abcs.py#L22-L40)
    * with bases ([PosixPath](#pathlib),)
    * with properties: (0 total)
      *  [`anchor`](/src/pynchon/abcs.py#L815) -> inspect._empty
      *  [`drive`](/src/pynchon/abcs.py#L22) -> None
      *  [`name`](/src/pynchon/abcs.py#L821) -> inspect._empty
      *  [`parent`](/src/pynchon/abcs.py#L976) -> inspect._empty
      *  [`parents`](/src/pynchon/abcs.py#L986) -> inspect._empty
      *  [`parts`](/src/pynchon/abcs.py#L944) -> inspect._empty
      *  [`root`](/src/pynchon/abcs.py#L22) -> None
      *  [`stem`](/src/pynchon/abcs.py#L856) -> inspect._empty
      *  [`suffix`](/src/pynchon/abcs.py#L829) -> inspect._empty
      *  [`suffixes`](/src/pynchon/abcs.py#L843) -> inspect._empty
  * [`pynchon.abcs.Config`](/src/pynchon/abcs.py#L43-L64)
    * with bases ([`__builtin__.dict`](https://docs.python.org/3/library/functions.html#func-dict),)
-------------------------------------------------------------------------------
### pynchon.config
* Overview:  [source code](/src/pynchon/config.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (5 total)
  * [`pynchon.config.GitConfig`](/src/pynchon/config.py#L16-L37)
    * with bases ([Config](#pynchonabcs),)
    * with properties: (0 total)
      *  [`hash`](/src/pynchon/config.py#L33) -> str
      *  [`repo`](/src/pynchon/config.py#L23) -> inspect._empty
      *  [`repo_name`](/src/pynchon/config.py#L29) -> inspect._empty
      *  [`root`](/src/pynchon/config.py#L19) -> inspect._empty
  * [`pynchon.config.PythonConfig`](/src/pynchon/config.py#L40-L75)
    * with bases ([Config](#pynchonabcs),)
    * with properties: (0 total)
      *  [`entrypoints`](/src/pynchon/config.py#L58) -> dict
      *  [`package`](/src/pynchon/config.py#L51) -> dict
      *  [`version`](/src/pynchon/config.py#L46) -> str
  * [`pynchon.config.PynchonConfig`](/src/pynchon/config.py#L78-L132)
    * with bases ([Config](#pynchonabcs),)
    * with properties: (0 total)
      *  [`docs_root`](/src/pynchon/config.py#L106) -> inspect._empty
      *  [`jinja_includes`](/src/pynchon/config.py#L118) -> list
      *  [`version`](/src/pynchon/config.py#L130) -> str
      *  [`working_dir`](/src/pynchon/config.py#L126) -> inspect._empty
  * [`pynchon.config.PackageConfig`](/src/pynchon/config.py#L135-L145)
    * with bases ([Config](#pynchonabcs),)
    * with properties: (0 total)
      *  [`name`](/src/pynchon/config.py#L136) -> str
      *  [`version`](/src/pynchon/config.py#L140) -> str
  * [`pynchon.config.ProjectConfig`](/src/pynchon/config.py#L148-L174)
    * with bases ([Config](#pynchonabcs),)
    * with properties: (0 total)
      *  [`name`](/src/pynchon/config.py#L156) -> str
      *  [`root`](/src/pynchon/config.py#L161) -> str
      *  [`subproject`](/src/pynchon/config.py#L166) -> dict
-------------------------------------------------------------------------------
### pynchon.annotate
* Overview:  [source code](/src/pynchon/annotate.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Functions: (3 total)
  * [`pynchon.annotate.function`](/src/pynchon/annotate.py#L86-L126) with signature `(name, fxn) -> None`
  * [`pynchon.annotate.klass`](/src/pynchon/annotate.py#L12-L77) with signature `(name, kls) -> None`
    * with admonitions:  [🐉 Complex](/src/pynchon/annotate.py#L1 "score 10 / 7") 
  * [`pynchon.annotate.module`](/src/pynchon/annotate.py#L80-L83) with signature `(name, module, working_dir=None) -> None`
-------------------------------------------------------------------------------
### pynchon.__main__
* Overview: (entrypoint) | [source code](/src/pynchon/__main__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
-------------------------------------------------------------------------------
### pynchon.util
* Overview:  [source code](/src/pynchon/util/__init__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (1 total)
  * [`pynchon.util.Checker`](/src/pynchon/util/__init__.py#L206-L218)
    * with bases ([McCabeChecker](#mccabe),)
* Classes: (1 total)
  * [`pynchon.util.Checker`](/src/pynchon/util/__init__.py#L206-L218)
    * with bases ([McCabeChecker](#mccabe),)
* Functions: (11 total)
  * [`pynchon.util.clean_text`](/src/pynchon/util/__init__.py#L201-L203) with signature `(txt: str) -> str`
  * [`pynchon.util.click_recursive_help`](/src/pynchon/util/__init__.py#L77-L101)
    * with signature `(cmd, parent=None, out={}, file=<_io.TextIOWrapper name='<stdout>' mode='w' encoding='utf-8'>)`
  * [`pynchon.util.complexity`](/src/pynchon/util/__init__.py#L221-L250) with signature `(code: str = None, fname: str = None, threshold: int = 7)`
  * [`pynchon.util.find_j2s`](/src/pynchon/util/__init__.py#L25-L46) with signature `(conf) -> list`
  * [`pynchon.util.find_src_root`](/src/pynchon/util/__init__.py#L67-L74) with signature `(config: dict) -> str`
  * [`pynchon.util.get_module`](/src/pynchon/util/__init__.py#L104-L122) with signature `(package: str = '', file: str = '')`
  * [`pynchon.util.get_refs`](/src/pynchon/util/__init__.py#L125-L156) with signature `(working_dir=None, module=None) -> dict`
  * [`pynchon.util.get_root`](/src/pynchon/util/__init__.py#L49-L57) with signature `(path: str = '.') -> str`
  * [`pynchon.util.invoke`](/src/pynchon/util/__init__.py#L253-L316)
    * with signature `(cmd=None, stdin='', interactive: bool = False, large_output: bool = False, log_command: bool = True, environment: dict = {}, log_stdin: bool = True, system: bool = False)`
  * [`pynchon.util.is_python_project`](/src/pynchon/util/__init__.py#L60-L64) with signature `() -> bool`
  * [`pynchon.util.visit_module`](/src/pynchon/util/__init__.py#L159-L198)
    * with signature `(output=['-------------------------------------------------------------------------------\n### pynchon\n* Overview:  [source code](/src/pynchon/__init__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)\n* Classes: (0 total)\n* Functions: (1 total)\n  * [`pynchon.get_logger`](/src/pynchon/__init__.py#L40-L65) with signature `(name)`', '-------------------------------------------------------------------------------\n### pynchon.abcs\n* Overview:  [source code](/src/pynchon/abcs.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)\n* Classes: (3 total)\n  * [`pynchon.abcs.JSONEncoder`](/src/pynchon/abcs.py#L13-L19)\n    * with bases ([JSONEncoder](#jsonencoder),)\n  * [`pynchon.abcs.Path`](/src/pynchon/abcs.py#L22-L40)\n    * with bases ([PosixPath](#pathlib),)\n    * with properties: (0 total)\n      *  [`anchor`](/src/pynchon/abcs.py#L815) -> inspect._empty\n      *  [`drive`](/src/pynchon/abcs.py#L22) -> None\n      *  [`name`](/src/pynchon/abcs.py#L821) -> inspect._empty\n      *  [`parent`](/src/pynchon/abcs.py#L976) -> inspect._empty\n      *  [`parents`](/src/pynchon/abcs.py#L986) -> inspect._empty\n      *  [`parts`](/src/pynchon/abcs.py#L944) -> inspect._empty\n      *  [`root`](/src/pynchon/abcs.py#L22) -> None\n      *  [`stem`](/src/pynchon/abcs.py#L856) -> inspect._empty\n      *  [`suffix`](/src/pynchon/abcs.py#L829) -> inspect._empty\n      *  [`suffixes`](/src/pynchon/abcs.py#L843) -> inspect._empty\n  * [`pynchon.abcs.Config`](/src/pynchon/abcs.py#L43-L64)\n    * with bases ([`__builtin__.dict`](https://docs.python.org/3/library/functions.html#func-dict),)', '-------------------------------------------------------------------------------\n### pynchon.config\n* Overview:  [source code](/src/pynchon/config.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)\n* Classes: (5 total)\n  * [`pynchon.config.GitConfig`](/src/pynchon/config.py#L16-L37)\n    * with bases ([Config](#pynchonabcs),)\n    * with properties: (0 total)\n      *  [`hash`](/src/pynchon/config.py#L33) -> str\n      *  [`repo`](/src/pynchon/config.py#L23) -> inspect._empty\n      *  [`repo_name`](/src/pynchon/config.py#L29) -> inspect._empty\n      *  [`root`](/src/pynchon/config.py#L19) -> inspect._empty\n  * [`pynchon.config.PythonConfig`](/src/pynchon/config.py#L40-L75)\n    * with bases ([Config](#pynchonabcs),)\n    * with properties: (0 total)\n      *  [`entrypoints`](/src/pynchon/config.py#L58) -> dict\n      *  [`package`](/src/pynchon/config.py#L51) -> dict\n      *  [`version`](/src/pynchon/config.py#L46) -> str\n  * [`pynchon.config.PynchonConfig`](/src/pynchon/config.py#L78-L132)\n    * with bases ([Config](#pynchonabcs),)\n    * with properties: (0 total)\n      *  [`docs_root`](/src/pynchon/config.py#L106) -> inspect._empty\n      *  [`jinja_includes`](/src/pynchon/config.py#L118) -> list\n      *  [`version`](/src/pynchon/config.py#L130) -> str\n      *  [`working_dir`](/src/pynchon/config.py#L126) -> inspect._empty\n  * [`pynchon.config.PackageConfig`](/src/pynchon/config.py#L135-L145)\n    * with bases ([Config](#pynchonabcs),)\n    * with properties: (0 total)\n      *  [`name`](/src/pynchon/config.py#L136) -> str\n      *  [`version`](/src/pynchon/config.py#L140) -> str\n  * [`pynchon.config.ProjectConfig`](/src/pynchon/config.py#L148-L174)\n    * with bases ([Config](#pynchonabcs),)\n    * with properties: (0 total)\n      *  [`name`](/src/pynchon/config.py#L156) -> str\n      *  [`root`](/src/pynchon/config.py#L161) -> str\n      *  [`subproject`](/src/pynchon/config.py#L166) -> dict', '-------------------------------------------------------------------------------\n### pynchon.annotate\n* Overview:  [source code](/src/pynchon/annotate.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)\n* Functions: (3 total)\n  * [`pynchon.annotate.function`](/src/pynchon/annotate.py#L86-L126) with signature `(name, fxn) -> None`\n  * [`pynchon.annotate.klass`](/src/pynchon/annotate.py#L12-L77) with signature `(name, kls) -> None`\n    * with admonitions:  [🐉 Complex](/src/pynchon/annotate.py#L1 "score 10 / 7") \n  * [`pynchon.annotate.module`](/src/pynchon/annotate.py#L80-L83) with signature `(name, module, working_dir=None) -> None`', '-------------------------------------------------------------------------------\n### pynchon.__main__\n* Overview: (entrypoint) | [source code](/src/pynchon/__main__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)'], stats={}, module=None, template=<Template 'api/TOC.md.j2'>, visited=[], exclude: list = [], module_name=None, working_dir='/Users/mattanderson-admin/code/elo/pynchon')`
-------------------------------------------------------------------------------
### pynchon.util.python
* Overview:  [source code](/src/pynchon/util/python.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Functions: (4 total)
  * [`pynchon.util.python.is_package`](/src/pynchon/util/python.py#L21-L25) with signature `() -> bool`
  * [`pynchon.util.python.load_entrypoints`](/src/pynchon/util/python.py#L63-L91) with signature `(config=None) -> dict`
  * [`pynchon.util.python.load_pyprojecttoml`](/src/pynchon/util/python.py#L42-L60) with signature `(path: str = '')`
  * [`pynchon.util.python.load_setupcfg`](/src/pynchon/util/python.py#L28-L39) with signature `(path: str = '')`
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
  * [`pynchon.bin.cli._all`](/src/pynchon/bin/cli.py#L47-L84) with signature `(*args: Any, **kwargs: Any) -> Any`
  * [`pynchon.bin.cli._entrypoint_docs`](/src/pynchon/bin/cli.py#L140-L162) with signature `(module=None, name=None)`
  * [`pynchon.bin.cli.entrypoint_docs`](/src/pynchon/bin/cli.py#L118-L137) with signature `(*args: Any, **kwargs: Any) -> Any`
  * [`pynchon.bin.cli.main_docs`](/src/pynchon/bin/cli.py#L87-L115) with signature `(*args: Any, **kwargs: Any) -> Any`
  * [`pynchon.bin.cli.toc`](/src/pynchon/bin/cli.py#L20-L44) with signature `(*args: Any, **kwargs: Any) -> Any`
-------------------------------------------------------------------------------
### pynchon.bin.project
* Overview:  [source code](/src/pynchon/bin/project.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Functions: (5 total)
  * [`pynchon.bin.project.project_apply`](/src/pynchon/bin/project.py#L80-L92) with signature `(*args: Any, **kwargs: Any) -> Any`
  * [`pynchon.bin.project.project_config`](/src/pynchon/bin/project.py#L67-L77) with signature `(*args: Any, **kwargs: Any) -> Any`
  * [`pynchon.bin.project.project_entrypoints`](/src/pynchon/bin/project.py#L19-L39) with signature `(*args: Any, **kwargs: Any) -> Any`
  * [`pynchon.bin.project.project_plan`](/src/pynchon/bin/project.py#L95-L108) with signature `(*args: Any, **kwargs: Any) -> Any`
  * [`pynchon.bin.project.project_version`](/src/pynchon/bin/project.py#L42-L64) with signature `(*args: Any, **kwargs: Any) -> Any`
-------------------------------------------------------------------------------
### pynchon.bin.render
* Overview:  [source code](/src/pynchon/bin/render.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Functions: (3 total)
  * [`pynchon.bin.render.render_any`](/src/pynchon/bin/render.py#L57-L74) with signature `(*args: Any, **kwargs: Any) -> Any`
  * [`pynchon.bin.render.render_j2`](/src/pynchon/bin/render.py#L77-L139) with signature `(*args: Any, **kwargs: Any) -> Any`
  * [`pynchon.bin.render.render_json5`](/src/pynchon/bin/render.py#L24-L54) with signature `(*args: Any, **kwargs: Any) -> Any`
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
  * [`pynchon.api.render._render`](/src/pynchon/api/render.py#L78-L101)
    * with signature `(text: str = '', context: dict = {}, templates='.', strict: bool = True)`
  * [`pynchon.api.render.j2`](/src/pynchon/api/render.py#L42-L75)
    * with signature `(file, output='', in_place=False, ctx={}, templates='.', strict: bool = True)`
  * [`pynchon.api.render.j5`](/src/pynchon/api/render.py#L22-L39) with signature `(file, output='', in_place=False)`
-------------------------------------------------------------------------------
### pynchon.api.pynchon
* Overview:  [source code](/src/pynchon/api/pynchon.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
-------------------------------------------------------------------------------
### pynchon.api.project
* Overview:  [source code](/src/pynchon/api/project/__init__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Functions: (2 total)
  * [`pynchon.api.project.get_config`](/src/pynchon/api/project/__init__.py#L16-L24) with signature `() -> dict`
  * [`pynchon.api.project.plan`](/src/pynchon/api/project/__init__.py#L27-L118) with signature `(config: dict = {}) -> dict`
-------------------------------------------------------------------------------
### pynchon.api.git
* Overview:  [source code](/src/pynchon/api/git/__init__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)