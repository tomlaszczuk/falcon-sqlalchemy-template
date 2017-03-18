falcon-sqlalchemy-template
==========================

Falcon project skeleton with working sqlalchemy connections, tests, linter, and migrations framework already set up.
Basically it's good entry point to develop every kind of sqlalchemy powered api using falcon.

## Prerequisites
Python 3.4 +

## Local usage
```
git clone https://github.com/tomlaszczuk/falcon-sqlalchemy-template.git
pip install -r dev/requirements.txt
gunicorn --reload api.wsgi:app
```
API will be exposed locally to http://127.0.0.1:8000

## Database
Provide SQLALCHEMY_DATABASE_URI and TEST_SQLALCHEMY_DATABASE_URI environment variables.

## Migrations
Project uses alembic to manage migrations script
http://alembic.zzzcomputing.com/en/latest/

### Example usage 
Add new migrations with
```
alembic revision --autogenerate -m "migration name"
```
Upgrade your database with
```
alembic upgrade head
```

## Tests
Put your tests into tests module.
Run your tests with
```
python runtests.py
```

To see test coverage
```
coverage run python runtests.py && coverage report -m
```
