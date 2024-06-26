
[tooltip-module-entrypoints]: ## "Module Entrypoints"
[tooltip-package-entrypoints]: ## "Console Script Entrypoint"

[Docs](../) *↔* [CLI](README.md) *↔* [Console Scripts](README.md#console-scripts) *↔* **Module Entrypoints**

---------------------------------------------------


## [**ℳ**][tooltip-module-entrypoints] pynchon.util.text

[**[Module]**](README.md#module-entrypoints) `pynchon.util.text` publishes a command line interface (*[source](/src/pynchon/util/text/__main__.py)*).

Example usage:

```bash
$ python -mpynchon.util.text --help

Usage: python -m pynchon.util.text [OPTIONS] COMMAND [ARGS]...

  pynchon.util.text CLI

Options:
  --help  Show this message and exit.

Commands:
  dumpf   pynchon.util.text.dumpf.__main__
  loadf   pynchon.util.text.loadf CLI
  render  pynchon.util.text.render CLI
```