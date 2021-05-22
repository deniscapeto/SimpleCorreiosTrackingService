from asgiref.sync import sync_to_async

from scts.tracking.domain.models import TrackingEvent
from scts.tracking.domain.repositories import TrackingEventRepository
from scts.tracking.infrastructure.data_models import TrackingEventModel


class DjangoTrackingEventRepository(TrackingEventRepository):

    @sync_to_async
    def save(self, trackingEvent: TrackingEvent):

        model = TrackingEventModel(
            code=trackingEvent.code,
            date=str(trackingEvent.date),
            location=trackingEvent.location,
            description=trackingEvent.location
        )

        model.save()
