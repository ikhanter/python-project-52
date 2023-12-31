.PHONY: install
install:
	@poetry install

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

.PHONY: test-coverage
test-coverage:
	@poetry run coverage run manage.py test && poetry run coverage report && poetry run coverage xml -o coverage.xml