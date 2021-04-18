import json

from aiohttp import web

from scts.tracking.adapters.correios.exceptions import CorreiosException
from scts.tracking.application.services import get_tracking_events


class CorreiosTrackingView(web.View):

    async def get(self):

        tracking_code = self.request.match_info.get('tracking_code')

        try:
            trackingCodes = await get_tracking_events(tracking_code)

        except CorreiosException:
            error_body = json.dumps(
                {
                    'Error': [
                        'No donuts from Correios now =[',
                        'Correios is unavailable'
                    ]
                }
            )
            return web.Response(text=error_body, status=200)
        except Exception:
            return web.Response(status=500)

        return web.Response(text=json.dumps(trackingCodes), status=200)
