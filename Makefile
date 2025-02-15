SHELL = /bin/bash
APP_DIR = text2pdf

all: install fmt types run-test

install:
	poetry install

update:
	poetry update

fmt:
	poetry run black .
	poetry run isort .
	poetry run ruff .

types:
	poetry run mypy $(APP_DIR)


run-test:
	poetry run text2pdf -o var/sample-txt.pdf sample/input.txt
	poetry run text2pdf -o var/sample-md.pdf sample/input.md --markdown
	echo -e "# Hello World\n\nPDF generated from stdin" \
		| poetry run text2pdf -o var/sample-stdin.pdf --markdown

run-help:
	poetry run text2pdf --help
