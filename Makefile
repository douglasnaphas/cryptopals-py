VENV := venv

all: help

help:
	@echo "try: help, venv, install, test, run, clean"

$(VENV)/bin/activate:
	python3 -m venv $(VENV)

install: requirements.txt venv
	. $(VENV)/bin activate; \
	./$(VENV)/bin/pip install -r requirements.txt

venv: $(VENV)/bin/activate

test: venv
	. $(VENV)/bin/activate; \
	pytest

run: venv
	./$(VENV)/bin/python3 app.py

clean:
	rm -rf $(VENV)
	find . -type f -name '*.pyc' -delete

.PHONY: all help install venv test run clean
