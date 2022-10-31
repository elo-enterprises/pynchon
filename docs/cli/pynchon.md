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
  --format TEXT      output format to write
  --stdout           whether to write to stdout.
  --header TEXT      header to prepend output with. (optional)
  -f, --file TEXT    file to read as input
  -o, --output TEXT  output file to write.  (optional)
  --name TEXT        name to use
  -m, --module TEXT  module to grab click-cli from. (must be used with
                     `name`)
  --help             Show this message and exit.
```

###  pynchon project   

```
Usage: pynchon project [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  entrypoints  Describe entrypoints for this project (parses...
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

###  pynchon ast   

```
Usage: pynchon ast [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.
```
