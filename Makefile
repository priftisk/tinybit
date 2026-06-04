.PHONY: run test

PYTHON := python

run:
	$(PYTHON) main.py

test:
	$(PYTHON) -m pytest ./tests -v

gen_csv:
	$(PYTHON) ./gen/gen_csv.py