
[tooltip-module-entrypoints]: ## "Module Entrypoints"
[tooltip-package-entrypoints]: ## "Console Script Entrypoint"

[Docs](../) *↔* [CLI](README.md) *↔* [Console Scripts](README.md#console-scripts) *↔* **Module Entrypoints**

---------------------------------------------------


## [**ℳ**][tooltip-module-entrypoints] pynchon.util.makefile

[**[Module]**](README.md#module-entrypoints) `pynchon.util.makefile` publishes a command line interface (*[source](/src/pynchon/util/makefile/__main__.py)*).

Example usage:

```bash
$ python -mpynchon.util.makefile --help

Usage: python -m pynchon.util.makefile [OPTIONS] COMMAND [ARGS]...

  pynchon.util.makefile CLI

Options:
  --help  Show this message and exit.

Commands:
  database  Get database for Makefile (i.e.
  parse     Parse Makefile to JSON.
```