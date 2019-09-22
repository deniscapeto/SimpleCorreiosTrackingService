from aiohttp import web
from scts.tracking.http_client import CorreiosHttpClient
from scts.tracking.helpers import ExtractTrackingEvents
import json

class CorreiosTrackingView(web.View):

    async def get(self):

        tracking_code = self.request.match_info.get('tracking_code')

        resp = await CorreiosHttpClient().get_correios_tracking_events(tracking_code)

        trackingCodes = ExtractTrackingEvents(resp)

        return web.Response(text=json.dumps(trackingCodes),status=200)