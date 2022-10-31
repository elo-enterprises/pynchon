-------------------------------------------------------------------------------




### pynchon   

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

 -------------------------------------------------------------------------------



### pynchon gen   

```
Usage: pynchon gen [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  api
  cli
```

 -------------------------------------------------------------------------------



### pynchon gen api   

```
Usage: pynchon gen api [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  toc
```

 -------------------------------------------------------------------------------



### pynchon gen api toc 

```
Usage: pynchon gen api toc [OPTIONS]



Options:
  --format TEXT       output format to write
  -o, --output TEXT   output file to write.  (optional)
  -f, --file TEXT     file to read as input
  --stdout            whether to write to stdout.
  --header TEXT       header to prepend output with. (optional)
  -p, --package TEXT
  --help              Show this message and exit.
```

 -------------------------------------------------------------------------------



### pynchon gen cli   

```
Usage: pynchon gen cli [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  click
```

 -------------------------------------------------------------------------------



### pynchon gen cli click 

```
Usage: pynchon gen cli click [OPTIONS]



Options:
  -m, --format TEXT  output format to write
  --stdout           whether to write to stdout.
  -o, --output TEXT  output file to write.  (optional)
  --header TEXT      header to prepend output with. (optional)
  -f, --file TEXT    file to read as input
  --name TEXT        name to use
  -m, --module TEXT  module to grab click-cli from. (must be used with `name`)
  --help             Show this message and exit.
```

 -------------------------------------------------------------------------------



### pynchon project   

```
Usage: pynchon project [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  entrypoints
```

 -------------------------------------------------------------------------------



### pynchon project entrypoints 

```
Usage: pynchon project entrypoints [OPTIONS]



Options:
  -f, --file TEXT    file to grab entrypoints from
  -m, --format TEXT  output format to write
  --stdout           whether to write to stdout.
  -o, --output TEXT  output file to write.  (optional)
  --header TEXT      header to prepend output with. (optional)
  --help             Show this message and exit.
```

 -------------------------------------------------------------------------------



### pynchon ast   

```
Usage: pynchon ast [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.
```

 -------------------------------------------------------------------------------
