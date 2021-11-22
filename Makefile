fmt:
	poetry run isort mc/ examples/
	poetry run black mc/ examples/

lint:
	poetry run flake8 mc/ examples/


mkdocs-deploy:
	poetry run mkdocs build
	poetry run mkdocs gh-deploy
