## API for 'pynchon' package

--------------------------------------------------------------------------------<!--- This is a markdown file.  Comments look like this --->
-------------------------------------------------------------------------------
### pynchon
* Overview:  [source code](/src/pynchon/__init__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
<!--- This is a markdown file.  Comments look like this --->
* Classes: (0 total)
<!--- This is a markdown file.  Comments look like this --->
-------------------------------------------------------------------------------
### pynchon.events
* Overview:  [source code](/src/pynchon/events.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
<!--- This is a markdown file.  Comments look like this --->
* Classes: (1 total)
  * [`pynchon.events.Signal`](/src/pynchon/events.py#L11-L16)
    * with bases ([Signal](#blinkerbase),)
<!--- This is a markdown file.  Comments look like this --->
* Functions: (6 total)
  * [`pynchon.events._lifecycle`](/src/pynchon/events.py#L74-L86) with signature ``
  * [`pynchon.events.lifecycle_applying`](/src/pynchon/events.py#L43-L48) with signature `(sender, applying=None, **kwargs)`
  * [`pynchon.events.lifecycle_config`](/src/pynchon/events.py#L34-L40) with signature `(sender, config)`
  * [`pynchon.events.lifecycle_msg`](/src/pynchon/events.py#L63-L70) with signature `(sender, msg=None, **unused)`
  * [`pynchon.events.lifecycle_plugin`](/src/pynchon/events.py#L25-L31) with signature `(sender, plugin)`
  * [`pynchon.events.lifecycle_stage`](/src/pynchon/events.py#L51-L60) with signature `(sender, stage=None, **unused)`
<!--- This is a markdown file.  Comments look like this --->
-------------------------------------------------------------------------------
### pynchon.constants
* Overview:  [source code](/src/pynchon/constants.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
<!--- This is a markdown file.  Comments look like this --->
-------------------------------------------------------------------------------
### pynchon.bin
* Overview:  [source code](/src/pynchon/bin.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
<!--- This is a markdown file.  Comments look like this --->
* Classes: (1 total)
  * [`pynchon.bin.RootGroup`](/src/pynchon/bin.py#L20-L25)
    * with bases ([RootGroup](#flekscliroot_group),)
<!--- This is a markdown file.  Comments look like this --->
* Functions: (3 total)
  * [`pynchon.bin.bootstrap`](/src/pynchon/bin.py#L45-L72) with signature `()`
  * [`pynchon.bin.default`](/src/pynchon/bin.py#L75-L96) with signature `(*args: Any, **kwargs: Any) -> Any`
  * [`pynchon.bin.entry`](/src/pynchon/bin.py#L28-L42) with signature `(*args: Any, **kwargs: Any) -> Any`
<!--- This is a markdown file.  Comments look like this --->
-------------------------------------------------------------------------------
### pynchon.core
* Overview:  [source code](/src/pynchon/core.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
<!--- This is a markdown file.  Comments look like this --->
* Classes: (1 total)
  * [`pynchon.core.Config`](/src/pynchon/core.py#L60-L134)
    * with bases ([Config](#pynchonabcsconfig),)
    * with properties: (4 total)
      *  [`plugins`](/src/pynchon/core.py#L114) -> inspect._empty
      *  [`root`](/src/pynchon/core.py#L98) -> str
      *  [`version`](/src/pynchon/core.py#L92) -> str
      *  [`working_dir`](/src/pynchon/core.py#L131) -> inspect._empty
<!--- This is a markdown file.  Comments look like this --->
* Functions: (1 total)
  * [`pynchon.core.validate`](/src/pynchon/core.py#L13-L54) with signature `(kls=None, self=None, vdata=None)`
    * with admonitions:  [🐉 Complex](/src/pynchon/core.py#L1 "score 10 / 7") 
<!--- This is a markdown file.  Comments look like this --->
-------------------------------------------------------------------------------
### pynchon.gripe
* Overview:  [source code](/src/pynchon/gripe.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
<!--- This is a markdown file.  Comments look like this --->
* Classes: (2 total)
  * [`pynchon.gripe.PortBusy`](/src/pynchon/gripe.py#L23-L24)
    * with bases ([`__builtin__.RuntimeError`](https://docs.python.org/3/library/functions.html#RuntimeError),)
  * [`pynchon.gripe.Server`](/src/pynchon/gripe.py#L72-L113)
    * with bases ([`__builtin__.object`](https://docs.python.org/3/library/functions.html#object),)
    * with properties: (5 total)
      *  [`app`](/src/pynchon/gripe.py#L106) -> inspect._empty
      *  [`live`](/src/pynchon/gripe.py#L83) -> bool
      *  [`port`](/src/pynchon/gripe.py#L88) -> inspect._empty
      *  [`proc`](/src/pynchon/gripe.py#L75) -> psutil.Process
      *  [`raw_file_server`](/src/pynchon/gripe.py#L93) -> inspect._empty
<!--- This is a markdown file.  Comments look like this --->
* Functions: (10 total)
  * [`pynchon.gripe._current_gripe_procs`](/src/pynchon/gripe.py#L27-L29) with signature ``
  * [`pynchon.gripe._do_serve`](/src/pynchon/gripe.py#L49-L62) with signature ``
  * [`pynchon.gripe._is_my_grip`](/src/pynchon/gripe.py#L65-L69) with signature ``
  * [`pynchon.gripe._list`](/src/pynchon/gripe.py#L127-L144) with signature ``
  * [`pynchon.gripe._used_ports`](/src/pynchon/gripe.py#L42-L46) with signature ``
  * [`pynchon.gripe.entry`](/src/pynchon/gripe.py#L120-L124) with signature `(*args: Any, **kwargs: Any) -> Any`
  * [`pynchon.gripe.get_port`](/src/pynchon/gripe.py#L32-L39) with signature `(proc)`
  * [`pynchon.gripe.restart`](/src/pynchon/gripe.py#L218-L223) with signature `()`
  * [`pynchon.gripe.start`](/src/pynchon/gripe.py#L147-L201)
    * with signature `(fg: bool = None, ls: bool = None, force: bool = None, port: str = None) -> object`
    * with admonitions:  [🐉 Complex](/src/pynchon/gripe.py#L11 "score 8 / 7") 
  * [`pynchon.gripe.stop`](/src/pynchon/gripe.py#L204-L215) with signature `(grips=[], grip=None)`
<!--- This is a markdown file.  Comments look like this --->
-------------------------------------------------------------------------------
### pynchon.annotate
* Overview:  [source code](/src/pynchon/annotate.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
<!--- This is a markdown file.  Comments look like this --->
* Functions: (4 total)
  * [`pynchon.annotate.function`](/src/pynchon/annotate.py#L129-L177) with signature `(name, fxn) -> None`
  * [`pynchon.annotate.klass`](/src/pynchon/annotate.py#L12-L94) with signature `(name, kls) -> NoneType`
    * with admonitions:  [🐉 Complex](/src/pynchon/annotate.py#L1 "score 16 / 7") 
  * [`pynchon.annotate.module`](/src/pynchon/annotate.py#L97-L108) with signature `(name, module, working_dir=None) -> None`
  * [`pynchon.annotate.should_skip`](/src/pynchon/annotate.py#L111-L126) with signature `(name: str)`
<!--- This is a markdown file.  Comments look like this --->
-------------------------------------------------------------------------------
### pynchon.app
* Overview:  [source code](/src/pynchon/app.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
<!--- This is a markdown file.  Comments look like this --->
* Classes: (4 total)
  * [`pynchon.app.AppEvents`](/src/pynchon/app.py#L20-L23)
    * with bases ([AppBase](#fleksapp),)
  * [`pynchon.app.AppConsole`](/src/pynchon/app.py#L26-L87)
    * with bases ([AppBase](#fleksapp),)
    * with properties: (2 total)
      *  [`manager`](/src/pynchon/app.py#L37) -> inspect._empty
      *  [`status_bar`](/src/pynchon/app.py#L37) -> inspect._empty
  * [`pynchon.app.AppExitHooks`](/src/pynchon/app.py#L90-L160)
    * with bases ([AppBase](#fleksapp),)
  * [`pynchon.app.App`](/src/pynchon/app.py#L163-L171)
    * with bases ([AppConsole](#pynchonapp),[AppEvents](#pynchonapp),[AppExitHooks](#pynchonapp),)
    * with properties: (2 total)
      *  [`manager`](/src/pynchon/app.py#L37) -> inspect._empty
      *  [`status_bar`](/src/pynchon/app.py#L37) -> inspect._empty
<!--- This is a markdown file.  Comments look like this --->
-------------------------------------------------------------------------------
### pynchon.testing
* Overview:  [source code](/src/pynchon/testing.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
<!--- This is a markdown file.  Comments look like this --->
-------------------------------------------------------------------------------
### pynchon.tagging
* Overview:  [source code](/src/pynchon/tagging.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
<!--- This is a markdown file.  Comments look like this --->
-------------------------------------------------------------------------------
### pynchon.__main__
* Overview: (entrypoint) | [source code](/src/pynchon/__main__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
<!--- This is a markdown file.  Comments look like this --->
-------------------------------------------------------------------------------
### pynchon.base
* Overview:  [source code](/src/pynchon/base.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
<!--- This is a markdown file.  Comments look like this --->
* Classes: (1 total)
  * [`pynchon.base.BaseModel`](/src/pynchon/base.py#L11-L96)
    * with bases ([BaseModel](#pydanticmain),)
    * with admonitions:  [🐉 Complex](/src/pynchon/base.py#L26 "score 8 / 7") 
<!--- This is a markdown file.  Comments look like this --->
-------------------------------------------------------------------------------
### pynchon.abcs
* Overview:  [source code](/src/pynchon/abcs/__init__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
<!--- This is a markdown file.  Comments look like this --->
* Classes: (0 total)
<!--- This is a markdown file.  Comments look like this --->
-------------------------------------------------------------------------------
### pynchon.abcs.config
* Overview:  [source code](/src/pynchon/abcs/config.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
<!--- This is a markdown file.  Comments look like this --->
* Classes: (1 total)
  * [`pynchon.abcs.config.Config`](/src/pynchon/abcs/config.py#L10-L52)
    * with bases ([BaseModel](#pynchonbase),)
<!--- This is a markdown file.  Comments look like this --->
-------------------------------------------------------------------------------
### pynchon.abcs.attrdict
* Overview:  [source code](/src/pynchon/abcs/attrdict.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
<!--- This is a markdown file.  Comments look like this --->
* Classes: (2 total)
  * [`pynchon.abcs.attrdict.AttrDictBase`](/src/pynchon/abcs/attrdict.py#L9-L49)
    * with bases ([`__builtin__.object`](https://docs.python.org/3/library/functions.html#object),)
  * [`pynchon.abcs.attrdict.AttrDict`](/src/pynchon/abcs/attrdict.py#L55-L56)
    * with bases ([AttrDictBase](#pynchonabcsattrdict),[`__builtin__.dict`](https://docs.python.org/3/library/functions.html#dict),)
<!--- This is a markdown file.  Comments look like this --->
-------------------------------------------------------------------------------
### pynchon.abcs.visitor
* Overview:  [source code](/src/pynchon/abcs/visitor.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
<!--- This is a markdown file.  Comments look like this --->
* Classes: (3 total)
  * [`pynchon.abcs.visitor.Visitor`](/src/pynchon/abcs/visitor.py#L14-L52)
    * with bases ([`__builtin__.object`](https://docs.python.org/3/library/functions.html#object),)
  * [`pynchon.abcs.visitor.TemplatedDict`](/src/pynchon/abcs/visitor.py#L105-L146)
    * with bases ([`__builtin__.dict`](https://docs.python.org/3/library/functions.html#dict),)
    * with properties: (2 total)
      *  [`traversal`](/src/pynchon/abcs/visitor.py#L134) -> inspect._empty
      *  [`unresolved`](/src/pynchon/abcs/visitor.py#L143) -> inspect._empty
  * [`pynchon.abcs.visitor.JinjaDict`](/src/pynchon/abcs/visitor.py#L154-L211)
    * with bases ([TemplatedDict](#pynchonabcsvisitor),)
    * with properties: (2 total)
      *  [`traversal`](/src/pynchon/abcs/visitor.py#L134) -> inspect._empty
      *  [`unresolved`](/src/pynchon/abcs/visitor.py#L143) -> inspect._empty
<!--- This is a markdown file.  Comments look like this --->
* Functions: (1 total)
  * [`pynchon.abcs.visitor.traverse`](/src/pynchon/abcs/visitor.py#L55-L102) with signature `(obj, visitor=None, visitor_kls=None, visitor_kwargs={})`
    * with admonitions:  [🐉 Complex](/src/pynchon/abcs/visitor.py#L1 "score 10 / 7") 
<!--- This is a markdown file.  Comments look like this --->
-------------------------------------------------------------------------------
### pynchon.abcs.path
* Overview:  [source code](/src/pynchon/abcs/path.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
<!--- This is a markdown file.  Comments look like this --->
* Classes: (1 total)
  * [`pynchon.abcs.path.Path`](/src/pynchon/abcs/path.py#L11-L72)
    * with bases ([PosixPath](#pathlib),)
    * with properties: (10 total)
      *  [`anchor`](/src/pynchon/abcs/path.py#L825) -> inspect._empty
      *  [`drive`](/src/pynchon/abcs/path.py#L11) -> None
      *  [`name`](/src/pynchon/abcs/path.py#L831) -> inspect._empty
      *  [`parent`](/src/pynchon/abcs/path.py#L986) -> inspect._empty
      *  [`parents`](/src/pynchon/abcs/path.py#L996) -> inspect._empty
      *  [`parts`](/src/pynchon/abcs/path.py#L954) -> inspect._empty
      *  [`root`](/src/pynchon/abcs/path.py#L11) -> None
      *  [`stem`](/src/pynchon/abcs/path.py#L866) -> inspect._empty
      *  [`suffix`](/src/pynchon/abcs/path.py#L839) -> inspect._empty
      *  [`suffixes`](/src/pynchon/abcs/path.py#L853) -> inspect._empty
<!--- This is a markdown file.  Comments look like this --->
-------------------------------------------------------------------------------
### pynchon.util
* Overview:  [source code](/src/pynchon/util/__init__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
<!--- This is a markdown file.  Comments look like this --->
* Classes: (0 total)
<!--- This is a markdown file.  Comments look like this --->
* Functions: (3 total)
  * [`pynchon.util.find_src_root`](/src/pynchon/util/__init__.py#L40-L53) with signature `(config: dict) -> str`
  * [`pynchon.util.get_root`](/src/pynchon/util/__init__.py#L11-L28) with signature `(path: str = '.') -> str`
  * [`pynchon.util.is_python_project`](/src/pynchon/util/__init__.py#L31-L37) with signature `() -> bool`
<!--- This is a markdown file.  Comments look like this --->
-------------------------------------------------------------------------------
### pynchon.util.click
* Overview:  [source code](/src/pynchon/util/click.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
<!--- This is a markdown file.  Comments look like this --->
-------------------------------------------------------------------------------
### pynchon.util.config
* Overview:  [source code](/src/pynchon/util/config.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
<!--- This is a markdown file.  Comments look like this --->
-------------------------------------------------------------------------------
### pynchon.util.events
* Overview:  [source code](/src/pynchon/util/events.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
<!--- This is a markdown file.  Comments look like this --->
* Classes: (1 total)
  * [`pynchon.util.events.Engine`](/src/pynchon/util/events.py#L11-L24)
    * with bases ([`__builtin__.object`](https://docs.python.org/3/library/functions.html#object),)
<!--- This is a markdown file.  Comments look like this --->
-------------------------------------------------------------------------------
### pynchon.util.splitvt
* Overview:  [source code](/src/pynchon/util/splitvt.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
<!--- This is a markdown file.  Comments look like this --->
-------------------------------------------------------------------------------
### pynchon.util.complexity
* Overview:  [source code](/src/pynchon/util/complexity.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
<!--- This is a markdown file.  Comments look like this --->
* Classes: (1 total)
  * [`pynchon.util.complexity.Checker`](/src/pynchon/util/complexity.py#L144-L156)
    * with bases ([McCabeChecker](#mccabe),)
<!--- This is a markdown file.  Comments look like this --->
* Functions: (5 total)
  * [`pynchon.util.complexity.clean_text`](/src/pynchon/util/complexity.py#L21-L28) with signature `(txt: str) -> str`
  * [`pynchon.util.complexity.complexity`](/src/pynchon/util/complexity.py#L159-L197) with signature `(code: str = None, fname: str = None, threshold: int = 7)`
  * [`pynchon.util.complexity.get_module`](/src/pynchon/util/complexity.py#L31-L56) with signature `(package: str = '', file: str = '')`
  * [`pynchon.util.complexity.get_refs`](/src/pynchon/util/complexity.py#L59-L87) with signature `(working_dir=None, module=None) -> dict`
  * [`pynchon.util.complexity.visit_module`](/src/pynchon/util/complexity.py#L90-L141)
    * with signature `(output=['<!--- This is a markdown file.  Comments look like this --->\n-------------------------------------------------------------------------------\n### pynchon\n* Overview:  [source code](/src/pynchon/__init__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)\n<!--- This is a markdown file.  Comments look like this --->\n* Classes: (0 total)', '<!--- This is a markdown file.  Comments look like this --->\n-------------------------------------------------------------------------------\n### pynchon.events\n* Overview:  [source code](/src/pynchon/events.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)\n<!--- This is a markdown file.  Comments look like this --->\n* Classes: (1 total)\n  * [`pynchon.events.Signal`](/src/pynchon/events.py#L11-L16)\n    * with bases ([Signal](#blinkerbase),)\n<!--- This is a markdown file.  Comments look like this --->\n* Functions: (6 total)\n  * [`pynchon.events._lifecycle`](/src/pynchon/events.py#L74-L86) with signature ``\n  * [`pynchon.events.lifecycle_applying`](/src/pynchon/events.py#L43-L48) with signature `(sender, applying=None, **kwargs)`\n  * [`pynchon.events.lifecycle_config`](/src/pynchon/events.py#L34-L40) with signature `(sender, config)`\n  * [`pynchon.events.lifecycle_msg`](/src/pynchon/events.py#L63-L70) with signature `(sender, msg=None, **unused)`\n  * [`pynchon.events.lifecycle_plugin`](/src/pynchon/events.py#L25-L31) with signature `(sender, plugin)`\n  * [`pynchon.events.lifecycle_stage`](/src/pynchon/events.py#L51-L60) with signature `(sender, stage=None, **unused)`', '<!--- This is a markdown file.  Comments look like this --->\n-------------------------------------------------------------------------------\n### pynchon.constants\n* Overview:  [source code](/src/pynchon/constants.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)', '<!--- This is a markdown file.  Comments look like this --->\n-------------------------------------------------------------------------------\n### pynchon.bin\n* Overview:  [source code](/src/pynchon/bin.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)\n<!--- This is a markdown file.  Comments look like this --->\n* Classes: (1 total)\n  * [`pynchon.bin.RootGroup`](/src/pynchon/bin.py#L20-L25)\n    * with bases ([RootGroup](#flekscliroot_group),)\n<!--- This is a markdown file.  Comments look like this --->\n* Functions: (3 total)\n  * [`pynchon.bin.bootstrap`](/src/pynchon/bin.py#L45-L72) with signature `()`\n  * [`pynchon.bin.default`](/src/pynchon/bin.py#L75-L96) with signature `(*args: Any, **kwargs: Any) -> Any`\n  * [`pynchon.bin.entry`](/src/pynchon/bin.py#L28-L42) with signature `(*args: Any, **kwargs: Any) -> Any`', '<!--- This is a markdown file.  Comments look like this --->\n-------------------------------------------------------------------------------\n### pynchon.core\n* Overview:  [source code](/src/pynchon/core.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)\n<!--- This is a markdown file.  Comments look like this --->\n* Classes: (1 total)\n  * [`pynchon.core.Config`](/src/pynchon/core.py#L60-L134)\n    * with bases ([Config](#pynchonabcsconfig),)\n    * with properties: (4 total)\n      *  [`plugins`](/src/pynchon/core.py#L114) -> inspect._empty\n      *  [`root`](/src/pynchon/core.py#L98) -> str\n      *  [`version`](/src/pynchon/core.py#L92) -> str\n      *  [`working_dir`](/src/pynchon/core.py#L131) -> inspect._empty\n<!--- This is a markdown file.  Comments look like this --->\n* Functions: (1 total)\n  * [`pynchon.core.validate`](/src/pynchon/core.py#L13-L54) with signature `(kls=None, self=None, vdata=None)`\n    * with admonitions:  [🐉 Complex](/src/pynchon/core.py#L1 "score 10 / 7") ', '<!--- This is a markdown file.  Comments look like this --->\n-------------------------------------------------------------------------------\n### pynchon.gripe\n* Overview:  [source code](/src/pynchon/gripe.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)\n<!--- This is a markdown file.  Comments look like this --->\n* Classes: (2 total)\n  * [`pynchon.gripe.PortBusy`](/src/pynchon/gripe.py#L23-L24)\n    * with bases ([`__builtin__.RuntimeError`](https://docs.python.org/3/library/functions.html#RuntimeError),)\n  * [`pynchon.gripe.Server`](/src/pynchon/gripe.py#L72-L113)\n    * with bases ([`__builtin__.object`](https://docs.python.org/3/library/functions.html#object),)\n    * with properties: (5 total)\n      *  [`app`](/src/pynchon/gripe.py#L106) -> inspect._empty\n      *  [`live`](/src/pynchon/gripe.py#L83) -> bool\n      *  [`port`](/src/pynchon/gripe.py#L88) -> inspect._empty\n      *  [`proc`](/src/pynchon/gripe.py#L75) -> psutil.Process\n      *  [`raw_file_server`](/src/pynchon/gripe.py#L93) -> inspect._empty\n<!--- This is a markdown file.  Comments look like this --->\n* Functions: (10 total)\n  * [`pynchon.gripe._current_gripe_procs`](/src/pynchon/gripe.py#L27-L29) with signature ``\n  * [`pynchon.gripe._do_serve`](/src/pynchon/gripe.py#L49-L62) with signature ``\n  * [`pynchon.gripe._is_my_grip`](/src/pynchon/gripe.py#L65-L69) with signature ``\n  * [`pynchon.gripe._list`](/src/pynchon/gripe.py#L127-L144) with signature ``\n  * [`pynchon.gripe._used_ports`](/src/pynchon/gripe.py#L42-L46) with signature ``\n  * [`pynchon.gripe.entry`](/src/pynchon/gripe.py#L120-L124) with signature `(*args: Any, **kwargs: Any) -> Any`\n  * [`pynchon.gripe.get_port`](/src/pynchon/gripe.py#L32-L39) with signature `(proc)`\n  * [`pynchon.gripe.restart`](/src/pynchon/gripe.py#L218-L223) with signature `()`\n  * [`pynchon.gripe.start`](/src/pynchon/gripe.py#L147-L201)\n    * with signature `(fg: bool = None, ls: bool = None, force: bool = None, port: str = None) -> object`\n    * with admonitions:  [🐉 Complex](/src/pynchon/gripe.py#L11 "score 8 / 7") \n  * [`pynchon.gripe.stop`](/src/pynchon/gripe.py#L204-L215) with signature `(grips=[], grip=None)`', '<!--- This is a markdown file.  Comments look like this --->\n-------------------------------------------------------------------------------\n### pynchon.annotate\n* Overview:  [source code](/src/pynchon/annotate.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)\n<!--- This is a markdown file.  Comments look like this --->\n* Functions: (4 total)\n  * [`pynchon.annotate.function`](/src/pynchon/annotate.py#L129-L177) with signature `(name, fxn) -> None`\n  * [`pynchon.annotate.klass`](/src/pynchon/annotate.py#L12-L94) with signature `(name, kls) -> NoneType`\n    * with admonitions:  [🐉 Complex](/src/pynchon/annotate.py#L1 "score 16 / 7") \n  * [`pynchon.annotate.module`](/src/pynchon/annotate.py#L97-L108) with signature `(name, module, working_dir=None) -> None`\n  * [`pynchon.annotate.should_skip`](/src/pynchon/annotate.py#L111-L126) with signature `(name: str)`', '<!--- This is a markdown file.  Comments look like this --->\n-------------------------------------------------------------------------------\n### pynchon.app\n* Overview:  [source code](/src/pynchon/app.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)\n<!--- This is a markdown file.  Comments look like this --->\n* Classes: (4 total)\n  * [`pynchon.app.AppEvents`](/src/pynchon/app.py#L20-L23)\n    * with bases ([AppBase](#fleksapp),)\n  * [`pynchon.app.AppConsole`](/src/pynchon/app.py#L26-L87)\n    * with bases ([AppBase](#fleksapp),)\n    * with properties: (2 total)\n      *  [`manager`](/src/pynchon/app.py#L37) -> inspect._empty\n      *  [`status_bar`](/src/pynchon/app.py#L37) -> inspect._empty\n  * [`pynchon.app.AppExitHooks`](/src/pynchon/app.py#L90-L160)\n    * with bases ([AppBase](#fleksapp),)\n  * [`pynchon.app.App`](/src/pynchon/app.py#L163-L171)\n    * with bases ([AppConsole](#pynchonapp),[AppEvents](#pynchonapp),[AppExitHooks](#pynchonapp),)\n    * with properties: (2 total)\n      *  [`manager`](/src/pynchon/app.py#L37) -> inspect._empty\n      *  [`status_bar`](/src/pynchon/app.py#L37) -> inspect._empty', '<!--- This is a markdown file.  Comments look like this --->\n-------------------------------------------------------------------------------\n### pynchon.testing\n* Overview:  [source code](/src/pynchon/testing.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)', '<!--- This is a markdown file.  Comments look like this --->\n-------------------------------------------------------------------------------\n### pynchon.tagging\n* Overview:  [source code](/src/pynchon/tagging.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)', '<!--- This is a markdown file.  Comments look like this --->\n-------------------------------------------------------------------------------\n### pynchon.__main__\n* Overview: (entrypoint) | [source code](/src/pynchon/__main__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)', '<!--- This is a markdown file.  Comments look like this --->\n-------------------------------------------------------------------------------\n### pynchon.base\n* Overview:  [source code](/src/pynchon/base.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)\n<!--- This is a markdown file.  Comments look like this --->\n* Classes: (1 total)\n  * [`pynchon.base.BaseModel`](/src/pynchon/base.py#L11-L96)\n    * with bases ([BaseModel](#pydanticmain),)\n    * with admonitions:  [🐉 Complex](/src/pynchon/base.py#L26 "score 8 / 7") ', '<!--- This is a markdown file.  Comments look like this --->\n-------------------------------------------------------------------------------\n### pynchon.abcs\n* Overview:  [source code](/src/pynchon/abcs/__init__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)\n<!--- This is a markdown file.  Comments look like this --->\n* Classes: (0 total)', '<!--- This is a markdown file.  Comments look like this --->\n-------------------------------------------------------------------------------\n### pynchon.abcs.config\n* Overview:  [source code](/src/pynchon/abcs/config.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)\n<!--- This is a markdown file.  Comments look like this --->\n* Classes: (1 total)\n  * [`pynchon.abcs.config.Config`](/src/pynchon/abcs/config.py#L10-L52)\n    * with bases ([BaseModel](#pynchonbase),)', '<!--- This is a markdown file.  Comments look like this --->\n-------------------------------------------------------------------------------\n### pynchon.abcs.attrdict\n* Overview:  [source code](/src/pynchon/abcs/attrdict.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)\n<!--- This is a markdown file.  Comments look like this --->\n* Classes: (2 total)\n  * [`pynchon.abcs.attrdict.AttrDictBase`](/src/pynchon/abcs/attrdict.py#L9-L49)\n    * with bases ([`__builtin__.object`](https://docs.python.org/3/library/functions.html#object),)\n  * [`pynchon.abcs.attrdict.AttrDict`](/src/pynchon/abcs/attrdict.py#L55-L56)\n    * with bases ([AttrDictBase](#pynchonabcsattrdict),[`__builtin__.dict`](https://docs.python.org/3/library/functions.html#dict),)', '<!--- This is a markdown file.  Comments look like this --->\n-------------------------------------------------------------------------------\n### pynchon.abcs.visitor\n* Overview:  [source code](/src/pynchon/abcs/visitor.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)\n<!--- This is a markdown file.  Comments look like this --->\n* Classes: (3 total)\n  * [`pynchon.abcs.visitor.Visitor`](/src/pynchon/abcs/visitor.py#L14-L52)\n    * with bases ([`__builtin__.object`](https://docs.python.org/3/library/functions.html#object),)\n  * [`pynchon.abcs.visitor.TemplatedDict`](/src/pynchon/abcs/visitor.py#L105-L146)\n    * with bases ([`__builtin__.dict`](https://docs.python.org/3/library/functions.html#dict),)\n    * with properties: (2 total)\n      *  [`traversal`](/src/pynchon/abcs/visitor.py#L134) -> inspect._empty\n      *  [`unresolved`](/src/pynchon/abcs/visitor.py#L143) -> inspect._empty\n  * [`pynchon.abcs.visitor.JinjaDict`](/src/pynchon/abcs/visitor.py#L154-L211)\n    * with bases ([TemplatedDict](#pynchonabcsvisitor),)\n    * with properties: (2 total)\n      *  [`traversal`](/src/pynchon/abcs/visitor.py#L134) -> inspect._empty\n      *  [`unresolved`](/src/pynchon/abcs/visitor.py#L143) -> inspect._empty\n<!--- This is a markdown file.  Comments look like this --->\n* Functions: (1 total)\n  * [`pynchon.abcs.visitor.traverse`](/src/pynchon/abcs/visitor.py#L55-L102) with signature `(obj, visitor=None, visitor_kls=None, visitor_kwargs={})`\n    * with admonitions:  [🐉 Complex](/src/pynchon/abcs/visitor.py#L1 "score 10 / 7") ', '<!--- This is a markdown file.  Comments look like this --->\n-------------------------------------------------------------------------------\n### pynchon.abcs.path\n* Overview:  [source code](/src/pynchon/abcs/path.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)\n<!--- This is a markdown file.  Comments look like this --->\n* Classes: (1 total)\n  * [`pynchon.abcs.path.Path`](/src/pynchon/abcs/path.py#L11-L72)\n    * with bases ([PosixPath](#pathlib),)\n    * with properties: (10 total)\n      *  [`anchor`](/src/pynchon/abcs/path.py#L825) -> inspect._empty\n      *  [`drive`](/src/pynchon/abcs/path.py#L11) -> None\n      *  [`name`](/src/pynchon/abcs/path.py#L831) -> inspect._empty\n      *  [`parent`](/src/pynchon/abcs/path.py#L986) -> inspect._empty\n      *  [`parents`](/src/pynchon/abcs/path.py#L996) -> inspect._empty\n      *  [`parts`](/src/pynchon/abcs/path.py#L954) -> inspect._empty\n      *  [`root`](/src/pynchon/abcs/path.py#L11) -> None\n      *  [`stem`](/src/pynchon/abcs/path.py#L866) -> inspect._empty\n      *  [`suffix`](/src/pynchon/abcs/path.py#L839) -> inspect._empty\n      *  [`suffixes`](/src/pynchon/abcs/path.py#L853) -> inspect._empty', "<!--- This is a markdown file.  Comments look like this --->\n-------------------------------------------------------------------------------\n### pynchon.util\n* Overview:  [source code](/src/pynchon/util/__init__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)\n<!--- This is a markdown file.  Comments look like this --->\n* Classes: (0 total)\n<!--- This is a markdown file.  Comments look like this --->\n* Functions: (3 total)\n  * [`pynchon.util.find_src_root`](/src/pynchon/util/__init__.py#L40-L53) with signature `(config: dict) -> str`\n  * [`pynchon.util.get_root`](/src/pynchon/util/__init__.py#L11-L28) with signature `(path: str = '.') -> str`\n  * [`pynchon.util.is_python_project`](/src/pynchon/util/__init__.py#L31-L37) with signature `() -> bool`", '<!--- This is a markdown file.  Comments look like this --->\n-------------------------------------------------------------------------------\n### pynchon.util.click\n* Overview:  [source code](/src/pynchon/util/click.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)', '<!--- This is a markdown file.  Comments look like this --->\n-------------------------------------------------------------------------------\n### pynchon.util.config\n* Overview:  [source code](/src/pynchon/util/config.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)', '<!--- This is a markdown file.  Comments look like this --->\n-------------------------------------------------------------------------------\n### pynchon.util.events\n* Overview:  [source code](/src/pynchon/util/events.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)\n<!--- This is a markdown file.  Comments look like this --->\n* Classes: (1 total)\n  * [`pynchon.util.events.Engine`](/src/pynchon/util/events.py#L11-L24)\n    * with bases ([`__builtin__.object`](https://docs.python.org/3/library/functions.html#object),)', '<!--- This is a markdown file.  Comments look like this --->\n-------------------------------------------------------------------------------\n### pynchon.util.splitvt\n* Overview:  [source code](/src/pynchon/util/splitvt.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)'], stats={}, module=None, template=None, visited=[], exclude: list = [], module_name=None, working_dir=Path('.'))`
<!--- This is a markdown file.  Comments look like this --->
-------------------------------------------------------------------------------
### pynchon.util.docker
* Overview:  [source code](/src/pynchon/util/docker.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
<!--- This is a markdown file.  Comments look like this --->
* Classes: (1 total)
  * [`pynchon.util.docker.DockerCtx`](/src/pynchon/util/docker.py#L10-L129)
    * with bases ([`__builtin__.object`](https://docs.python.org/3/library/functions.html#object),)
    * with properties: (6 total)
      *  [`fhandle`](/src/pynchon/util/docker.py#L89) -> inspect._empty
      *  [`file`](/src/pynchon/util/docker.py#L85) -> inspect._empty
      *  [`has_bash`](/src/pynchon/util/docker.py#L127) -> inspect._empty
      *  [`has_sh`](/src/pynchon/util/docker.py#L122) -> inspect._empty
      *  [`name`](/src/pynchon/util/docker.py#L75) -> inspect._empty
      *  [`tag`](/src/pynchon/util/docker.py#L81) -> inspect._empty
<!--- This is a markdown file.  Comments look like this --->
* Functions: (1 total)
  * [`pynchon.util.docker.Dockerfile`](/src/pynchon/util/docker.py#L132-L133) with signature `(txt, **kwargs)`
<!--- This is a markdown file.  Comments look like this --->
-------------------------------------------------------------------------------
### pynchon.util.oop
* Overview:  [source code](/src/pynchon/util/oop.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
<!--- This is a markdown file.  Comments look like this --->
* Classes: (2 total)
  * [`pynchon.util.oop.classproperty`](/src/pynchon/util/oop.py#L34-L41)
    * with bases ([`__builtin__.object`](https://docs.python.org/3/library/functions.html#object),)
  * [`pynchon.util.oop.classproperty_cached`](/src/pynchon/util/oop.py#L44-L52)
    * with bases ([classproperty](#pynchonutiloop),)
<!--- This is a markdown file.  Comments look like this --->
* Functions: (2 total)
  * [`pynchon.util.oop.is_subclass`](/src/pynchon/util/oop.py#L19-L31) with signature `(x, y, strict=True)`
  * [`pynchon.util.oop.new_in_class`](/src/pynchon/util/oop.py#L6-L16) with signature `(name: str, kls: Type)`
<!--- This is a markdown file.  Comments look like this --->
-------------------------------------------------------------------------------
### pynchon.util.python
* Overview:  [source code](/src/pynchon/util/python.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
<!--- This is a markdown file.  Comments look like this --->
* Functions: (3 total)
  * [`pynchon.util.python.is_package`](/src/pynchon/util/python.py#L10-L22) with signature `(folder: str) -> bool`
  * [`pynchon.util.python.load_entrypoints`](/src/pynchon/util/python.py#L40-L72) with signature `(config=None) -> dict`
  * [`pynchon.util.python.load_setupcfg`](/src/pynchon/util/python.py#L25-L37) with signature `(file: str = '', folder: str = '')`
<!--- This is a markdown file.  Comments look like this --->
-------------------------------------------------------------------------------
### pynchon.util.typing
* Overview:  [source code](/src/pynchon/util/typing.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
<!--- This is a markdown file.  Comments look like this --->
* Functions: (1 total)
  * [`pynchon.util.typing.bind_method`](/src/pynchon/util/typing.py#L22-L37) with signature `(func, instance, as_name=None)`
<!--- This is a markdown file.  Comments look like this --->
-------------------------------------------------------------------------------
### pynchon.util.testing
* Overview:  [source code](/src/pynchon/util/testing.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
<!--- This is a markdown file.  Comments look like this --->
* Functions: (1 total)
  * [`pynchon.util.testing.get_test_info`](/src/pynchon/util/testing.py#L9-L22) with signature `(fname: str) -> dict`
<!--- This is a markdown file.  Comments look like this --->
-------------------------------------------------------------------------------
### pynchon.util.lme
* Overview:  [source code](/src/pynchon/util/lme.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
<!--- This is a markdown file.  Comments look like this --->
* Classes: (1 total)
  * [`pynchon.util.lme.Fake`](/src/pynchon/util/lme.py#L53-L54)
    * with bases ([`__builtin__.object`](https://docs.python.org/3/library/functions.html#object),)
<!--- This is a markdown file.  Comments look like this --->
* Functions: (2 total)
  * [`pynchon.util.lme.get_logger`](/src/pynchon/util/lme.py#L60-L95) with signature `(name, console=<console width=106 None>, fake=False)`
  * [`pynchon.util.lme.set_global_level`](/src/pynchon/util/lme.py#L41-L50) with signature `(level)`
<!--- This is a markdown file.  Comments look like this --->
-------------------------------------------------------------------------------
### pynchon.util.makefile
* Overview:  [source code](/src/pynchon/util/makefile/__init__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
<!--- This is a markdown file.  Comments look like this --->
* Classes: (0 total)
<!--- This is a markdown file.  Comments look like this --->
* Functions: (5 total)
  * [`pynchon.util.makefile._get_file`](/src/pynchon/util/makefile/__init__.py#L58-L63) with signature ``
  * [`pynchon.util.makefile._get_prov_line`](/src/pynchon/util/makefile/__init__.py#L51-L55) with signature ``
  * [`pynchon.util.makefile._test`](/src/pynchon/util/makefile/__init__.py#L39-L48) with signature ``
  * [`pynchon.util.makefile.database`](/src/pynchon/util/makefile/__init__.py#L17-L36) with signature `(makefile: str = '', make='make') -> List[str]`
  * [`pynchon.util.makefile.parse`](/src/pynchon/util/makefile/__init__.py#L66-L161) with signature `(makefile: str = None, bodies=False, **kwargs)`
    * with admonitions:  [🐉 Complex](/src/pynchon/util/makefile/__init__.py#L2 "score 19 / 7") 
<!--- This is a markdown file.  Comments look like this --->
-------------------------------------------------------------------------------
### pynchon.util.makefile.__main__
* Overview: (entrypoint) | [source code](/src/pynchon/util/makefile/__main__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
<!--- This is a markdown file.  Comments look like this --->
-------------------------------------------------------------------------------
### pynchon.util.files
* Overview:  [source code](/src/pynchon/util/files/__init__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
<!--- This is a markdown file.  Comments look like this --->
* Classes: (0 total)
<!--- This is a markdown file.  Comments look like this --->
* Functions: (7 total)
  * [`pynchon.util.files.dumps`](/src/pynchon/util/files/__init__.py#L137-L144)
    * with signature `(content: str = None, file: str = None, quiet: bool = True, logger=<bound method Logger.info of <Logger pynchon.util.files (WARNING)>>) -> None`
  * [`pynchon.util.files.find_globs`](/src/pynchon/util/files/__init__.py#L113-L134)
    * with signature `(globs: List[pynchon.abcs.path.Path], includes=[], logger: object = None, quiet: bool = False) -> List[str]`
  * [`pynchon.util.files.find_src`](/src/pynchon/util/files/__init__.py#L92-L110) with signature `(src_root: str, exclude_patterns=[], quiet: bool = False) -> list`
  * [`pynchon.util.files.find_suffix`](/src/pynchon/util/files/__init__.py#L68-L73) with signature `(root: str = '', suffix: str = '') -> Optional[str]`
  * [`pynchon.util.files.get_git_root`](/src/pynchon/util/files/__init__.py#L76-L89) with signature `(path: str = '.') -> Optional[str]`
  * [`pynchon.util.files.is_prefix`](/src/pynchon/util/files/__init__.py#L18-L38)
    * with signature `(prepend_file: str = None, target_file: str = None, clean: bool = False) -> str`
  * [`pynchon.util.files.prepend`](/src/pynchon/util/files/__init__.py#L41-L65)
    * with signature `(prepend_file: str = None, target_file: str = None, clean: bool = False) -> bool`
<!--- This is a markdown file.  Comments look like this --->
-------------------------------------------------------------------------------
### pynchon.util.files.diff
* Overview:  [source code](/src/pynchon/util/files/diff.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
<!--- This is a markdown file.  Comments look like this --->
* Functions: (4 total)
  * [`pynchon.util.files.diff.diff`](/src/pynchon/util/files/diff.py#L70-L82) with signature `(file1: str = None, file2: str = None)`
  * [`pynchon.util.files.diff.diff_percent`](/src/pynchon/util/files/diff.py#L32-L45) with signature `(file1: str = None, file2: str = None)`
  * [`pynchon.util.files.diff.diff_report`](/src/pynchon/util/files/diff.py#L12-L29)
    * with signature `(diff, logger=<bound method Logger.debug of <Logger pynchon.util.files.diff (WARNING)>>)`
  * [`pynchon.util.files.diff.strdiff`](/src/pynchon/util/files/diff.py#L48-L64) with signature `(str1: str = None, str2: str = None, n=1)`
<!--- This is a markdown file.  Comments look like this --->
-------------------------------------------------------------------------------
### pynchon.util.files.__main__
* Overview: (entrypoint) | [source code](/src/pynchon/util/files/__main__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
<!--- This is a markdown file.  Comments look like this --->
-------------------------------------------------------------------------------
### pynchon.util.os
* Overview:  [source code](/src/pynchon/util/os/__init__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
<!--- This is a markdown file.  Comments look like this --->
* Classes: (0 total)
<!--- This is a markdown file.  Comments look like this --->
* Functions: (1 total)
  * [`pynchon.util.os.slurp_json`](/src/pynchon/util/os/__init__.py#L19-L25) with signature `(cmd: str, **kwargs)`
<!--- This is a markdown file.  Comments look like this --->
-------------------------------------------------------------------------------
### pynchon.util.os.pidfile
* Overview:  [source code](/src/pynchon/util/os/pidfile.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
<!--- This is a markdown file.  Comments look like this --->
-------------------------------------------------------------------------------
### pynchon.util.os.models
* Overview:  [source code](/src/pynchon/util/os/models.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
<!--- This is a markdown file.  Comments look like this --->
-------------------------------------------------------------------------------
### pynchon.util.os.pids
* Overview:  [source code](/src/pynchon/util/os/pids.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
<!--- This is a markdown file.  Comments look like this --->
* Functions: (1 total)
  * [`pynchon.util.os.pids.filter_pids`](/src/pynchon/util/os/pids.py#L12-L41) with signature `(cmdline__contains: str = None, **kwargs)`
    * with admonitions:  [🐉 Complex](/src/pynchon/util/os/pids.py#L1 "score 13 / 7") 
<!--- This is a markdown file.  Comments look like this --->
-------------------------------------------------------------------------------
### pynchon.util.text
* Overview:  [source code](/src/pynchon/util/text/__init__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
<!--- This is a markdown file.  Comments look like this --->
* Classes: (0 total)
<!--- This is a markdown file.  Comments look like this --->
* Functions: (1 total)
  * [`pynchon.util.text.indent`](/src/pynchon/util/text/__init__.py#L11-L22) with signature `(txt: str, level: int = 2) -> str`
<!--- This is a markdown file.  Comments look like this --->
-------------------------------------------------------------------------------
### pynchon.util.text.loads
* Overview:  [source code](/src/pynchon/util/text/loads.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
<!--- This is a markdown file.  Comments look like this --->
* Functions: (5 total)
  * [`pynchon.util.text.loads.ini`](/src/pynchon/util/text/loads.py#L14-L21) with signature `(content: str) -> Optional[str]`
  * [`pynchon.util.text.loads.json`](/src/pynchon/util/text/loads.py#L44-L53) with signature `(content: str = '') -> Optional[str]`
  * [`pynchon.util.text.loads.json5`](/src/pynchon/util/text/loads.py#L56-L80) with signature `(content: str = '', quiet=True) -> Optional[str]`
  * [`pynchon.util.text.loads.toml`](/src/pynchon/util/text/loads.py#L34-L41) with signature `(content: str) -> Optional[str]`
  * [`pynchon.util.text.loads.yaml`](/src/pynchon/util/text/loads.py#L24-L31) with signature `(content: str) -> Optional[str]`
<!--- This is a markdown file.  Comments look like this --->
-------------------------------------------------------------------------------
### pynchon.util.text.dumps
* Overview:  [source code](/src/pynchon/util/text/dumps.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
<!--- This is a markdown file.  Comments look like this --->
* Classes: (1 total)
  * [`pynchon.util.text.dumps.JSONEncoder`](/src/pynchon/util/text/dumps.py#L11-L41)
    * with bases ([JSONEncoder](#jsonencoder),)
<!--- This is a markdown file.  Comments look like this --->
* Functions: (2 total)
  * [`pynchon.util.text.dumps.json`](/src/pynchon/util/text/dumps.py#L54-L59) with signature `(obj, cls=None, minified=False, indent: int = 2) -> str`
  * [`pynchon.util.text.dumps.yaml`](/src/pynchon/util/text/dumps.py#L44-L51) with signature `(file=None, content=None, obj=None)`
<!--- This is a markdown file.  Comments look like this --->
-------------------------------------------------------------------------------
### pynchon.util.text.__main__
* Overview: (entrypoint) | [source code](/src/pynchon/util/text/__main__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
<!--- This is a markdown file.  Comments look like this --->
-------------------------------------------------------------------------------
### pynchon.util.text.loadf
* Overview:  [source code](/src/pynchon/util/text/loadf/__init__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
<!--- This is a markdown file.  Comments look like this --->
* Classes: (0 total)
<!--- This is a markdown file.  Comments look like this --->
* Functions: (6 total)
  * [`pynchon.util.text.loadf.ini`](/src/pynchon/util/text/loadf/__init__.py#L29-L41) with signature `(file)`
  * [`pynchon.util.text.loadf.json`](/src/pynchon/util/text/loadf/__init__.py#L220-L241) with signature `(file: str = '', content: str = '', strict: bool = True) -> dict`
  * [`pynchon.util.text.loadf.json5`](/src/pynchon/util/text/loadf/__init__.py#L93-L217)
    * with signature `(file: str = '', files: List[str] = [], output: str = '', should_print: bool = False, wrapper_key: str = '', pull: str = '', push_data: str = '', push_file_data: str = '', push_json_data: str = '', push_command_output: str = '', under_key: str = '') -> None`
    * with admonitions:  [🐉 Complex](/src/pynchon/util/text/loadf/__init__.py#L28 "score 12 / 7") 
  * [`pynchon.util.text.loadf.loadf`](/src/pynchon/util/text/loadf/__init__.py#L18-L26) with signature `(file=None, content=None)`
  * [`pynchon.util.text.loadf.toml`](/src/pynchon/util/text/loadf/__init__.py#L54-L76) with signature `(file: str = None, strict: bool = True)`
  * [`pynchon.util.text.loadf.yaml`](/src/pynchon/util/text/loadf/__init__.py#L44-L51) with signature `(*args, **kwargs)`
<!--- This is a markdown file.  Comments look like this --->
-------------------------------------------------------------------------------
### pynchon.util.text.loadf.__main__
* Overview: (entrypoint) | [source code](/src/pynchon/util/text/loadf/__main__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
<!--- This is a markdown file.  Comments look like this --->
-------------------------------------------------------------------------------
### pynchon.util.text.dumpf
* Overview:  [source code](/src/pynchon/util/text/dumpf/__init__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
<!--- This is a markdown file.  Comments look like this --->
* Classes: (0 total)
<!--- This is a markdown file.  Comments look like this --->
* Functions: (2 total)
  * [`pynchon.util.text.dumpf.json`](/src/pynchon/util/text/dumpf/__init__.py#L14-L18) with signature `(obj, file=None, **kwargs) -> None`
  * [`pynchon.util.text.dumpf.yaml`](/src/pynchon/util/text/dumpf/__init__.py#L21-L31) with signature `(file=None, output=None, **kwargs)`
<!--- This is a markdown file.  Comments look like this --->
-------------------------------------------------------------------------------
### pynchon.util.text.dumpf.__main__
* Overview: (entrypoint) | [source code](/src/pynchon/util/text/dumpf/__main__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
<!--- This is a markdown file.  Comments look like this --->
-------------------------------------------------------------------------------
### pynchon.util.text.render
* Overview:  [source code](/src/pynchon/util/text/render/__init__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
<!--- This is a markdown file.  Comments look like this --->
* Classes: (0 total)
<!--- This is a markdown file.  Comments look like this --->
* Functions: (4 total)
  * [`pynchon.util.text.render.j2cli`](/src/pynchon/util/text/render/__init__.py#L186-L229)
    * with signature `(output: str, should_print: bool, file: str, context: str, format: str = 'json') -> None`
  * [`pynchon.util.text.render.jinja`](/src/pynchon/util/text/render/__init__.py#L20-L63)
    * with signature `(text: str = '', file: str = '?', context: dict = {}, includes: List[str] = [], strict: bool = True)`
  * [`pynchon.util.text.render.jinja_file`](/src/pynchon/util/text/render/__init__.py#L102-L183)
    * with signature `(file: str, output: Optional[str] = '', should_print: bool = False, in_place: bool = False, context: Dict = {}, context_file: Dict = {}, includes: List[str] = [], strict: bool = True) -> str`
  * [`pynchon.util.text.render.jinja_loadf`](/src/pynchon/util/text/render/__init__.py#L66-L99)
    * with signature `(file: str, context: Dict = {}, includes: List[str] = [], strict: bool = True, quiet: bool = False) -> str`
<!--- This is a markdown file.  Comments look like this --->
-------------------------------------------------------------------------------
### pynchon.util.text.render.__main__
* Overview: (entrypoint) | [source code](/src/pynchon/util/text/render/__main__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
<!--- This is a markdown file.  Comments look like this --->
-------------------------------------------------------------------------------
### pynchon.util.text.normalize
* Overview:  [source code](/src/pynchon/util/text/normalize/__init__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
<!--- This is a markdown file.  Comments look like this --->
* Functions: (2 total)
  * [`pynchon.util.text.normalize.normalize`](/src/pynchon/util/text/normalize/__init__.py#L21-L48)
    * with signature `(txt: str = '', post: List[Callable] = [<function <lambda> at 0x1114e9160>, <function <lambda> at 0x1114e9040>], rules: List[Callable] = {' ': '_', '/': '_', '-': '_'}) -> str`
  * [`pynchon.util.text.normalize.snake_case`](/src/pynchon/util/text/normalize/__init__.py#L7-L15) with signature `(name: str) -> str`
<!--- This is a markdown file.  Comments look like this --->
-------------------------------------------------------------------------------
### pynchon.util.console
* Overview:  [source code](/src/pynchon/util/console/__init__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
<!--- This is a markdown file.  Comments look like this --->
* Classes: (0 total)
<!--- This is a markdown file.  Comments look like this --->
-------------------------------------------------------------------------------
### pynchon.util.console.__main__
* Overview: (entrypoint) | [source code](/src/pynchon/util/console/__main__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
<!--- This is a markdown file.  Comments look like this --->
-------------------------------------------------------------------------------
### pynchon.config
* Overview:  [source code](/src/pynchon/config/__init__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
<!--- This is a markdown file.  Comments look like this --->
* Classes: (0 total)
<!--- This is a markdown file.  Comments look like this --->
-------------------------------------------------------------------------------
### pynchon.config.util
* Overview:  [source code](/src/pynchon/config/util.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
<!--- This is a markdown file.  Comments look like this --->
* Functions: (4 total)
  * [`pynchon.config.util.config_folders`](/src/pynchon/config/util.py#L107-L111) with signature `()`
  * [`pynchon.config.util.finalize`](/src/pynchon/config/util.py#L18-L104) with signature `()`
  * [`pynchon.config.util.get_config_files`](/src/pynchon/config/util.py#L114-L132) with signature `()`
  * [`pynchon.config.util.load_config_from_files`](/src/pynchon/config/util.py#L135-L155) with signature `() -> Dict[str, str]`
<!--- This is a markdown file.  Comments look like this --->
-------------------------------------------------------------------------------
### pynchon.plugins
* Overview:  [source code](/src/pynchon/plugins/__init__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
<!--- This is a markdown file.  Comments look like this --->
* Classes: (0 total)
<!--- This is a markdown file.  Comments look like this --->
-------------------------------------------------------------------------------
### pynchon.plugins.plugins
* Overview:  [source code](/src/pynchon/plugins/plugins.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
<!--- This is a markdown file.  Comments look like this --->
* Classes: (1 total)
  * [`pynchon.plugins.plugins.PluginsMan`](/src/pynchon/plugins/plugins.py#L13-L47)
    * with bases ([Manager](#pynchonmodelsplanner),)
    * with properties: (7 total)
      *  [`Plan`](/src/pynchon/plugins/plugins.py#L33) -> inspect._empty
      *  [`apply_hooks`](/src/pynchon/plugins/plugins.py#L37) -> inspect._empty
      *  [`config`](/src/pynchon/plugins/plugins.py#L108) -> inspect._empty
      *  [`hooks`](/src/pynchon/plugins/plugins.py#L37) -> inspect._empty
      *  [`logger`](/src/pynchon/plugins/plugins.py#L37) -> inspect._empty
      *  [`plugin_config`](/src/pynchon/plugins/plugins.py#L103) -> inspect._empty
      *  [`project_root`](/src/pynchon/plugins/plugins.py#L98) -> inspect._empty
<!--- This is a markdown file.  Comments look like this --->
-------------------------------------------------------------------------------
### pynchon.plugins.__template__
* Overview:  [source code](/src/pynchon/plugins/__template__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
<!--- This is a markdown file.  Comments look like this --->
* Classes: (1 total)
  * [`pynchon.plugins.__template__.PluginTemplate`](/src/pynchon/plugins/__template__.py#L9-L17)
    * with bases ([Provider](#pynchonmodelspluginsprovider),)
    * with properties: (4 total)
      *  [`config`](/src/pynchon/plugins/__template__.py#L108) -> inspect._empty
      *  [`logger`](/src/pynchon/plugins/__template__.py#L37) -> inspect._empty
      *  [`plugin_config`](/src/pynchon/plugins/__template__.py#L103) -> inspect._empty
      *  [`project_root`](/src/pynchon/plugins/__template__.py#L98) -> inspect._empty
<!--- This is a markdown file.  Comments look like this --->
-------------------------------------------------------------------------------
### pynchon.plugins.git
* Overview:  [source code](/src/pynchon/plugins/git.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
<!--- This is a markdown file.  Comments look like this --->
* Classes: (2 total)
  * [`pynchon.plugins.git.GitConfig`](/src/pynchon/plugins/git.py#L12-L106)
    * with bases ([Config](#pynchonabcsconfig),)
    * with properties: (8 total)
      *  [`branch_name`](/src/pynchon/plugins/git.py#L90) -> inspect._empty
      *  [`github_org`](/src/pynchon/plugins/git.py#L67) -> inspect._empty
      *  [`hash`](/src/pynchon/plugins/git.py#L99) -> str
      *  [`is_github`](/src/pynchon/plugins/git.py#L61) -> inspect._empty
      *  [`repo`](/src/pynchon/plugins/git.py#L51) -> typing.Optional[str]
      *  [`repo_name`](/src/pynchon/plugins/git.py#L75) -> typing.Optional[str]
      *  [`repo_url`](/src/pynchon/plugins/git.py#L84) -> inspect._empty
      *  [`root`](/src/pynchon/plugins/git.py#L42) -> typing.Optional[str]
  * [`pynchon.plugins.git.Git`](/src/pynchon/plugins/git.py#L109-L143)
    * with bases ([Provider](#pynchonmodelspluginsprovider),)
    * with properties: (5 total)
      *  [`config`](/src/pynchon/plugins/git.py#L108) -> inspect._empty
      *  [`logger`](/src/pynchon/plugins/git.py#L37) -> inspect._empty
      *  [`modified`](/src/pynchon/plugins/git.py#L127) -> typing.List[pynchon.abcs.path.Path]
      *  [`plugin_config`](/src/pynchon/plugins/git.py#L103) -> inspect._empty
      *  [`project_root`](/src/pynchon/plugins/git.py#L98) -> inspect._empty
<!--- This is a markdown file.  Comments look like this --->
-------------------------------------------------------------------------------
### pynchon.plugins.hooks
* Overview:  [source code](/src/pynchon/plugins/hooks.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
<!--- This is a markdown file.  Comments look like this --->
-------------------------------------------------------------------------------
### pynchon.plugins.release
* Overview:  [source code](/src/pynchon/plugins/release.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
<!--- This is a markdown file.  Comments look like this --->
-------------------------------------------------------------------------------
### pynchon.plugins.deck
* Overview:  [source code](/src/pynchon/plugins/deck.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
<!--- This is a markdown file.  Comments look like this --->
* Classes: (1 total)
  * [`pynchon.plugins.deck.Deck`](/src/pynchon/plugins/deck.py#L9-L57)
    * with bases ([ResourceManager](#pynchonmodelsplanner),)
    * with properties: (8 total)
      *  [`Plan`](/src/pynchon/plugins/deck.py#L33) -> inspect._empty
      *  [`apply_hooks`](/src/pynchon/plugins/deck.py#L37) -> inspect._empty
      *  [`changes`](/src/pynchon/plugins/deck.py#L173) -> inspect._empty
      *  [`config`](/src/pynchon/plugins/deck.py#L108) -> inspect._empty
      *  [`hooks`](/src/pynchon/plugins/deck.py#L37) -> inspect._empty
      *  [`logger`](/src/pynchon/plugins/deck.py#L37) -> inspect._empty
      *  [`plugin_config`](/src/pynchon/plugins/deck.py#L103) -> inspect._empty
      *  [`project_root`](/src/pynchon/plugins/deck.py#L98) -> inspect._empty
<!--- This is a markdown file.  Comments look like this --->
-------------------------------------------------------------------------------
### pynchon.plugins.cicd
* Overview:  [source code](/src/pynchon/plugins/cicd.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
<!--- This is a markdown file.  Comments look like this --->
* Classes: (1 total)
  * [`pynchon.plugins.cicd.CiCd`](/src/pynchon/plugins/cicd.py#L12-L53)
    * with bases ([Provider](#pynchonmodelspluginsprovider),)
    * with properties: (4 total)
      *  [`config`](/src/pynchon/plugins/cicd.py#L108) -> inspect._empty
      *  [`logger`](/src/pynchon/plugins/cicd.py#L37) -> inspect._empty
      *  [`plugin_config`](/src/pynchon/plugins/cicd.py#L103) -> inspect._empty
      *  [`project_root`](/src/pynchon/plugins/cicd.py#L98) -> inspect._empty
<!--- This is a markdown file.  Comments look like this --->
-------------------------------------------------------------------------------
### pynchon.plugins.gen
* Overview:  [source code](/src/pynchon/plugins/gen.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
<!--- This is a markdown file.  Comments look like this --->
* Classes: (1 total)
  * [`pynchon.plugins.gen.Generators`](/src/pynchon/plugins/gen.py#L10-L82)
    * with bases ([NameSpace](#pynchonmodelsplugins),)
    * with admonitions:  [🐉 Complex](/src/pynchon/plugins/gen.py#L21 "score 11 / 7") 
    * with properties: (4 total)
      *  [`config`](/src/pynchon/plugins/gen.py#L108) -> inspect._empty
      *  [`logger`](/src/pynchon/plugins/gen.py#L37) -> inspect._empty
      *  [`plugin_config`](/src/pynchon/plugins/gen.py#L103) -> inspect._empty
      *  [`project_root`](/src/pynchon/plugins/gen.py#L98) -> inspect._empty
<!--- This is a markdown file.  Comments look like this --->
-------------------------------------------------------------------------------
### pynchon.plugins.render
* Overview:  [source code](/src/pynchon/plugins/render.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
<!--- This is a markdown file.  Comments look like this --->
* Classes: (1 total)
  * [`pynchon.plugins.render.Renderers`](/src/pynchon/plugins/render.py#L10-L14)
    * with bases ([NameSpace](#pynchonmodelsplugins),)
    * with properties: (4 total)
      *  [`config`](/src/pynchon/plugins/render.py#L108) -> inspect._empty
      *  [`logger`](/src/pynchon/plugins/render.py#L37) -> inspect._empty
      *  [`plugin_config`](/src/pynchon/plugins/render.py#L103) -> inspect._empty
      *  [`project_root`](/src/pynchon/plugins/render.py#L98) -> inspect._empty
<!--- This is a markdown file.  Comments look like this --->
-------------------------------------------------------------------------------
### pynchon.plugins.util
* Overview:  [source code](/src/pynchon/plugins/util.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
<!--- This is a markdown file.  Comments look like this --->
* Classes: (3 total)
  * [`pynchon.plugins.util.PluginNotInitialized`](/src/pynchon/plugins/util.py#L12-L13)
    * with bases ([`__builtin__.RuntimeError`](https://docs.python.org/3/library/functions.html#RuntimeError),)
  * [`pynchon.plugins.util.PluginNotRegistered`](/src/pynchon/plugins/util.py#L16-L17)
    * with bases ([`__builtin__.RuntimeError`](https://docs.python.org/3/library/functions.html#RuntimeError),)
  * [`pynchon.plugins.util.PluginNotConfigured`](/src/pynchon/plugins/util.py#L20-L21)
    * with bases ([`__builtin__.RuntimeError`](https://docs.python.org/3/library/functions.html#RuntimeError),)
<!--- This is a markdown file.  Comments look like this --->
* Functions: (3 total)
  * [`pynchon.plugins.util.get_plugin_class`](/src/pynchon/plugins/util.py#L35-L46) with signature `(plugin_name: str) -> Type`
  * [`pynchon.plugins.util.get_plugin_meta`](/src/pynchon/plugins/util.py#L24-L32) with signature `(plugin_name: str) -> Dict`
  * [`pynchon.plugins.util.get_plugin_obj`](/src/pynchon/plugins/util.py#L52-L65) with signature `(plugin_name: str) -> object`
<!--- This is a markdown file.  Comments look like this --->
-------------------------------------------------------------------------------
### pynchon.plugins.mermaid
* Overview:  [source code](/src/pynchon/plugins/mermaid.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
<!--- This is a markdown file.  Comments look like this --->
* Classes: (1 total)
  * [`pynchon.plugins.mermaid.Mermaid`](/src/pynchon/plugins/mermaid.py#L16-L98)
    * with bases ([Planner](#pynchonmodelsplanner),)
    * with properties: (9 total)
      *  [`Plan`](/src/pynchon/plugins/mermaid.py#L33) -> inspect._empty
      *  [`apply_hooks`](/src/pynchon/plugins/mermaid.py#L37) -> inspect._empty
      *  [`config`](/src/pynchon/plugins/mermaid.py#L108) -> inspect._empty
      *  [`hooks`](/src/pynchon/plugins/mermaid.py#L37) -> inspect._empty
      *  [`logger`](/src/pynchon/plugins/mermaid.py#L37) -> inspect._empty
      *  [`output_root`](/src/pynchon/plugins/mermaid.py#L74) -> inspect._empty
      *  [`plugin_config`](/src/pynchon/plugins/mermaid.py#L103) -> inspect._empty
      *  [`project_root`](/src/pynchon/plugins/mermaid.py#L98) -> inspect._empty
      *  [`working_dir`](/src/pynchon/plugins/mermaid.py#L26) -> inspect._empty
<!--- This is a markdown file.  Comments look like this --->
-------------------------------------------------------------------------------
### pynchon.plugins.globals
* Overview:  [source code](/src/pynchon/plugins/globals.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
<!--- This is a markdown file.  Comments look like this --->
* Classes: (1 total)
  * [`pynchon.plugins.globals.Globals`](/src/pynchon/plugins/globals.py#L7-L17)
    * with bases ([Provider](#pynchonmodelspluginsprovider),)
    * with properties: (4 total)
      *  [`config`](/src/pynchon/plugins/globals.py#L108) -> inspect._empty
      *  [`logger`](/src/pynchon/plugins/globals.py#L37) -> inspect._empty
      *  [`plugin_config`](/src/pynchon/plugins/globals.py#L103) -> inspect._empty
      *  [`project_root`](/src/pynchon/plugins/globals.py#L98) -> inspect._empty
<!--- This is a markdown file.  Comments look like this --->
-------------------------------------------------------------------------------
### pynchon.plugins.griffe
* Overview:  [source code](/src/pynchon/plugins/griffe.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
<!--- This is a markdown file.  Comments look like this --->
* Classes: (1 total)
  * [`pynchon.plugins.griffe.Griffe`](/src/pynchon/plugins/griffe.py#L11-L51)
    * with bases ([ToolPlugin](#pynchonmodelspluginstool),)
    * with properties: (4 total)
      *  [`config`](/src/pynchon/plugins/griffe.py#L108) -> inspect._empty
      *  [`logger`](/src/pynchon/plugins/griffe.py#L37) -> inspect._empty
      *  [`plugin_config`](/src/pynchon/plugins/griffe.py#L103) -> inspect._empty
      *  [`project_root`](/src/pynchon/plugins/griffe.py#L98) -> inspect._empty
<!--- This is a markdown file.  Comments look like this --->
-------------------------------------------------------------------------------
### pynchon.plugins.rtd
* Overview:  [source code](/src/pynchon/plugins/rtd.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
<!--- This is a markdown file.  Comments look like this --->
-------------------------------------------------------------------------------
### pynchon.plugins.docs
* Overview:  [source code](/src/pynchon/plugins/docs.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
<!--- This is a markdown file.  Comments look like this --->
* Classes: (2 total)
  * [`pynchon.plugins.docs.OpenerMixin`](/src/pynchon/plugins/docs.py#L20-L76)
    * with bases ([`__builtin__.object`](https://docs.python.org/3/library/functions.html#object),)
  * [`pynchon.plugins.docs.DocsMan`](/src/pynchon/plugins/docs.py#L79-L216)
    * with bases ([ResourceManager](#pynchonmodelsplanner),[OpenerMixin](#pynchonpluginsdocs),)
    * with properties: (12 total)
      *  [`Plan`](/src/pynchon/plugins/docs.py#L33) -> inspect._empty
      *  [`apply_hooks`](/src/pynchon/plugins/docs.py#L37) -> inspect._empty
      *  [`changes`](/src/pynchon/plugins/docs.py#L173) -> inspect._empty
      *  [`config`](/src/pynchon/plugins/docs.py#L108) -> inspect._empty
      *  [`git_root`](/src/pynchon/plugins/docs.py#L114) -> inspect._empty
      *  [`hooks`](/src/pynchon/plugins/docs.py#L37) -> inspect._empty
      *  [`logger`](/src/pynchon/plugins/docs.py#L37) -> inspect._empty
      *  [`plugin_config`](/src/pynchon/plugins/docs.py#L103) -> inspect._empty
      *  [`project_root`](/src/pynchon/plugins/docs.py#L98) -> inspect._empty
      *  [`server`](/src/pynchon/plugins/docs.py#L37) -> inspect._empty
      *  [`server_pid`](/src/pynchon/plugins/docs.py#L105) -> inspect._empty
      *  [`server_url`](/src/pynchon/plugins/docs.py#L110) -> inspect._empty
<!--- This is a markdown file.  Comments look like this --->
-------------------------------------------------------------------------------
### pynchon.plugins.pattern
* Overview:  [source code](/src/pynchon/plugins/pattern.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
<!--- This is a markdown file.  Comments look like this --->
* Classes: (4 total)
  * [`pynchon.plugins.pattern.RenderResult`](/src/pynchon/plugins/pattern.py#L23-L35)
    * with bases ([Config](#pynchonabcsconfig),)
    * with properties: (1 total)
      *  [`diff`](/src/pynchon/plugins/pattern.py#L30) -> inspect._empty
  * [`pynchon.plugins.pattern.ScaffoldAdvice`](/src/pynchon/plugins/pattern.py#L38-L60)
    * with bases ([Config](#pynchonabcsconfig),)
    * with properties: (1 total)
      *  [`inherits`](/src/pynchon/plugins/pattern.py#L43) -> inspect._empty
  * [`pynchon.plugins.pattern.Scaffold`](/src/pynchon/plugins/pattern.py#L63-L212)
    * with bases ([Config](#pynchonabcsconfig),)
    * with properties: (4 total)
      *  [`advice`](/src/pynchon/plugins/pattern.py#L186) -> inspect._empty
      *  [`dirs`](/src/pynchon/plugins/pattern.py#L202) -> typing.List
      *  [`files`](/src/pynchon/plugins/pattern.py#L194) -> typing.List[str]
      *  [`has_advice`](/src/pynchon/plugins/pattern.py#L182) -> bool
  * [`pynchon.plugins.pattern.Pattern`](/src/pynchon/plugins/pattern.py#L215-L430)
    * with bases ([ResourceManager](#pynchonmodelsplanner),)
    * with properties: (11 total)
      *  [`Plan`](/src/pynchon/plugins/pattern.py#L33) -> inspect._empty
      *  [`apply_hooks`](/src/pynchon/plugins/pattern.py#L37) -> inspect._empty
      *  [`changes`](/src/pynchon/plugins/pattern.py#L173) -> inspect._empty
      *  [`config`](/src/pynchon/plugins/pattern.py#L108) -> inspect._empty
      *  [`hooks`](/src/pynchon/plugins/pattern.py#L37) -> inspect._empty
      *  [`logger`](/src/pynchon/plugins/pattern.py#L37) -> inspect._empty
      *  [`pattern_folder`](/src/pynchon/plugins/pattern.py#L243) -> inspect._empty
      *  [`pattern_names`](/src/pynchon/plugins/pattern.py#L247) -> inspect._empty
      *  [`patterns`](/src/pynchon/plugins/pattern.py#L234) -> typing.Dict
      *  [`plugin_config`](/src/pynchon/plugins/pattern.py#L103) -> inspect._empty
      *  [`project_root`](/src/pynchon/plugins/pattern.py#L98) -> inspect._empty
<!--- This is a markdown file.  Comments look like this --->
-------------------------------------------------------------------------------
### pynchon.plugins.core
* Overview:  [source code](/src/pynchon/plugins/core.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
<!--- This is a markdown file.  Comments look like this --->
* Classes: (1 total)
  * [`pynchon.plugins.core.Core`](/src/pynchon/plugins/core.py#L17-L179)
    * with bases ([Planner](#pynchonmodelsplanner),)
    * with properties: (7 total)
      *  [`Plan`](/src/pynchon/plugins/core.py#L33) -> inspect._empty
      *  [`apply_hooks`](/src/pynchon/plugins/core.py#L37) -> inspect._empty
      *  [`config`](/src/pynchon/plugins/core.py#L108) -> inspect._empty
      *  [`hooks`](/src/pynchon/plugins/core.py#L37) -> inspect._empty
      *  [`logger`](/src/pynchon/plugins/core.py#L37) -> inspect._empty
      *  [`plugin_config`](/src/pynchon/plugins/core.py#L103) -> inspect._empty
      *  [`project_root`](/src/pynchon/plugins/core.py#L98) -> inspect._empty
<!--- This is a markdown file.  Comments look like this --->
-------------------------------------------------------------------------------
### pynchon.plugins.jinja
* Overview:  [source code](/src/pynchon/plugins/jinja.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
<!--- This is a markdown file.  Comments look like this --->
* Classes: (1 total)
  * [`pynchon.plugins.jinja.Jinja`](/src/pynchon/plugins/jinja.py#L12-L156)
    * with bases ([Planner](#pynchonmodelsplanner),)
    * with properties: (7 total)
      *  [`Plan`](/src/pynchon/plugins/jinja.py#L33) -> inspect._empty
      *  [`apply_hooks`](/src/pynchon/plugins/jinja.py#L37) -> inspect._empty
      *  [`config`](/src/pynchon/plugins/jinja.py#L108) -> inspect._empty
      *  [`hooks`](/src/pynchon/plugins/jinja.py#L37) -> inspect._empty
      *  [`logger`](/src/pynchon/plugins/jinja.py#L37) -> inspect._empty
      *  [`plugin_config`](/src/pynchon/plugins/jinja.py#L103) -> inspect._empty
      *  [`project_root`](/src/pynchon/plugins/jinja.py#L98) -> inspect._empty
<!--- This is a markdown file.  Comments look like this --->
-------------------------------------------------------------------------------
### pynchon.plugins.api
* Overview:  [source code](/src/pynchon/plugins/api.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
<!--- This is a markdown file.  Comments look like this --->
-------------------------------------------------------------------------------
### pynchon.plugins.src
* Overview:  [source code](/src/pynchon/plugins/src.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
<!--- This is a markdown file.  Comments look like this --->
* Classes: (1 total)
  * [`pynchon.plugins.src.SourceMan`](/src/pynchon/plugins/src.py#L37-L218)
    * with bases ([ResourceManager](#pynchonmodelsplanner),)
    * with properties: (9 total)
      *  [`Plan`](/src/pynchon/plugins/src.py#L33) -> inspect._empty
      *  [`apply_hooks`](/src/pynchon/plugins/src.py#L37) -> inspect._empty
      *  [`changes`](/src/pynchon/plugins/src.py#L173) -> inspect._empty
      *  [`config`](/src/pynchon/plugins/src.py#L108) -> inspect._empty
      *  [`exclude_patterns`](/src/pynchon/plugins/src.py#L53) -> inspect._empty
      *  [`hooks`](/src/pynchon/plugins/src.py#L37) -> inspect._empty
      *  [`logger`](/src/pynchon/plugins/src.py#L37) -> inspect._empty
      *  [`plugin_config`](/src/pynchon/plugins/src.py#L103) -> inspect._empty
      *  [`project_root`](/src/pynchon/plugins/src.py#L98) -> inspect._empty
<!--- This is a markdown file.  Comments look like this --->
-------------------------------------------------------------------------------
### pynchon.plugins.makefile
* Overview:  [source code](/src/pynchon/plugins/makefile.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
<!--- This is a markdown file.  Comments look like this --->
* Classes: (1 total)
  * [`pynchon.plugins.makefile.Make`](/src/pynchon/plugins/makefile.py#L14-L124)
    * with bases ([Planner](#pynchonmodelsplanner),)
    * with properties: (9 total)
      *  [`Plan`](/src/pynchon/plugins/makefile.py#L33) -> inspect._empty
      *  [`apply_hooks`](/src/pynchon/plugins/makefile.py#L37) -> inspect._empty
      *  [`config`](/src/pynchon/plugins/makefile.py#L108) -> inspect._empty
      *  [`diagrams_root`](/src/pynchon/plugins/makefile.py#L36) -> inspect._empty
      *  [`hooks`](/src/pynchon/plugins/makefile.py#L37) -> inspect._empty
      *  [`logger`](/src/pynchon/plugins/makefile.py#L37) -> inspect._empty
      *  [`output_file`](/src/pynchon/plugins/makefile.py#L40) -> inspect._empty
      *  [`plugin_config`](/src/pynchon/plugins/makefile.py#L103) -> inspect._empty
      *  [`project_root`](/src/pynchon/plugins/makefile.py#L98) -> inspect._empty
<!--- This is a markdown file.  Comments look like this --->
-------------------------------------------------------------------------------
### pynchon.plugins.fixme
* Overview:  [source code](/src/pynchon/plugins/fixme.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
<!--- This is a markdown file.  Comments look like this --->
* Classes: (2 total)
  * [`pynchon.plugins.fixme.FixMeConfig`](/src/pynchon/plugins/fixme.py#L15-L16)
    * with bases ([Config](#pynchonabcsconfig),)
  * [`pynchon.plugins.fixme.FixMe`](/src/pynchon/plugins/fixme.py#L19-L112)
    * with bases ([Planner](#pynchonmodelsplanner),)
    * with properties: (7 total)
      *  [`Plan`](/src/pynchon/plugins/fixme.py#L33) -> inspect._empty
      *  [`apply_hooks`](/src/pynchon/plugins/fixme.py#L37) -> inspect._empty
      *  [`config`](/src/pynchon/plugins/fixme.py#L108) -> inspect._empty
      *  [`hooks`](/src/pynchon/plugins/fixme.py#L37) -> inspect._empty
      *  [`logger`](/src/pynchon/plugins/fixme.py#L37) -> inspect._empty
      *  [`plugin_config`](/src/pynchon/plugins/fixme.py#L103) -> inspect._empty
      *  [`project_root`](/src/pynchon/plugins/fixme.py#L98) -> inspect._empty
<!--- This is a markdown file.  Comments look like this --->
-------------------------------------------------------------------------------
### pynchon.plugins.ast
* Overview:  [source code](/src/pynchon/plugins/ast.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
<!--- This is a markdown file.  Comments look like this --->
-------------------------------------------------------------------------------
### pynchon.plugins.dot
* Overview:  [source code](/src/pynchon/plugins/dot.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
<!--- This is a markdown file.  Comments look like this --->
* Classes: (1 total)
  * [`pynchon.plugins.dot.Dot`](/src/pynchon/plugins/dot.py#L15-L87)
    * with bases ([Planner](#pynchonmodelsplanner),)
    * with properties: (7 total)
      *  [`Plan`](/src/pynchon/plugins/dot.py#L33) -> inspect._empty
      *  [`apply_hooks`](/src/pynchon/plugins/dot.py#L37) -> inspect._empty
      *  [`config`](/src/pynchon/plugins/dot.py#L108) -> inspect._empty
      *  [`hooks`](/src/pynchon/plugins/dot.py#L37) -> inspect._empty
      *  [`logger`](/src/pynchon/plugins/dot.py#L37) -> inspect._empty
      *  [`plugin_config`](/src/pynchon/plugins/dot.py#L103) -> inspect._empty
      *  [`project_root`](/src/pynchon/plugins/dot.py#L98) -> inspect._empty
<!--- This is a markdown file.  Comments look like this --->
-------------------------------------------------------------------------------
### pynchon.plugins.github
* Overview:  [source code](/src/pynchon/plugins/github.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
<!--- This is a markdown file.  Comments look like this --->
* Classes: (1 total)
  * [`pynchon.plugins.github.GitHub`](/src/pynchon/plugins/github.py#L19-L128)
    * with bases ([ToolPlugin](#pynchonmodelspluginstool),)
    * with properties: (4 total)
      *  [`config`](/src/pynchon/plugins/github.py#L108) -> inspect._empty
      *  [`logger`](/src/pynchon/plugins/github.py#L37) -> inspect._empty
      *  [`plugin_config`](/src/pynchon/plugins/github.py#L103) -> inspect._empty
      *  [`project_root`](/src/pynchon/plugins/github.py#L98) -> inspect._empty
<!--- This is a markdown file.  Comments look like this --->
-------------------------------------------------------------------------------
### pynchon.plugins.parse
* Overview:  [source code](/src/pynchon/plugins/parse.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
<!--- This is a markdown file.  Comments look like this --->
-------------------------------------------------------------------------------
### pynchon.plugins.tests
* Overview:  [source code](/src/pynchon/plugins/tests.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
<!--- This is a markdown file.  Comments look like this --->
* Classes: (1 total)
  * [`pynchon.plugins.tests.Tests`](/src/pynchon/plugins/tests.py#L9-L27)
    * with bases ([ResourceManager](#pynchonmodelsplanner),)
    * with properties: (8 total)
      *  [`Plan`](/src/pynchon/plugins/tests.py#L33) -> inspect._empty
      *  [`apply_hooks`](/src/pynchon/plugins/tests.py#L37) -> inspect._empty
      *  [`changes`](/src/pynchon/plugins/tests.py#L173) -> inspect._empty
      *  [`config`](/src/pynchon/plugins/tests.py#L108) -> inspect._empty
      *  [`hooks`](/src/pynchon/plugins/tests.py#L37) -> inspect._empty
      *  [`logger`](/src/pynchon/plugins/tests.py#L37) -> inspect._empty
      *  [`plugin_config`](/src/pynchon/plugins/tests.py#L103) -> inspect._empty
      *  [`project_root`](/src/pynchon/plugins/tests.py#L98) -> inspect._empty
<!--- This is a markdown file.  Comments look like this --->
-------------------------------------------------------------------------------
### pynchon.plugins.tox
* Overview:  [source code](/src/pynchon/plugins/tox.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
<!--- This is a markdown file.  Comments look like this --->
* Classes: (1 total)
  * [`pynchon.plugins.tox.PluginTemplate`](/src/pynchon/plugins/tox.py#L9-L17)
    * with bases ([Provider](#pynchonmodelspluginsprovider),)
    * with properties: (4 total)
      *  [`config`](/src/pynchon/plugins/tox.py#L108) -> inspect._empty
      *  [`logger`](/src/pynchon/plugins/tox.py#L37) -> inspect._empty
      *  [`plugin_config`](/src/pynchon/plugins/tox.py#L103) -> inspect._empty
      *  [`project_root`](/src/pynchon/plugins/tox.py#L98) -> inspect._empty
<!--- This is a markdown file.  Comments look like this --->
-------------------------------------------------------------------------------
### pynchon.plugins.json
* Overview:  [source code](/src/pynchon/plugins/json.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
<!--- This is a markdown file.  Comments look like this --->
* Classes: (1 total)
  * [`pynchon.plugins.json.Json`](/src/pynchon/plugins/json.py#L49-L136)
    * with bases ([ToolPlugin](#pynchonmodelspluginstool),)
    * with properties: (4 total)
      *  [`config`](/src/pynchon/plugins/json.py#L108) -> inspect._empty
      *  [`logger`](/src/pynchon/plugins/json.py#L37) -> inspect._empty
      *  [`plugin_config`](/src/pynchon/plugins/json.py#L103) -> inspect._empty
      *  [`project_root`](/src/pynchon/plugins/json.py#L98) -> inspect._empty
<!--- This is a markdown file.  Comments look like this --->
-------------------------------------------------------------------------------
### pynchon.plugins.project
* Overview:  [source code](/src/pynchon/plugins/project.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
<!--- This is a markdown file.  Comments look like this --->
* Classes: (2 total)
  * [`pynchon.plugins.project.ProjectConfig`](/src/pynchon/plugins/project.py#L11-L46)
    * with bases ([Config](#pynchonabcsconfig),)
    * with properties: (3 total)
      *  [`name`](/src/pynchon/plugins/project.py#L18) -> typing.Optional[str]
      *  [`root`](/src/pynchon/plugins/project.py#L28) -> str
      *  [`subproject`](/src/pynchon/plugins/project.py#L34) -> typing.Dict
  * [`pynchon.plugins.project.Project`](/src/pynchon/plugins/project.py#L49-L54)
    * with bases ([Manager](#pynchonmodelsplanner),)
    * with properties: (7 total)
      *  [`Plan`](/src/pynchon/plugins/project.py#L33) -> inspect._empty
      *  [`apply_hooks`](/src/pynchon/plugins/project.py#L37) -> inspect._empty
      *  [`config`](/src/pynchon/plugins/project.py#L108) -> inspect._empty
      *  [`hooks`](/src/pynchon/plugins/project.py#L37) -> inspect._empty
      *  [`logger`](/src/pynchon/plugins/project.py#L37) -> inspect._empty
      *  [`plugin_config`](/src/pynchon/plugins/project.py#L103) -> inspect._empty
      *  [`project_root`](/src/pynchon/plugins/project.py#L98) -> inspect._empty
<!--- This is a markdown file.  Comments look like this --->
-------------------------------------------------------------------------------
### pynchon.plugins.python
* Overview:  [source code](/src/pynchon/plugins/python/__init__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
<!--- This is a markdown file.  Comments look like this --->
* Classes: (0 total)
<!--- This is a markdown file.  Comments look like this --->
-------------------------------------------------------------------------------
### pynchon.plugins.python.libcst
* Overview:  [source code](/src/pynchon/plugins/python/libcst.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
<!--- This is a markdown file.  Comments look like this --->
* Classes: (1 total)
  * [`pynchon.plugins.python.libcst.LibCST`](/src/pynchon/plugins/python/libcst.py#L15-L115)
    * with bases ([Planner](#pynchonmodelsplanner),)
    * with properties: (7 total)
      *  [`Plan`](/src/pynchon/plugins/python/libcst.py#L33) -> inspect._empty
      *  [`apply_hooks`](/src/pynchon/plugins/python/libcst.py#L37) -> inspect._empty
      *  [`config`](/src/pynchon/plugins/python/libcst.py#L108) -> inspect._empty
      *  [`hooks`](/src/pynchon/plugins/python/libcst.py#L37) -> inspect._empty
      *  [`logger`](/src/pynchon/plugins/python/libcst.py#L37) -> inspect._empty
      *  [`plugin_config`](/src/pynchon/plugins/python/libcst.py#L103) -> inspect._empty
      *  [`project_root`](/src/pynchon/plugins/python/libcst.py#L98) -> inspect._empty
<!--- This is a markdown file.  Comments look like this --->
-------------------------------------------------------------------------------
### pynchon.plugins.python.config
* Overview:  [source code](/src/pynchon/plugins/python/config.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
<!--- This is a markdown file.  Comments look like this --->
-------------------------------------------------------------------------------
### pynchon.plugins.python.models
* Overview:  [source code](/src/pynchon/plugins/python/models.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
<!--- This is a markdown file.  Comments look like this --->
-------------------------------------------------------------------------------
### pynchon.plugins.python.cst
* Overview:  [source code](/src/pynchon/plugins/python/cst.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
<!--- This is a markdown file.  Comments look like this --->
-------------------------------------------------------------------------------
### pynchon.plugins.python.platform
* Overview:  [source code](/src/pynchon/plugins/python/platform.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
<!--- This is a markdown file.  Comments look like this --->
* Classes: (2 total)
  * [`pynchon.plugins.python.platform.PythonPlatform`](/src/pynchon/plugins/python/platform.py#L14-L79)
    * with bases ([Planner](#pynchonmodelsplanner),)
    * with properties: (7 total)
      *  [`Plan`](/src/pynchon/plugins/python/platform.py#L33) -> inspect._empty
      *  [`apply_hooks`](/src/pynchon/plugins/python/platform.py#L37) -> inspect._empty
      *  [`config`](/src/pynchon/plugins/python/platform.py#L108) -> inspect._empty
      *  [`hooks`](/src/pynchon/plugins/python/platform.py#L37) -> inspect._empty
      *  [`logger`](/src/pynchon/plugins/python/platform.py#L37) -> inspect._empty
      *  [`plugin_config`](/src/pynchon/plugins/python/platform.py#L103) -> inspect._empty
      *  [`project_root`](/src/pynchon/plugins/python/platform.py#L98) -> inspect._empty
  * [`pynchon.plugins.python.platform.PackageConfig`](/src/pynchon/plugins/python/platform.py#L82-L102)
    * with bases ([Config](#pynchonabcsconfig),)
    * with properties: (2 total)
      *  [`name`](/src/pynchon/plugins/python/platform.py#L88) -> str
      *  [`version`](/src/pynchon/plugins/python/platform.py#L96) -> str
<!--- This is a markdown file.  Comments look like this --->
-------------------------------------------------------------------------------
### pynchon.plugins.python.api
* Overview:  [source code](/src/pynchon/plugins/python/api.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
<!--- This is a markdown file.  Comments look like this --->
* Classes: (1 total)
  * [`pynchon.plugins.python.api.PythonAPI`](/src/pynchon/plugins/python/api.py#L13-L110)
    * with bases ([Planner](#pynchonmodelsplanner),)
    * with properties: (7 total)
      *  [`Plan`](/src/pynchon/plugins/python/api.py#L33) -> inspect._empty
      *  [`apply_hooks`](/src/pynchon/plugins/python/api.py#L37) -> inspect._empty
      *  [`config`](/src/pynchon/plugins/python/api.py#L108) -> inspect._empty
      *  [`hooks`](/src/pynchon/plugins/python/api.py#L37) -> inspect._empty
      *  [`logger`](/src/pynchon/plugins/python/api.py#L37) -> inspect._empty
      *  [`plugin_config`](/src/pynchon/plugins/python/api.py#L103) -> inspect._empty
      *  [`project_root`](/src/pynchon/plugins/python/api.py#L98) -> inspect._empty
<!--- This is a markdown file.  Comments look like this --->
-------------------------------------------------------------------------------
### pynchon.plugins.python.cli
* Overview:  [source code](/src/pynchon/plugins/python/cli.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
<!--- This is a markdown file.  Comments look like this --->
* Classes: (2 total)
  * [`pynchon.plugins.python.cli.PythonCliConfig`](/src/pynchon/plugins/python/cli.py#L28-L97)
    * with bases ([Config](#pynchonabcsconfig),)
    * with properties: (3 total)
      *  [`entrypoints`](/src/pynchon/plugins/python/cli.py#L64) -> typing.List[typing.Dict]
      *  [`root`](/src/pynchon/plugins/python/cli.py#L39) -> inspect._empty
      *  [`src_root`](/src/pynchon/plugins/python/cli.py#L49) -> pynchon.abcs.path.Path
  * [`pynchon.plugins.python.cli.PythonCLI`](/src/pynchon/plugins/python/cli.py#L100-L358)
    * with bases ([Planner](#pynchonmodelsplanner),)
    * with properties: (8 total)
      *  [`Plan`](/src/pynchon/plugins/python/cli.py#L33) -> inspect._empty
      *  [`apply_hooks`](/src/pynchon/plugins/python/cli.py#L37) -> inspect._empty
      *  [`config`](/src/pynchon/plugins/python/cli.py#L108) -> inspect._empty
      *  [`hooks`](/src/pynchon/plugins/python/cli.py#L37) -> inspect._empty
      *  [`logger`](/src/pynchon/plugins/python/cli.py#L37) -> inspect._empty
      *  [`plugin_config`](/src/pynchon/plugins/python/cli.py#L103) -> inspect._empty
      *  [`project_root`](/src/pynchon/plugins/python/cli.py#L98) -> inspect._empty
      *  [`root`](/src/pynchon/plugins/python/cli.py#L281) -> inspect._empty
<!--- This is a markdown file.  Comments look like this --->
-------------------------------------------------------------------------------
### pynchon.plugins.python.ast
* Overview:  [source code](/src/pynchon/plugins/python/ast.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
<!--- This is a markdown file.  Comments look like this --->
-------------------------------------------------------------------------------
### pynchon.plugins.python.pypi
* Overview:  [source code](/src/pynchon/plugins/python/pypi.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
<!--- This is a markdown file.  Comments look like this --->
* Classes: (2 total)
  * [`pynchon.plugins.python.pypi.PyPiConfig`](/src/pynchon/plugins/python/pypi.py#L9-L13)
    * with bases ([Config](#pynchonabcsconfig),)
  * [`pynchon.plugins.python.pypi.PyPI`](/src/pynchon/plugins/python/pypi.py#L16-L20)
    * with bases ([Provider](#pynchonmodelspluginsprovider),)
    * with properties: (4 total)
      *  [`config`](/src/pynchon/plugins/python/pypi.py#L108) -> inspect._empty
      *  [`logger`](/src/pynchon/plugins/python/pypi.py#L37) -> inspect._empty
      *  [`plugin_config`](/src/pynchon/plugins/python/pypi.py#L103) -> inspect._empty
      *  [`project_root`](/src/pynchon/plugins/python/pypi.py#L98) -> inspect._empty
<!--- This is a markdown file.  Comments look like this --->
-------------------------------------------------------------------------------
### pynchon.plugins.scaffolding
* Overview:  [source code](/src/pynchon/plugins/scaffolding/__init__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
<!--- This is a markdown file.  Comments look like this --->
* Classes: (1 total)
  * [`pynchon.plugins.scaffolding.Scaffolding`](/src/pynchon/plugins/scaffolding/__init__.py#L15-L120)
    * with bases ([ShyPlanner](#pynchonmodelsplanner),)
    * with properties: (9 total)
      *  [`Plan`](/src/pynchon/plugins/scaffolding/__init__.py#L33) -> inspect._empty
      *  [`apply_hooks`](/src/pynchon/plugins/scaffolding/__init__.py#L37) -> inspect._empty
      *  [`config`](/src/pynchon/plugins/scaffolding/__init__.py#L108) -> inspect._empty
      *  [`hooks`](/src/pynchon/plugins/scaffolding/__init__.py#L37) -> inspect._empty
      *  [`logger`](/src/pynchon/plugins/scaffolding/__init__.py#L37) -> inspect._empty
      *  [`matches`](/src/pynchon/plugins/scaffolding/__init__.py#L43) -> inspect._empty
      *  [`plugin_config`](/src/pynchon/plugins/scaffolding/__init__.py#L103) -> inspect._empty
      *  [`project_root`](/src/pynchon/plugins/scaffolding/__init__.py#L98) -> inspect._empty
      *  [`scaffolds`](/src/pynchon/plugins/scaffolding/__init__.py#L58) -> inspect._empty
<!--- This is a markdown file.  Comments look like this --->
* Classes: (1 total)
  * [`pynchon.plugins.scaffolding.Scaffolding`](/src/pynchon/plugins/scaffolding/__init__.py#L15-L120)
    * with bases ([ShyPlanner](#pynchonmodelsplanner),)
    * with properties: (9 total)
      *  [`Plan`](/src/pynchon/plugins/scaffolding/__init__.py#L33) -> inspect._empty
      *  [`apply_hooks`](/src/pynchon/plugins/scaffolding/__init__.py#L37) -> inspect._empty
      *  [`config`](/src/pynchon/plugins/scaffolding/__init__.py#L108) -> inspect._empty
      *  [`hooks`](/src/pynchon/plugins/scaffolding/__init__.py#L37) -> inspect._empty
      *  [`logger`](/src/pynchon/plugins/scaffolding/__init__.py#L37) -> inspect._empty
      *  [`matches`](/src/pynchon/plugins/scaffolding/__init__.py#L43) -> inspect._empty
      *  [`plugin_config`](/src/pynchon/plugins/scaffolding/__init__.py#L103) -> inspect._empty
      *  [`project_root`](/src/pynchon/plugins/scaffolding/__init__.py#L98) -> inspect._empty
      *  [`scaffolds`](/src/pynchon/plugins/scaffolding/__init__.py#L58) -> inspect._empty
<!--- This is a markdown file.  Comments look like this --->
-------------------------------------------------------------------------------
### pynchon.plugins.scaffolding.config
* Overview:  [source code](/src/pynchon/plugins/scaffolding/config.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
<!--- This is a markdown file.  Comments look like this --->
* Classes: (2 total)
  * [`pynchon.plugins.scaffolding.config.ScaffoldingItem`](/src/pynchon/plugins/scaffolding/config.py#L11-L35)
    * with bases ([AttrDict](#pynchonabcsattrdict),)
    * with properties: (1 total)
      *  [`exists`](/src/pynchon/plugins/scaffolding/config.py#L28) -> bool
  * [`pynchon.plugins.scaffolding.config.ScaffoldingConfig`](/src/pynchon/plugins/scaffolding/config.py#L38-L41)
    * with bases ([Config](#pynchonabcsconfig),)
<!--- This is a markdown file.  Comments look like this --->
-------------------------------------------------------------------------------
### pynchon.plugins.doctor
* Overview:  [source code](/src/pynchon/plugins/doctor/__init__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
<!--- This is a markdown file.  Comments look like this --->
-------------------------------------------------------------------------------
### pynchon.models
* Overview:  [source code](/src/pynchon/models/__init__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
<!--- This is a markdown file.  Comments look like this --->
* Classes: (0 total)
<!--- This is a markdown file.  Comments look like this --->
-------------------------------------------------------------------------------
### pynchon.models.planner
* Overview:  [source code](/src/pynchon/models/planner.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
<!--- This is a markdown file.  Comments look like this --->
* Classes: (5 total)
  * [`pynchon.models.planner.AbstractPlanner`](/src/pynchon/models/planner.py#L20-L154)
    * with bases ([BasePlugin](#pynchonmodelsplugins),)
    * with properties: (7 total)
      *  [`Plan`](/src/pynchon/models/planner.py#L33) -> inspect._empty
      *  [`apply_hooks`](/src/pynchon/models/planner.py#L37) -> inspect._empty
      *  [`config`](/src/pynchon/models/planner.py#L108) -> inspect._empty
      *  [`hooks`](/src/pynchon/models/planner.py#L37) -> inspect._empty
      *  [`logger`](/src/pynchon/models/planner.py#L37) -> inspect._empty
      *  [`plugin_config`](/src/pynchon/models/planner.py#L103) -> inspect._empty
      *  [`project_root`](/src/pynchon/models/planner.py#L98) -> inspect._empty
  * [`pynchon.models.planner.ShyPlanner`](/src/pynchon/models/planner.py#L157-L164)
    * with bases ([AbstractPlanner](#pynchonmodelsplanner),)
    * with properties: (7 total)
      *  [`Plan`](/src/pynchon/models/planner.py#L33) -> inspect._empty
      *  [`apply_hooks`](/src/pynchon/models/planner.py#L37) -> inspect._empty
      *  [`config`](/src/pynchon/models/planner.py#L108) -> inspect._empty
      *  [`hooks`](/src/pynchon/models/planner.py#L37) -> inspect._empty
      *  [`logger`](/src/pynchon/models/planner.py#L37) -> inspect._empty
      *  [`plugin_config`](/src/pynchon/models/planner.py#L103) -> inspect._empty
      *  [`project_root`](/src/pynchon/models/planner.py#L98) -> inspect._empty
  * [`pynchon.models.planner.Manager`](/src/pynchon/models/planner.py#L167-L169)
    * with bases ([ShyPlanner](#pynchonmodelsplanner),)
    * with properties: (7 total)
      *  [`Plan`](/src/pynchon/models/planner.py#L33) -> inspect._empty
      *  [`apply_hooks`](/src/pynchon/models/planner.py#L37) -> inspect._empty
      *  [`config`](/src/pynchon/models/planner.py#L108) -> inspect._empty
      *  [`hooks`](/src/pynchon/models/planner.py#L37) -> inspect._empty
      *  [`logger`](/src/pynchon/models/planner.py#L37) -> inspect._empty
      *  [`plugin_config`](/src/pynchon/models/planner.py#L103) -> inspect._empty
      *  [`project_root`](/src/pynchon/models/planner.py#L98) -> inspect._empty
  * [`pynchon.models.planner.ResourceManager`](/src/pynchon/models/planner.py#L172-L216)
    * with bases ([Manager](#pynchonmodelsplanner),)
    * with properties: (8 total)
      *  [`Plan`](/src/pynchon/models/planner.py#L33) -> inspect._empty
      *  [`apply_hooks`](/src/pynchon/models/planner.py#L37) -> inspect._empty
      *  [`changes`](/src/pynchon/models/planner.py#L173) -> inspect._empty
      *  [`config`](/src/pynchon/models/planner.py#L108) -> inspect._empty
      *  [`hooks`](/src/pynchon/models/planner.py#L37) -> inspect._empty
      *  [`logger`](/src/pynchon/models/planner.py#L37) -> inspect._empty
      *  [`plugin_config`](/src/pynchon/models/planner.py#L103) -> inspect._empty
      *  [`project_root`](/src/pynchon/models/planner.py#L98) -> inspect._empty
  * [`pynchon.models.planner.Planner`](/src/pynchon/models/planner.py#L219-L226)
    * with bases ([ShyPlanner](#pynchonmodelsplanner),)
    * with properties: (7 total)
      *  [`Plan`](/src/pynchon/models/planner.py#L33) -> inspect._empty
      *  [`apply_hooks`](/src/pynchon/models/planner.py#L37) -> inspect._empty
      *  [`config`](/src/pynchon/models/planner.py#L108) -> inspect._empty
      *  [`hooks`](/src/pynchon/models/planner.py#L37) -> inspect._empty
      *  [`logger`](/src/pynchon/models/planner.py#L37) -> inspect._empty
      *  [`plugin_config`](/src/pynchon/models/planner.py#L103) -> inspect._empty
      *  [`project_root`](/src/pynchon/models/planner.py#L98) -> inspect._empty
<!--- This is a markdown file.  Comments look like this --->
-------------------------------------------------------------------------------
### pynchon.models.planning
* Overview:  [source code](/src/pynchon/models/planning.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
<!--- This is a markdown file.  Comments look like this --->
* Classes: (4 total)
  * [`pynchon.models.planning.Goal`](/src/pynchon/models/planning.py#L17-L60)
    * with bases ([BaseModel](#pynchonbase),)
    * with properties: (1 total)
      *  [`rel_resource`](/src/pynchon/models/planning.py#L19) -> str
  * [`pynchon.models.planning.Action`](/src/pynchon/models/planning.py#L68-L88)
    * with bases ([BaseModel](#pydanticmain),)
    * with properties: (1 total)
      *  [`status_string`](/src/pynchon/models/planning.py#L77) -> inspect._empty
  * [`pynchon.models.planning.Plan`](/src/pynchon/models/planning.py#L92-L203)
    * with bases ([BaseModel](#pydanticmain),)
  * [`pynchon.models.planning.ApplyResults`](/src/pynchon/models/planning.py#L209-L233)
    * with bases ([`__builtin__.list`](https://docs.python.org/3/library/functions.html#list),[Generic](#typing),)
    * with properties: (2 total)
      *  [`action_types`](/src/pynchon/models/planning.py#L214) -> inspect._empty
      *  [`ok`](/src/pynchon/models/planning.py#L210) -> inspect._empty
<!--- This is a markdown file.  Comments look like this --->
-------------------------------------------------------------------------------
### pynchon.models.plugins
* Overview:  [source code](/src/pynchon/models/plugins/__init__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
<!--- This is a markdown file.  Comments look like this --->
* Classes: (2 total)
  * [`pynchon.models.plugins.BasePlugin`](/src/pynchon/models/plugins/__init__.py#L21-L24)
    * with bases ([CliPlugin](#pynchonmodelspluginscli),)
    * with properties: (4 total)
      *  [`config`](/src/pynchon/models/plugins/__init__.py#L108) -> inspect._empty
      *  [`logger`](/src/pynchon/models/plugins/__init__.py#L37) -> inspect._empty
      *  [`plugin_config`](/src/pynchon/models/plugins/__init__.py#L103) -> inspect._empty
      *  [`project_root`](/src/pynchon/models/plugins/__init__.py#L98) -> inspect._empty
  * [`pynchon.models.plugins.NameSpace`](/src/pynchon/models/plugins/__init__.py#L27-L37)
    * with bases ([CliPlugin](#pynchonmodelspluginscli),)
    * with properties: (4 total)
      *  [`config`](/src/pynchon/models/plugins/__init__.py#L108) -> inspect._empty
      *  [`logger`](/src/pynchon/models/plugins/__init__.py#L37) -> inspect._empty
      *  [`plugin_config`](/src/pynchon/models/plugins/__init__.py#L103) -> inspect._empty
      *  [`project_root`](/src/pynchon/models/plugins/__init__.py#L98) -> inspect._empty
<!--- This is a markdown file.  Comments look like this --->
* Classes: (2 total)
  * [`pynchon.models.plugins.BasePlugin`](/src/pynchon/models/plugins/__init__.py#L21-L24)
    * with bases ([CliPlugin](#pynchonmodelspluginscli),)
    * with properties: (4 total)
      *  [`config`](/src/pynchon/models/plugins/__init__.py#L108) -> inspect._empty
      *  [`logger`](/src/pynchon/models/plugins/__init__.py#L37) -> inspect._empty
      *  [`plugin_config`](/src/pynchon/models/plugins/__init__.py#L103) -> inspect._empty
      *  [`project_root`](/src/pynchon/models/plugins/__init__.py#L98) -> inspect._empty
  * [`pynchon.models.plugins.NameSpace`](/src/pynchon/models/plugins/__init__.py#L27-L37)
    * with bases ([CliPlugin](#pynchonmodelspluginscli),)
    * with properties: (4 total)
      *  [`config`](/src/pynchon/models/plugins/__init__.py#L108) -> inspect._empty
      *  [`logger`](/src/pynchon/models/plugins/__init__.py#L37) -> inspect._empty
      *  [`plugin_config`](/src/pynchon/models/plugins/__init__.py#L103) -> inspect._empty
      *  [`project_root`](/src/pynchon/models/plugins/__init__.py#L98) -> inspect._empty
<!--- This is a markdown file.  Comments look like this --->
-------------------------------------------------------------------------------
### pynchon.models.plugins.cli
* Overview:  [source code](/src/pynchon/models/plugins/cli.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
<!--- This is a markdown file.  Comments look like this --->
* Classes: (1 total)
  * [`pynchon.models.plugins.cli.CliPlugin`](/src/pynchon/models/plugins/cli.py#L21-L303)
    * with bases ([PynchonPlugin](#pynchonmodelspluginspynchon),)
    * with admonitions:  [🐉 Complex](/src/pynchon/models/plugins/cli.py#L179 "score 11 / 7") 
    * with properties: (4 total)
      *  [`config`](/src/pynchon/models/plugins/cli.py#L108) -> inspect._empty
      *  [`logger`](/src/pynchon/models/plugins/cli.py#L37) -> inspect._empty
      *  [`plugin_config`](/src/pynchon/models/plugins/cli.py#L103) -> inspect._empty
      *  [`project_root`](/src/pynchon/models/plugins/cli.py#L98) -> inspect._empty
<!--- This is a markdown file.  Comments look like this --->
-------------------------------------------------------------------------------
### pynchon.models.plugins.provider
* Overview:  [source code](/src/pynchon/models/plugins/provider.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
<!--- This is a markdown file.  Comments look like this --->
* Classes: (1 total)
  * [`pynchon.models.plugins.provider.Provider`](/src/pynchon/models/plugins/provider.py#L15-L29)
    * with bases ([CliPlugin](#pynchonmodelspluginscli),)
    * with properties: (4 total)
      *  [`config`](/src/pynchon/models/plugins/provider.py#L108) -> inspect._empty
      *  [`logger`](/src/pynchon/models/plugins/provider.py#L37) -> inspect._empty
      *  [`plugin_config`](/src/pynchon/models/plugins/provider.py#L103) -> inspect._empty
      *  [`project_root`](/src/pynchon/models/plugins/provider.py#L98) -> inspect._empty
<!--- This is a markdown file.  Comments look like this --->
-------------------------------------------------------------------------------
### pynchon.models.plugins.validators
* Overview:  [source code](/src/pynchon/models/plugins/validators.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
<!--- This is a markdown file.  Comments look like this --->
* Functions: (2 total)
  * [`pynchon.models.plugins.validators.require_conf_key`](/src/pynchon/models/plugins/validators.py#L13-L28) with signature `(kls, self=None, vdata=None, strict: bool = True)`
  * [`pynchon.models.plugins.validators.warn_config_kls`](/src/pynchon/models/plugins/validators.py#L31-L42) with signature `(kls, self=None, vdata=None)`
<!--- This is a markdown file.  Comments look like this --->
-------------------------------------------------------------------------------
### pynchon.models.plugins.pynchon
* Overview:  [source code](/src/pynchon/models/plugins/pynchon.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
<!--- This is a markdown file.  Comments look like this --->
* Classes: (1 total)
  * [`pynchon.models.plugins.pynchon.PynchonPlugin`](/src/pynchon/models/plugins/pynchon.py#L22-L183)
    * with bases ([Plugin](#fleksplugin),)
    * with admonitions:  [🐉 Complex](/src/pynchon/models/plugins/pynchon.py#L102 "score 12 / 7") 
    * with properties: (4 total)
      *  [`config`](/src/pynchon/models/plugins/pynchon.py#L108) -> inspect._empty
      *  [`logger`](/src/pynchon/models/plugins/pynchon.py#L37) -> inspect._empty
      *  [`plugin_config`](/src/pynchon/models/plugins/pynchon.py#L103) -> inspect._empty
      *  [`project_root`](/src/pynchon/models/plugins/pynchon.py#L98) -> inspect._empty
<!--- This is a markdown file.  Comments look like this --->
-------------------------------------------------------------------------------
### pynchon.models.plugins.tool
* Overview:  [source code](/src/pynchon/models/plugins/tool.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
<!--- This is a markdown file.  Comments look like this --->
* Classes: (1 total)
  * [`pynchon.models.plugins.tool.ToolPlugin`](/src/pynchon/models/plugins/tool.py#L12-L24)
    * with bases ([CliPlugin](#pynchonmodelspluginscli),)
    * with properties: (4 total)
      *  [`config`](/src/pynchon/models/plugins/tool.py#L108) -> inspect._empty
      *  [`logger`](/src/pynchon/models/plugins/tool.py#L37) -> inspect._empty
      *  [`plugin_config`](/src/pynchon/models/plugins/tool.py#L103) -> inspect._empty
      *  [`project_root`](/src/pynchon/models/plugins/tool.py#L98) -> inspect._empty
<!--- This is a markdown file.  Comments look like this --->
-------------------------------------------------------------------------------
### pynchon.cli
* Overview:  [source code](/src/pynchon/cli/__init__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
<!--- This is a markdown file.  Comments look like this --->
* Classes: (0 total)
<!--- This is a markdown file.  Comments look like this --->
-------------------------------------------------------------------------------
### pynchon.cli.options
* Overview:  [source code](/src/pynchon/cli/options.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
<!--- This is a markdown file.  Comments look like this --->
-------------------------------------------------------------------------------
### pynchon.cli.common
* Overview:  [source code](/src/pynchon/cli/common.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
<!--- This is a markdown file.  Comments look like this --->
* Classes: (2 total)
  * [`pynchon.cli.common.kommand`](/src/pynchon/cli/common.py#L96-L183)
    * with bases ([`__builtin__.object`](https://docs.python.org/3/library/functions.html#object),)
  * [`pynchon.cli.common.groop`](/src/pynchon/cli/common.py#L186-L200)
    * with bases ([kommand](#pynchonclicommon),)
<!--- This is a markdown file.  Comments look like this --->
* Functions: (3 total)
  /src/pynchon/cli/common.py#L70-L93 "")
  * [`pynchon.cli.common.create_command`](/src/pynchon/cli/common.py#L70-L93) with signature `(_name: str, fxn: Callable, entry=None)`
    * with admonitions:  [ 🚩has FIXMEs ](/src/pynchon/cli/common.py#L71 "on lines [71]") 
  * [`pynchon.cli.common.entry_for`](/src/pynchon/cli/common.py#L48-L67) with signature `(name)`
  * [`pynchon.cli.common.load_groups_from_children`](/src/pynchon/cli/common.py#L15-L29) with signature `(root=None, parent=None)`
<!--- This is a markdown file.  Comments look like this --->
-------------------------------------------------------------------------------
### pynchon.api
* Overview:  [source code](/src/pynchon/api/__init__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
<!--- This is a markdown file.  Comments look like this --->
* Classes: (0 total)
<!--- This is a markdown file.  Comments look like this --->
-------------------------------------------------------------------------------
### pynchon.api.render
* Overview:  [source code](/src/pynchon/api/render.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
<!--- This is a markdown file.  Comments look like this --->
* Functions: (9 total)
  * [`pynchon.api.render.clean_whitespace`](/src/pynchon/api/render.py#L157-L159) with signature `(txt: str)`
  * [`pynchon.api.render.dictionary`](/src/pynchon/api/render.py#L30-L36) with signature `(input, context)`
  * [`pynchon.api.render.get_jinja_env`](/src/pynchon/api/render.py#L79-L105) with signature `(*includes, quiet: bool = False)`
  * [`pynchon.api.render.get_jinja_globals`](/src/pynchon/api/render.py#L39-L68) with signature `()`
  * [`pynchon.api.render.get_jinja_includes`](/src/pynchon/api/render.py#L71-L76) with signature `(*includes)`
  * [`pynchon.api.render.get_template`](/src/pynchon/api/render.py#L133-L154)
    * with signature `(template_name: Union[str, pynchon.abcs.path.Path] = None, env=None, from_string: str = None)`
  * [`pynchon.api.render.get_template_from_file`](/src/pynchon/api/render.py#L120-L130) with signature `(file: str = None, **kwargs)`
  * [`pynchon.api.render.get_template_from_string`](/src/pynchon/api/render.py#L108-L117) with signature `(content, env=None)`
  * [`pynchon.api.render.is_templated`](/src/pynchon/api/render.py#L25-L27) with signature `(txt: str = '') -> bool`
<!--- This is a markdown file.  Comments look like this --->
-------------------------------------------------------------------------------
### pynchon.api.pynchon
* Overview:  [source code](/src/pynchon/api/pynchon.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
<!--- This is a markdown file.  Comments look like this --->
-------------------------------------------------------------------------------
### pynchon.api.parsers
* Overview:  [source code](/src/pynchon/api/parsers/__init__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
<!--- This is a markdown file.  Comments look like this --->
-------------------------------------------------------------------------------
### pynchon.api.project
* Overview:  [source code](/src/pynchon/api/project/__init__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
<!--- This is a markdown file.  Comments look like this --->
* Functions: (2 total)
  * [`pynchon.api.project.get_config`](/src/pynchon/api/project/__init__.py#L8-L12) with signature `() -> dict`
  * [`pynchon.api.project.plan`](/src/pynchon/api/project/__init__.py#L15-L44) with signature `(config: dict = {}) -> dict`
<!--- This is a markdown file.  Comments look like this --->
-------------------------------------------------------------------------------
### pynchon.api.git
* Overview:  [source code](/src/pynchon/api/git/__init__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
<!--- This is a markdown file.  Comments look like this --->
-------------------------------------------------------------------------------
### pynchon.codemod
* Overview:  [source code](/src/pynchon/codemod/__init__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
<!--- This is a markdown file.  Comments look like this --->
* Classes: (0 total)
<!--- This is a markdown file.  Comments look like this --->
-------------------------------------------------------------------------------
### pynchon.codemod.commands
* Overview:  [source code](/src/pynchon/codemod/commands/__init__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
<!--- This is a markdown file.  Comments look like this --->
* Classes: (0 total)
<!--- This is a markdown file.  Comments look like this --->
-------------------------------------------------------------------------------
### pynchon.codemod.commands.docstrings
* Overview:  [source code](/src/pynchon/codemod/commands/docstrings/__init__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
<!--- This is a markdown file.  Comments look like this --->
* Classes: (0 total)
<!--- This is a markdown file.  Comments look like this --->
-------------------------------------------------------------------------------
### pynchon.codemod.commands.docstrings.base
* Overview:  [source code](/src/pynchon/codemod/commands/docstrings/base.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
<!--- This is a markdown file.  Comments look like this --->
* Classes: (1 total)
  * [`pynchon.codemod.commands.docstrings.base.base`](/src/pynchon/codemod/commands/docstrings/base.py#L13-L29)
    * with bases ([ContextAwareTransformer](#libcstcodemod_visitor),)
    * with properties: (1 total)
      *  [`module`](/src/pynchon/codemod/commands/docstrings/base.py#L48) -> libcst._nodes.module.Module
<!--- This is a markdown file.  Comments look like this --->
-------------------------------------------------------------------------------
### pynchon.codemod.commands.docstrings.javadoc
* Overview:  [source code](/src/pynchon/codemod/commands/docstrings/javadoc.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
<!--- This is a markdown file.  Comments look like this --->
* Classes: (2 total)
  * [`pynchon.codemod.commands.docstrings.javadoc.module`](/src/pynchon/codemod/commands/docstrings/javadoc.py#L11-L12)
    * with bases ([base](#pynchoncodemodcommandsdocstringsbase),)
    * with properties: (1 total)
      *  [`module`](/src/pynchon/codemod/commands/docstrings/javadoc.py#L48) -> libcst._nodes.module.Module
  * [`pynchon.codemod.commands.docstrings.javadoc.function`](/src/pynchon/codemod/commands/docstrings/javadoc.py#L15-L24)
    * with bases ([base](#pynchoncodemodcommandsdocstringsbase),)
    * with properties: (1 total)
      *  [`module`](/src/pynchon/codemod/commands/docstrings/javadoc.py#L48) -> libcst._nodes.module.Module
<!--- This is a markdown file.  Comments look like this --->
-------------------------------------------------------------------------------
### pynchon.codemod.commands.docstrings.simple
* Overview:  [source code](/src/pynchon/codemod/commands/docstrings/simple.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
<!--- This is a markdown file.  Comments look like this --->
* Classes: (3 total)
  * [`pynchon.codemod.commands.docstrings.simple.klass`](/src/pynchon/codemod/commands/docstrings/simple.py#L152-L153)
    * with bases ([base](#pynchoncodemodcommandsdocstringsbase),)
    * with properties: (1 total)
      *  [`module`](/src/pynchon/codemod/commands/docstrings/simple.py#L48) -> libcst._nodes.module.Module
  * [`pynchon.codemod.commands.docstrings.simple.module`](/src/pynchon/codemod/commands/docstrings/simple.py#L160-L192)
    * with bases ([base](#pynchoncodemodcommandsdocstringsbase),)
    * with properties: (1 total)
      *  [`module`](/src/pynchon/codemod/commands/docstrings/simple.py#L48) -> libcst._nodes.module.Module
  * [`pynchon.codemod.commands.docstrings.simple.function`](/src/pynchon/codemod/commands/docstrings/simple.py#L195-L299)
    * with bases ([base](#pynchoncodemodcommandsdocstringsbase),)
    * with admonitions:  [🐉 Complex](/src/pynchon/codemod/commands/docstrings/simple.py#L33 "score 9 / 7") 
    * with properties: (1 total)
      *  [`module`](/src/pynchon/codemod/commands/docstrings/simple.py#L48) -> libcst._nodes.module.Module
<!--- This is a markdown file.  Comments look like this --->
* Functions: (4 total)
  * [`pynchon.codemod.commands.docstrings.simple._get_docstring`](/src/pynchon/codemod/commands/docstrings/simple.py#L122-L149) with signature ``
  * [`pynchon.codemod.commands.docstrings.simple.get_obj`](/src/pynchon/codemod/commands/docstrings/simple.py#L25-L40) with signature `(mod=None, dotpath=None)`
  * [`pynchon.codemod.commands.docstrings.simple.is_param_doc`](/src/pynchon/codemod/commands/docstrings/simple.py#L18-L22) with signature `(txt: str)`
  * [`pynchon.codemod.commands.docstrings.simple.write_docstring`](/src/pynchon/codemod/commands/docstrings/simple.py#L43-L119) with signature `(mod=None, dotpath=None, obj=None, docstring=None)`
