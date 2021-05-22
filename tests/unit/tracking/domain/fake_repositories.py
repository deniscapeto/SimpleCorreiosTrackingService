from asgiref.sync import sync_to_async

from scts.tracking.domain.models import TrackingEvent
from scts.tracking.domain.repositories import TrackingEventRepository


class FakeTrackingEventRepository(TrackingEventRepository):

    def __init__(self) -> None:
        self.tracking_events = []

    @sync_to_async
    def save(self, trackingEvent: TrackingEvent):
        self.tracking_events.append(
            {
                "code": trackingEvent.code,
                "date": trackingEvent.date,
                "description": trackingEvent.description,
                "location": trackingEvent.location,
            }
        )
