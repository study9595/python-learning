
.PHONY: check

check:
	python -m mypy src && python -m pytest
