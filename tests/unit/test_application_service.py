import pytest
from unittest.mock import patch

from scts.tracking.application.services import get_tracking_events

@pytest.fixture
def mock_get_tracking_events(tracking_codes_list):
    with patch(
        'scts.tracking.application.services.get_correios_tracking_events'
    ) as mock:
        mock.return_value = tracking_codes_list
        yield mock

async def test_should_return_tracking_codes_when_valid_code_is_provided(
    mock_get_tracking_events,
    tracking_code
):
    tracking_codes = await get_tracking_events(tracking_code)

    assert len(tracking_codes) == 5
