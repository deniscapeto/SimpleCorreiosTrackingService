from asgiref.sync import sync_to_async

from scts.tracking.adapters.correios.http_client import get_correios_tracking_events


async def get_tracking_events(tracking_code: str):

    tracking_events = await get_correios_tracking_events(tracking_code)

    await _save_tracking_events(tracking_events)

    result = [tracking_event.as_dict() for tracking_event in tracking_events]

    return result


@sync_to_async
def _save_tracking_events(tracking_events):
    for t in tracking_events:
        t.save()
