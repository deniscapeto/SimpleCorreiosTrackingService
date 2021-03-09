from django import setup

setup()

from src.scts.factory.build_app import build_app  # noqa

app = build_app()
