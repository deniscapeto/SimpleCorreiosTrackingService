import inject

from scts.tracking.adapters.correios.http_client import get_correios_tracking_events
from scts.tracking.domain.repositories import TrackingEventRepository


class GetTrackingEventsService:

    @inject.autoparams('trackingEventRepository')
    def __init__(
        self,
        trackingEventRepository: TrackingEventRepository
    ) -> None:
        self.trackingEventRepository = trackingEventRepository()

    async def get_tracking_events(self, tracking_code: str):

        tracking_events = await get_correios_tracking_events(tracking_code)

        for tracking_event in tracking_events:
            await self.trackingEventRepository.save(tracking_event)

        result = [tracking_event.as_dict() for tracking_event in tracking_events]

        return result
