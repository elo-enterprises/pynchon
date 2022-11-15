<table>
  <tr>
    <td colspan=2><strong>
      pynchon
      </strong>&nbsp;&nbsp;&nbsp;&nbsp;
      <small><small>
      </small></small>
    </td>
  </tr>
  <tr>
    <td width=15%><img src=img/icon.png style="width:150px"></td>
    <td>
    Autodocs for python projects
    </td>
  </tr>
</table>

---------------------------------------------------------------------------------

## Overview

Pynchon is a tool/library for autogenerating documentation for python projects.  

### Motivation

This project exists because frameworks like [sphinx](#), [pydoc](#), and [mkdocs](#) do a lot, but require quite a bit of setup, and in the end it's pretty hard to do basic stuff.  

See for example [this stack overflow question](https://stackoverflow.com/questions/36237477/python-docstrings-to-github-readme-md).

### Features

The primary use-case for `pynchon` is generating API / CLI documentation that lives alongside the code, inside github repos.
(Using github-repos is optional, but by default `pynchon` writes  relative-links that assume github-compatible anchors, etc.)

* **Pure markdown output for docs,** in github flavored markdown.
* **API documentation for python-packages**
  * Top-level index/outline for included modules, classes, functions. ([example](#))
  * (Detail views coming soon but not implemented yet)
* **CLI documentation for package entry-points**
  * Top-level overview of all commands defined in setup.cfg ([example](#))
  * Detail view for individual scripts ([example](#))
    * (Currently only available for projects using `click`)
* **Test-discovery and links to related code:**
  * (Basic heuristics at this time, more sophisticated ones soon)
* **Admonitions / badges:**
  * 🐉: Complexity dragon for [cyclomatic-complexity](https://en.wikipedia.org/wiki/Cyclomatic_complexity)
  * 🚩 Red flags for code docs or comments that include `FIXME`s
  * 🟡 Yellow indicators for code docs or comments that include `WARNING`s
* **Self-hosted:** For concrete examples, see the pynchon-generated [API docs](docs/api) and [CLI docs][docs/cli] for `pynchon`.

---------------------------------------------------------------------------------

## Usage

```
pynchon gen version-metadata
pynchon gen api toc
pynchon gen cli toc
pynchon gen api detail
```

---------------------------------------------------------------------------------

## Implementation

For auto-discovery of things like "name of this package" or "entry-points for this package" `pynchon` assumes by default that it is working inside the source-tree for a modern python project (in other words it parses `setup.cfg`).  If your project is using older standards or you're working on a group of files that's not a proper python project, you can usually work around this by passing information in directly instead of relying on auto-discovery.

Pynchon relies heavily on [griffe](https://pypi.org/project/griffe/) for parsing and for [AST-walking](https://docs.python.org/3/library/ast.html).  Currently the approach being used ignores the [griffe-agent / plugin framework](#) because I couldn't get it to work, but in the future that will probably change.

For cyclomatic complexity, we rely on [mccabe](https://github.com/PyCQA/mccabe).

---------------------------------------------------------------------------------

## Packaging & Releases

---------------------------------------------------------------------------------

## Dependencies

---------------------------------------------------------------------------------

## Related Work

---------------------------------------------------------------------------------

## Workflows

### Workflow: Bug Reports or Feature Requests

### Workflow: Finding a Library Release

### Workflow: Installation for Library Developers

### Workflow: Installation for Users

### Workflow: Build, install, testing, etc

### Workflow: Running Tests

---------------------------------------------------------------------------------
