## API for 'pynchon' package



--------------------------------------------------------------------------------### pynchon
* Overview:  [source code](/src/pynchon/__init__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Modules: (4 total)
  * [`pynchon.annotate`](/src/pynchon/annotate.py): [index](#pynchonannotate), [source](/src/pynchon/annotate.py), [tests](#FIXME)
  * [`pynchon.util`](/src/pynchon/util.py): [index](#pynchonutil), [source](/src/pynchon/util.py), [tests](#FIXME)
  * [`pynchon.cli`](/src/pynchon/cli.py): [index](#pynchoncli), [source](/src/pynchon/cli.py), [tests](#FIXME)
  * [`pynchon.bin`](/src/pynchon/bin/__init__.py): [index](#pynchonbin), [source](/src/pynchon/bin/__init__.py), [tests](#FIXME)
* Functions: (1 total)
  * [`pynchon.get_logger`](/src/pynchon/__init__.py#L29-L56) with signature `(name)`
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
  * [`pynchon.util.Checker`](/src/pynchon/util.py#L119-L131)
    * with bases ([McCabeChecker](#mccabe),)
* Functions: (8 total)
  * [`pynchon.util.load_setupcfg`](/src/pynchon/util.py#L17-L22) with signature `(file: str = 'setup.cfg')`
  * [`pynchon.util.load_entrypoints`](/src/pynchon/util.py#L24-L36) with signature `(config=None)`
  * [`pynchon.util.click_recursive_help`](/src/pynchon/util.py#L38-L52)
    * with signature `(cmd, parent=None, out={}, file=<_io.TextIOWrapper name='<stdout>' mode='w' encoding='utf-8'>)`
  * [`pynchon.util.get_module`](/src/pynchon/util.py#L54-L72) with signature `(package: str = '', file: str = '')`
  * [`pynchon.util.get_refs`](/src/pynchon/util.py#L74-L87) with signature `(working_dir=None, module=None) -> dict`
  * [`pynchon.util.visit_module`](/src/pynchon/util.py#L89-L111)
    * with signature `(output=['### pynchon\n* Overview:  [source code](/src/pynchon/__init__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)\n* Modules: (4 total)\n  * [`pynchon.annotate`](/src/pynchon/annotate.py): [index](#pynchonannotate), [source](/src/pynchon/annotate.py), [tests](#FIXME)\n  * [`pynchon.util`](/src/pynchon/util.py): [index](#pynchonutil), [source](/src/pynchon/util.py), [tests](#FIXME)\n  * [`pynchon.cli`](/src/pynchon/cli.py): [index](#pynchoncli), [source](/src/pynchon/cli.py), [tests](#FIXME)\n  * [`pynchon.bin`](/src/pynchon/bin/__init__.py): [index](#pynchonbin), [source](/src/pynchon/bin/__init__.py), [tests](#FIXME)\n* Functions: (1 total)\n  * [`pynchon.get_logger`](/src/pynchon/__init__.py#L29-L56) with signature `(name)`\n-------------------------------------------------------------------------------', '### pynchon.annotate\n* Overview:  [source code](/src/pynchon/annotate.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)\n* Functions: (3 total)\n  * [`pynchon.annotate.klass`](/src/pynchon/annotate.py#L10-L61) with signature `(name, kls) -> None`\n    * with admonitions:  [🐉 Complex](/src/pynchon/annotate.py#L1 "score 8 / 7") \n  * [`pynchon.annotate.module`](/src/pynchon/annotate.py#L63-L67) with signature `(name, module, working_dir=None) -> None`\n  * [`pynchon.annotate.function`](/src/pynchon/annotate.py#L69-L99) with signature `(name, fxn) -> None`\n-------------------------------------------------------------------------------'], stats={}, module=None, template=<Template 'api-toc.md.j2'>, visited=[], module_name=None, working_dir='/home/matt/code/elo/pynchon')`
  * [`pynchon.util.clean_text`](/src/pynchon/util.py#L114-L117) with signature `(txt: str) -> str`
  * [`pynchon.util.complexity`](/src/pynchon/util.py#L133-L155) with signature `(code: str = None, fname: str = None, threshold: int = 7)`
-------------------------------------------------------------------------------
### pynchon.cli
* Overview:  [source code](/src/pynchon/cli.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
-------------------------------------------------------------------------------
### pynchon.bin
* Overview:  [source code](/src/pynchon/bin/__init__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Modules: (2 total)
  * [`pynchon.bin.common`](/src/pynchon/bin/common.py): [index](#pynchonbincommon), [source](/src/pynchon/bin/common.py), [tests](#FIXME)
  * [`pynchon.bin.groups`](/src/pynchon/bin/groups.py): [index](#pynchonbingroups), [source](/src/pynchon/bin/groups.py), [tests](#FIXME)
* Functions: (4 total)
  * [`pynchon.bin.project_entrypoints`](/src/pynchon/bin/__init__.py#L19-L29) with signature `(*args: Any, **kwargs: Any) -> Any`
  * [`pynchon.bin.click_dump`](/src/pynchon/bin/__init__.py#L32-L56) with signature `(*args: Any, **kwargs: Any) -> Any`
  * [`pynchon.bin.markdown`](/src/pynchon/bin/__init__.py#L59-L60) with signature `(**result)`
  * [`pynchon.bin.toc`](/src/pynchon/bin/__init__.py#L61-L74) with signature `(*args: Any, **kwargs: Any) -> Any`
-------------------------------------------------------------------------------
### pynchon.bin.common
* Overview:  [source code](/src/pynchon/bin/common.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (5 total)
  * [`pynchon.bin.common.handler`](/src/pynchon/bin/common.py#L13-L25)
    * with bases ([`__builtin__.object`](https://docs.python.org/3/library/functions.html#func-object),)
  * [`pynchon.bin.common.stdout_handler`](/src/pynchon/bin/common.py#L27-L35)
    * with bases ([handler](#pynchonbincommon),)
  * [`pynchon.bin.common.output_handler`](/src/pynchon/bin/common.py#L37-L47)
    * with bases ([handler](#pynchonbincommon),)
  * [`pynchon.bin.common.format_handler`](/src/pynchon/bin/common.py#L49-L76)
    * with bases ([handler](#pynchonbincommon),)
  * [`pynchon.bin.common.kommand`](/src/pynchon/bin/common.py#L78-L125)
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