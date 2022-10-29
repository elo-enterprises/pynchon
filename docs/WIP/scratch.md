# Pynchon as a Suite of Utilities

Many use-cases for pynchon require no [project configuration](#pynchon-config).  As


The modules inside the pynchon library publish several stand-alone tools, and for these you won't need to use the pynchon CLI directly.

## pynchon.util
### pynchon.util.os
### pynchon.util.files
### pynchon.util.loadf
### pynchon.util.jinja
### pynchon.util.splitvt
### pynchon.util.ansible
### pynchon.util.json
### pynchon.util.pydash
### pynchon.util.shfmt
### pynchon.util.grip

---------------------------------------------------------------------------------

# Pynchon as a Framework

## Plugins
### Plugin Priority

### Plugin Config
#### User Config
#### Config Defaults
#### Lazy Config
#### Dynamic Config
#### Syntactic Sugar

### Plugin CLIs
#### CLI Aliases
#### Hidden Commands

### Plugin Types
#### Core-Plugins
#### Provider-Plugins
#### Planner-Plugins
#### Manager-Plugins
#### Tool-Plugins
#### Nested-Plugins
#### Namespaces
## Rendering Engine
## Projects & Subprojects
## Data vs Display
## Hooks & Events

---------------------------------------------------------------------------------

## Pynchon as a Library

### Planners

### Solvers

### Tagging & Typing

### Orchestration

System Command Invocation

### CLI Framework

### Application Framework

### OOP Framework

### Event Framework



---------------------------------------------------------------------------------

## Example Usage

```
```

---------------------------------------------------------------------------------

## Packaging & Releases

---------------------------------------------------------------------------------

## Dependencies

---------------------------------------------------------------------------------

## Related Work

---------------------------------------------------------------------------------

## Workflows

### Workflow: Bug Reports or Feature Requests

### Workflow: Finding a Release

### Workflow: Installation for Library Developers

---------------------------------------------------------------------------------

## Implementation Notes


### Python Plugins

For auto-discovery of things like "name of this package" or "entry-points for this package" `pynchon` assumes by default that it is working inside the source-tree for a modern python project.

If your project is using older packaging standards, or you're working on a group of files that's not a proper python project, you can usually work around this by passing information in directly instead of relying on auto-discovery.  Use the `pkg_name` top-level config key.


Pynchon relies heavily on [griffe](https://pypi.org/project/griffe/) for parsing and for [AST-walking](https://docs.python.org/3/library/ast.html).

For cyclomatic complexity, pynchon relies on the [mccabe library](https://github.com/PyCQA/mccabe).

---------------------------------------------------------------------------------

## Known Issues

* Use the [griffe-agent / plugin framework](#FIXME)?
* See [FIXME.md](docs/FIXME.md)
* See [TODO.md](docs/TODO.md)

---------------------------------------------------------------------------------
