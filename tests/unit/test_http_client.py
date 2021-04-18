import pytest
from aiohttp.client_exceptions import ClientResponseError
from aioresponses import aioresponses

from scts.tracking.exceptions import CorreiosException
from scts.tracking.http_client import CorreiosHttpClient


class TestCorreiosHttpClient():

    async def test_should_return_response_body_on_valid_tracking_code(
        self
    ):
        with aioresponses() as mock_aioresponse:

            url = 'https://www2.correios.com.br/sistemas/rastreamento/ctrl/ctrlRastreamento.cfm'

            mock_aioresponse.post(url, status=200)

            html = await CorreiosHttpClient().get_correios_tracking_events('PU524124388BR')

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

                await CorreiosHttpClient().get_correios_tracking_events('PU524124388BR')
