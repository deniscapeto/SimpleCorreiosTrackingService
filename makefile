settings=scts.settings.scts_settings
export DJANGO_SETTINGS_MODULE=$(settings)
export PYTHONPATH=$(shell pwd)/src/

run:
	pipenv run gunicorn -b 0.0.0.0:8000 scts:app --worker-class aiohttp.GunicornUVLoopWebWorker --reload

check:
	isort src
	flake8 src

install:
	pip install pipenv
	pipenv install --dev

migrations:
	django-admin makemigrations

migrate:
	django-admin migrate

test:
	pipenv run pytest -s -x --cov=src --cov-config=setup.cfg --cov-report term-missing $(path)

release-patch:  ## Create a patch release
	@bumpversion patch
	git push --follow-tags

release-minor:  ## Create a minor release
	@bumpversion minor

release-major:  ## Create a major release
	@bumpversion major

coveralls:
	coverage run --source=src/scts --rcfile=setup.cfg -m pytest src
	coveralls --rcfile=setup.cfg

generate-docs:
	python docs/architecture_doc.py

docker-build:
	@docker rmi -f scts
	@docker build --tag scts .

docker-run: # Run in background
	@docker start scts || echo "No container found."  && echo "Running new container..."  && docker run -d --publish 8000:8000 --name scts scts && echo "Container created and running!"
