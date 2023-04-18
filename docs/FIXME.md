
## FIXMES

* [src/pynchon/util/lme.py:28](#): `# FIXME: get this from some kind of global config`
* [src/pynchon/bin/gen.py:32](#): `formatters=dict(markdown=constants.T_FIXME),`
* [src/pynchon/bin/gen.py:38](#): `default="docs/FIXME.md",`
* [src/pynchon/bin/gen.py:47](#): `Generate FIXME.md files, aggregating references to all FIXME's in code-base`
* [src/pynchon/bin/gen.py:55](#): `cmd = invoke(f'grep --line-number -R FIXME {src_root}')`
* [src/pynchon/bin/project.py:45](#): `# FIXME: options.output_with_default('docs/VERSION.md'),`
* [src/pynchon/plugins/__init__.py:84](#): `plan += [f"pynchon gen fixme --output {config.pynchon.docs_root}/FIXME.md"]`
* [src/pynchon/plugins/__init__.py:112](#): `# # FIXME: do this substition everywhere!`
* [src/pynchon/constants.py:19](#): `T_FIXME = ENV.get_template("FIXME.md.j2")`
* [src/pynchon/annotate.py:45](#): `end="",  # FIXME`
* [src/pynchon/annotate.py:50](#): `fixme="FIXME" in fxn_doc,`
* [src/pynchon/annotate.py:123](#): `i + fxn.lineno for i, l in enumerate(fxn_doc.split("\n")) if "FIXME" in l`
* [src/pynchon/annotate.py:135](#): `glyph=" 🚩has FIXMEs ",`
* [src/pynchon/templates/toc.md.j2:14](#): `* [`{{module_name}}.{{name}}`]({{src_url}}): [index](#{{toc_link}}), [source]({{src_url}}), [tests](#FIXME)`
* [src/pynchon/templates/toc.md.j2:42](#): `* {%if e.fixme %}[🚩]({{e_url}} "has FIXMEs"){%endif%} [`{{e.name}}`]({{e_url}}) -> {{e.annotation}}`
* [src/pynchon/templates/api/classes.md.j2:24](#): `* {%if e.fixme %}[🚩]({{e_url}} "has FIXMEs"){%endif%} [`{{e.name}}`]({{e_url}}) -> {{e.annotation}}`
* [src/pynchon/templates/api/modules.md.j2:5](#): `* [`{{module_name}}.{{name}}`]({{src_url}}): [index](#{{toc_link}}), [source]({{src_url}}), [tests](#FIXME)`
* [src/pynchon/templates/FIXME.md.j2:3](#): `## FIXMES`

