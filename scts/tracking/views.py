import json

from aiohttp import web

from scts.tracking.adapters.correios.exceptions import CorreiosException
from scts.tracking.adapters.correios.http_client import CorreiosHttpClient
from scts.tracking.helpers import extract_tracking_events


class CorreiosTrackingView(web.View):

    async def get(self):

        tracking_code = self.request.match_info.get('tracking_code')

        try:
            html_response = await CorreiosHttpClient().get_correios_tracking_events(tracking_code)

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

        trackingCodes = extract_tracking_events(html_response)

        return web.Response(text=json.dumps(trackingCodes), status=200)
