from unittest.mock import AsyncMock

import inject
import pytest

from scts.tracking.application.services import GetTrackingEventsService


class TestGetTrackingEventsService:

    @pytest.fixture
    def mock_get_tracking_events(
        self,
        tracking_events_list,
    ):
        service = inject.instance(GetTrackingEventsService)
        service.get_correios_tracking_events = AsyncMock(
            return_value=tracking_events_list
        )

        yield service

    async def test_should_return_tracking_events_when_valid_code_is_provided(
        self,
        mock_get_tracking_events,
        tracking_code,
    ):
        service = inject.instance(GetTrackingEventsService)()
        repository = service.trackingEventRepository
        repository_count_before = len(repository.tracking_events)

        tracking_events = await service.get_tracking_events(tracking_code)

        assert len(tracking_events) == 5
        assert len(repository.tracking_events) == repository_count_before + 5
