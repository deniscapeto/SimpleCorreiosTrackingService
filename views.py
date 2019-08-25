from aiohttp import web
import json

class CorreiosTrackingView(web.View):

    async def get(self):
        trackingCode = self.request.match_info.get('trackingcode')
        response_obj = { 'status': 'success', 'tracking-code': trackingCode }
        return web.Response(text=json.dumps(response_obj),status=200)