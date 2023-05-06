#!/usr/bin/env bash
set -xeuo pipefail
python -mpynchon.util.text --help
python -mpynchon.util.text.loadf --help
python -mpynchon.util.text loadf --help
python -mpynchon.util.text.render --help
python -mpynchon.util.text render --help
pynchon raw | jq .config_files
pynchon cfg
# python -mpynchon.util.text.render jinja README.md.j2 --output /dev/null
pynchon jinja list
pynchon jinja plan
pynchon src plan
