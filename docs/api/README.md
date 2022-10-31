## API for 'pynchon' package



--------------------------------------------------------------------------------### pynchon
* Overview:  [source code](/src/pynchon/__init__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Modules: (4 total)
  * [`pynchon._version`](/src/pynchon/_version.py): [index](#pynchon_version), [source](/src/pynchon/_version.py), [tests](#FIXME)
  * [`pynchon.annotate`](/src/pynchon/annotate.py): [index](#pynchonannotate), [source](/src/pynchon/annotate.py), [tests](#FIXME)
  * [`pynchon.util`](/src/pynchon/util.py): [index](#pynchonutil), [source](/src/pynchon/util.py), [tests](#FIXME)
  * [`pynchon.bin`](/src/pynchon/bin/__init__.py): [index](#pynchonbin), [source](/src/pynchon/bin/__init__.py), [tests](#FIXME)
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
  * [`pynchon.util.Checker`](/src/pynchon/util.py#L136-L148)
    * with bases ([McCabeChecker](#mccabe),)
* Functions: (8 total)
  * [`pynchon.util.load_setupcfg`](/src/pynchon/util.py#L17-L26) with signature `(file: str = 'setup.cfg')`
  * [`pynchon.util.load_entrypoints`](/src/pynchon/util.py#L28-L44) with signature `(config=None)`
  * [`pynchon.util.click_recursive_help`](/src/pynchon/util.py#L46-L69)
    * with signature `(cmd, parent=None, out={}, file=<_io.TextIOWrapper name='<stdout>' mode='w' encoding='utf-8'>)`
  * [`pynchon.util.get_module`](/src/pynchon/util.py#L71-L89) with signature `(package: str = '', file: str = '')`
  * [`pynchon.util.get_refs`](/src/pynchon/util.py#L91-L104) with signature `(working_dir=None, module=None) -> dict`
  * [`pynchon.util.visit_module`](/src/pynchon/util.py#L106-L128)
    * with signature `(output=['### pynchon\n* Overview:  [source code](/src/pynchon/__init__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)\n* Modules: (4 total)\n  * [`pynchon._version`](/src/pynchon/_version.py): [index](#pynchon_version), [source](/src/pynchon/_version.py), [tests](#FIXME)\n  * [`pynchon.annotate`](/src/pynchon/annotate.py): [index](#pynchonannotate), [source](/src/pynchon/annotate.py), [tests](#FIXME)\n  * [`pynchon.util`](/src/pynchon/util.py): [index](#pynchonutil), [source](/src/pynchon/util.py), [tests](#FIXME)\n  * [`pynchon.bin`](/src/pynchon/bin/__init__.py): [index](#pynchonbin), [source](/src/pynchon/bin/__init__.py), [tests](#FIXME)\n* Functions: (1 total)\n  * [`pynchon.get_logger`](/src/pynchon/__init__.py#L37-L63) with signature `(name)`\n-------------------------------------------------------------------------------', '### pynchon._version\n* Overview:  [source code](/src/pynchon/_version.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)\n-------------------------------------------------------------------------------', '### pynchon.annotate\n* Overview:  [source code](/src/pynchon/annotate.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)\n* Functions: (3 total)\n  * [`pynchon.annotate.klass`](/src/pynchon/annotate.py#L10-L61) with signature `(name, kls) -> None`\n    * with admonitions:  [🐉 Complex](/src/pynchon/annotate.py#L1 "score 8 / 7") \n  * [`pynchon.annotate.module`](/src/pynchon/annotate.py#L63-L67) with signature `(name, module, working_dir=None) -> None`\n  * [`pynchon.annotate.function`](/src/pynchon/annotate.py#L69-L99) with signature `(name, fxn) -> None`\n-------------------------------------------------------------------------------'], stats={}, module=None, template=<Template 'api/TOC.md.j2'>, visited=[], module_name=None, working_dir='/home/matt/code/elo/pynchon')`
  * [`pynchon.util.clean_text`](/src/pynchon/util.py#L131-L134) with signature `(txt: str) -> str`
  * [`pynchon.util.complexity`](/src/pynchon/util.py#L150-L172) with signature `(code: str = None, fname: str = None, threshold: int = 7)`
-------------------------------------------------------------------------------
### pynchon.bin
* Overview:  [source code](/src/pynchon/bin/__init__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Modules: (6 total)
  * [`pynchon.bin.api`](/src/pynchon/bin/api.py): [index](#pynchonbinapi), [source](/src/pynchon/bin/api.py), [tests](#FIXME)
  * [`pynchon.bin.cli`](/src/pynchon/bin/cli.py): [index](#pynchonbincli), [source](/src/pynchon/bin/cli.py), [tests](#FIXME)
  * [`pynchon.bin.project`](/src/pynchon/bin/project.py): [index](#pynchonbinproject), [source](/src/pynchon/bin/project.py), [tests](#FIXME)
  * [`pynchon.bin.options`](/src/pynchon/bin/options.py): [index](#pynchonbinoptions), [source](/src/pynchon/bin/options.py), [tests](#FIXME)
  * [`pynchon.bin.common`](/src/pynchon/bin/common.py): [index](#pynchonbincommon), [source](/src/pynchon/bin/common.py), [tests](#FIXME)
  * [`pynchon.bin.groups`](/src/pynchon/bin/groups.py): [index](#pynchonbingroups), [source](/src/pynchon/bin/groups.py), [tests](#FIXME)
-------------------------------------------------------------------------------
### pynchon.bin.api
* Overview:  [source code](/src/pynchon/bin/api.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Functions: (2 total)
  * [`pynchon.bin.api.markdown`](/src/pynchon/bin/api.py#L10-L11) with signature `(**result)`
  * [`pynchon.bin.api.toc`](/src/pynchon/bin/api.py#L13-L29) with signature `(*args: Any, **kwargs: Any) -> Any`
-------------------------------------------------------------------------------
### pynchon.bin.cli
* Overview:  [source code](/src/pynchon/bin/cli.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Functions: (4 total)
  * [`pynchon.bin.cli.toc`](/src/pynchon/bin/cli.py#L10-L24) with signature `(*args: Any, **kwargs: Any) -> Any`
  * [`pynchon.bin.cli._all`](/src/pynchon/bin/cli.py#L26-L60) with signature `(*args: Any, **kwargs: Any) -> Any`
  * [`pynchon.bin.cli.entrypoint_docs`](/src/pynchon/bin/cli.py#L62-L78) with signature `(*args: Any, **kwargs: Any) -> Any`
  * [`pynchon.bin.cli._entrypoint_docs`](/src/pynchon/bin/cli.py#L80-L101) with signature `(module=None, name=None)`
-------------------------------------------------------------------------------
### pynchon.bin.project
* Overview:  [source code](/src/pynchon/bin/project.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Functions: (1 total)
  * [`pynchon.bin.project.project_entrypoints`](/src/pynchon/bin/project.py#L9-L19) with signature `(*args: Any, **kwargs: Any) -> Any`
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
  * [`pynchon.bin.common.kommand`](/src/pynchon/bin/common.py#L86-L137)
    * with bases ([`__builtin__.object`](https://docs.python.org/3/library/functions.html#func-object),)
-------------------------------------------------------------------------------
### pynchon.bin.groups
* Overview:  [source code](/src/pynchon/bin/groups.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (1 total)
  * [`pynchon.bin.groups.group`](/src/pynchon/bin/groups.py#L5-L18)
    * with bases ([`__builtin__.object`](https://docs.python.org/3/library/functions.html#func-object),)
* Functions: (6 total)
  * [`pynchon.bin.groups.entry`](/src/pynchon/bin/groups.py#L20-L23) with signature `(*args: Any, **kwargs: Any) -> Any`
  * [`pynchon.bin.groups.gen`](/src/pynchon/bin/groups.py#L28-L30) with signature `(*args: Any, **kwargs: Any) -> Any`
  * [`pynchon.bin.groups.gen_api`](/src/pynchon/bin/groups.py#L32-L36) with signature `(*args: Any, **kwargs: Any) -> Any`
  * [`pynchon.bin.groups.gen_cli`](/src/pynchon/bin/groups.py#L38-L40) with signature `(*args: Any, **kwargs: Any) -> Any`
  * [`pynchon.bin.groups.project`](/src/pynchon/bin/groups.py#L42-L44) with signature `(*args: Any, **kwargs: Any) -> Any`
  * [`pynchon.bin.groups.ast`](/src/pynchon/bin/groups.py#L46-L48) with signature `(*args: Any, **kwargs: Any) -> Any`
-------------------------------------------------------------------------------