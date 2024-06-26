
[tooltip-module-entrypoints]: ## "Module Entrypoints"
[tooltip-package-entrypoints]: ## "Console Script Entrypoint"

[Docs](../) *↔* [CLI](README.md) *↔* [Console Scripts](README.md#console-scripts) *↔* **Module Entrypoints**

---------------------------------------------------


## [**ℳ**][tooltip-module-entrypoints] pynchon.util.text.loadf

[**[Module]**](README.md#module-entrypoints) `pynchon.util.text.loadf` publishes a command line interface (*[source](/src/pynchon/util/text/loadf/__main__.py)*).

Example usage:

```bash
$ python -mpynchon.util.text.loadf --help

Usage: python -m pynchon.util.text.loadf [OPTIONS] COMMAND [ARGS]...

  pynchon.util.text.loadf CLI

Options:
  --help  Show this message and exit.

Commands:
  ini    Parses ini file and returns JSON :param file:
  json   loads json to python dictionary from given file or string :param...
  json5  Parses JSON-5 file(s) and outputs json.
  loadf
  toml   Parses toml file and returns JSON :param file: str: (Default...
  yaml   parses yaml file and returns JSON :param *args: :param **kwargs:
```