install:
	uv pip install

lint:
	uv run flake8 gendiff

check:
	uv run flake8 gendiff

test:
	uv run pytest

build:
	uv build

publish:
	uv publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

package-reinstall:
	python3 -m pip install --force-reinstall --user dist/*.whl