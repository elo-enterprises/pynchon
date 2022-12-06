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
  -f, --file TEXT    file to read as input
  --stdout           whether to write to stdout.
  -o, --output TEXT  output file to write.  (optional)
  --in-place         if true, writes to {file}.json (dropping any other
                     extensions)
  --help             Show this message and exit.
```

###  pynchon render any 

```
Usage: pynchon render any [OPTIONS]

  Render files with given renderer

Options:
  -f, --file TEXT    file to read as input
  -m, --format TEXT  output format to write
  --stdout           whether to write to stdout.
  -o, --output TEXT  output file to write.  (optional)
  --help             Show this message and exit.
```

###  pynchon render jinja  [FILES]

```
Usage: pynchon render jinja [OPTIONS] [FILES]...

  Render render J2 files with given context

Options:
  -f, --file TEXT    file to read as input
  --ctx TEXT         context to use
  --stdout           whether to write to stdout.
  -o, --output TEXT  output file to write.  (optional)
  --in-place         if true, writes to {file}.{ext} (dropping any .j2
                     extension if present)
  --help             Show this message and exit.
```

###  pynchon project   

```
Usage: pynchon project [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  entrypoints  Describe entrypoints for this project (parses setup.cfg)
  version      Describes version details for package (and pynchon itself).
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

  Describes version details for package (and pynchon itself).

Options:
  -m, --format TEXT  output format to write
  --stdout           whether to write to stdout.
  --header TEXT      header to prepend output with. (optional)
  --help             Show this message and exit.
```

###  pynchon ast   

```
Usage: pynchon ast [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.
```
