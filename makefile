settings=scts.settings.scts_settings
export DJANGO_SETTINGS_MODULE=$(settings)
export PYTHONPATH=$(shell pwd)/src/

run:
	gunicorn -b 0.0.0.0:8000 scts:app --worker-class aiohttp.GunicornUVLoopWebWorker --reload

install-dependencies:
	pip install -r requirements.txt

migrations:
	django-admin makemigrations

migrate:
	django-admin migrate