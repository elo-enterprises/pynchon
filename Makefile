##
# Python project makefile.
##
.SHELL := bash
MAKEFLAGS += --warn-undefined-variables
# .SHELLFLAGS := -euo pipefail -c
.DEFAULT_GOAL := none

THIS_MAKEFILE := $(abspath $(firstword $(MAKEFILE_LIST)))
THIS_MAKEFILE := `python3 -c 'import os,sys;print(os.path.realpath(sys.argv[1]))' ${THIS_MAKEFILE}`
SRC_ROOT := $(shell dirname ${THIS_MAKEFILE})

NO_COLOR:=\033[0m
COLOR_GREEN=\033[92m

PYPI_PROJECT_NAME:=pynchon

.PHONY: build docs

init: py-init
build: py-build
clean: py-clean

py-init:
	# $(call _announce_target, $@)
	set -x \
	; pip install build \
	; pip install --quiet -e .[dev] \
	; pip install --quiet -e .[testing] \
	; pip install --quiet -e .[publish]

py-build: py-clean
	export version=`python setup.py --version` \
	&& (git tag $$version \
	|| printf 'WARNING: Failed to git-tag with release-tag (this is normal if tag already exists).\n' > /dev/stderr) \
	&& printf "# WARNING: file is maintained by automation\n\n__version__ = \"$${version}\"\n\n" \
	| tee src/${PYPI_PROJECT_NAME}/_version.py \
	&& python -m build

py-clean:
	rm -rf tmp.pypi* dist/* build/* \
	&& rm -rf src/*.egg-info/
	find . -name '*.tmp.*' -delete
	find . -name '*.pyc' -delete
	find . -name  __pycache__ -delete
	find . -type d -name .tox | xargs -n1 -I% bash -x -c "rm -rf %"
	rmdir build || true

version:
	@python setup.py --version

pypi-release:
	PYPI_RELEASE=1 make build \
	&& twine upload \
	--user $${PYPI_USER} \
	--password $${PYPI_TOKEN} \
	dist/*

release: clean normalize static-analysis test pypi-release

tox-%:
	tox -e ${*}

normalize: tox-normalize
lint: static-analysis
static-analysis: tox-static-analysis
test-units: utest
test-integrations: itest
smoke-test: stest
stest: tox-stest
itest: tox-itest
utest: tox-utest
dtest: tox-dtest
docs-test: dtest
test: test-units test-integrations smoke-test
iterate: clean normalize lint test
# coverage:
# 	echo NotImplementedYet

plan: docs-plan
plan-docs: docs-plan

docs-plan:
	@# Run from tox, not vice versa 
	pynchon src plan 
	pynchon docs plan
	pynchon python-api plan
	pynchon python-cli plan
docs: docs-apply
docs-apply:
	@# Run from tox, not vice versa 
	pynchon src apply
	pynchon docs apply
	pynchon python-api apply
	pynchon python-cli apply
apply: docs-apply
