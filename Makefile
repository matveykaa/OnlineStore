PROJECT_NAME = onlineStore
MANAGE_PY = python3 manage.py

venv:
	source venv/bin/activate

install:
	pip3 install -r requirements.txt

freeze:
	pip3 freeze > requirement.txt

run:
	$(MANAGE_PY) runserver localhost:8000

superuser:
	$(MANAGE_PY) createsuperuser

migrate:
	$(MANAGE_PY) migrate

migrations:
	$(MANAGE_PY) makemigartions