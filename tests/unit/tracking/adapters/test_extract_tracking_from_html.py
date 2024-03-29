from scts.tracking.adapters.correios.http_client import extract_tracking_events


class Testextract_tracking_events:

    def test_should_return_list_with_valid_html(self, fake_html, tracking_code):
        tracking_event_list = extract_tracking_events(fake_html, tracking_code)
        assert len(tracking_event_list) == 5

    def test_should_return_list_with_invalid_html(self, fake_invalid_html, tracking_code):
        tracking_event_list = extract_tracking_events(fake_invalid_html, tracking_code)
        assert len(tracking_event_list) == 0
