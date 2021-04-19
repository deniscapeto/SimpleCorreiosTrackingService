from asgiref.sync import sync_to_async

from scts.tracking.adapters.correios.http_client import get_correios_tracking_events


async def get_tracking_events(tracking_code: str):

    tracking_codes = await get_correios_tracking_events(tracking_code)

    await _save_tracking_code(tracking_codes)

    result = [tracking_code.as_dict() for tracking_code in tracking_codes]

    return result


@sync_to_async
def _save_tracking_code(tracking_codes):
    for t in tracking_codes:
        t.save()
