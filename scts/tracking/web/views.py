import json
import logging

import inject
from aiohttp import web
from aiohttp.web_request import Request

from scts.tracking.adapters.correios.exceptions import CorreiosException
from scts.tracking.application.services import GetTrackingEventsService

logger = logging.getLogger(__name__)


class CorreiosTrackingView(web.View):

    @inject.autoparams('service')
    def __init__(self, request: Request, service: GetTrackingEventsService) -> None:
        self.service = service()
        super().__init__(request)

    async def get(self):
        tracking_code = self.request.match_info.get('tracking_code')

        try:
            tracking_events = await self.service.get_tracking_events(tracking_code)

        except CorreiosException as exc:

            logger.error(exc)
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

        return web.Response(text=json.dumps(tracking_events), status=200)
