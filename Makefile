.PHONY: %

APP = cat-facts
SLUG := $(subst -,_,${APP})
VERSION := $(shell python -c 'import toml; print(toml.load("pyproject.toml")["tool"]["poetry"]["version"])')

install:
	@poetry install

docker:
	docker build . --tag ${APP}:${VERSION}

clean:
	@rm -vrf ${SLUG}.egg-info venv

dev:
	@poetry run ${APP}

venv:
	@virtualenv venv
	@echo "# run:"
	@echo "source venv/bin/activate"

setup:
	@dephell deps convert

version: setup
	$(shell echo "__version__ = \"${VERSION}\"" > ${SLUG}/__init__.py)

version-patch:
	@poetry version patch
	@(make version)

version-minor:
	@poetry version minor
	@(make version)

version-major:
	@poetry version major
	@(make version)

publish:
	@poetry build
	@poetry publish