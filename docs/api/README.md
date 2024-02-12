## API for 'pynchon' package

---------------------------------------------------------------------------------------------------------------------------------------------------------------
### pynchon
* Overview:  [source code](/src/pynchon/__init__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (0 total)
-------------------------------------------------------------------------------
### pynchon.events
* Overview:  [source code](/src/pynchon/events.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (1 total)
  * [`pynchon.events.Signal`](/src/pynchon/events.py#L12-L17)
    * with bases ([Signal](#blinkerbase),)
* Functions: (6 total)
  * [`pynchon.events._lifecycle`](/src/pynchon/events.py#L73-L85) with signature ``
  * [`pynchon.events.lifecycle_applying`](/src/pynchon/events.py#L42-L47) with signature `(sender, applying=None, **kwargs)`
  * [`pynchon.events.lifecycle_config`](/src/pynchon/events.py#L34-L39) with signature `(sender, config)`
  * [`pynchon.events.lifecycle_msg`](/src/pynchon/events.py#L62-L69) with signature `(sender, msg=None, **unused)`
  * [`pynchon.events.lifecycle_plugin`](/src/pynchon/events.py#L26-L31) with signature `(sender, plugin)`
  * [`pynchon.events.lifecycle_stage`](/src/pynchon/events.py#L50-L59) with signature `(sender, stage=None, **unused)`
-------------------------------------------------------------------------------
### pynchon.constants
* Overview:  [source code](/src/pynchon/constants.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
-------------------------------------------------------------------------------
### pynchon.bin
* Overview:  [source code](/src/pynchon/bin.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (1 total)
  * [`pynchon.bin.RootGroup`](/src/pynchon/bin.py#L20-L25)
    * with bases ([RootGroup](#flekscliroot_group),)
* Functions: (3 total)
  * [`pynchon.bin.bootstrap`](/src/pynchon/bin.py#L45-L72) with signature `()`
  * [`pynchon.bin.default`](/src/pynchon/bin.py#L75-L96) with signature `(*args: Any, **kwargs: Any) -> Any`
  * [`pynchon.bin.entry`](/src/pynchon/bin.py#L28-L42) with signature `(*args: Any, **kwargs: Any) -> Any`
-------------------------------------------------------------------------------
### pynchon.core
* Overview:  [source code](/src/pynchon/core.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (1 total)
  * [`pynchon.core.Config`](/src/pynchon/core.py#L50-L124)
    * with bases ([Config](#pynchonabcs),)
    * with properties: (4 total)
      *  [`plugins`](/src/pynchon/core.py#L104) -> inspect._empty
      *  [`root`](/src/pynchon/core.py#L88) -> str
      *  [`version`](/src/pynchon/core.py#L82) -> str
      *  [`working_dir`](/src/pynchon/core.py#L121) -> inspect._empty
* Functions: (1 total)
  * [`pynchon.core.validate`](/src/pynchon/core.py#L15-L47) with signature `(kls=None, self=None, vdata=None)`
    * with admonitions:  [🐉 Complex](/src/pynchon/core.py#L1 "score 10 / 7") 
-------------------------------------------------------------------------------
### pynchon.annotate
* Overview:  [source code](/src/pynchon/annotate.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Functions: (4 total)
  * [`pynchon.annotate.function`](/src/pynchon/annotate.py#L127-L178) with signature `(name, fxn) -> None`
  * [`pynchon.annotate.klass`](/src/pynchon/annotate.py#L13-L95) with signature `(name, kls) -> NoneType`
    * with admonitions:  [🐉 Complex](/src/pynchon/annotate.py#L1 "score 16 / 7") 
  * [`pynchon.annotate.module`](/src/pynchon/annotate.py#L98-L109) with signature `(name, module, working_dir=None) -> None`
  * [`pynchon.annotate.should_skip`](/src/pynchon/annotate.py#L112-L124) with signature `(name: str)`
-------------------------------------------------------------------------------
### pynchon.app
* Overview:  [source code](/src/pynchon/app.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
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
  * [`pynchon.app.App`](/src/pynchon/app.py#L163-L170)
    * with bases ([AppConsole](#pynchonapp),[AppEvents](#pynchonapp),[AppExitHooks](#pynchonapp),)
    * with properties: (2 total)
      *  [`manager`](/src/pynchon/app.py#L37) -> inspect._empty
      *  [`status_bar`](/src/pynchon/app.py#L37) -> inspect._empty
-------------------------------------------------------------------------------
### pynchon.testing
* Overview:  [source code](/src/pynchon/testing.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
-------------------------------------------------------------------------------
### pynchon.tagging
* Overview:  [source code](/src/pynchon/tagging.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
-------------------------------------------------------------------------------
### pynchon.__main__
* Overview: (entrypoint) | [source code](/src/pynchon/__main__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
-------------------------------------------------------------------------------
### pynchon.base
* Overview:  [source code](/src/pynchon/base.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
-------------------------------------------------------------------------------
### pynchon.abcs
* Overview:  [source code](/src/pynchon/abcs/__init__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (1 total)
  * [`pynchon.abcs.Config`](/src/pynchon/abcs/__init__.py#L14-L15)
    * with bases ([Config](#fleksconfig),)
* Classes: (1 total)
  * [`pynchon.abcs.Config`](/src/pynchon/abcs/__init__.py#L14-L15)
    * with bases ([Config](#fleksconfig),)
-------------------------------------------------------------------------------
### pynchon.abcs.config
* Overview:  [source code](/src/pynchon/abcs/config.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
-------------------------------------------------------------------------------
### pynchon.abcs.attrdict
* Overview:  [source code](/src/pynchon/abcs/attrdict.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (2 total)
  * [`pynchon.abcs.attrdict.AttrDictBase`](/src/pynchon/abcs/attrdict.py#L9-L49)
    * with bases ([`__builtin__.object`](https://docs.python.org/3/library/functions.html#object),)
  * [`pynchon.abcs.attrdict.AttrDict`](/src/pynchon/abcs/attrdict.py#L55-L56)
    * with bases ([AttrDictBase](#pynchonabcsattrdict),[`__builtin__.dict`](https://docs.python.org/3/library/functions.html#dict),)
-------------------------------------------------------------------------------
### pynchon.abcs.visitor
* Overview:  [source code](/src/pynchon/abcs/visitor.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (3 total)
  * [`pynchon.abcs.visitor.Visitor`](/src/pynchon/abcs/visitor.py#L15-L53)
    * with bases ([`__builtin__.object`](https://docs.python.org/3/library/functions.html#object),)
  * [`pynchon.abcs.visitor.TemplatedDict`](/src/pynchon/abcs/visitor.py#L106-L147)
    * with bases ([`__builtin__.dict`](https://docs.python.org/3/library/functions.html#dict),)
    * with properties: (2 total)
      *  [`traversal`](/src/pynchon/abcs/visitor.py#L135) -> inspect._empty
      *  [`unresolved`](/src/pynchon/abcs/visitor.py#L144) -> inspect._empty
  * [`pynchon.abcs.visitor.JinjaDict`](/src/pynchon/abcs/visitor.py#L155-L212)
    * with bases ([TemplatedDict](#pynchonabcsvisitor),)
    * with properties: (2 total)
      *  [`traversal`](/src/pynchon/abcs/visitor.py#L135) -> inspect._empty
      *  [`unresolved`](/src/pynchon/abcs/visitor.py#L144) -> inspect._empty
* Functions: (1 total)
  * [`pynchon.abcs.visitor.traverse`](/src/pynchon/abcs/visitor.py#L56-L103) with signature `(obj, visitor=None, visitor_kls=None, visitor_kwargs={})`
    * with admonitions:  [🐉 Complex](/src/pynchon/abcs/visitor.py#L1 "score 10 / 7") 
-------------------------------------------------------------------------------
### pynchon.abcs.path
* Overview:  [source code](/src/pynchon/abcs/path.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (1 total)
  * [`pynchon.abcs.path.Path`](/src/pynchon/abcs/path.py#L14-L76)
    * with bases ([PosixPath](#pathlib),)
    * with properties: (10 total)
      *  [`anchor`](/src/pynchon/abcs/path.py#L616) -> inspect._empty
      *  [`drive`](/src/pynchon/abcs/path.py#L14) -> None
      *  [`name`](/src/pynchon/abcs/path.py#L622) -> inspect._empty
      *  [`parent`](/src/pynchon/abcs/path.py#L777) -> inspect._empty
      *  [`parents`](/src/pynchon/abcs/path.py#L787) -> inspect._empty
      *  [`parts`](/src/pynchon/abcs/path.py#L745) -> inspect._empty
      *  [`root`](/src/pynchon/abcs/path.py#L14) -> None
      *  [`stem`](/src/pynchon/abcs/path.py#L657) -> inspect._empty
      *  [`suffix`](/src/pynchon/abcs/path.py#L630) -> inspect._empty
      *  [`suffixes`](/src/pynchon/abcs/path.py#L644) -> inspect._empty
-------------------------------------------------------------------------------
### pynchon.util
* Overview:  [source code](/src/pynchon/util/__init__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (0 total)
* Functions: (3 total)
  * [`pynchon.util.find_src_root`](/src/pynchon/util/__init__.py#L40-L53) with signature `(config: dict) -> str`
  * [`pynchon.util.get_root`](/src/pynchon/util/__init__.py#L11-L28) with signature `(path: str = '.') -> str`
  * [`pynchon.util.is_python_project`](/src/pynchon/util/__init__.py#L31-L37) with signature `() -> bool`
-------------------------------------------------------------------------------
### pynchon.util.click
* Overview:  [source code](/src/pynchon/util/click.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
-------------------------------------------------------------------------------
### pynchon.util.config
* Overview:  [source code](/src/pynchon/util/config.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
-------------------------------------------------------------------------------
### pynchon.util.events
* Overview:  [source code](/src/pynchon/util/events.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (1 total)
  * [`pynchon.util.events.Engine`](/src/pynchon/util/events.py#L12-L25)
    * with bases ([`__builtin__.object`](https://docs.python.org/3/library/functions.html#object),)
-------------------------------------------------------------------------------
### pynchon.util.splitvt
* Overview:  [source code](/src/pynchon/util/splitvt.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
-------------------------------------------------------------------------------
### pynchon.util.complexity
* Overview:  [source code](/src/pynchon/util/complexity.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (1 total)
  * [`pynchon.util.complexity.Checker`](/src/pynchon/util/complexity.py#L145-L157)
    * with bases ([McCabeChecker](#mccabe),)
* Functions: (5 total)
  * [`pynchon.util.complexity.clean_text`](/src/pynchon/util/complexity.py#L22-L29) with signature `(txt: str) -> str`
  * [`pynchon.util.complexity.complexity`](/src/pynchon/util/complexity.py#L160-L198) with signature `(code: str = None, fname: str = None, threshold: int = 7)`
  * [`pynchon.util.complexity.get_module`](/src/pynchon/util/complexity.py#L32-L57) with signature `(package: str = '', file: str = '')`
  * [`pynchon.util.complexity.get_refs`](/src/pynchon/util/complexity.py#L60-L88) with signature `(working_dir=None, module=None) -> dict`
  * [`pynchon.util.complexity.visit_module`](/src/pynchon/util/complexity.py#L91-L142)
    * with signature `(output=['-------------------------------------------------------------------------------\n### pynchon\n* Overview:  [source code](/src/pynchon/__init__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)\n* Classes: (0 total)', '-------------------------------------------------------------------------------\n### pynchon.events\n* Overview:  [source code](/src/pynchon/events.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)\n* Classes: (1 total)\n  * [`pynchon.events.Signal`](/src/pynchon/events.py#L12-L17)\n    * with bases ([Signal](#blinkerbase),)\n* Functions: (6 total)\n  * [`pynchon.events._lifecycle`](/src/pynchon/events.py#L73-L85) with signature ``\n  * [`pynchon.events.lifecycle_applying`](/src/pynchon/events.py#L42-L47) with signature `(sender, applying=None, **kwargs)`\n  * [`pynchon.events.lifecycle_config`](/src/pynchon/events.py#L34-L39) with signature `(sender, config)`\n  * [`pynchon.events.lifecycle_msg`](/src/pynchon/events.py#L62-L69) with signature `(sender, msg=None, **unused)`\n  * [`pynchon.events.lifecycle_plugin`](/src/pynchon/events.py#L26-L31) with signature `(sender, plugin)`\n  * [`pynchon.events.lifecycle_stage`](/src/pynchon/events.py#L50-L59) with signature `(sender, stage=None, **unused)`', '-------------------------------------------------------------------------------\n### pynchon.constants\n* Overview:  [source code](/src/pynchon/constants.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)', '-------------------------------------------------------------------------------\n### pynchon.bin\n* Overview:  [source code](/src/pynchon/bin.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)\n* Classes: (1 total)\n  * [`pynchon.bin.RootGroup`](/src/pynchon/bin.py#L20-L25)\n    * with bases ([RootGroup](#flekscliroot_group),)\n* Functions: (3 total)\n  * [`pynchon.bin.bootstrap`](/src/pynchon/bin.py#L45-L72) with signature `()`\n  * [`pynchon.bin.default`](/src/pynchon/bin.py#L75-L96) with signature `(*args: Any, **kwargs: Any) -> Any`\n  * [`pynchon.bin.entry`](/src/pynchon/bin.py#L28-L42) with signature `(*args: Any, **kwargs: Any) -> Any`', '-------------------------------------------------------------------------------\n### pynchon.core\n* Overview:  [source code](/src/pynchon/core.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)\n* Classes: (1 total)\n  * [`pynchon.core.Config`](/src/pynchon/core.py#L50-L124)\n    * with bases ([Config](#pynchonabcs),)\n    * with properties: (4 total)\n      *  [`plugins`](/src/pynchon/core.py#L104) -> inspect._empty\n      *  [`root`](/src/pynchon/core.py#L88) -> str\n      *  [`version`](/src/pynchon/core.py#L82) -> str\n      *  [`working_dir`](/src/pynchon/core.py#L121) -> inspect._empty\n* Functions: (1 total)\n  * [`pynchon.core.validate`](/src/pynchon/core.py#L15-L47) with signature `(kls=None, self=None, vdata=None)`\n    * with admonitions:  [🐉 Complex](/src/pynchon/core.py#L1 "score 10 / 7") ', '-------------------------------------------------------------------------------\n### pynchon.annotate\n* Overview:  [source code](/src/pynchon/annotate.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)\n* Functions: (4 total)\n  * [`pynchon.annotate.function`](/src/pynchon/annotate.py#L127-L178) with signature `(name, fxn) -> None`\n  * [`pynchon.annotate.klass`](/src/pynchon/annotate.py#L13-L95) with signature `(name, kls) -> NoneType`\n    * with admonitions:  [🐉 Complex](/src/pynchon/annotate.py#L1 "score 16 / 7") \n  * [`pynchon.annotate.module`](/src/pynchon/annotate.py#L98-L109) with signature `(name, module, working_dir=None) -> None`\n  * [`pynchon.annotate.should_skip`](/src/pynchon/annotate.py#L112-L124) with signature `(name: str)`', '-------------------------------------------------------------------------------\n### pynchon.app\n* Overview:  [source code](/src/pynchon/app.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)\n* Classes: (4 total)\n  * [`pynchon.app.AppEvents`](/src/pynchon/app.py#L20-L23)\n    * with bases ([AppBase](#fleksapp),)\n  * [`pynchon.app.AppConsole`](/src/pynchon/app.py#L26-L87)\n    * with bases ([AppBase](#fleksapp),)\n    * with properties: (2 total)\n      *  [`manager`](/src/pynchon/app.py#L37) -> inspect._empty\n      *  [`status_bar`](/src/pynchon/app.py#L37) -> inspect._empty\n  * [`pynchon.app.AppExitHooks`](/src/pynchon/app.py#L90-L160)\n    * with bases ([AppBase](#fleksapp),)\n  * [`pynchon.app.App`](/src/pynchon/app.py#L163-L170)\n    * with bases ([AppConsole](#pynchonapp),[AppEvents](#pynchonapp),[AppExitHooks](#pynchonapp),)\n    * with properties: (2 total)\n      *  [`manager`](/src/pynchon/app.py#L37) -> inspect._empty\n      *  [`status_bar`](/src/pynchon/app.py#L37) -> inspect._empty', '-------------------------------------------------------------------------------\n### pynchon.testing\n* Overview:  [source code](/src/pynchon/testing.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)', '-------------------------------------------------------------------------------\n### pynchon.tagging\n* Overview:  [source code](/src/pynchon/tagging.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)', '-------------------------------------------------------------------------------\n### pynchon.__main__\n* Overview: (entrypoint) | [source code](/src/pynchon/__main__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)', '-------------------------------------------------------------------------------\n### pynchon.base\n* Overview:  [source code](/src/pynchon/base.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)', '-------------------------------------------------------------------------------\n### pynchon.abcs\n* Overview:  [source code](/src/pynchon/abcs/__init__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)\n* Classes: (1 total)\n  * [`pynchon.abcs.Config`](/src/pynchon/abcs/__init__.py#L14-L15)\n    * with bases ([Config](#fleksconfig),)\n* Classes: (1 total)\n  * [`pynchon.abcs.Config`](/src/pynchon/abcs/__init__.py#L14-L15)\n    * with bases ([Config](#fleksconfig),)', '-------------------------------------------------------------------------------\n### pynchon.abcs.config\n* Overview:  [source code](/src/pynchon/abcs/config.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)', '-------------------------------------------------------------------------------\n### pynchon.abcs.attrdict\n* Overview:  [source code](/src/pynchon/abcs/attrdict.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)\n* Classes: (2 total)\n  * [`pynchon.abcs.attrdict.AttrDictBase`](/src/pynchon/abcs/attrdict.py#L9-L49)\n    * with bases ([`__builtin__.object`](https://docs.python.org/3/library/functions.html#object),)\n  * [`pynchon.abcs.attrdict.AttrDict`](/src/pynchon/abcs/attrdict.py#L55-L56)\n    * with bases ([AttrDictBase](#pynchonabcsattrdict),[`__builtin__.dict`](https://docs.python.org/3/library/functions.html#dict),)', '-------------------------------------------------------------------------------\n### pynchon.abcs.visitor\n* Overview:  [source code](/src/pynchon/abcs/visitor.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)\n* Classes: (3 total)\n  * [`pynchon.abcs.visitor.Visitor`](/src/pynchon/abcs/visitor.py#L15-L53)\n    * with bases ([`__builtin__.object`](https://docs.python.org/3/library/functions.html#object),)\n  * [`pynchon.abcs.visitor.TemplatedDict`](/src/pynchon/abcs/visitor.py#L106-L147)\n    * with bases ([`__builtin__.dict`](https://docs.python.org/3/library/functions.html#dict),)\n    * with properties: (2 total)\n      *  [`traversal`](/src/pynchon/abcs/visitor.py#L135) -> inspect._empty\n      *  [`unresolved`](/src/pynchon/abcs/visitor.py#L144) -> inspect._empty\n  * [`pynchon.abcs.visitor.JinjaDict`](/src/pynchon/abcs/visitor.py#L155-L212)\n    * with bases ([TemplatedDict](#pynchonabcsvisitor),)\n    * with properties: (2 total)\n      *  [`traversal`](/src/pynchon/abcs/visitor.py#L135) -> inspect._empty\n      *  [`unresolved`](/src/pynchon/abcs/visitor.py#L144) -> inspect._empty\n* Functions: (1 total)\n  * [`pynchon.abcs.visitor.traverse`](/src/pynchon/abcs/visitor.py#L56-L103) with signature `(obj, visitor=None, visitor_kls=None, visitor_kwargs={})`\n    * with admonitions:  [🐉 Complex](/src/pynchon/abcs/visitor.py#L1 "score 10 / 7") ', '-------------------------------------------------------------------------------\n### pynchon.abcs.path\n* Overview:  [source code](/src/pynchon/abcs/path.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)\n* Classes: (1 total)\n  * [`pynchon.abcs.path.Path`](/src/pynchon/abcs/path.py#L14-L76)\n    * with bases ([PosixPath](#pathlib),)\n    * with properties: (10 total)\n      *  [`anchor`](/src/pynchon/abcs/path.py#L616) -> inspect._empty\n      *  [`drive`](/src/pynchon/abcs/path.py#L14) -> None\n      *  [`name`](/src/pynchon/abcs/path.py#L622) -> inspect._empty\n      *  [`parent`](/src/pynchon/abcs/path.py#L777) -> inspect._empty\n      *  [`parents`](/src/pynchon/abcs/path.py#L787) -> inspect._empty\n      *  [`parts`](/src/pynchon/abcs/path.py#L745) -> inspect._empty\n      *  [`root`](/src/pynchon/abcs/path.py#L14) -> None\n      *  [`stem`](/src/pynchon/abcs/path.py#L657) -> inspect._empty\n      *  [`suffix`](/src/pynchon/abcs/path.py#L630) -> inspect._empty\n      *  [`suffixes`](/src/pynchon/abcs/path.py#L644) -> inspect._empty', "-------------------------------------------------------------------------------\n### pynchon.util\n* Overview:  [source code](/src/pynchon/util/__init__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)\n* Classes: (0 total)\n* Functions: (3 total)\n  * [`pynchon.util.find_src_root`](/src/pynchon/util/__init__.py#L40-L53) with signature `(config: dict) -> str`\n  * [`pynchon.util.get_root`](/src/pynchon/util/__init__.py#L11-L28) with signature `(path: str = '.') -> str`\n  * [`pynchon.util.is_python_project`](/src/pynchon/util/__init__.py#L31-L37) with signature `() -> bool`", '-------------------------------------------------------------------------------\n### pynchon.util.click\n* Overview:  [source code](/src/pynchon/util/click.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)', '-------------------------------------------------------------------------------\n### pynchon.util.config\n* Overview:  [source code](/src/pynchon/util/config.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)', '-------------------------------------------------------------------------------\n### pynchon.util.events\n* Overview:  [source code](/src/pynchon/util/events.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)\n* Classes: (1 total)\n  * [`pynchon.util.events.Engine`](/src/pynchon/util/events.py#L12-L25)\n    * with bases ([`__builtin__.object`](https://docs.python.org/3/library/functions.html#object),)', '-------------------------------------------------------------------------------\n### pynchon.util.splitvt\n* Overview:  [source code](/src/pynchon/util/splitvt.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)'], stats={}, module=None, template=None, visited=[], exclude: list = [], module_name=None, working_dir=Path('.'))`
-------------------------------------------------------------------------------
### pynchon.util.docker
* Overview:  [source code](/src/pynchon/util/docker.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (1 total)
  * [`pynchon.util.docker.DockerCtx`](/src/pynchon/util/docker.py#L11-L130)
    * with bases ([`__builtin__.object`](https://docs.python.org/3/library/functions.html#object),)
    * with properties: (6 total)
      *  [`fhandle`](/src/pynchon/util/docker.py#L90) -> inspect._empty
      *  [`file`](/src/pynchon/util/docker.py#L86) -> inspect._empty
      *  [`has_bash`](/src/pynchon/util/docker.py#L128) -> inspect._empty
      *  [`has_sh`](/src/pynchon/util/docker.py#L123) -> inspect._empty
      *  [`name`](/src/pynchon/util/docker.py#L76) -> inspect._empty
      *  [`tag`](/src/pynchon/util/docker.py#L82) -> inspect._empty
* Functions: (1 total)
  * [`pynchon.util.docker.Dockerfile`](/src/pynchon/util/docker.py#L133-L134) with signature `(txt, **kwargs)`
-------------------------------------------------------------------------------
### pynchon.util.oop
* Overview:  [source code](/src/pynchon/util/oop.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (2 total)
  * [`pynchon.util.oop.classproperty`](/src/pynchon/util/oop.py#L35-L42)
    * with bases ([`__builtin__.object`](https://docs.python.org/3/library/functions.html#object),)
  * [`pynchon.util.oop.classproperty_cached`](/src/pynchon/util/oop.py#L45-L53)
    * with bases ([classproperty](#pynchonutiloop),)
* Functions: (2 total)
  * [`pynchon.util.oop.is_subclass`](/src/pynchon/util/oop.py#L20-L32) with signature `(x, y, strict=True)`
  * [`pynchon.util.oop.new_in_class`](/src/pynchon/util/oop.py#L7-L17) with signature `(name: str, kls: Type)`
-------------------------------------------------------------------------------
### pynchon.util.python
* Overview:  [source code](/src/pynchon/util/python.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Functions: (3 total)
  * [`pynchon.util.python.is_package`](/src/pynchon/util/python.py#L11-L23) with signature `(folder: str) -> bool`
  * [`pynchon.util.python.load_entrypoints`](/src/pynchon/util/python.py#L44-L71) with signature `(config: dict = None) -> List[Dict]`
  * [`pynchon.util.python.load_setupcfg`](/src/pynchon/util/python.py#L26-L38) with signature `(file: str = '', folder: str = '')`
-------------------------------------------------------------------------------
### pynchon.util.typing
* Overview:  [source code](/src/pynchon/util/typing.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Functions: (1 total)
  * [`pynchon.util.typing.bind_method`](/src/pynchon/util/typing.py#L16-L31) with signature `(func, instance, as_name=None)`
-------------------------------------------------------------------------------
### pynchon.util.testing
* Overview:  [source code](/src/pynchon/util/testing.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Functions: (1 total)
  * [`pynchon.util.testing.get_test_info`](/src/pynchon/util/testing.py#L9-L22) with signature `(fname: str) -> dict`
-------------------------------------------------------------------------------
### pynchon.util.lme
* Overview:  [source code](/src/pynchon/util/lme.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (1 total)
  * [`pynchon.util.lme.Fake`](/src/pynchon/util/lme.py#L54-L55)
    * with bases ([`__builtin__.object`](https://docs.python.org/3/library/functions.html#object),)
* Functions: (2 total)
  * [`pynchon.util.lme.get_logger`](/src/pynchon/util/lme.py#L61-L96)
    * with signature `(name, console=<console width=88 ColorSystem.TRUECOLOR>, fake=False)`
  * [`pynchon.util.lme.set_global_level`](/src/pynchon/util/lme.py#L42-L51) with signature `(level)`
-------------------------------------------------------------------------------
### pynchon.util.makefile
* Overview:  [source code](/src/pynchon/util/makefile/__init__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (0 total)
* Functions: (5 total)
  * [`pynchon.util.makefile._get_file`](/src/pynchon/util/makefile/__init__.py#L59-L64) with signature ``
  * [`pynchon.util.makefile._get_prov_line`](/src/pynchon/util/makefile/__init__.py#L52-L56) with signature ``
  * [`pynchon.util.makefile._test`](/src/pynchon/util/makefile/__init__.py#L40-L49) with signature ``
  * [`pynchon.util.makefile.database`](/src/pynchon/util/makefile/__init__.py#L18-L37) with signature `(makefile: str = '', make='make') -> List[str]`
  * [`pynchon.util.makefile.parse`](/src/pynchon/util/makefile/__init__.py#L67-L162) with signature `(makefile: str = None, bodies=False, **kwargs)`
    * with admonitions:  [🐉 Complex](/src/pynchon/util/makefile/__init__.py#L2 "score 19 / 7") 
-------------------------------------------------------------------------------
### pynchon.util.makefile.__main__
* Overview: (entrypoint) | [source code](/src/pynchon/util/makefile/__main__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
-------------------------------------------------------------------------------
### pynchon.util.files
* Overview:  [source code](/src/pynchon/util/files/__init__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (0 total)
* Functions: (7 total)
  * [`pynchon.util.files.dumps`](/src/pynchon/util/files/__init__.py#L138-L145)
    * with signature `(content: str = None, file: str = None, quiet: bool = True, logger=<bound method Logger.info of <Logger pynchon.util.files (WARNING)>>) -> None`
  * [`pynchon.util.files.find_globs`](/src/pynchon/util/files/__init__.py#L114-L135)
    * with signature `(globs: List[pynchon.abcs.path.Path], includes=[], logger: object = None, quiet: bool = False) -> List[str]`
  * [`pynchon.util.files.find_src`](/src/pynchon/util/files/__init__.py#L93-L111) with signature `(src_root: str, exclude_patterns=[], quiet: bool = False) -> list`
  * [`pynchon.util.files.find_suffix`](/src/pynchon/util/files/__init__.py#L69-L74) with signature `(root: str = '', suffix: str = '') -> Optional[str]`
  * [`pynchon.util.files.get_git_root`](/src/pynchon/util/files/__init__.py#L77-L90) with signature `(path: str = '.') -> Optional[str]`
  * [`pynchon.util.files.is_prefix`](/src/pynchon/util/files/__init__.py#L19-L39)
    * with signature `(prepend_file: str = None, target_file: str = None, clean: bool = False) -> str`
  * [`pynchon.util.files.prepend`](/src/pynchon/util/files/__init__.py#L42-L66)
    * with signature `(prepend_file: str = None, target_file: str = None, clean: bool = False) -> bool`
-------------------------------------------------------------------------------
### pynchon.util.files.diff
* Overview:  [source code](/src/pynchon/util/files/diff.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Functions: (4 total)
  * [`pynchon.util.files.diff.diff`](/src/pynchon/util/files/diff.py#L71-L83) with signature `(file1: str = None, file2: str = None)`
  * [`pynchon.util.files.diff.diff_percent`](/src/pynchon/util/files/diff.py#L33-L46) with signature `(file1: str = None, file2: str = None)`
  * [`pynchon.util.files.diff.diff_report`](/src/pynchon/util/files/diff.py#L13-L30)
    * with signature `(diff, logger=<bound method Logger.debug of <Logger pynchon.util.files.diff (WARNING)>>)`
  * [`pynchon.util.files.diff.strdiff`](/src/pynchon/util/files/diff.py#L49-L65) with signature `(str1: str = None, str2: str = None, n=1)`
-------------------------------------------------------------------------------
### pynchon.util.files.__main__
* Overview: (entrypoint) | [source code](/src/pynchon/util/files/__main__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
-------------------------------------------------------------------------------
### pynchon.util.os
* Overview:  [source code](/src/pynchon/util/os/__init__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (0 total)
* Functions: (1 total)
  * [`pynchon.util.os.slurp_json`](/src/pynchon/util/os/__init__.py#L19-L25) with signature `(cmd: str, **kwargs)`
-------------------------------------------------------------------------------
### pynchon.util.os.pidfile
* Overview:  [source code](/src/pynchon/util/os/pidfile.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
-------------------------------------------------------------------------------
### pynchon.util.os.models
* Overview:  [source code](/src/pynchon/util/os/models.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
-------------------------------------------------------------------------------
### pynchon.util.os.pids
* Overview:  [source code](/src/pynchon/util/os/pids.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Functions: (1 total)
  * [`pynchon.util.os.pids.filter_pids`](/src/pynchon/util/os/pids.py#L13-L42) with signature `(cmdline__contains: str = None, **kwargs)`
    * with admonitions:  [🐉 Complex](/src/pynchon/util/os/pids.py#L1 "score 13 / 7") 
-------------------------------------------------------------------------------
### pynchon.util.text
* Overview:  [source code](/src/pynchon/util/text/__init__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (0 total)
* Functions: (1 total)
  * [`pynchon.util.text.indent`](/src/pynchon/util/text/__init__.py#L10-L21) with signature `(txt: str, level: int = 2) -> str`
-------------------------------------------------------------------------------
### pynchon.util.text.loads
* Overview:  [source code](/src/pynchon/util/text/loads.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Functions: (5 total)
  * [`pynchon.util.text.loads.ini`](/src/pynchon/util/text/loads.py#L16-L21) with signature `(content: str) -> Optional[str]`
  * [`pynchon.util.text.loads.json`](/src/pynchon/util/text/loads.py#L44-L51) with signature `(content: str = '') -> Optional[str]`
  * [`pynchon.util.text.loads.json5`](/src/pynchon/util/text/loads.py#L54-L76) with signature `(content: str = '', quiet=True) -> Dict`
  * [`pynchon.util.text.loads.toml`](/src/pynchon/util/text/loads.py#L35-L41) with signature `(content: str) -> Optional[str]`
  * [`pynchon.util.text.loads.yaml`](/src/pynchon/util/text/loads.py#L24-L30) with signature `(content: str) -> Optional[str]`
-------------------------------------------------------------------------------
### pynchon.util.text.dumps
* Overview:  [source code](/src/pynchon/util/text/dumps.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Functions: (1 total)
  * [`pynchon.util.text.dumps.yaml`](/src/pynchon/util/text/dumps.py#L18-L25) with signature `(file=None, content=None, obj=None)`
-------------------------------------------------------------------------------
### pynchon.util.text.__main__
* Overview: (entrypoint) | [source code](/src/pynchon/util/text/__main__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
-------------------------------------------------------------------------------
### pynchon.util.text.loadf
* Overview:  [source code](/src/pynchon/util/text/loadf/__init__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (0 total)
* Functions: (6 total)
  * [`pynchon.util.text.loadf.ini`](/src/pynchon/util/text/loadf/__init__.py#L30-L42) with signature `(file)`
  * [`pynchon.util.text.loadf.json`](/src/pynchon/util/text/loadf/__init__.py#L223-L244) with signature `(file: str = '', content: str = '', strict: bool = True) -> dict`
  * [`pynchon.util.text.loadf.json5`](/src/pynchon/util/text/loadf/__init__.py#L96-L220)
    * with signature `(file: str = '', files: List[str] = [], output: str = '', should_print: bool = False, wrapper_key: str = '', pull: str = '', push_data: str = '', push_file_data: str = '', push_json_data: str = '', push_command_output: str = '', under_key: str = '') -> None`
    * with admonitions:  [🐉 Complex](/src/pynchon/util/text/loadf/__init__.py#L28 "score 12 / 7") 
  * [`pynchon.util.text.loadf.loadf`](/src/pynchon/util/text/loadf/__init__.py#L19-L27) with signature `(file=None, content=None)`
  * [`pynchon.util.text.loadf.toml`](/src/pynchon/util/text/loadf/__init__.py#L57-L79) with signature `(file: str = None, strict: bool = True)`
  * [`pynchon.util.text.loadf.yaml`](/src/pynchon/util/text/loadf/__init__.py#L45-L54) with signature `(fname: str) -> Dict`
-------------------------------------------------------------------------------
### pynchon.util.text.loadf.__main__
* Overview: (entrypoint) | [source code](/src/pynchon/util/text/loadf/__main__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
-------------------------------------------------------------------------------
### pynchon.util.text.dumpf
* Overview:  [source code](/src/pynchon/util/text/dumpf/__init__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (0 total)
* Functions: (2 total)
  * [`pynchon.util.text.dumpf.json`](/src/pynchon/util/text/dumpf/__init__.py#L15-L19) with signature `(obj, file=None, **kwargs) -> None`
  * [`pynchon.util.text.dumpf.yaml`](/src/pynchon/util/text/dumpf/__init__.py#L22-L32) with signature `(file=None, output=None, **kwargs)`
-------------------------------------------------------------------------------
### pynchon.util.text.dumpf.__main__
* Overview: (entrypoint) | [source code](/src/pynchon/util/text/dumpf/__main__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
-------------------------------------------------------------------------------
### pynchon.util.text.render
* Overview:  [source code](/src/pynchon/util/text/render/__init__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (0 total)
* Functions: (4 total)
  * [`pynchon.util.text.render.j2cli`](/src/pynchon/util/text/render/__init__.py#L164-L207)
    * with signature `(output: str, should_print: bool, file: str, context: str, format: str = 'json') -> None`
  * [`pynchon.util.text.render.jinja`](/src/pynchon/util/text/render/__init__.py#L22-L65)
    * with signature `(text: str = '', file: str = '?', context: dict = {}, includes: List[str] = [], strict: bool = True)`
  * [`pynchon.util.text.render.jinja_file`](/src/pynchon/util/text/render/__init__.py#L104-L161)
    * with signature `(file: str, output: Optional[str] = '', should_print: bool = False, context: Dict = {}, context_file: Dict = {}, includes: List[str] = [], strict: bool = True) -> str`
  * [`pynchon.util.text.render.jinja_loadf`](/src/pynchon/util/text/render/__init__.py#L68-L101)
    * with signature `(file: str, context: Dict = {}, includes: List[str] = [], strict: bool = True, quiet: bool = False) -> str`
-------------------------------------------------------------------------------
### pynchon.util.text.render.__main__
* Overview: (entrypoint) | [source code](/src/pynchon/util/text/render/__main__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
-------------------------------------------------------------------------------
### pynchon.util.text.normalize
* Overview:  [source code](/src/pynchon/util/text/normalize/__init__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Functions: (2 total)
  * [`pynchon.util.text.normalize.normalize`](/src/pynchon/util/text/normalize/__init__.py#L22-L49)
    * with signature `(txt: str = '', post: List[Callable] = [<function <lambda> at 0x10cd419e0>, <function <lambda> at 0x10cd41260>], rules: List[Callable] = {' ': '_', '/': '_', '-': '_'}) -> str`
  * [`pynchon.util.text.normalize.snake_case`](/src/pynchon/util/text/normalize/__init__.py#L8-L16) with signature `(name: str) -> str`
-------------------------------------------------------------------------------
### pynchon.util.console
* Overview:  [source code](/src/pynchon/util/console/__init__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (0 total)
-------------------------------------------------------------------------------
### pynchon.util.console.__main__
* Overview: (entrypoint) | [source code](/src/pynchon/util/console/__main__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
-------------------------------------------------------------------------------
### pynchon.config
* Overview:  [source code](/src/pynchon/config/__init__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (0 total)
-------------------------------------------------------------------------------
### pynchon.config.util
* Overview:  [source code](/src/pynchon/config/util.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Functions: (4 total)
  * [`pynchon.config.util.config_folders`](/src/pynchon/config/util.py#L99-L116) with signature `()`
  * [`pynchon.config.util.finalize`](/src/pynchon/config/util.py#L19-L96) with signature `()`
  * [`pynchon.config.util.get_config_files`](/src/pynchon/config/util.py#L119-L129) with signature `()`
  * [`pynchon.config.util.load_config_from_files`](/src/pynchon/config/util.py#L132-L159) with signature `() -> Dict[str, str]`
-------------------------------------------------------------------------------
### pynchon.plugins
* Overview:  [source code](/src/pynchon/plugins/__init__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (0 total)
-------------------------------------------------------------------------------
### pynchon.plugins.plugins
* Overview:  [source code](/src/pynchon/plugins/plugins.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (1 total)
  * [`pynchon.plugins.plugins.PluginsMan`](/src/pynchon/plugins/plugins.py#L14-L49)
    * with bases ([Manager](#pynchonmodelsplanner),)
    * with properties: (9 total)
      *  [`Plan`](/src/pynchon/plugins/plugins.py#L35) -> inspect._empty
      *  [`apply_hooks`](/src/pynchon/plugins/plugins.py#L37) -> inspect._empty
      *  [`config`](/src/pynchon/plugins/plugins.py#L118) -> inspect._empty
      *  [`exclude_patterns`](/src/pynchon/plugins/plugins.py#L32) -> inspect._empty
      *  [`hooks`](/src/pynchon/plugins/plugins.py#L37) -> inspect._empty
      *  [`logger`](/src/pynchon/plugins/plugins.py#L37) -> inspect._empty
      *  [`plugin_config`](/src/pynchon/plugins/plugins.py#L113) -> inspect._empty
      *  [`project_root`](/src/pynchon/plugins/plugins.py#L108) -> inspect._empty
      *  [`working_dir`](/src/pynchon/plugins/plugins.py#L27) -> inspect._empty
-------------------------------------------------------------------------------
### pynchon.plugins.__template__
* Overview:  [source code](/src/pynchon/plugins/__template__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (1 total)
  * [`pynchon.plugins.__template__.PluginTemplate`](/src/pynchon/plugins/__template__.py#L10-L18)
    * with bases ([Provider](#pynchonmodelspluginsprovider),)
    * with properties: (4 total)
      *  [`config`](/src/pynchon/plugins/__template__.py#L118) -> inspect._empty
      *  [`logger`](/src/pynchon/plugins/__template__.py#L37) -> inspect._empty
      *  [`plugin_config`](/src/pynchon/plugins/__template__.py#L113) -> inspect._empty
      *  [`project_root`](/src/pynchon/plugins/__template__.py#L108) -> inspect._empty
-------------------------------------------------------------------------------
### pynchon.plugins.git
* Overview:  [source code](/src/pynchon/plugins/git.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (2 total)
  * [`pynchon.plugins.git.GitConfig`](/src/pynchon/plugins/git.py#L12-L112)
    * with bases ([Config](#pynchonabcs),)
    * with properties: (8 total)
      *  [`branch_name`](/src/pynchon/plugins/git.py#L96) -> inspect._empty
      *  [`github_org`](/src/pynchon/plugins/git.py#L67) -> typing.Optional[str]
      *  [`hash`](/src/pynchon/plugins/git.py#L105) -> str
      *  [`is_github`](/src/pynchon/plugins/git.py#L61) -> inspect._empty
      *  [`repo`](/src/pynchon/plugins/git.py#L51) -> typing.Optional[str]
      *  [`repo_name`](/src/pynchon/plugins/git.py#L78) -> typing.Optional[str]
      *  [`repo_url`](/src/pynchon/plugins/git.py#L90) -> inspect._empty
      *  [`root`](/src/pynchon/plugins/git.py#L42) -> typing.Optional[str]
  * [`pynchon.plugins.git.Git`](/src/pynchon/plugins/git.py#L115-L150)
    * with bases ([Provider](#pynchonmodelspluginsprovider),)
    * with properties: (5 total)
      *  [`config`](/src/pynchon/plugins/git.py#L118) -> inspect._empty
      *  [`logger`](/src/pynchon/plugins/git.py#L37) -> inspect._empty
      *  [`modified`](/src/pynchon/plugins/git.py#L134) -> typing.List[pynchon.abcs.path.Path]
      *  [`plugin_config`](/src/pynchon/plugins/git.py#L113) -> inspect._empty
      *  [`project_root`](/src/pynchon/plugins/git.py#L108) -> inspect._empty
-------------------------------------------------------------------------------
### pynchon.plugins.hooks
* Overview:  [source code](/src/pynchon/plugins/hooks.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
-------------------------------------------------------------------------------
### pynchon.plugins.release
* Overview:  [source code](/src/pynchon/plugins/release.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
-------------------------------------------------------------------------------
### pynchon.plugins.deck
* Overview:  [source code](/src/pynchon/plugins/deck.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (1 total)
  * [`pynchon.plugins.deck.Deck`](/src/pynchon/plugins/deck.py#L10-L58)
    * with bases ([ResourceManager](#pynchonmodelsplanner),)
    * with properties: (10 total)
      *  [`Plan`](/src/pynchon/plugins/deck.py#L35) -> inspect._empty
      *  [`apply_hooks`](/src/pynchon/plugins/deck.py#L37) -> inspect._empty
      *  [`changes`](/src/pynchon/plugins/deck.py#L191) -> inspect._empty
      *  [`config`](/src/pynchon/plugins/deck.py#L118) -> inspect._empty
      *  [`exclude_patterns`](/src/pynchon/plugins/deck.py#L32) -> inspect._empty
      *  [`hooks`](/src/pynchon/plugins/deck.py#L37) -> inspect._empty
      *  [`logger`](/src/pynchon/plugins/deck.py#L37) -> inspect._empty
      *  [`plugin_config`](/src/pynchon/plugins/deck.py#L113) -> inspect._empty
      *  [`project_root`](/src/pynchon/plugins/deck.py#L108) -> inspect._empty
      *  [`working_dir`](/src/pynchon/plugins/deck.py#L27) -> inspect._empty
-------------------------------------------------------------------------------
### pynchon.plugins.cicd
* Overview:  [source code](/src/pynchon/plugins/cicd.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (1 total)
  * [`pynchon.plugins.cicd.CiCd`](/src/pynchon/plugins/cicd.py#L13-L54)
    * with bases ([Provider](#pynchonmodelspluginsprovider),)
    * with properties: (4 total)
      *  [`config`](/src/pynchon/plugins/cicd.py#L118) -> inspect._empty
      *  [`logger`](/src/pynchon/plugins/cicd.py#L37) -> inspect._empty
      *  [`plugin_config`](/src/pynchon/plugins/cicd.py#L113) -> inspect._empty
      *  [`project_root`](/src/pynchon/plugins/cicd.py#L108) -> inspect._empty
-------------------------------------------------------------------------------
### pynchon.plugins.gen
* Overview:  [source code](/src/pynchon/plugins/gen.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (1 total)
  * [`pynchon.plugins.gen.Generators`](/src/pynchon/plugins/gen.py#L10-L84)
    * with bases ([NameSpace](#pynchonmodelsplugins),)
    * with admonitions:  [🐉 Complex](/src/pynchon/plugins/gen.py#L21 "score 11 / 7") 
    * with properties: (4 total)
      *  [`config`](/src/pynchon/plugins/gen.py#L118) -> inspect._empty
      *  [`logger`](/src/pynchon/plugins/gen.py#L37) -> inspect._empty
      *  [`plugin_config`](/src/pynchon/plugins/gen.py#L113) -> inspect._empty
      *  [`project_root`](/src/pynchon/plugins/gen.py#L108) -> inspect._empty
-------------------------------------------------------------------------------
### pynchon.plugins.render
* Overview:  [source code](/src/pynchon/plugins/render.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (1 total)
  * [`pynchon.plugins.render.Renderers`](/src/pynchon/plugins/render.py#L11-L15)
    * with bases ([NameSpace](#pynchonmodelsplugins),)
    * with properties: (4 total)
      *  [`config`](/src/pynchon/plugins/render.py#L118) -> inspect._empty
      *  [`logger`](/src/pynchon/plugins/render.py#L37) -> inspect._empty
      *  [`plugin_config`](/src/pynchon/plugins/render.py#L113) -> inspect._empty
      *  [`project_root`](/src/pynchon/plugins/render.py#L108) -> inspect._empty
-------------------------------------------------------------------------------
### pynchon.plugins.util
* Overview:  [source code](/src/pynchon/plugins/util.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (3 total)
  * [`pynchon.plugins.util.PluginNotInitialized`](/src/pynchon/plugins/util.py#L13-L14)
    * with bases ([`__builtin__.RuntimeError`](https://docs.python.org/3/library/functions.html#RuntimeError),)
  * [`pynchon.plugins.util.PluginNotRegistered`](/src/pynchon/plugins/util.py#L17-L18)
    * with bases ([`__builtin__.RuntimeError`](https://docs.python.org/3/library/functions.html#RuntimeError),)
  * [`pynchon.plugins.util.PluginNotConfigured`](/src/pynchon/plugins/util.py#L21-L22)
    * with bases ([`__builtin__.RuntimeError`](https://docs.python.org/3/library/functions.html#RuntimeError),)
* Functions: (3 total)
  * [`pynchon.plugins.util.get_plugin_class`](/src/pynchon/plugins/util.py#L38-L49) with signature `(plugin_name: str, strict: bool = True) -> Type`
  * [`pynchon.plugins.util.get_plugin_meta`](/src/pynchon/plugins/util.py#L25-L35) with signature `(plugin_name: str, strict: bool = True) -> Dict`
  * [`pynchon.plugins.util.get_plugin_obj`](/src/pynchon/plugins/util.py#L55-L68) with signature `(plugin_name: str) -> object`
-------------------------------------------------------------------------------
### pynchon.plugins.mermaid
* Overview:  [source code](/src/pynchon/plugins/mermaid.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (1 total)
  * [`pynchon.plugins.mermaid.Mermaid`](/src/pynchon/plugins/mermaid.py#L17-L93)
    * with bases ([Planner](#pynchonmodelsplanner),)
    * with properties: (10 total)
      *  [`Plan`](/src/pynchon/plugins/mermaid.py#L35) -> inspect._empty
      *  [`apply_hooks`](/src/pynchon/plugins/mermaid.py#L37) -> inspect._empty
      *  [`config`](/src/pynchon/plugins/mermaid.py#L118) -> inspect._empty
      *  [`exclude_patterns`](/src/pynchon/plugins/mermaid.py#L32) -> inspect._empty
      *  [`hooks`](/src/pynchon/plugins/mermaid.py#L37) -> inspect._empty
      *  [`logger`](/src/pynchon/plugins/mermaid.py#L37) -> inspect._empty
      *  [`output_root`](/src/pynchon/plugins/mermaid.py#L69) -> inspect._empty
      *  [`plugin_config`](/src/pynchon/plugins/mermaid.py#L113) -> inspect._empty
      *  [`project_root`](/src/pynchon/plugins/mermaid.py#L108) -> inspect._empty
      *  [`working_dir`](/src/pynchon/plugins/mermaid.py#L27) -> inspect._empty
-------------------------------------------------------------------------------
### pynchon.plugins.globals
* Overview:  [source code](/src/pynchon/plugins/globals.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (1 total)
  * [`pynchon.plugins.globals.Globals`](/src/pynchon/plugins/globals.py#L8-L18)
    * with bases ([Provider](#pynchonmodelspluginsprovider),)
    * with properties: (4 total)
      *  [`config`](/src/pynchon/plugins/globals.py#L118) -> inspect._empty
      *  [`logger`](/src/pynchon/plugins/globals.py#L37) -> inspect._empty
      *  [`plugin_config`](/src/pynchon/plugins/globals.py#L113) -> inspect._empty
      *  [`project_root`](/src/pynchon/plugins/globals.py#L108) -> inspect._empty
-------------------------------------------------------------------------------
### pynchon.plugins.griffe
* Overview:  [source code](/src/pynchon/plugins/griffe.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (1 total)
  * [`pynchon.plugins.griffe.Griffe`](/src/pynchon/plugins/griffe.py#L12-L52)
    * with bases ([ToolPlugin](#pynchonmodelspluginstool),)
    * with properties: (4 total)
      *  [`config`](/src/pynchon/plugins/griffe.py#L118) -> inspect._empty
      *  [`logger`](/src/pynchon/plugins/griffe.py#L37) -> inspect._empty
      *  [`plugin_config`](/src/pynchon/plugins/griffe.py#L113) -> inspect._empty
      *  [`project_root`](/src/pynchon/plugins/griffe.py#L108) -> inspect._empty
-------------------------------------------------------------------------------
### pynchon.plugins.rtd
* Overview:  [source code](/src/pynchon/plugins/rtd.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
-------------------------------------------------------------------------------
### pynchon.plugins.pattern
* Overview:  [source code](/src/pynchon/plugins/pattern.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (4 total)
  * [`pynchon.plugins.pattern.RenderResult`](/src/pynchon/plugins/pattern.py#L23-L35)
    * with bases ([Config](#pynchonabcs),)
    * with properties: (1 total)
      *  [`diff`](/src/pynchon/plugins/pattern.py#L30) -> inspect._empty
  * [`pynchon.plugins.pattern.ScaffoldAdvice`](/src/pynchon/plugins/pattern.py#L38-L60)
    * with bases ([Config](#pynchonabcs),)
    * with properties: (1 total)
      *  [`inherits`](/src/pynchon/plugins/pattern.py#L43) -> inspect._empty
  * [`pynchon.plugins.pattern.Scaffold`](/src/pynchon/plugins/pattern.py#L63-L212)
    * with bases ([Config](#pynchonabcs),)
    * with properties: (4 total)
      *  [`advice`](/src/pynchon/plugins/pattern.py#L186) -> inspect._empty
      *  [`dirs`](/src/pynchon/plugins/pattern.py#L202) -> typing.List
      *  [`files`](/src/pynchon/plugins/pattern.py#L194) -> typing.List[str]
      *  [`has_advice`](/src/pynchon/plugins/pattern.py#L182) -> bool
  * [`pynchon.plugins.pattern.Pattern`](/src/pynchon/plugins/pattern.py#L215-L438)
    * with bases ([ResourceManager](#pynchonmodelsplanner),)
    * with properties: (13 total)
      *  [`Plan`](/src/pynchon/plugins/pattern.py#L35) -> inspect._empty
      *  [`apply_hooks`](/src/pynchon/plugins/pattern.py#L37) -> inspect._empty
      *  [`changes`](/src/pynchon/plugins/pattern.py#L191) -> inspect._empty
      *  [`config`](/src/pynchon/plugins/pattern.py#L118) -> inspect._empty
      *  [`exclude_patterns`](/src/pynchon/plugins/pattern.py#L32) -> inspect._empty
      *  [`hooks`](/src/pynchon/plugins/pattern.py#L37) -> inspect._empty
      *  [`logger`](/src/pynchon/plugins/pattern.py#L37) -> inspect._empty
      *  [`pattern_folder`](/src/pynchon/plugins/pattern.py#L243) -> inspect._empty
      *  [`pattern_names`](/src/pynchon/plugins/pattern.py#L247) -> inspect._empty
      *  [`patterns`](/src/pynchon/plugins/pattern.py#L234) -> typing.Dict
      *  [`plugin_config`](/src/pynchon/plugins/pattern.py#L113) -> inspect._empty
      *  [`project_root`](/src/pynchon/plugins/pattern.py#L108) -> inspect._empty
      *  [`working_dir`](/src/pynchon/plugins/pattern.py#L27) -> inspect._empty
-------------------------------------------------------------------------------
### pynchon.plugins.core
* Overview:  [source code](/src/pynchon/plugins/core.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (1 total)
  * [`pynchon.plugins.core.Core`](/src/pynchon/plugins/core.py#L18-L180)
    * with bases ([Planner](#pynchonmodelsplanner),)
    * with properties: (9 total)
      *  [`Plan`](/src/pynchon/plugins/core.py#L35) -> inspect._empty
      *  [`apply_hooks`](/src/pynchon/plugins/core.py#L37) -> inspect._empty
      *  [`config`](/src/pynchon/plugins/core.py#L118) -> inspect._empty
      *  [`exclude_patterns`](/src/pynchon/plugins/core.py#L32) -> inspect._empty
      *  [`hooks`](/src/pynchon/plugins/core.py#L37) -> inspect._empty
      *  [`logger`](/src/pynchon/plugins/core.py#L37) -> inspect._empty
      *  [`plugin_config`](/src/pynchon/plugins/core.py#L113) -> inspect._empty
      *  [`project_root`](/src/pynchon/plugins/core.py#L108) -> inspect._empty
      *  [`working_dir`](/src/pynchon/plugins/core.py#L27) -> inspect._empty
-------------------------------------------------------------------------------
### pynchon.plugins.jinja
* Overview:  [source code](/src/pynchon/plugins/jinja.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (1 total)
  * [`pynchon.plugins.jinja.Jinja`](/src/pynchon/plugins/jinja.py#L13-L157)
    * with bases ([Planner](#pynchonmodelsplanner),)
    * with properties: (9 total)
      *  [`Plan`](/src/pynchon/plugins/jinja.py#L35) -> inspect._empty
      *  [`apply_hooks`](/src/pynchon/plugins/jinja.py#L37) -> inspect._empty
      *  [`config`](/src/pynchon/plugins/jinja.py#L118) -> inspect._empty
      *  [`exclude_patterns`](/src/pynchon/plugins/jinja.py#L32) -> inspect._empty
      *  [`hooks`](/src/pynchon/plugins/jinja.py#L37) -> inspect._empty
      *  [`logger`](/src/pynchon/plugins/jinja.py#L37) -> inspect._empty
      *  [`plugin_config`](/src/pynchon/plugins/jinja.py#L113) -> inspect._empty
      *  [`project_root`](/src/pynchon/plugins/jinja.py#L108) -> inspect._empty
      *  [`working_dir`](/src/pynchon/plugins/jinja.py#L27) -> inspect._empty
-------------------------------------------------------------------------------
### pynchon.plugins.api
* Overview:  [source code](/src/pynchon/plugins/api.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
-------------------------------------------------------------------------------
### pynchon.plugins.markdown
* Overview:  [source code](/src/pynchon/plugins/markdown.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (1 total)
  * [`pynchon.plugins.markdown.Markdown`](/src/pynchon/plugins/markdown.py#L20-L118)
    * with bases ([CliPlugin](#pynchonmodelspluginscli),)
    * with properties: (4 total)
      *  [`config`](/src/pynchon/plugins/markdown.py#L118) -> inspect._empty
      *  [`logger`](/src/pynchon/plugins/markdown.py#L37) -> inspect._empty
      *  [`plugin_config`](/src/pynchon/plugins/markdown.py#L113) -> inspect._empty
      *  [`project_root`](/src/pynchon/plugins/markdown.py#L108) -> inspect._empty
-------------------------------------------------------------------------------
### pynchon.plugins.src
* Overview:  [source code](/src/pynchon/plugins/src.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (1 total)
  * [`pynchon.plugins.src.SourceMan`](/src/pynchon/plugins/src.py#L38-L219)
    * with bases ([ResourceManager](#pynchonmodelsplanner),)
    * with properties: (10 total)
      *  [`Plan`](/src/pynchon/plugins/src.py#L35) -> inspect._empty
      *  [`apply_hooks`](/src/pynchon/plugins/src.py#L37) -> inspect._empty
      *  [`changes`](/src/pynchon/plugins/src.py#L191) -> inspect._empty
      *  [`config`](/src/pynchon/plugins/src.py#L118) -> inspect._empty
      *  [`exclude_patterns`](/src/pynchon/plugins/src.py#L32) -> inspect._empty
      *  [`hooks`](/src/pynchon/plugins/src.py#L37) -> inspect._empty
      *  [`logger`](/src/pynchon/plugins/src.py#L37) -> inspect._empty
      *  [`plugin_config`](/src/pynchon/plugins/src.py#L113) -> inspect._empty
      *  [`project_root`](/src/pynchon/plugins/src.py#L108) -> inspect._empty
      *  [`working_dir`](/src/pynchon/plugins/src.py#L27) -> inspect._empty
-------------------------------------------------------------------------------
### pynchon.plugins.makefile
* Overview:  [source code](/src/pynchon/plugins/makefile.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (1 total)
  * [`pynchon.plugins.makefile.Make`](/src/pynchon/plugins/makefile.py#L14-L125)
    * with bases ([Planner](#pynchonmodelsplanner),)
    * with properties: (11 total)
      *  [`Plan`](/src/pynchon/plugins/makefile.py#L35) -> inspect._empty
      *  [`apply_hooks`](/src/pynchon/plugins/makefile.py#L37) -> inspect._empty
      *  [`config`](/src/pynchon/plugins/makefile.py#L118) -> inspect._empty
      *  [`diagrams_root`](/src/pynchon/plugins/makefile.py#L36) -> inspect._empty
      *  [`exclude_patterns`](/src/pynchon/plugins/makefile.py#L32) -> inspect._empty
      *  [`hooks`](/src/pynchon/plugins/makefile.py#L37) -> inspect._empty
      *  [`logger`](/src/pynchon/plugins/makefile.py#L37) -> inspect._empty
      *  [`output_file`](/src/pynchon/plugins/makefile.py#L40) -> inspect._empty
      *  [`plugin_config`](/src/pynchon/plugins/makefile.py#L113) -> inspect._empty
      *  [`project_root`](/src/pynchon/plugins/makefile.py#L108) -> inspect._empty
      *  [`working_dir`](/src/pynchon/plugins/makefile.py#L27) -> inspect._empty
-------------------------------------------------------------------------------
### pynchon.plugins.fixme
* Overview:  [source code](/src/pynchon/plugins/fixme.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (2 total)
  * [`pynchon.plugins.fixme.FixMeConfig`](/src/pynchon/plugins/fixme.py#L16-L17)
    * with bases ([Config](#pynchonabcs),)
  * [`pynchon.plugins.fixme.FixMe`](/src/pynchon/plugins/fixme.py#L20-L113)
    * with bases ([Planner](#pynchonmodelsplanner),)
    * with properties: (9 total)
      *  [`Plan`](/src/pynchon/plugins/fixme.py#L35) -> inspect._empty
      *  [`apply_hooks`](/src/pynchon/plugins/fixme.py#L37) -> inspect._empty
      *  [`config`](/src/pynchon/plugins/fixme.py#L118) -> inspect._empty
      *  [`exclude_patterns`](/src/pynchon/plugins/fixme.py#L32) -> inspect._empty
      *  [`hooks`](/src/pynchon/plugins/fixme.py#L37) -> inspect._empty
      *  [`logger`](/src/pynchon/plugins/fixme.py#L37) -> inspect._empty
      *  [`plugin_config`](/src/pynchon/plugins/fixme.py#L113) -> inspect._empty
      *  [`project_root`](/src/pynchon/plugins/fixme.py#L108) -> inspect._empty
      *  [`working_dir`](/src/pynchon/plugins/fixme.py#L27) -> inspect._empty
-------------------------------------------------------------------------------
### pynchon.plugins.dot
* Overview:  [source code](/src/pynchon/plugins/dot.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (1 total)
  * [`pynchon.plugins.dot.Dot`](/src/pynchon/plugins/dot.py#L14-L74)
    * with bases ([Planner](#pynchonmodelsplanner),)
    * with properties: (9 total)
      *  [`Plan`](/src/pynchon/plugins/dot.py#L35) -> inspect._empty
      *  [`apply_hooks`](/src/pynchon/plugins/dot.py#L37) -> inspect._empty
      *  [`config`](/src/pynchon/plugins/dot.py#L118) -> inspect._empty
      *  [`exclude_patterns`](/src/pynchon/plugins/dot.py#L32) -> inspect._empty
      *  [`hooks`](/src/pynchon/plugins/dot.py#L37) -> inspect._empty
      *  [`logger`](/src/pynchon/plugins/dot.py#L37) -> inspect._empty
      *  [`plugin_config`](/src/pynchon/plugins/dot.py#L113) -> inspect._empty
      *  [`project_root`](/src/pynchon/plugins/dot.py#L108) -> inspect._empty
      *  [`working_dir`](/src/pynchon/plugins/dot.py#L27) -> inspect._empty
-------------------------------------------------------------------------------
### pynchon.plugins.github
* Overview:  [source code](/src/pynchon/plugins/github.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (1 total)
  * [`pynchon.plugins.github.GitHub`](/src/pynchon/plugins/github.py#L19-L133)
    * with bases ([ToolPlugin](#pynchonmodelspluginstool),)
    * with properties: (4 total)
      *  [`config`](/src/pynchon/plugins/github.py#L118) -> inspect._empty
      *  [`logger`](/src/pynchon/plugins/github.py#L37) -> inspect._empty
      *  [`plugin_config`](/src/pynchon/plugins/github.py#L113) -> inspect._empty
      *  [`project_root`](/src/pynchon/plugins/github.py#L108) -> inspect._empty
-------------------------------------------------------------------------------
### pynchon.plugins.parse
* Overview:  [source code](/src/pynchon/plugins/parse.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (1 total)
  * [`pynchon.plugins.parse.Parse`](/src/pynchon/plugins/parse.py#L13-L23)
    * with bases ([ToolPlugin](#pynchonmodelspluginstool),)
    * with properties: (4 total)
      *  [`config`](/src/pynchon/plugins/parse.py#L118) -> inspect._empty
      *  [`logger`](/src/pynchon/plugins/parse.py#L37) -> inspect._empty
      *  [`plugin_config`](/src/pynchon/plugins/parse.py#L113) -> inspect._empty
      *  [`project_root`](/src/pynchon/plugins/parse.py#L108) -> inspect._empty
-------------------------------------------------------------------------------
### pynchon.plugins.tests
* Overview:  [source code](/src/pynchon/plugins/tests.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (2 total)
  * [`pynchon.plugins.tests.TestConfig`](/src/pynchon/plugins/tests.py#L23-L27)
    * with bases ([Config](#pynchonabcs),)
  * [`pynchon.plugins.tests.Tests`](/src/pynchon/plugins/tests.py#L63-L140)
    * with bases ([Planner](#pynchonmodelsplanner),)
    * with admonitions:  [🐉 Complex](/src/pynchon/plugins/tests.py#L24 "score 11 / 7") 
    * with properties: (9 total)
      *  [`Plan`](/src/pynchon/plugins/tests.py#L35) -> inspect._empty
      *  [`apply_hooks`](/src/pynchon/plugins/tests.py#L37) -> inspect._empty
      *  [`config`](/src/pynchon/plugins/tests.py#L118) -> inspect._empty
      *  [`exclude_patterns`](/src/pynchon/plugins/tests.py#L32) -> inspect._empty
      *  [`hooks`](/src/pynchon/plugins/tests.py#L37) -> inspect._empty
      *  [`logger`](/src/pynchon/plugins/tests.py#L37) -> inspect._empty
      *  [`plugin_config`](/src/pynchon/plugins/tests.py#L113) -> inspect._empty
      *  [`project_root`](/src/pynchon/plugins/tests.py#L108) -> inspect._empty
      *  [`working_dir`](/src/pynchon/plugins/tests.py#L27) -> inspect._empty
-------------------------------------------------------------------------------
### pynchon.plugins.tox
* Overview:  [source code](/src/pynchon/plugins/tox.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (1 total)
  * [`pynchon.plugins.tox.PluginTemplate`](/src/pynchon/plugins/tox.py#L10-L18)
    * with bases ([Provider](#pynchonmodelspluginsprovider),)
    * with properties: (4 total)
      *  [`config`](/src/pynchon/plugins/tox.py#L118) -> inspect._empty
      *  [`logger`](/src/pynchon/plugins/tox.py#L37) -> inspect._empty
      *  [`plugin_config`](/src/pynchon/plugins/tox.py#L113) -> inspect._empty
      *  [`project_root`](/src/pynchon/plugins/tox.py#L108) -> inspect._empty
-------------------------------------------------------------------------------
### pynchon.plugins.json
* Overview:  [source code](/src/pynchon/plugins/json.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (1 total)
  * [`pynchon.plugins.json.Json`](/src/pynchon/plugins/json.py#L13-L66)
    * with bases ([ToolPlugin](#pynchonmodelspluginstool),)
    * with properties: (4 total)
      *  [`config`](/src/pynchon/plugins/json.py#L118) -> inspect._empty
      *  [`logger`](/src/pynchon/plugins/json.py#L37) -> inspect._empty
      *  [`plugin_config`](/src/pynchon/plugins/json.py#L113) -> inspect._empty
      *  [`project_root`](/src/pynchon/plugins/json.py#L108) -> inspect._empty
-------------------------------------------------------------------------------
### pynchon.plugins.project
* Overview:  [source code](/src/pynchon/plugins/project.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (2 total)
  * [`pynchon.plugins.project.ProjectConfig`](/src/pynchon/plugins/project.py#L12-L47)
    * with bases ([Config](#pynchonabcs),)
    * with properties: (3 total)
      *  [`name`](/src/pynchon/plugins/project.py#L19) -> typing.Optional[str]
      *  [`root`](/src/pynchon/plugins/project.py#L29) -> str
      *  [`subproject`](/src/pynchon/plugins/project.py#L35) -> typing.Dict
  * [`pynchon.plugins.project.Project`](/src/pynchon/plugins/project.py#L50-L55)
    * with bases ([Manager](#pynchonmodelsplanner),)
    * with properties: (9 total)
      *  [`Plan`](/src/pynchon/plugins/project.py#L35) -> inspect._empty
      *  [`apply_hooks`](/src/pynchon/plugins/project.py#L37) -> inspect._empty
      *  [`config`](/src/pynchon/plugins/project.py#L118) -> inspect._empty
      *  [`exclude_patterns`](/src/pynchon/plugins/project.py#L32) -> inspect._empty
      *  [`hooks`](/src/pynchon/plugins/project.py#L37) -> inspect._empty
      *  [`logger`](/src/pynchon/plugins/project.py#L37) -> inspect._empty
      *  [`plugin_config`](/src/pynchon/plugins/project.py#L113) -> inspect._empty
      *  [`project_root`](/src/pynchon/plugins/project.py#L108) -> inspect._empty
      *  [`working_dir`](/src/pynchon/plugins/project.py#L27) -> inspect._empty
-------------------------------------------------------------------------------
### pynchon.plugins.mkdocs
* Overview:  [source code](/src/pynchon/plugins/mkdocs.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (2 total)
  * [`pynchon.plugins.mkdocs.MkdocsPluginConfig`](/src/pynchon/plugins/mkdocs.py#L15-L54)
    * with bases ([Config](#pynchonabcs),)
    * with properties: (3 total)
      *  [`config`](/src/pynchon/plugins/mkdocs.py#L23) -> typing.Dict
      *  [`config_file`](/src/pynchon/plugins/mkdocs.py#L34) -> typing.Optional[str]
      *  [`site_dir`](/src/pynchon/plugins/mkdocs.py#L19) -> inspect._empty
  * [`pynchon.plugins.mkdocs.Mkdocs`](/src/pynchon/plugins/mkdocs.py#L57-L103)
    * with bases ([Planner](#pynchonmodelsplanner),)
    * with properties: (10 total)
      *  [`Plan`](/src/pynchon/plugins/mkdocs.py#L35) -> inspect._empty
      *  [`apply_hooks`](/src/pynchon/plugins/mkdocs.py#L37) -> inspect._empty
      *  [`config`](/src/pynchon/plugins/mkdocs.py#L118) -> inspect._empty
      *  [`exclude_patterns`](/src/pynchon/plugins/mkdocs.py#L32) -> inspect._empty
      *  [`hooks`](/src/pynchon/plugins/mkdocs.py#L37) -> inspect._empty
      *  [`logger`](/src/pynchon/plugins/mkdocs.py#L37) -> inspect._empty
      *  [`plugin_config`](/src/pynchon/plugins/mkdocs.py#L113) -> inspect._empty
      *  [`project_root`](/src/pynchon/plugins/mkdocs.py#L108) -> inspect._empty
      *  [`site_dir`](/src/pynchon/plugins/mkdocs.py#L76) -> str
      *  [`working_dir`](/src/pynchon/plugins/mkdocs.py#L27) -> inspect._empty
-------------------------------------------------------------------------------
### pynchon.plugins.python
* Overview:  [source code](/src/pynchon/plugins/python/__init__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (0 total)
-------------------------------------------------------------------------------
### pynchon.plugins.python.libcst
* Overview:  [source code](/src/pynchon/plugins/python/libcst.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (1 total)
  * [`pynchon.plugins.python.libcst.LibCST`](/src/pynchon/plugins/python/libcst.py#L15-L114)
    * with bases ([Planner](#pynchonmodelsplanner),)
    * with properties: (9 total)
      *  [`Plan`](/src/pynchon/plugins/python/libcst.py#L35) -> inspect._empty
      *  [`apply_hooks`](/src/pynchon/plugins/python/libcst.py#L37) -> inspect._empty
      *  [`config`](/src/pynchon/plugins/python/libcst.py#L118) -> inspect._empty
      *  [`exclude_patterns`](/src/pynchon/plugins/python/libcst.py#L32) -> inspect._empty
      *  [`hooks`](/src/pynchon/plugins/python/libcst.py#L37) -> inspect._empty
      *  [`logger`](/src/pynchon/plugins/python/libcst.py#L37) -> inspect._empty
      *  [`plugin_config`](/src/pynchon/plugins/python/libcst.py#L113) -> inspect._empty
      *  [`project_root`](/src/pynchon/plugins/python/libcst.py#L108) -> inspect._empty
      *  [`working_dir`](/src/pynchon/plugins/python/libcst.py#L27) -> inspect._empty
-------------------------------------------------------------------------------
### pynchon.plugins.python.config
* Overview:  [source code](/src/pynchon/plugins/python/config.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
-------------------------------------------------------------------------------
### pynchon.plugins.python.models
* Overview:  [source code](/src/pynchon/plugins/python/models.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
-------------------------------------------------------------------------------
### pynchon.plugins.python.cst
* Overview:  [source code](/src/pynchon/plugins/python/cst.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
-------------------------------------------------------------------------------
### pynchon.plugins.python.platform
* Overview:  [source code](/src/pynchon/plugins/python/platform.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (2 total)
  * [`pynchon.plugins.python.platform.PythonPlatform`](/src/pynchon/plugins/python/platform.py#L15-L84)
    * with bases ([Planner](#pynchonmodelsplanner),)
    * with properties: (9 total)
      *  [`Plan`](/src/pynchon/plugins/python/platform.py#L35) -> inspect._empty
      *  [`apply_hooks`](/src/pynchon/plugins/python/platform.py#L37) -> inspect._empty
      *  [`config`](/src/pynchon/plugins/python/platform.py#L118) -> inspect._empty
      *  [`exclude_patterns`](/src/pynchon/plugins/python/platform.py#L32) -> inspect._empty
      *  [`hooks`](/src/pynchon/plugins/python/platform.py#L37) -> inspect._empty
      *  [`logger`](/src/pynchon/plugins/python/platform.py#L37) -> inspect._empty
      *  [`plugin_config`](/src/pynchon/plugins/python/platform.py#L113) -> inspect._empty
      *  [`project_root`](/src/pynchon/plugins/python/platform.py#L108) -> inspect._empty
      *  [`working_dir`](/src/pynchon/plugins/python/platform.py#L27) -> inspect._empty
  * [`pynchon.plugins.python.platform.PackageConfig`](/src/pynchon/plugins/python/platform.py#L87-L114)
    * with bases ([Config](#pynchonabcs),)
    * with properties: (3 total)
      *  [`console_scripts`](/src/pynchon/plugins/python/platform.py#L101) -> str
      *  [`name`](/src/pynchon/plugins/python/platform.py#L93) -> str
      *  [`version`](/src/pynchon/plugins/python/platform.py#L108) -> str
-------------------------------------------------------------------------------
### pynchon.plugins.python.api
* Overview:  [source code](/src/pynchon/plugins/python/api.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (1 total)
  * [`pynchon.plugins.python.api.PythonAPI`](/src/pynchon/plugins/python/api.py#L13-L107)
    * with bases ([Planner](#pynchonmodelsplanner),)
    * with properties: (9 total)
      *  [`Plan`](/src/pynchon/plugins/python/api.py#L35) -> inspect._empty
      *  [`apply_hooks`](/src/pynchon/plugins/python/api.py#L37) -> inspect._empty
      *  [`config`](/src/pynchon/plugins/python/api.py#L118) -> inspect._empty
      *  [`exclude_patterns`](/src/pynchon/plugins/python/api.py#L32) -> inspect._empty
      *  [`hooks`](/src/pynchon/plugins/python/api.py#L37) -> inspect._empty
      *  [`logger`](/src/pynchon/plugins/python/api.py#L37) -> inspect._empty
      *  [`plugin_config`](/src/pynchon/plugins/python/api.py#L113) -> inspect._empty
      *  [`project_root`](/src/pynchon/plugins/python/api.py#L108) -> inspect._empty
      *  [`working_dir`](/src/pynchon/plugins/python/api.py#L27) -> inspect._empty
-------------------------------------------------------------------------------
### pynchon.plugins.python.cli
* Overview:  [source code](/src/pynchon/plugins/python/cli.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (2 total)
  * [`pynchon.plugins.python.cli.PythonCliConfig`](/src/pynchon/plugins/python/cli.py#L37-L106)
    * with bases ([Config](#pynchonabcs),)
    * with properties: (3 total)
      *  [`module_entrypoints`](/src/pynchon/plugins/python/cli.py#L69) -> typing.List[typing.Dict]
      *  [`root`](/src/pynchon/plugins/python/cli.py#L48) -> inspect._empty
      *  [`src_root`](/src/pynchon/plugins/python/cli.py#L58) -> pynchon.abcs.path.Path
  * [`pynchon.plugins.python.cli.PythonCLI`](/src/pynchon/plugins/python/cli.py#L109-L453)
    * with bases ([Planner](#pynchonmodelsplanner),)
    * with properties: (14 total)
      *  [`Plan`](/src/pynchon/plugins/python/cli.py#L35) -> inspect._empty
      *  [`apply_hooks`](/src/pynchon/plugins/python/cli.py#L37) -> inspect._empty
      *  [`config`](/src/pynchon/plugins/python/cli.py#L118) -> inspect._empty
      *  [`console_script_entrypoints`](/src/pynchon/plugins/python/cli.py#L37) -> typing.List[pynchon.models.python.EntrypointMetadata]
      *  [`docs_root`](/src/pynchon/plugins/python/cli.py#L332) -> inspect._empty
      *  [`exclude_patterns`](/src/pynchon/plugins/python/cli.py#L32) -> inspect._empty
      *  [`hooks`](/src/pynchon/plugins/python/cli.py#L37) -> inspect._empty
      *  [`logger`](/src/pynchon/plugins/python/cli.py#L37) -> inspect._empty
      *  [`plugin_config`](/src/pynchon/plugins/python/cli.py#L113) -> inspect._empty
      *  [`plugin_invocation`](/src/pynchon/plugins/python/cli.py#L401) -> inspect._empty
      *  [`project_root`](/src/pynchon/plugins/python/cli.py#L108) -> inspect._empty
      *  [`root`](/src/pynchon/plugins/python/cli.py#L340) -> inspect._empty
      *  [`src_root`](/src/pynchon/plugins/python/cli.py#L37) -> inspect._empty
      *  [`working_dir`](/src/pynchon/plugins/python/cli.py#L27) -> inspect._empty
* Functions: (1 total)
  * [`pynchon.plugins.python.cli._check_click`](/src/pynchon/plugins/python/cli.py#L24-L34) with signature ``
-------------------------------------------------------------------------------
### pynchon.plugins.python.pypi
* Overview:  [source code](/src/pynchon/plugins/python/pypi.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (2 total)
  * [`pynchon.plugins.python.pypi.PyPiConfig`](/src/pynchon/plugins/python/pypi.py#L10-L22)
    * with bases ([Config](#pynchonabcs),)
    * with properties: (1 total)
      *  [`project_url`](/src/pynchon/plugins/python/pypi.py#L17) -> inspect._empty
  * [`pynchon.plugins.python.pypi.PyPI`](/src/pynchon/plugins/python/pypi.py#L25-L29)
    * with bases ([Provider](#pynchonmodelspluginsprovider),)
    * with properties: (4 total)
      *  [`config`](/src/pynchon/plugins/python/pypi.py#L118) -> inspect._empty
      *  [`logger`](/src/pynchon/plugins/python/pypi.py#L37) -> inspect._empty
      *  [`plugin_config`](/src/pynchon/plugins/python/pypi.py#L113) -> inspect._empty
      *  [`project_root`](/src/pynchon/plugins/python/pypi.py#L108) -> inspect._empty
-------------------------------------------------------------------------------
### pynchon.plugins.scaffolding
* Overview:  [source code](/src/pynchon/plugins/scaffolding/__init__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (1 total)
  * [`pynchon.plugins.scaffolding.Scaffolding`](/src/pynchon/plugins/scaffolding/__init__.py#L16-L121)
    * with bases ([ShyPlanner](#pynchonmodelsplanner),)
    * with properties: (11 total)
      *  [`Plan`](/src/pynchon/plugins/scaffolding/__init__.py#L35) -> inspect._empty
      *  [`apply_hooks`](/src/pynchon/plugins/scaffolding/__init__.py#L37) -> inspect._empty
      *  [`config`](/src/pynchon/plugins/scaffolding/__init__.py#L118) -> inspect._empty
      *  [`exclude_patterns`](/src/pynchon/plugins/scaffolding/__init__.py#L32) -> inspect._empty
      *  [`hooks`](/src/pynchon/plugins/scaffolding/__init__.py#L37) -> inspect._empty
      *  [`logger`](/src/pynchon/plugins/scaffolding/__init__.py#L37) -> inspect._empty
      *  [`matches`](/src/pynchon/plugins/scaffolding/__init__.py#L44) -> inspect._empty
      *  [`plugin_config`](/src/pynchon/plugins/scaffolding/__init__.py#L113) -> inspect._empty
      *  [`project_root`](/src/pynchon/plugins/scaffolding/__init__.py#L108) -> inspect._empty
      *  [`scaffolds`](/src/pynchon/plugins/scaffolding/__init__.py#L59) -> inspect._empty
      *  [`working_dir`](/src/pynchon/plugins/scaffolding/__init__.py#L27) -> inspect._empty
* Classes: (1 total)
  * [`pynchon.plugins.scaffolding.Scaffolding`](/src/pynchon/plugins/scaffolding/__init__.py#L16-L121)
    * with bases ([ShyPlanner](#pynchonmodelsplanner),)
    * with properties: (11 total)
      *  [`Plan`](/src/pynchon/plugins/scaffolding/__init__.py#L35) -> inspect._empty
      *  [`apply_hooks`](/src/pynchon/plugins/scaffolding/__init__.py#L37) -> inspect._empty
      *  [`config`](/src/pynchon/plugins/scaffolding/__init__.py#L118) -> inspect._empty
      *  [`exclude_patterns`](/src/pynchon/plugins/scaffolding/__init__.py#L32) -> inspect._empty
      *  [`hooks`](/src/pynchon/plugins/scaffolding/__init__.py#L37) -> inspect._empty
      *  [`logger`](/src/pynchon/plugins/scaffolding/__init__.py#L37) -> inspect._empty
      *  [`matches`](/src/pynchon/plugins/scaffolding/__init__.py#L44) -> inspect._empty
      *  [`plugin_config`](/src/pynchon/plugins/scaffolding/__init__.py#L113) -> inspect._empty
      *  [`project_root`](/src/pynchon/plugins/scaffolding/__init__.py#L108) -> inspect._empty
      *  [`scaffolds`](/src/pynchon/plugins/scaffolding/__init__.py#L59) -> inspect._empty
      *  [`working_dir`](/src/pynchon/plugins/scaffolding/__init__.py#L27) -> inspect._empty
-------------------------------------------------------------------------------
### pynchon.plugins.scaffolding.config
* Overview:  [source code](/src/pynchon/plugins/scaffolding/config.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (2 total)
  * [`pynchon.plugins.scaffolding.config.ScaffoldingItem`](/src/pynchon/plugins/scaffolding/config.py#L12-L36)
    * with bases ([AttrDict](#pynchonabcsattrdict),)
    * with properties: (1 total)
      *  [`exists`](/src/pynchon/plugins/scaffolding/config.py#L29) -> bool
  * [`pynchon.plugins.scaffolding.config.ScaffoldingConfig`](/src/pynchon/plugins/scaffolding/config.py#L39-L42)
    * with bases ([Config](#pynchonabcs),)
-------------------------------------------------------------------------------
### pynchon.plugins.doctor
* Overview:  [source code](/src/pynchon/plugins/doctor/__init__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
-------------------------------------------------------------------------------
### pynchon.plugins.docs
* Overview:  [source code](/src/pynchon/plugins/docs/__init__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (0 total)
-------------------------------------------------------------------------------
### pynchon.plugins.docs.opener
* Overview:  [source code](/src/pynchon/plugins/docs/opener.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (1 total)
  * [`pynchon.plugins.docs.opener.OpenerMixin`](/src/pynchon/plugins/docs/opener.py#L12-L68)
    * with bases ([`__builtin__.object`](https://docs.python.org/3/library/functions.html#object),)
-------------------------------------------------------------------------------
### pynchon.plugins.docs.main
* Overview:  [source code](/src/pynchon/plugins/docs/main.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (1 total)
  * [`pynchon.plugins.docs.main.DocsMan`](/src/pynchon/plugins/docs/main.py#L19-L158)
    * with bases ([ResourceManager](#pynchonmodelsplanner),[OpenerMixin](#pynchonpluginsdocsopener),)
    * with properties: (14 total)
      *  [`Plan`](/src/pynchon/plugins/docs/main.py#L35) -> inspect._empty
      *  [`apply_hooks`](/src/pynchon/plugins/docs/main.py#L37) -> inspect._empty
      *  [`changes`](/src/pynchon/plugins/docs/main.py#L191) -> inspect._empty
      *  [`config`](/src/pynchon/plugins/docs/main.py#L118) -> inspect._empty
      *  [`exclude_patterns`](/src/pynchon/plugins/docs/main.py#L32) -> inspect._empty
      *  [`git_root`](/src/pynchon/plugins/docs/main.py#L54) -> inspect._empty
      *  [`hooks`](/src/pynchon/plugins/docs/main.py#L37) -> inspect._empty
      *  [`logger`](/src/pynchon/plugins/docs/main.py#L37) -> inspect._empty
      *  [`plugin_config`](/src/pynchon/plugins/docs/main.py#L113) -> inspect._empty
      *  [`project_root`](/src/pynchon/plugins/docs/main.py#L108) -> inspect._empty
      *  [`server`](/src/pynchon/plugins/docs/main.py#L37) -> inspect._empty
      *  [`server_pid`](/src/pynchon/plugins/docs/main.py#L45) -> inspect._empty
      *  [`server_url`](/src/pynchon/plugins/docs/main.py#L50) -> inspect._empty
      *  [`working_dir`](/src/pynchon/plugins/docs/main.py#L27) -> inspect._empty
-------------------------------------------------------------------------------
### pynchon.models
* Overview:  [source code](/src/pynchon/models/__init__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (0 total)
-------------------------------------------------------------------------------
### pynchon.models.planner
* Overview:  [source code](/src/pynchon/models/planner.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (5 total)
  * [`pynchon.models.planner.AbstractPlanner`](/src/pynchon/models/planner.py#L22-L171)
    * with bases ([BasePlugin](#pynchonmodelsplugins),)
    * with properties: (9 total)
      *  [`Plan`](/src/pynchon/models/planner.py#L35) -> inspect._empty
      *  [`apply_hooks`](/src/pynchon/models/planner.py#L37) -> inspect._empty
      *  [`config`](/src/pynchon/models/planner.py#L118) -> inspect._empty
      *  [`exclude_patterns`](/src/pynchon/models/planner.py#L32) -> inspect._empty
      *  [`hooks`](/src/pynchon/models/planner.py#L37) -> inspect._empty
      *  [`logger`](/src/pynchon/models/planner.py#L37) -> inspect._empty
      *  [`plugin_config`](/src/pynchon/models/planner.py#L113) -> inspect._empty
      *  [`project_root`](/src/pynchon/models/planner.py#L108) -> inspect._empty
      *  [`working_dir`](/src/pynchon/models/planner.py#L27) -> inspect._empty
  * [`pynchon.models.planner.ShyPlanner`](/src/pynchon/models/planner.py#L174-L182)
    * with bases ([AbstractPlanner](#pynchonmodelsplanner),)
    * with properties: (9 total)
      *  [`Plan`](/src/pynchon/models/planner.py#L35) -> inspect._empty
      *  [`apply_hooks`](/src/pynchon/models/planner.py#L37) -> inspect._empty
      *  [`config`](/src/pynchon/models/planner.py#L118) -> inspect._empty
      *  [`exclude_patterns`](/src/pynchon/models/planner.py#L32) -> inspect._empty
      *  [`hooks`](/src/pynchon/models/planner.py#L37) -> inspect._empty
      *  [`logger`](/src/pynchon/models/planner.py#L37) -> inspect._empty
      *  [`plugin_config`](/src/pynchon/models/planner.py#L113) -> inspect._empty
      *  [`project_root`](/src/pynchon/models/planner.py#L108) -> inspect._empty
      *  [`working_dir`](/src/pynchon/models/planner.py#L27) -> inspect._empty
  * [`pynchon.models.planner.Manager`](/src/pynchon/models/planner.py#L185-L187)
    * with bases ([ShyPlanner](#pynchonmodelsplanner),)
    * with properties: (9 total)
      *  [`Plan`](/src/pynchon/models/planner.py#L35) -> inspect._empty
      *  [`apply_hooks`](/src/pynchon/models/planner.py#L37) -> inspect._empty
      *  [`config`](/src/pynchon/models/planner.py#L118) -> inspect._empty
      *  [`exclude_patterns`](/src/pynchon/models/planner.py#L32) -> inspect._empty
      *  [`hooks`](/src/pynchon/models/planner.py#L37) -> inspect._empty
      *  [`logger`](/src/pynchon/models/planner.py#L37) -> inspect._empty
      *  [`plugin_config`](/src/pynchon/models/planner.py#L113) -> inspect._empty
      *  [`project_root`](/src/pynchon/models/planner.py#L108) -> inspect._empty
      *  [`working_dir`](/src/pynchon/models/planner.py#L27) -> inspect._empty
  * [`pynchon.models.planner.ResourceManager`](/src/pynchon/models/planner.py#L190-L231)
    * with bases ([Manager](#pynchonmodelsplanner),)
    * with properties: (10 total)
      *  [`Plan`](/src/pynchon/models/planner.py#L35) -> inspect._empty
      *  [`apply_hooks`](/src/pynchon/models/planner.py#L37) -> inspect._empty
      *  [`changes`](/src/pynchon/models/planner.py#L191) -> inspect._empty
      *  [`config`](/src/pynchon/models/planner.py#L118) -> inspect._empty
      *  [`exclude_patterns`](/src/pynchon/models/planner.py#L32) -> inspect._empty
      *  [`hooks`](/src/pynchon/models/planner.py#L37) -> inspect._empty
      *  [`logger`](/src/pynchon/models/planner.py#L37) -> inspect._empty
      *  [`plugin_config`](/src/pynchon/models/planner.py#L113) -> inspect._empty
      *  [`project_root`](/src/pynchon/models/planner.py#L108) -> inspect._empty
      *  [`working_dir`](/src/pynchon/models/planner.py#L27) -> inspect._empty
  * [`pynchon.models.planner.Planner`](/src/pynchon/models/planner.py#L234-L239)
    * with bases ([ShyPlanner](#pynchonmodelsplanner),)
    * with properties: (9 total)
      *  [`Plan`](/src/pynchon/models/planner.py#L35) -> inspect._empty
      *  [`apply_hooks`](/src/pynchon/models/planner.py#L37) -> inspect._empty
      *  [`config`](/src/pynchon/models/planner.py#L118) -> inspect._empty
      *  [`exclude_patterns`](/src/pynchon/models/planner.py#L32) -> inspect._empty
      *  [`hooks`](/src/pynchon/models/planner.py#L37) -> inspect._empty
      *  [`logger`](/src/pynchon/models/planner.py#L37) -> inspect._empty
      *  [`plugin_config`](/src/pynchon/models/planner.py#L113) -> inspect._empty
      *  [`project_root`](/src/pynchon/models/planner.py#L108) -> inspect._empty
      *  [`working_dir`](/src/pynchon/models/planner.py#L27) -> inspect._empty
-------------------------------------------------------------------------------
### pynchon.models.python
* Overview:  [source code](/src/pynchon/models/python.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (1 total)
  * [`pynchon.models.python.EntrypointMetadata`](/src/pynchon/models/python.py#L12-L86)
    * with bases ([BaseModel](#fleksmodels),)
    * with properties: (4 total)
      *  [`help_invocation`](/src/pynchon/models/python.py#L44) -> inspect._empty
      *  [`help_output`](/src/pynchon/models/python.py#L54) -> inspect._empty
      *  [`module`](/src/pynchon/models/python.py#L80) -> inspect._empty
      *  [`src_url`](/src/pynchon/models/python.py#L39) -> str
-------------------------------------------------------------------------------
### pynchon.models.planning
* Overview:  [source code](/src/pynchon/models/planning.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (5 total)
  * [`pynchon.models.planning.BaseModel`](/src/pynchon/models/planning.py#L20-L33)
    * with bases ([BaseModel](#fleksmodels),)
    * with properties: (1 total)
      *  [`rel_resource`](/src/pynchon/models/planning.py#L29) -> str
  * [`pynchon.models.planning.Goal`](/src/pynchon/models/planning.py#L36-L81)
    * with bases ([BaseModel](#pynchonmodelsplanning),)
    * with properties: (1 total)
      *  [`rel_resource`](/src/pynchon/models/planning.py#L29) -> str
  * [`pynchon.models.planning.Action`](/src/pynchon/models/planning.py#L84-L174)
    * with bases ([BaseModel](#pynchonmodelsplanning),)
    * with properties: (2 total)
      *  [`rel_resource`](/src/pynchon/models/planning.py#L29) -> str
      *  [`status_string`](/src/pynchon/models/planning.py#L163) -> inspect._empty
  * [`pynchon.models.planning.Plan`](/src/pynchon/models/planning.py#L177-L269)
    * with bases ([BaseModel](#pydanticmain),)
  * [`pynchon.models.planning.ApplyResults`](/src/pynchon/models/planning.py#L275-L303)
    * with bases ([`__builtin__.list`](https://docs.python.org/3/library/functions.html#list),[Generic](#typing),)
    * with properties: (2 total)
      *  [`action_types`](/src/pynchon/models/planning.py#L282) -> inspect._empty
      *  [`ok`](/src/pynchon/models/planning.py#L278) -> inspect._empty
-------------------------------------------------------------------------------
### pynchon.models.plugins
* Overview:  [source code](/src/pynchon/models/plugins/__init__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (2 total)
  * [`pynchon.models.plugins.BasePlugin`](/src/pynchon/models/plugins/__init__.py#L22-L42)
    * with bases ([CliPlugin](#pynchonmodelspluginscli),)
    * with properties: (6 total)
      *  [`config`](/src/pynchon/models/plugins/__init__.py#L118) -> inspect._empty
      *  [`exclude_patterns`](/src/pynchon/models/plugins/__init__.py#L32) -> inspect._empty
      *  [`logger`](/src/pynchon/models/plugins/__init__.py#L37) -> inspect._empty
      *  [`plugin_config`](/src/pynchon/models/plugins/__init__.py#L113) -> inspect._empty
      *  [`project_root`](/src/pynchon/models/plugins/__init__.py#L108) -> inspect._empty
      *  [`working_dir`](/src/pynchon/models/plugins/__init__.py#L27) -> inspect._empty
  * [`pynchon.models.plugins.NameSpace`](/src/pynchon/models/plugins/__init__.py#L45-L55)
    * with bases ([CliPlugin](#pynchonmodelspluginscli),)
    * with properties: (4 total)
      *  [`config`](/src/pynchon/models/plugins/__init__.py#L118) -> inspect._empty
      *  [`logger`](/src/pynchon/models/plugins/__init__.py#L37) -> inspect._empty
      *  [`plugin_config`](/src/pynchon/models/plugins/__init__.py#L113) -> inspect._empty
      *  [`project_root`](/src/pynchon/models/plugins/__init__.py#L108) -> inspect._empty
* Classes: (2 total)
  * [`pynchon.models.plugins.BasePlugin`](/src/pynchon/models/plugins/__init__.py#L22-L42)
    * with bases ([CliPlugin](#pynchonmodelspluginscli),)
    * with properties: (6 total)
      *  [`config`](/src/pynchon/models/plugins/__init__.py#L118) -> inspect._empty
      *  [`exclude_patterns`](/src/pynchon/models/plugins/__init__.py#L32) -> inspect._empty
      *  [`logger`](/src/pynchon/models/plugins/__init__.py#L37) -> inspect._empty
      *  [`plugin_config`](/src/pynchon/models/plugins/__init__.py#L113) -> inspect._empty
      *  [`project_root`](/src/pynchon/models/plugins/__init__.py#L108) -> inspect._empty
      *  [`working_dir`](/src/pynchon/models/plugins/__init__.py#L27) -> inspect._empty
  * [`pynchon.models.plugins.NameSpace`](/src/pynchon/models/plugins/__init__.py#L45-L55)
    * with bases ([CliPlugin](#pynchonmodelspluginscli),)
    * with properties: (4 total)
      *  [`config`](/src/pynchon/models/plugins/__init__.py#L118) -> inspect._empty
      *  [`logger`](/src/pynchon/models/plugins/__init__.py#L37) -> inspect._empty
      *  [`plugin_config`](/src/pynchon/models/plugins/__init__.py#L113) -> inspect._empty
      *  [`project_root`](/src/pynchon/models/plugins/__init__.py#L108) -> inspect._empty
-------------------------------------------------------------------------------
### pynchon.models.plugins.cli
* Overview:  [source code](/src/pynchon/models/plugins/cli.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (1 total)
  * [`pynchon.models.plugins.cli.CliPlugin`](/src/pynchon/models/plugins/cli.py#L20-L324)
    * with bases ([PynchonPlugin](#pynchonmodelspluginspynchon),)
    * with admonitions:  [🐉 Complex](/src/pynchon/models/plugins/cli.py#L196 "score 11 / 7") 
    * with properties: (4 total)
      *  [`config`](/src/pynchon/models/plugins/cli.py#L118) -> inspect._empty
      *  [`logger`](/src/pynchon/models/plugins/cli.py#L37) -> inspect._empty
      *  [`plugin_config`](/src/pynchon/models/plugins/cli.py#L113) -> inspect._empty
      *  [`project_root`](/src/pynchon/models/plugins/cli.py#L108) -> inspect._empty
-------------------------------------------------------------------------------
### pynchon.models.plugins.provider
* Overview:  [source code](/src/pynchon/models/plugins/provider.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (1 total)
  * [`pynchon.models.plugins.provider.Provider`](/src/pynchon/models/plugins/provider.py#L15-L29)
    * with bases ([CliPlugin](#pynchonmodelspluginscli),)
    * with properties: (4 total)
      *  [`config`](/src/pynchon/models/plugins/provider.py#L118) -> inspect._empty
      *  [`logger`](/src/pynchon/models/plugins/provider.py#L37) -> inspect._empty
      *  [`plugin_config`](/src/pynchon/models/plugins/provider.py#L113) -> inspect._empty
      *  [`project_root`](/src/pynchon/models/plugins/provider.py#L108) -> inspect._empty
-------------------------------------------------------------------------------
### pynchon.models.plugins.validators
* Overview:  [source code](/src/pynchon/models/plugins/validators.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Functions: (2 total)
  * [`pynchon.models.plugins.validators.require_conf_key`](/src/pynchon/models/plugins/validators.py#L14-L29) with signature `(kls, self=None, vdata=None, strict: bool = True)`
  * [`pynchon.models.plugins.validators.warn_config_kls`](/src/pynchon/models/plugins/validators.py#L32-L43) with signature `(kls, self=None, vdata=None)`
-------------------------------------------------------------------------------
### pynchon.models.plugins.pynchon
* Overview:  [source code](/src/pynchon/models/plugins/pynchon.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (1 total)
  * [`pynchon.models.plugins.pynchon.PynchonPlugin`](/src/pynchon/models/plugins/pynchon.py#L23-L194)
    * with bases ([Plugin](#fleksplugin),)
    * with admonitions:  [🐉 Complex](/src/pynchon/models/plugins/pynchon.py#L111 "score 12 / 7") 
    * with properties: (4 total)
      *  [`config`](/src/pynchon/models/plugins/pynchon.py#L118) -> inspect._empty
      *  [`logger`](/src/pynchon/models/plugins/pynchon.py#L37) -> inspect._empty
      *  [`plugin_config`](/src/pynchon/models/plugins/pynchon.py#L113) -> inspect._empty
      *  [`project_root`](/src/pynchon/models/plugins/pynchon.py#L108) -> inspect._empty
-------------------------------------------------------------------------------
### pynchon.models.plugins.tool
* Overview:  [source code](/src/pynchon/models/plugins/tool.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (1 total)
  * [`pynchon.models.plugins.tool.ToolPlugin`](/src/pynchon/models/plugins/tool.py#L13-L25)
    * with bases ([CliPlugin](#pynchonmodelspluginscli),)
    * with properties: (4 total)
      *  [`config`](/src/pynchon/models/plugins/tool.py#L118) -> inspect._empty
      *  [`logger`](/src/pynchon/models/plugins/tool.py#L37) -> inspect._empty
      *  [`plugin_config`](/src/pynchon/models/plugins/tool.py#L113) -> inspect._empty
      *  [`project_root`](/src/pynchon/models/plugins/tool.py#L108) -> inspect._empty
-------------------------------------------------------------------------------
### pynchon.cli
* Overview:  [source code](/src/pynchon/cli/__init__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (0 total)
-------------------------------------------------------------------------------
### pynchon.cli.options
* Overview:  [source code](/src/pynchon/cli/options.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
-------------------------------------------------------------------------------
### pynchon.cli.common
* Overview:  [source code](/src/pynchon/cli/common.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (2 total)
  * [`pynchon.cli.common.kommand`](/src/pynchon/cli/common.py#L55-L138)
    * with bases ([`__builtin__.object`](https://docs.python.org/3/library/functions.html#object),)
  * [`pynchon.cli.common.groop`](/src/pynchon/cli/common.py#L167-L181)
    * with bases ([kommand](#pynchonclicommon),)
* Functions: (3 total)
  /src/pynchon/cli/common.py#L141-L164 "")
  * [`pynchon.cli.common.create_command`](/src/pynchon/cli/common.py#L141-L164) with signature `(_name: str, fxn: Callable, entry=None)`
    * with admonitions:  [ 🚩has FIXMEs ](/src/pynchon/cli/common.py#L142 "on lines [142]") 
  * [`pynchon.cli.common.entry_for`](/src/pynchon/cli/common.py#L33-L52) with signature `(name)`
  * [`pynchon.cli.common.load_groups_from_children`](/src/pynchon/cli/common.py#L16-L30) with signature `(root=None, parent=None)`
-------------------------------------------------------------------------------
### pynchon.api
* Overview:  [source code](/src/pynchon/api/__init__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (0 total)
-------------------------------------------------------------------------------
### pynchon.api.render
* Overview:  [source code](/src/pynchon/api/render.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Functions: (9 total)
  * [`pynchon.api.render.clean_whitespace`](/src/pynchon/api/render.py#L160-L162) with signature `(txt: str)`
  * [`pynchon.api.render.dictionary`](/src/pynchon/api/render.py#L30-L36) with signature `(input, context)`
  * [`pynchon.api.render.get_jinja_env`](/src/pynchon/api/render.py#L81-L107) with signature `(*includes, quiet: bool = False)`
  * [`pynchon.api.render.get_jinja_globals`](/src/pynchon/api/render.py#L39-L70) with signature `()`
  * [`pynchon.api.render.get_jinja_includes`](/src/pynchon/api/render.py#L73-L78) with signature `(*includes)`
  * [`pynchon.api.render.get_template`](/src/pynchon/api/render.py#L135-L157)
    * with signature `(template_name: Union[str, pynchon.abcs.path.Path] = None, env=None, from_string: str = None)`
  * [`pynchon.api.render.get_template_from_file`](/src/pynchon/api/render.py#L122-L132) with signature `(file: str = None, **kwargs)`
  * [`pynchon.api.render.get_template_from_string`](/src/pynchon/api/render.py#L110-L119) with signature `(content, env=None)`
  * [`pynchon.api.render.is_templated`](/src/pynchon/api/render.py#L25-L27) with signature `(txt: str = '') -> bool`
-------------------------------------------------------------------------------
### pynchon.api.pynchon
* Overview:  [source code](/src/pynchon/api/pynchon.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
-------------------------------------------------------------------------------
### pynchon.api.parsers
* Overview:  [source code](/src/pynchon/api/parsers/__init__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
-------------------------------------------------------------------------------
### pynchon.api.project
* Overview:  [source code](/src/pynchon/api/project/__init__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Functions: (2 total)
  * [`pynchon.api.project.get_config`](/src/pynchon/api/project/__init__.py#L9-L13) with signature `() -> dict`
  * [`pynchon.api.project.plan`](/src/pynchon/api/project/__init__.py#L16-L45) with signature `(config: dict = {}) -> dict`
-------------------------------------------------------------------------------
### pynchon.api.git
* Overview:  [source code](/src/pynchon/api/git/__init__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
-------------------------------------------------------------------------------
### pynchon.codemod
* Overview:  [source code](/src/pynchon/codemod/__init__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (0 total)
-------------------------------------------------------------------------------
### pynchon.codemod.commands
* Overview:  [source code](/src/pynchon/codemod/commands/__init__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (0 total)
-------------------------------------------------------------------------------
### pynchon.codemod.commands.docstrings
* Overview:  [source code](/src/pynchon/codemod/commands/docstrings/__init__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (0 total)
-------------------------------------------------------------------------------
### pynchon.codemod.commands.docstrings.base
* Overview:  [source code](/src/pynchon/codemod/commands/docstrings/base.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (1 total)
  * [`pynchon.codemod.commands.docstrings.base.base`](/src/pynchon/codemod/commands/docstrings/base.py#L14-L30)
    * with bases ([ContextAwareTransformer](#libcstcodemod_visitor),)
    * with properties: (1 total)
      *  [`module`](/src/pynchon/codemod/commands/docstrings/base.py#L48) -> libcst._nodes.module.Module
-------------------------------------------------------------------------------
### pynchon.codemod.commands.docstrings.javadoc
* Overview:  [source code](/src/pynchon/codemod/commands/docstrings/javadoc.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (2 total)
  * [`pynchon.codemod.commands.docstrings.javadoc.module`](/src/pynchon/codemod/commands/docstrings/javadoc.py#L12-L13)
    * with bases ([base](#pynchoncodemodcommandsdocstringsbase),)
    * with properties: (1 total)
      *  [`module`](/src/pynchon/codemod/commands/docstrings/javadoc.py#L48) -> libcst._nodes.module.Module
  * [`pynchon.codemod.commands.docstrings.javadoc.function`](/src/pynchon/codemod/commands/docstrings/javadoc.py#L16-L25)
    * with bases ([base](#pynchoncodemodcommandsdocstringsbase),)
    * with properties: (1 total)
      *  [`module`](/src/pynchon/codemod/commands/docstrings/javadoc.py#L48) -> libcst._nodes.module.Module
-------------------------------------------------------------------------------
### pynchon.codemod.commands.docstrings.simple
* Overview:  [source code](/src/pynchon/codemod/commands/docstrings/simple.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (3 total)
  * [`pynchon.codemod.commands.docstrings.simple.klass`](/src/pynchon/codemod/commands/docstrings/simple.py#L153-L154)
    * with bases ([base](#pynchoncodemodcommandsdocstringsbase),)
    * with properties: (1 total)
      *  [`module`](/src/pynchon/codemod/commands/docstrings/simple.py#L48) -> libcst._nodes.module.Module
  * [`pynchon.codemod.commands.docstrings.simple.module`](/src/pynchon/codemod/commands/docstrings/simple.py#L161-L193)
    * with bases ([base](#pynchoncodemodcommandsdocstringsbase),)
    * with properties: (1 total)
      *  [`module`](/src/pynchon/codemod/commands/docstrings/simple.py#L48) -> libcst._nodes.module.Module
  * [`pynchon.codemod.commands.docstrings.simple.function`](/src/pynchon/codemod/commands/docstrings/simple.py#L196-L300)
    * with bases ([base](#pynchoncodemodcommandsdocstringsbase),)
    * with admonitions:  [🐉 Complex](/src/pynchon/codemod/commands/docstrings/simple.py#L33 "score 9 / 7") 
    * with properties: (1 total)
      *  [`module`](/src/pynchon/codemod/commands/docstrings/simple.py#L48) -> libcst._nodes.module.Module
* Functions: (4 total)
  * [`pynchon.codemod.commands.docstrings.simple._get_docstring`](/src/pynchon/codemod/commands/docstrings/simple.py#L123-L150) with signature ``
  * [`pynchon.codemod.commands.docstrings.simple.get_obj`](/src/pynchon/codemod/commands/docstrings/simple.py#L26-L41) with signature `(mod=None, dotpath=None)`
  * [`pynchon.codemod.commands.docstrings.simple.is_param_doc`](/src/pynchon/codemod/commands/docstrings/simple.py#L19-L23) with signature `(txt: str)`
  * [`pynchon.codemod.commands.docstrings.simple.write_docstring`](/src/pynchon/codemod/commands/docstrings/simple.py#L44-L120) with signature `(mod=None, dotpath=None, obj=None, docstring=None)`
