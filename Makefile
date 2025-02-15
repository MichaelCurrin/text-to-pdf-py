SHELL = /bin/bash
APP_DIR = text2pdf

all: install fmt types run-test

install:
	poetry install

update:
	poetry update

fmt-check:
	poetry run ruff format --check .

fmt:
	poetry run ruff format .
	poetry run ruff . --fix

types:
	poetry run mypy $(APP_DIR)


.txt:
	poetry run text2pdf -o var/sample-txt.pdf sample/input.txt
.md:
	poetry run text2pdf -o var/sample-md.pdf sample/input.md --markdown
.stdin:
	echo -e "# Hello World\n\nPDF generated from stdin" \
		| poetry run text2pdf -o var/sample-stdin.pdf --markdown

run-test: .text .md .std

run-help:
	poetry run text2pdf --help
