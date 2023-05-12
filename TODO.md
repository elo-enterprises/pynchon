release:
  pynchon.gripe- better interaction with grip
  shimport- built on importlib, imphook, and deals.module_contract
    * shimport.registry
    * shimport.wrapper
    * shimport.filter_module

research:
  lazy:
    importlib.set_lazy_imports()
    https://github.com/facebookincubator/cinder
  contracts:
    https://crosshair.readthedocs.io/en/latest/contracts.html
    https://github.com/life4/deal
  typing:
    runtime checks w/o pydantic? typing.runtime_checkable
  oop:
    py protocols;
    abstract mcls into interface?

refactor:
  app model
  lazy imports everywhere to speed up loading
  fleks.meta validators to use deal contracts
  `cli_label` with tags- works with:
    - Plugin's
    - Plugin.method_name

abstract:
  shfmt
  oops or woops:
    from pynchon.abcs.meta pynchon.util.oop

fix:

impl:
  visitor.resolution struct
  shfmt/back-ticks; parens; brackets/curly; sorting
  p/--get --set --plugins
  plugin/planner/jinja/tpl
  plugin/planner/jinja/template
  plugin/proj/clean
  plugin/tool/release
  plugin/tool/stream
  cli/p proj alias
  cli/top-level group aliases
  help/footnotes
  help/sorting
  help/colorize output

!i
  reflektr
  rflktr
  myrror
