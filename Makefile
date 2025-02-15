install:
	poetry install
update:
	poetry update

fmt:
	poetry run black .
	poetry run isort .
	poetry run ruff .

run-test:
	poetry run text2pdf -o var/sample-txt.pdf sample/input.txt
	poetry run text2pdf -o var/sample-md.pdf sample/input.md --markdown

run-help:
	poetry run text2pdf --help
