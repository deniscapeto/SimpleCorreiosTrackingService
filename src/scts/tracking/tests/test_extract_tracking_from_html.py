from scts.tracking.helpers import extract_tracking_events


class Testextract_tracking_events:

    def test_should_return_list_with_valid_html(self, fake_html):
        tracking_code_list = extract_tracking_events(fake_html)
        assert len(tracking_code_list) == 5
