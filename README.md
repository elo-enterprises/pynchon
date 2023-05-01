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
    pynchon
    </td>
  </tr>
</table>

---------------------------------------------------------------------------------

## Overview

Pynchon is a library, tool, and extensible framework for project management.  It's useful in general, but also specializes in autogenerating documentation for python projects.

## Motivation & Design

This project exists because frameworks like [sphinx](#), [pydoc](#), and [mkdocs](#) do a lot, but require quite a bit of opionated/fragile setup, and in the end it's pretty hard to do basic stuff.

See for example [this stack overflow question](https://stackoverflow.com/questions/36237477/python-docstrings-to-github-readme-md).

Popular docs-frameworks also stop short of managing things *besides* docs, although code-gen or code-annotation is a pretty similar task.  After you start thinking about stuff like this, API-docs generation probably can't succeed anyway as long as you have syntax errors, so why not lint files while you're scanning them, and make sure the spec for each is using the *source tree* DRY-ly?

But.. *pynchon is not a build tool, it's a project tool.*  The approach is spiritually related to things like [tox](#), [cog](#), [make](#), [helm](#), [jinja](#), and [cookie-cutter](#).  But it's more likely to orchestrate *across* these things than try to replace them.

Management / generation tasks in source-repositories are usually ongoing iterative processes.  For this kind of work, pynchon's interface choices are heavily influenced by the design of [terraform](#): most things are using a plan/apply workflow, where context information is arrived at via optional "providers".  A plugin/config system then allows for easy expansion on the basic model.

## Overview

Pynchon is a library, tool, and extensible framework for project management.  It's useful in general, but also specializes in autogenerating documentation for python projects.

## Motivation & Design

This project exists because frameworks like [sphinx](#), [pydoc](#), and [mkdocs](#) do a lot, but require quite a bit of opionated/fragile setup, and in the end it's pretty hard to do basic stuff.

See for example [this stack overflow question](https://stackoverflow.com/questions/36237477/python-docstrings-to-github-readme-md).

Popular docs-frameworks also stop short of managing things *besides* docs, although code-gen or code-annotation is a pretty similar task.  After you start thinking about stuff like this, API-docs generation probably can't succeed anyway as long as you have syntax errors, so why not lint files while you're scanning them, and make sure the spec for each is using the *source tree* DRY-ly?

But.. *pynchon is not a build tool, it's a project tool.*  The approach is spiritually related to things like [tox](#), [cog](#), [make](#), [helm](#), [jinja](#), and [cookie-cutter](#).  But it's more likely to orchestrate *across* these things than try to replace them.

Management / generation tasks in source-repositories are usually ongoing iterative processes.  For this kind of work, pynchon's interface choices are heavily influenced by the design of [terraform](#): most things are using a plan/apply workflow, where context information is arrived at via optional "providers".  A plugin/config system then allows for easy expansion on the basic model.

## Quick Start

Pynchon is on PyPI, so to get the latest:

```
pip install pynchon
```

Or, for developers:

```
git clone ..FIXME..
pip install -e .
```

---------------------------------------------------------------------------------

## Pynchon as a Library

---------------------------------------------------------------------------------

## Pynchon as a Tool

The modules inside the pynchon library publish several stand-alone tools.

---------------------------------------------------------------------------------

## Pynchon as a CLI

---------------------------------------------------------------------------------

## Pynchon as a Framework

---------------------------------------------------------------------------------

## Tutorials

```
pynchon gen version-metadata
pynchon gen api toc
pynchon gen cli toc
pynchon gen api detail
```


---------------------------------------------------------------------------------

## Implementation Notes


### Python Plugins

For auto-discovery of things like "name of this package" or "entry-points for this package" `pynchon` assumes by default that it is working inside the source-tree for a modern python project.

If your project is using older packaging standards, or you're working on a group of files that's not a proper python project, you can usually work around this by passing information in directly instead of relying on auto-discovery.  Use the `pkg_name` top-level config key.


Pynchon relies heavily on [griffe](https://pypi.org/project/griffe/) for parsing and for [AST-walking](https://docs.python.org/3/library/ast.html).

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

## Known Issues

* Use the [griffe-agent / plugin framework](#FIXME)?

---------------------------------------------------------------------------------
