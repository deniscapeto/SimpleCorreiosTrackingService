from aiohttp import web
from scts.tracking.http_client import CorreiosHttpClient
from scts.tracking.helpers import ExtractTrackingEvents
import json

class CorreiosTrackingView(web.View):

    async def get(self):
        resp = await CorreiosHttpClient().get_correios_tracking_events()

        trackingCodes = ExtractTrackingEvents(resp)

        return web.Response(text=json.dumps(trackingCodes),status=200)