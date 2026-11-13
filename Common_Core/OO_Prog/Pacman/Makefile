VENV_PATH=mazeenv/bin/activate.fish
FILES = pac_man.py utils

run:
	python3 pac_man.py config.json

env:
	python3 -m venv mazeenv
	mazeenv/bin/pip install --upgrade pip
	mazeenv/bin/pip install pygame
	mazeenv/bin/pip install deps/mazegenerator-2.1.0-py3-none-any.whl
	@echo "Do \"source $(VENV_PATH)\" then make install and make run"

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	rm -rf build
	rm -rf dist
	find . -type d -name ".mypy_cache" -exec rm -rf {} +

.PHONY: lint lint-strict

lint:
	flake8 $(FILES)
	mypy --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs $(FILES)

lint-strict:
	flake8 $(FILES)
	mypy --strict --ignore-missing-imports $(FILES)
