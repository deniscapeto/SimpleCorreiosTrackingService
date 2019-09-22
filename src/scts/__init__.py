from django import setup
setup()

from .factory.build_app import build_app
app = build_app()