##
# Python project makefile.
##
.SHELL := bash
# .SHELLFLAGS := -euo pipefail -c
MAKEFLAGS += --warn-undefined-variables
.DEFAULT_GOAL := none

THIS_MAKEFILE := $(abspath $(firstword $(MAKEFILE_LIST)))
THIS_MAKEFILE := `python3 -c 'import os,sys;print(os.path.realpath(sys.argv[1]))' ${THIS_MAKEFILE}`
SRC_ROOT := $(shell dirname ${THIS_MAKEFILE})
