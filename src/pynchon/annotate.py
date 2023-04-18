""" """
import os
import inspect
import importlib

import pynchon
from pynchon import util
from pynchon.util import lme

LOGGER = lme.get_logger(__name__)


def klass(name, kls) -> None:
    """annotates a class"""
    LOGGER.debug(f"annotating class: {name}")
    mod = importlib.import_module(kls.parent.canonical_path)
    kls._handle = getattr(mod, name)

    properties = []
    for x in dir(kls._handle):
        if x.startswith("_"):
            continue
        prop = getattr(kls._handle, x)
        is_property = type(prop).__name__ == "property"
        if not is_property:
            continue
        fxn = prop.fget
        fxn_doc = fxn.__doc__ or ""
        try:
            fxn_sig = inspect.signature(fxn)
        except (ValueError,) as exc:
            LOGGER.warning(f"Could not retrieve function signature for {fxn}!")
            fxn_sig = None
        try:
            fxn_code = fxn.__code__
        except AttributeError:  # C extensions..
            fxn_code = None
        start = fxn_code.co_firstlineno if fxn_code else kls.lineno
        properties.append(
            dict(
                name=x,
                doc=fxn_doc,
                signature=fxn_sig,
                start=str(start),
                end="",  # FIXME
                annotation=fxn_sig
                and str(fxn_sig.return_annotation)
                .replace("<class '", "")
                .replace("'>", ""),
                fixme="FIXME" in fxn_doc,
            )
        )

    bases = []
    for x in kls._handle.__bases__:
        tmp = "[{name}]({link})"
        qname = x.__module__.replace(".", "")
        bname = x.__name__
        if "builtin" in qname:
            tmp = tmp.format(
                name=f"`__builtin__.{bname}`",
                link=f"{pynchon.URL_BUILTINS}#func-{bname}",
            )
        else:
            tmp = tmp.format(name=bname, link=f"#{qname}")
        bases.append(tmp)

    kls_code = inspect.getsource(kls._handle)
    kls_fname = inspect.getfile(kls._handle)
    kls._metadata = dict(
        bases=bases,
        code=kls_code,
        start=str(kls.lineno),
        end=str(kls.endlineno or ""),
        properties=properties,
    )

    kls._metadata.update(mccabe=util.complexity(kls_code, kls_fname))


def module(name, module, working_dir=None) -> None:
    """annotates a module"""
    LOGGER.debug(f"annotating module: {name}")
    module._metadata = dict(base_url=str(module.filepath.relative_to(working_dir)))


def should_skip(name: str):
    """ """
    from pynchon.config import pynchon as pynchon_config

    api_config = pynchon_config.get("api")
    should_skip = api_config.get("skip_private_methods", False)
    should_skip = should_skip and name.startswith("_")
    LOGGER.warning(
        f"annotation for `{name}` exits early; `pynchon.api.skip_private_methods` is set and this looks private"
    )
    return should_skip


def function(name, fxn) -> None:
    """annotates a function"""
    LOGGER.debug(f"annotating fxn: {name}")
    fxn._metadata = dict()
    if should_skip(name):
        return
    mod = importlib.import_module(fxn.parent.canonical_path)
    handle = getattr(mod, name)
    fxn._handle = getattr(mod, name)
    fxn_doc = fxn._handle.__doc__ or ""
    try:
        fxn_fname = inspect.getfile(fxn._handle)
    except (Exception,) as exc:
        fxn_fname = "?"
        fxn_code = None
    else:
        fxn_fname = os.path.relpath(fxn_fname)
        fxn_code = inspect.getsource(fxn._handle)
    try:
        fxn_sig = inspect.signature(fxn._handle)
    except (Exception,) as exc:
        fxn_sig = None
    fixme_lines = [
        i + fxn.lineno for i, l in enumerate(fxn_doc.split("\n")) if "FIXME" in l
    ]
    fxn._metadata = dict(
        name=name,
        doc=fxn_doc,
        signature=fxn_sig,
        # start=str(fxn._handle.__code__.co_firstlineno),
        annotation=str(fxn_sig and fxn_sig.return_annotation or "")
        .replace("<class '", "")
        .replace("'>", ""),
        fixme=[
            dict(
                glyph=" 🚩has FIXMEs ",
                link=f"/{fxn_fname}#L{fixme_lines[0]}",
                hover=f"on lines {fixme_lines}",
            )
        ]
        if fixme_lines
        else [],
    )
    fxn_code and fxn._metadata.update(mccabe=util.complexity(fxn_code, fxn_fname))
