-------------------------------------------------------------------------------


###  pynchon   

```
Usage: pynchon [OPTIONS] COMMAND [ARGS]...

  pynchon CLI:

Options:
  --version  Show the version and exit.
  --help     Show this message and exit.

Commands:
  ast
  gen
  parse
  project
  render
```

###  pynchon gen   

```
Usage: pynchon gen [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  api
  cli
```

###  pynchon gen api   

```
Usage: pynchon gen api [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  toc  Generate table-of-contents
```

###  pynchon gen cli toc 

```
Usage: pynchon gen cli toc [OPTIONS]

  Describe entrypoints for this project (parses setup.cfg)

Options:
  -f, --file TEXT    file to grab entrypoints from
  -m, --format TEXT  output format to write
  -o, --output TEXT  output file to write.  (optional)
  --stdout           whether to write to stdout.
  --header TEXT      header to prepend output with. (optional)
  --help             Show this message and exit.
```

###  pynchon gen cli   

```
Usage: pynchon gen cli [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  all         Generates help for every entrypoint
  entrypoint  Autogenenerate docs for python CLIs using click
  main        Autogenenerate docs for python modules using __main__
  toc         Describe entrypoints for this project (parses setup.cfg)
```

###  pynchon gen cli all 

```
Usage: pynchon gen cli all [OPTIONS]

  Generates help for every entrypoint

Options:
  -f, --file TEXT    file to grab entrypoints from
  --output-dir TEXT  output directory (optional)
  --stdout           whether to write to stdout.
  --help             Show this message and exit.
```

###  pynchon gen cli main 

```
Usage: pynchon gen cli main [OPTIONS]

  Autogenenerate docs for python modules using __main__

Options:
  -m, --format TEXT  output format to write
  --stdout           whether to write to stdout.
  --header TEXT      header to prepend output with. (optional)
  -f, --file TEXT    file to read as input
  --output-dir TEXT  output directory (optional)
  --name TEXT        name to use
  -m, --module TEXT  module to grab click-cli from. (must be used with `name`)
  --help             Show this message and exit.
```

###  pynchon gen cli entrypoint 

```
Usage: pynchon gen cli entrypoint [OPTIONS]

  Autogenenerate docs for python CLIs using click

Options:
  -m, --format TEXT  output format to write
  --stdout           whether to write to stdout.
  --header TEXT      header to prepend output with. (optional)
  -f, --file TEXT    file to read as input
  -o, --output TEXT  output file to write.  (optional)
  --name TEXT        name to use
  -m, --module TEXT  module to grab click-cli from. (must be used with `name`)
  --help             Show this message and exit.
```

###  pynchon render   

```
Usage: pynchon render [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  any    Render files with given renderer
  jinja  Render render J2 files with given context
  json5  Render render JSON5 files -> JSON
```

###  pynchon render json5  [FILES]

```
Usage: pynchon render json5 [OPTIONS] [FILES]...

  Render render JSON5 files -> JSON

Options:
  -o, --output TEXT     output file to write.  (optional)
  -t, --templates TEXT  path to use for template-root / includes
  --in-place            if true, writes to {file}.json (dropping any other
                        extensions)
  --help                Show this message and exit.
```

###  pynchon render any 

```
Usage: pynchon render any [OPTIONS]

  Render files with given renderer

Options:
  -m, --format TEXT  output format to write
  -o, --output TEXT  output file to write.  (optional)
  --help             Show this message and exit.
```

###  pynchon render jinja  [FILES]

```
Usage: pynchon render jinja [OPTIONS] [FILES]...

  Render render J2 files with given context

Options:
  --ctx TEXT            context to use
  -o, --output TEXT     output file to write.  (optional)
  -t, --templates TEXT  path to use for template-root / includes
  --in-place            if true, writes to {file}.{ext} (dropping any .j2
                        extension if present)
  --help                Show this message and exit.
```

###  pynchon project   

```
Usage: pynchon project [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  apply        Apply the plan created by `pynchon project plan`
  config       Describe the config for this project
  entrypoints  Describe entrypoints for this project (parses setup.cfg)
  plan         List goals for auto-documenting this project
  version      Describes version details for this package (and pynchon...
```

###  pynchon project entrypoints 

```
Usage: pynchon project entrypoints [OPTIONS]

  Describe entrypoints for this project (parses setup.cfg)

Options:
  -f, --file TEXT    file to grab entrypoints from
  -m, --format TEXT  output format to write
  --stdout           whether to write to stdout.
  -o, --output TEXT  output file to write.  (optional)
  --header TEXT      header to prepend output with. (optional)
  --help             Show this message and exit.
```

###  pynchon project version 

```
Usage: pynchon project version [OPTIONS]

  Describes version details for this package (and pynchon itself).

Options:
  -m, --format TEXT  output format to write
  -o, --output TEXT  output file to write.  (optional)
  --header TEXT      header to prepend output with. (optional)
  --help             Show this message and exit.
```

###  pynchon project config 

```
Usage: pynchon project config [OPTIONS]

  Describe the config for this project

Options:
  --help  Show this message and exit.
```

###  pynchon project apply 

```
Usage: pynchon project apply [OPTIONS]

  Apply the plan created by `pynchon project plan`

Options:
  --help  Show this message and exit.
```

###  pynchon project plan 

```
Usage: pynchon project plan [OPTIONS]

  List goals for auto-documenting this project

Options:
  --stdout  whether to write to stdout.
  --help    Show this message and exit.
```

###  pynchon parse   

```
Usage: pynchon parse [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  pyright  Parses pyright output into a markdown-based report card
```

###  pynchon parse pyright 

```
Usage: pynchon parse pyright [OPTIONS]

  Parses pyright output into a markdown-based report card

Options:
  --help  Show this message and exit.
```

###  pynchon ast   

```
Usage: pynchon ast [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.
```
