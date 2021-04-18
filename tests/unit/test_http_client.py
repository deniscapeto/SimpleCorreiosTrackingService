from unittest.mock import patch
import pytest
from aiohttp.client_exceptions import ClientResponseError
from aioresponses import aioresponses

from scts.tracking.adapters.correios.exceptions import CorreiosException
from scts.tracking.adapters.correios.http_client import CorreiosHttpClient, get_correios_tracking_events


class TestCorreiosHttpClient():

    async def test_should_return_response_body_on_valid_tracking_code(
        self
    ):
        with aioresponses() as mock_aioresponse:

            url = 'https://www2.correios.com.br/sistemas/rastreamento/ctrl/ctrlRastreamento.cfm'

            mock_aioresponse.post(url, status=200)

            html = await CorreiosHttpClient().get_tracking_events('PU524124388BR')

            assert html is not None

    async def test_should_raise_correios_exception_when_client_response_error_returned(
        self
    ):
        with aioresponses() as mock_aioresponse:

            url = 'https://www2.correios.com.br/sistemas/rastreamento/ctrl/ctrlRastreamento.cfm'

            mock_aioresponse.post(
                url,
                status=503,
                exception=ClientResponseError('server is unable to handle the request', history=('', ''))
            )

            with pytest.raises(CorreiosException):

                await CorreiosHttpClient().get_tracking_events('PU524124388BR')

@pytest.fixture
def mock_extract_tracking_events(tracking_codes_list):
    with patch(
        'scts.tracking.adapters.correios.http_client.extract_tracking_events'
    ) as mock:
        mock.return_value = tracking_codes_list
        yield mock

@pytest.fixture
def mock_get_tracking_events(fake_html):
    with patch(
        'scts.tracking.adapters.correios.http_client.CorreiosHttpClient.get_tracking_events'
    ) as mock:
        mock.return_value = fake_html
        yield mock

async def test_should_return_valid_tracking_codes_when_given_valid_code(
    mock_get_tracking_events,
    mock_extract_tracking_events,
    tracking_code,
    tracking_codes_list
):

    events = await get_correios_tracking_events(tracking_code)

    assert events == tracking_codes_list
