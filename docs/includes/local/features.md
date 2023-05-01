## Features

A primary use-case for `pynchon` is generating API / CLI documentation that lives alongside the code, inside github repos.

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
* **Self-hosted:** For concrete examples, see the pynchon-generated [API docs](docs/api) and [CLI docs][docs/cli].  You can also view the [config files that the pynchon-project uses to run pynchon on itself](.pynchon.json5).
