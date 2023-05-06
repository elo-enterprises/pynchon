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

init:
	$(call _announce_target, $@)
	set -x \
	; pip install --quiet -e .[dev] \
	; pip install --quiet -e .[testing] \
	; pip install --quiet -e .[publish]

.PHONY: build
build: clean
	export version=`python setup.py --version` \
	&& (git tag $$version \
	|| printf 'WARNING: Failed to git-tag with release-tag (this is normal if tag already exists).\n' > /dev/stderr) \
	&& printf "# WARNING: file is maintained by automation\n\n__version__ = \"$${version}\"\n\n" \
	| tee src/${PYPI_PROJECT_NAME}/_version.py \
	&& python -m build

version:
	@python setup.py --version

clean:
	rm -rf tmp.pypi* dist/* build/* \
	&& rm -rf src/*.egg-info/
	find . -name '*.tmp.*' -delete
	find . -name '*.pyc' -delete
	find . -name  __pycache__ -delete
	find . -type d -name .tox | xargs -n1 -I% bash -x -c "rm -rf %"
	rmdir build || true

pypi-release: clean
	PYPI_RELEASE=1 make build \
	&& twine upload \
	--user elo-e \
	--password `secrets get /elo/pypi/elo-e` \
	dist/*

release: normalize static-analysis test docs pypi-release

tox-%:
	tox -e ${*}

normalize: tox-normalize
static-analysis: tox-static-analysis
test-units: test
test-integrations: itest
smoke-test: stest
itest: tox-itest
utest: tox-utest
stest: tox-stest
test: utest itest stest
# coverage:
# 	echo NotImplementedYet

plan: docs-plan
docs-plan:
	pynchon project plan | jq .

.PHONY: docs
docs:
	set -x \
	&& pynchon project plan \
	&& pynchon project apply \
	&& pynchon gen api toc --package ${PYPI_PROJECT_NAME} \
	&& pynchon gen cli toc \
	&& pynchon gen cli all
purge: clean pip-purge
pip-purge: python-require-pipenv
	@# Purges all dependencies from the currently active virtualenv
	set -x \
	&& pipenv uninstall --all --quiet
python-require-pipenv:
	@# Installs pipenv[0] if not present.
	@# This is sometimes useful even if the project doesn't use a Pipfile..
	@# see `python-pip-purge` target.
	pip freeze | grep pipenv \
	&& ( \
		printf '$(COLOR_GREEN)Detected pipenv is already present.$(NO_COLOR)\n' 1>&2 \
	) \
	|| ( \
		printf '$(COLOR_GREEN)Detected pipenv is missing. Installing it..$(NO_COLOR)\n' 1>&2 \
		&& pip install pipenv==2022.10.12 \
)
