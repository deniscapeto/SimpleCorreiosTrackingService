from aiohttp import web
from http_client import CorreiosHttpClient
from helpers import ExtractTrackingEvents
import json

class CorreiosTrackingView(web.View):

    async def get(self):
        resp = await CorreiosHttpClient().get_correios_tracking_events()

        trackingCodes = ExtractTrackingEvents(resp)

        result = [trackingCode.__dict__ for trackingCode in trackingCodes]

        return web.Response(text=json.dumps(result),status=200)