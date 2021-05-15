from aiohttp import web

from scts.tracking.web.routes import setup_routes


def build_app():

    app = web.Application()
    setup_routes(app)
    return app
