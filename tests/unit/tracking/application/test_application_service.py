from unittest.mock import patch

import inject

from scts.tracking.application.services import GetTrackingEventsService


class TestGetTrackingEventsService:

    async def test_should_return_tracking_events_when_valid_code_is_provided(
        self,
        tracking_events_list,
        tracking_code,
    ):
        service = inject.instance(GetTrackingEventsService)()
        repository = service.trackingEventRepository
        repository_count_before = len(repository.tracking_events)

        with patch(
            'scts.tracking.application.services.get_correios_tracking_events', return_value=tracking_events_list
        ):

            tracking_events = await service.get_tracking_events(tracking_code)

        assert len(tracking_events) == 5
        assert len(repository.tracking_events) == repository_count_before + 5
