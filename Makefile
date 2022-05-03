.PHONY: test lint pretty plint

CODE = source
SRC = .
TEST = tests

test:
	pip install pytest
	PYTHONPATH=$(SRC) pytest --verbosity=2 --showlocals --strict-markers $(TEST)

lint:
	pip install flake8 mypy black
	flake8 --jobs 4 --statistics --show-source $(CODE) $(TEST)
	mypy $(CODE)
	black --target-version py36 --skip-string-normalization --line-length=119 --check $(CODE) $(TEST)

pretty:
	isort $(CODE) $(TEST)
	black --target-version py36 --skip-string-normalization --line-length=119 $(CODE) $(TEST)
	unify --in-place --recursive $(CODE) $(TEST)

plint: pretty lint
