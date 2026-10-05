VENV_PATH=mazeenv/bin/activate.fish

env:
	python3 -m venv mazeenv
	mazeenv/bin/pip install --upgrade pip
	mazeenv/bin/pip install minilibx-python python-xlib
	@echo "Do \"source $(VENV_PATH)\" then make install and make run"

run:
	python3 a_maze_ing.py arg.txt

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	rm -rf build
	rm -rf dist
	find . -type d -name ".mypy_cache" -exec rm -rf {} +

lint:
	flake8 a_maze_ing.py & mypy --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs  a_maze_ing.py
	flake8 src & mypy --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs  src
	flake8 utils & mypy --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs  utils

lint-strict:
	mypy a_maze_ing.py --strict --ignore-missing-imports & flake8 a_maze_ing.py
	mypy src --strict --ignore-missing-imports & flake8 src
	mypy utils --strict --ignore-missing-imports & flake8 utils

build:
	python3 -m pip install --upgrade build
	python3 -m build
