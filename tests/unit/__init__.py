"""
THIS IS A TEMPORARY SOLUTION, BEFORE IMPLEMENTING
THE USE OF A LIB TO INJECT DEPENDENCIES
"""

from scts.tracking import Container
from scts.tracking.application.services import GetTrackingEventsService
from scts.tracking.domain.repositories import TrackingEventRepository
from tests.unit.tracking.domain.fake_repositories import FakeTrackingEventRepository

container = Container

container.add(TrackingEventRepository, FakeTrackingEventRepository())
container.add(GetTrackingEventsService, GetTrackingEventsService(
        container.get(TrackingEventRepository)
    )
)
