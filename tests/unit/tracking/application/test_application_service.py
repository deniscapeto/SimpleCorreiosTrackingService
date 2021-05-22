from unittest.mock import AsyncMock

import pytest

from scts.tracking import Container
from scts.tracking.application.services import GetTrackingEventsService
from scts.tracking.domain.repositories import TrackingEventRepository


@pytest.fixture
def mock_get_tracking_events(tracking_events_list):
    service = Container.get(GetTrackingEventsService)
    service.get_correios_tracking_events = AsyncMock(
        return_value=tracking_events_list
    )

    yield service


async def test_should_return_tracking_events_when_valid_code_is_provided(
    mock_get_tracking_events,
    tracking_code
):
    service = Container.get(GetTrackingEventsService)
    repository = Container.get(TrackingEventRepository)
    repository_count_before = len(repository.tracking_events)
    tracking_events = await service.get_tracking_events(tracking_code)

    assert len(tracking_events) == 5
    assert len(repository.tracking_events) == repository_count_before + 5
