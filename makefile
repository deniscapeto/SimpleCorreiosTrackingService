settings=scts.settings.scts_settings
export DJANGO_SETTINGS_MODULE=$(settings)
export PYTHONPATH=$(shell pwd)/src/

run:
	gunicorn -b 0.0.0.0:8000 scts:app --worker-class aiohttp.GunicornUVLoopWebWorker --reload

check:
	isort src
	flake8 src

install:
	pip install -r requirements.txt

migrations:
	django-admin makemigrations

migrate:
	django-admin migrate

test:
	pytest -s -x --cov=src --cov-config=setup.cfg --cov-report term-missing $(path)

release-patch:  ## Create a patch release
	@bumpversion patch
	git push --follow-tags

release-minor:  ## Create a minor release
	@bumpversion minor

release-major:  ## Create a major release
	@bumpversion major
