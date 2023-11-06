### Hexlet tests and linter status:
[![Actions Status](https://github.com/ikhanter/python-project-52/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/ikhanter/python-project-52/actions)

### CI and CodeClimate
[![CI](https://github.com/ikhanter/python-project-52/actions/workflows/CI.yml/badge.svg)](https://github.com/ikhanter/python-project-52/actions/workflows/CI.yml)
[![Maintainability](https://api.codeclimate.com/v1/badges/9a396dd3b145c2d70354/maintainability)](https://codeclimate.com/github/ikhanter/python-project-52/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/9a396dd3b145c2d70354/test_coverage)](https://codeclimate.com/github/ikhanter/python-project-52/test_coverage)

Link: [https://task-manager-2wl4.onrender.com/](https://task-manager-2wl4.onrender.com/)

# About
Task Manager is the web-service for organizing tasks between registered users. Each task must have status, executor, and optionally labels (m2m). All content (statuses, labels) creates by users themselves and can be updated by creators. If status, label or user are linked with tasks, the are unavailable for deleting.

# System requirements
#### PL, Virtual Environment, DBMS
- Python ^3.10;
- Poetry ^1.6.1;
- PostgreSQL ^15.
#### Modules
- django ^4.2.5;
- python-dotenv ^1.0.0;
- gunicorn ^21.2.0;
- psycopg2-binary ^2.9.9;
- django-bootstrap5 ^23.3;
- django-filter ^23.3;
- rollbar ^0.16.3.
#### Linter and tests
- flake8 ^6.1.0;
- coverage ^7.3.2.

# Installing
The command below will install all dependencies and database template for correct work of the web-service locally or on a deploy.
```make build```

After installing file ".env" should be created in the root directory of the project. This file must contain environment variables:
- SECRET_KEY;
- DEBUG;
- DATABASE_URL;
- ACCESS_TOKEN (for error tracking with Rollbar).

On a deployment these variables should be defined on your deploy service.

# Dev mode with debug
```make dev```

#Launch web-service
```make start```
