import json

from aiohttp import web

from scts.tracking.helpers import extract_tracking_events
from scts.tracking.http_client import CorreiosHttpClient


class CorreiosTrackingView(web.View):

    async def get(self):

        tracking_code = self.request.match_info.get('tracking_code')

        resp = await CorreiosHttpClient().get_correios_tracking_events(tracking_code)

        trackingCodes = extract_tracking_events(resp)

        return web.Response(text=json.dumps(trackingCodes), status=200)
