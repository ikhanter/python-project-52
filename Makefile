lint:
	poetry run flake8 .

dev:
	poetry run python3 manage.py runserver
