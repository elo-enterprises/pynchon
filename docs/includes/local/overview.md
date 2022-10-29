## Overview

Pynchon is a library, tool, and extensible framework for project management.  It's useful in general, but also specializes in autogenerating documentation for python projects.

## Motivation & Design

This project exists because frameworks like [sphinx](#), [pydoc](#), and [mkdocs](#), and [pandoc](#) do a lot, but require quite a bit of opinionated /fragile setup, and in the end it's often pretty difficult to do basic stuff.  

If you get basic stuff working and want slight customization, then you're quickly deep into the guts of one of these systems and running into a need for trying different versions or building containers with customized tool-chains.  

Stack-overflow is full of examples of this sort of thing, but here's a quick list of typical complaints:

* You want table-of-contents generation for markdown, then try to do things the "right way" with sophisticated tools, but eventually [hit a wall](https://stackoverflow.com/questions/73965242/pandoc-how-to-generate-github-markdown-table-of-content-toc). This is the third approach you've looked at too.  You wanted to be cool.. but to get work done you'll retreat to using a [bash script](https://github.com/ekalinin/github-markdown-toc) that just works.
* You build out a docker-container for pandoc/tex trying to put together a math-markdown to pdf pipeline, then find that the pandoc filter you needed all this for just fails silently??  You read about panflute for 3 days and finally just have to skip the pretty equations and dump tex gibberish in a doc string.
* You have lots of choices, [but module docs are still hard](https://stackoverflow.com/questions/36237477/python-docstrings-to-github-readme-md)
* You can import your code, [but your docs framework can't](https://stackoverflow.com/questions/17368747/will-sphinx-work-with-code-that-doesnt-import-well).
* [grip](https://pypi.org/project/grip/) is a lifesaver if you're serious about docs on github, but what a pity that you need another tab with `file:///...` to view coverage HTML.
* You have some almost-working docs pipeline, but you still need orchestration.  Orchestration [is subtle](https://github.com/sphinx-doc/sphinx/issues/8437) and [orchestration boilerplate](https://gist.github.com/kristopherjohnson/7466917) begins to clutter your project.  Even worse, that hard-earned boilerplate tends to be very difficult to reuse across projects.


For obvious reasons, popular docs-frameworks also stop short of managing things *besides* docs; but code-gen or code-annotation is a pretty similar task.  After you start thinking about stuff like this, you notice that API-docs generation probably can't succeed anyway as long as you have syntax errors, so why not lint files before or during scan, and make sure the spec for lint/docs-gen are using the same source-tree config in a way that's [DRY](#)?  Annotations along the lines of type-checks or [contract verification](https://github.com/life4/deal) in many projects are also done gradually before they are enforced in builds or runtimes anyway. Since unenforced "informational" content from a CI server is usually just ignored, why not at least organize/publish this data alongside documentation?

But.. *pynchon is not a build tool, it's a project tool.*  The approach is spiritually related to things like [pandoc](#), [helm](#), [jinja](#), [tox](#), [cog](#), [make](#), [cookie-cutter](#), or [pyscaffold](#).  But pynchon is much likely to orchestrate *across* these things than try to replace them.

Management / generation tasks in source-repositories are usually on-going and iterative processes.  For this kind of work, pynchon's interface choices are heavily influenced by the design of [terraform](#): most things are using a plan/apply workflow, where all the context information is arrived at via optional "providers".  After that basic model is established, a plugin/config system then allows for easy expansion.
