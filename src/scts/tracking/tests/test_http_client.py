from scts.tracking.http_client import CorreiosHttpClient

class TestCorreiosHttpClient:
    async def test_should_return_response_body_on_valid_tracking_code(
        self
    ):
        html = await CorreiosHttpClient().get_correios_tracking_events('PU524124388BR')