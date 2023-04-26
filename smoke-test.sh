#!/usr/bin/env bash
set -euo pipefail
pynchon config-raw | jq .config_files
