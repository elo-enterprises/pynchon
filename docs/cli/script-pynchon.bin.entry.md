
[tooltip-package-entrypoints]: ## "Console Script Entrypoint"
[tooltip-module-entrypoints]: ## "Module Entrypoint"

[Docs](../) *↔* [CLI](README.md) *↔* Console Scripts *↔* [Module Entrypoints](README.md#module-entrypoints)

---------------------------------------------------


## [**℮**][tooltip-package-entrypoints] pynchon

Module [*pynchon.bin.entry*](/src/pynchon/bin.py) publishes a CLI named `pynchon` via a [console script](https://python-packaging.readthedocs.io/en/latest/command-line-scripts.html#the-console-scripts-entry-point). (*[source](/src/pynchon/bin.py)*)

**Example usage:**

```bash
$ pynchon --help

------------------------------
Usage: pynchon [OPTIONS] COMMAND [ARGS]...

Options:
  --get TEXT      config retrieval
  --set TEXT      config overrides
  --plugins TEXT  shortcut for `--set plugins=...`
  --version       Show the version and exit.
  --help          Show this message and exit.

Core COMMANDs:
  apply:          Executes the plan for this plugin
  bootstrap:      Bootstrap for shell integration, etc
  cfg:            Show current project config (with templating/interpolation)
  cicd:           Context for CI/CD
  deck:           Tool for working with markdown based slide-decks
  docs:           Management tool for project docs, including helpers for
                  enumerating, serving, & opening them.
  dot:            Finds / Renders (graphviz) dot files for this project
  fixme:          Generates {docs_root}/FIXME.md from source
  gen:            Collects `gen` commands from other plugins
  git:            Context for git
  github:         Tools for working with GitHub
  globals:        Context for pynchon globals
  griffe:         Tools for working with Python ASTs
  jinja:          Renders files with {jinja.template_includes}
  json:           Tools for working with JSON & JSON5
  makefile:       Makefile parser
  markdown:       Markdown
  mermaid:        Mermaid Plugin
  parse:          Misc tools for parsing
  pattern:        Tools for working with file/directory patterns
  plan:           Runs plan for all plugins  ..
  plugins:        Meta-plugin for managing plugins
  project:        Meta-plugin for managing this project
  pypi:           Context for PyPI
  python:         Code transformation and docs-generation utilities for python
                  projects.
  python-api:     Generators for Python API docs
  python-cli:     Generators for Python CLI docs
  python-libcst:  Code-transforms via libcst[1]
  raw:            Returns (almost) raw config, without interpolation
  render:         Collects `render` commands from other plugins
  src:            Management tool for project source
  test:           Management tool for project tests
  tui:            Open Textual TUI.
```
