"""
"""
import sys
import logging


def get_logger(name):
    """
    utility function for returning a logger
    with standard formatting patterns, etc
    """
    if sys.stdout.isatty():
        import coloredlogs

        FormatterClass = coloredlogs.ColoredFormatter
    else:
        FormatterClass = logging.Formatter
    formatter = FormatterClass(
        fmt=" - ".join(["%(levelname)s", "%(name)s", "%(message)s"]),
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    log_handler = logging.StreamHandler()
    log_handler.setFormatter(formatter)
    logger = logging.getLogger(name)
    if not logger.handlers:
        # prevents duplicate registration
        logger.addHandler(log_handler)
    # FIXME: get this from some kind of global config
    logger.setLevel("DEBUG")
    # intermittent duplicated stuff without this
    logger.propagate = False
    return logger
