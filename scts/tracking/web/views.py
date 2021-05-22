import json
import logging

from aiohttp import web

from scts.tracking import Container
from scts.tracking.adapters.correios.exceptions import CorreiosException
from scts.tracking.application.services import GetTrackingEventsService

logger = logging.getLogger(__name__)


class CorreiosTrackingView(web.View):

    async def get(self):

        tracking_code = self.request.match_info.get('tracking_code')

        try:
            service = Container.get(GetTrackingEventsService)
            tracking_events = await service.get_tracking_events(tracking_code)

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
