<table>
  <tr>
    <td colspan=2><strong>
    pynchon
      </strong>&nbsp;&nbsp;&nbsp;&nbsp;
    </td>
  </tr>
  <tr>
    <td width=15%><img src=docs/img/icon.png style="width:150px"></td>
    <td>
      <br/><br/>
      <a href=https://pypi.python.org/pypi/pynchon/><img src="https://img.shields.io/pypi/l/pynchon.svg"></a>
      <a href=https://pypi.python.org/pypi/pynchon/><img src="https://badge.fury.io/py/pynchon.svg"></a>
      <a href="https://github.com/elo-enterprises/pynchon/actions/workflows/python-publish.yml"><img src="https://github.com/elo-enterprises/pynchon/actions/workflows/python-publish.yml/badge.svg"></a><a href="https://github.com/elo-enterprises/pynchon/actions/workflows/python-test.yml"><img src="https://github.com/elo-enterprises/pynchon/actions/workflows/python-test.yml/badge.svg"></a>
    </td>
  </tr>
</table>

---------------------------------------------------------------------------------

<div class="toc">
<ul>
<li><a href="#overview">Overview</a></li>
<li><a href="#features">Features</a></li>
<li><a href="#installation">Installation</a></li>
<li><a href="#quick-start">Quick Start</a></li>
<li><a href="#configuration">Configuration</a></li>
</ul>
</div>


---------------------------------------------------------------------------------

## Overview

Pynchon is a library, tool, and extensible framework that helps with generating documentation, working with diagrams, rendering templates, and maybe other aspects of project management.  It's useful in general, but specializes in autogenerating documentation for python projects.

This code is still experimental and interface stability is not yet guaranteed.. make sure to pin pynchon at specific versions for your project.

---------------------------------------------------------------------------------

## Features

* Terraform-style plan/apply workflows, with support for parallel execution
* Plugin framework for extensions
* Tight integration with [Jinja](#),
* Support for tools like Markdown, [Mermaid](#), [draw.io](#), and [pandoc](#)
* Friendly output for machines and for humans.  Most

---------------------------------------------------------------------------------

## Installation

Pynchon is on PyPI, so to get the latest:

```bash
pip install pynchon
```

Or, for developers:

```bash
# for ssh
git clone git@github.com:elo-enterprises/pynchon.git

# or for http
# git clone https://github.com/elo-enterprises/pynchon

cd pynchon
pip install -e .
```

---------------------------------------------------------------------------------

## Quick Start

### Utility Invocation

If you're more interested in tools than a framework, some functionality is available without completely loading pynchon.

For this you can use module-invocations like `python -mpynchon.util.text ..`. For example:

```bash
# Helpers for loading/converting config from many file formats:
$ python -mpynchon.util.text loadf --help
Usage: python -m pynchon.util.text loadf [OPTIONS] COMMAND [ARGS]...

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


# Helpers for rendering Jinja templates
$ python -mpynchon.util.text render jinja --help
Usage: python -m pynchon.util.text render jinja [OPTIONS] FILE

  alias for `jinja_file`

Options:
  -o, --output TEXT    output file to write.  (optional)
  --print              if set, displays result on stdout even when `--output
                       <file>` is passed
  --include TEXT       path to use for template-root / includes
  --context TEXT       context literal.  must be JSON
  --context-file TEXT  context file.  must be JSON
  --help               Show this message and exit.

```

### CLI, Plugins, & Config

For most functionality, you'll want to use the main `pynchon` tool.  Here, that functionality is provided via plugins, where every plugin is a subcommand for the main CLI.  There are several plugins which are provided by default, and you can see the plugins in use with the following command:

```bash
# Shows the default plugin list, with no pynchon config present
$ pynchon plugins list
[
  "git",
  "core",
  "markdown",
  "docs",
  "github",
  "src",
  "render",
  "json",
  "gen",
  "parse",
  "python",
  "project",
  "globals",
  "jinja",
  "pattern"
]


# Add mermaid plugin, which is non-default, using the command-line.
# Note that this is still without any file-based config
$ pynchon --plugins mermaid mermaid --help
Usage: pynchon mermaid [OPTIONS] COMMAND [ARGS]...

  Finds & renders Mermaid diagram files

Options:
  --help  Show this message and exit.

Commands:
  cfg     Shows current config for this plugin
  list    Find mermaid diagrams under `{{project_root}}/**/*.mmd`
  ls      (alias for `ls`)
  plan    Run planning for this plugin
  render  Renders mermaid diagram to image
  run     Passes given command through to docker-image this plugin wraps

```

To get started with file-based config, run `pynchon init` in your project folder to create `.pynchon.json5`.  From here you can modify `pynchon.plugins` to use a custom set of plugins, and configure the plugins as well.

Every plugin has config, which can be overriden, which may include defaults, or which is dynamically determined from the current context.  To show plugin config, there's always a subcommand available.

For example, with the `github` plugin

```bash

# Outside of a github repository,
# the config is empty and not very interesting
$ pynchon github cfg
{
  "enterprise": false,
  "actions": [],
  "org_name": null,
  "org_url": null,
  "raw_url": null,
  "repo_ssh_url": null,
  "repo_url": null
}

# Inside of a github repository, there's some useful information
$ pynchon github cfg
{
  "enterprise": false,
  "actions": [ ... ],
  "org_name": "elo-enterprises",
  "org_url": "https://github.com/elo-enterprises",
  "raw_url": "https://raw.githubusercontent.com/elo-enterprises/pynchon",
  "repo_ssh_url": "git@github.com:elo-enterprises/pynchon.git",
  "repo_url": "https://github.com/elo-enterprises/pynchon"
}
```





---------------------------------------------------------------------------------

## Configuration


Pynchon works without any configuration at all, but loads no
