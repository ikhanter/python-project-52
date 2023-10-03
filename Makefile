include .env
export

lint:
	poetry run flake8 .

dev:
	poetry run python3 manage.py runserver

start:
	poetry run gunicorn task_manager.wsgi

migrate:
	poetry run python manage.py migrate