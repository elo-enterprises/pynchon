
[tooltip-module-entrypoints]: ## "Module Entrypoints"
[tooltip-package-entrypoints]: ## "Console Script Entrypoint"

[Docs](../) *↔* [CLI](README.md) *↔* [Console Scripts](README.md#console-scripts) *↔* **Module Entrypoints**

---------------------------------------------------


## [**ℳ**][tooltip-module-entrypoints] pynchon.util.files

[**[Module]**](README.md#module-entrypoints) `pynchon.util.files` publishes a command line interface (*[source](/src/pynchon/util/files/__main__.py)*).

Example usage:

```bash
$ python -mpynchon.util.files --help

Usage: python -m pynchon.util.files [OPTIONS] COMMAND [ARGS]...

  pynchon.util.files CLI

Options:
  --help  Show this message and exit.

Commands:
  dumps
  find-src
  find-suffix
  is-prefix    True if given file already prepends given target
  prepend      Prepends given file contents to given target
```