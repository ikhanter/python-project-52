.PHONY: install
install:
	@poetry install
	@poetry run python manage.py migrate

.PHONY: lint
lint:
	@poetry run flake8 .

.PHONY: dev
dev:
	@poetry run python3 manage.py runserver

.PHONY: start
start:
	@poetry run gunicorn task_manager.wsgi

.PHONY: migrate
migrate:
	@poetry run python manage.py migrate

.PHONY: build
build:
	./build.sh

.PHONY: test
test:
	@poetry run python manage.py test

.PHONY: shell
shell:
	@poetry run python manage.py shell
