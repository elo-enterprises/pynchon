## Overview

Pynchon is a library, tool, and extensible framework for project management.  It's useful in general, but also specializes in autogenerating documentation for python projects.

## Motivation & Design

This project exists because frameworks like [sphinx](#), [pydoc](#), and [mkdocs](#) do a lot, but require quite a bit of opionated/fragile setup, and in the end it's pretty hard to do basic stuff.

See for example [this stack overflow question](https://stackoverflow.com/questions/36237477/python-docstrings-to-github-readme-md).

Popular docs-frameworks also stop short of managing things *besides* docs, although code-gen or code-annotation is a pretty similar task.  After you start thinking about stuff like this, API-docs generation probably can't succeed anyway as long as you have syntax errors, so why not lint files while you're scanning them, and make sure the spec for each is using the *source tree* DRY-ly?

But.. *pynchon is not a build tool, it's a project tool.*  The approach is spiritually related to things like [tox](#), [cog](#), [make](#), [helm](#), [jinja](#), [cookie-cutter](#), or [pyscaffold](#).  But pynchon is much likely to orchestrate *across* these things than try to replace them.

Management / generation tasks in source-repositories are usually on-going and iterative processes.  For this kind of work, pynchon's interface choices are heavily influenced by the design of [terraform](#): most things are using a plan/apply workflow, where all the context information is arrived at via optional "providers".  After that basic model is established, a plugin/config system then allows for easy expansion.
