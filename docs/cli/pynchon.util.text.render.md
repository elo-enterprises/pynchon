
[tooltip-module-entrypoints]: ## "Module Entrypoints"
[tooltip-package-entrypoints]: ## "Console Script Entrypoint"

[Docs](../) *↔* [CLI](README.md) *↔* [Console Scripts](README.md#console-scripts) *↔* **Module Entrypoints**

---------------------------------------------------


## [**ℳ**][tooltip-module-entrypoints] pynchon.util.text.render

[**[Module]**](README.md#module-entrypoints) `pynchon.util.text.render` publishes a command line interface (*[source](/src/pynchon/util/text/render/__main__.py)*).

Example usage:

```bash
$ python -mpynchon.util.text.render --help

Usage: python -m pynchon.util.text.render [OPTIONS] COMMAND [ARGS]...

  pynchon.util.text.render CLI

Options:
  --help  Show this message and exit.

Commands:
  j2          alias for `j2cli`
  j2cli       A wrapper on the `j2` command (j2cli must be installed)...
  jinja       alias for `jinja_file`
  jinja-file  Renders jinja2 file (supports includes, custom filters)
```