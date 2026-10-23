
.PHONY: check

check:
	python -m mypy src/main.py && python -m pytest
