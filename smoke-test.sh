#!/usr/bin/env bash
set -xeuo pipefail
python -mpynchon.util.files --help
python -mpynchon.util.text --help
python -mpynchon.util.text.loadf --help
python -mpynchon.util.text loadf --help
python -mpynchon.util.text.render --help
python -mpynchon.util.text render --help
pynchon raw | jq .config_files
pynchon cfg
pynchon src cfg
pynchon src plan
pynchon jinja list
pynchon jinja plan
