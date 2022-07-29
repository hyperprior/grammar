.PHONY: test

test:
	poetry run tox -e python36,python37,py38,py39,python310
