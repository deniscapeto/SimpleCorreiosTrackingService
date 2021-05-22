import asyncio
import json
from unittest.mock import AsyncMock

import pytest

from scts.factory.build_app import build_app
from scts.tracking import Container
from scts.tracking.adapters.correios.exceptions import CorreiosException
from scts.tracking.application.services import GetTrackingEventsService


class TestCorreiosTrackingView():

    @pytest.fixture
    def client(self, aiohttp_client):
        loop = asyncio.get_event_loop()
        app = build_app()
        return loop.run_until_complete(aiohttp_client(app))

    @pytest.fixture
    def mock_get_tracking_events(self, tracking_events_list):
        service = Container.get(GetTrackingEventsService)
        service.get_tracking_events = AsyncMock(
            return_value=[tracking_event.as_dict() for tracking_event in tracking_events_list]
        )

        yield service.get_tracking_events

    async def test_should_return_200_when_tracking_code_is_valid(
        self,
        client,
        mock_get_tracking_events,
        tracking_events_dict,
        tracking_code
    ):
        resp = await client.get(f'/tracking/{tracking_code}')

        assert resp.status == 200
        response_text = await resp.text()

        assert json.loads(response_text) == tracking_events_dict

    async def test_should_return_200_when_correios_client_returned_error(
        self,
        client,
        mock_get_tracking_events,
        tracking_code
    ):

        mock_get_tracking_events.side_effect = CorreiosException

        resp = await client.get(f'/tracking/{tracking_code}')

        assert resp.status == 200
        assert '{"Error": ["No donuts from Correios now =[", "Correios is unavailable"]}' == await resp.text()

    async def test_should_return_500_when_correios_client_returned_unexpected(
        self,
        client,
        mock_get_tracking_events,
        tracking_code
    ):

        mock_get_tracking_events.side_effect = Exception

        resp = await client.get(f'/tracking/{tracking_code}')

        assert resp.status == 500
