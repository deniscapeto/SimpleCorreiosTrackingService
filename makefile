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

test:
	pytest -s

release-patch:  ## Create a patch release
	@bumpversion patch

release-minor:  ## Create a minor release
	@bumpversion minor

release-major:  ## Create a major release
	@bumpversion major
