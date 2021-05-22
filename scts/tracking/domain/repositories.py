
from abc import ABC, abstractmethod

from scts.tracking.domain.models import TrackingEvent


class TrackingEventRepository(ABC):

    @abstractmethod
    async def save(self, trackingEvent: TrackingEvent):
        pass
