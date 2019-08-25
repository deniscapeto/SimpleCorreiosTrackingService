from aiohttp import web
from http_client import CorreiosHttpClient
import json

class CorreiosTrackingView(web.View):

    async def get(self):
        resp = await CorreiosHttpClient().get_correios_tracking_events()
        return web.Response(text=json.dumps(resp),status=200)