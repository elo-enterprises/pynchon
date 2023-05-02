""" {{pkg}}.util.lme
"""
import logging


def get_logger(name):
    """
    utility function for returning a logger
    with standard formatting patterns, etc
    """
    from rich.style import Style
    from rich.theme import Theme
    from rich.console import Console
    from rich.logging import RichHandler
    from rich.default_styles import DEFAULT_STYLES

    theme = Theme(
        {
            **DEFAULT_STYLES,
            **{
                "logging.keyword": Style(bold=True, color="yellow"),
                # "logging.level.notset": Style(dim=True),
                "logging.level.debug": Style(color="green"),
                "logging.level.info": Style(
                    dim=True,
                    # color="blue",
                ),
                "logging.level.warning": Style(color="yellow"),
                "logging.level.error": Style(color="red", dim=True, bold=True),
                "logging.level.critical": Style(
                    color="red",
                    bold=True,
                    # reverse=True
                ),
                "log.level": Style.null(),
                "log.time": Style(color="cyan", dim=True),
                "log.message": Style.null(),
                "log.path": Style(dim=True),
            },
        }
    )
    log_handler = RichHandler(
        rich_tracebacks=True,
        console=Console(theme=theme, stderr=True),
        show_time=False,
    )

    logging.basicConfig(
        # level="DEBUG",
        format="%(message)s",
        datefmt="[%X]",
        handlers=[log_handler],
    )
    FormatterClass = logging.Formatter
    formatter = FormatterClass(
        fmt=" ".join(["%(name)s", "%(message)s"]),
        # datefmt="%Y-%m-%d %H:%M:%S",
        datefmt="",
    )
    log_handler.setFormatter(formatter)

    logger = logging.getLogger(name)

    # FIXME: get this from some kind of global config
    logger.setLevel("DEBUG")
    return logger
