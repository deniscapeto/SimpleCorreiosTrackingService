from bs4 import BeautifulSoup

from scts.tracking.domain.models import TrackingCode


def extract_tracking_events(html):
    parsed_html = BeautifulSoup(html, features="lxml")
    tables = parsed_html.find_all("table", {"class": "listEvent"})

    if len(tables) == 0:
        return {}

    events = []

    for tab in tables:
        rows = tab.find_all('tr')
        for row in rows:
            cols = row.find_all('td')
            cols = [ele.text.replace("&nbsp;", "").replace("\xa0", "").strip().split("\n") for ele in cols]
            events.append([ele for ele in cols if ele])  # Get rid of empty values

    tracking_codes = get_tracking_codes_from_list(events)

    store_tracking_code(tracking_codes)

    result = [tracking_code.as_dict() for tracking_code in tracking_codes]

    return result


def get_tracking_codes_from_list(events):
    trackingCodes = []

    for d in events:
        date = d[0][0].strip()
        time = d[0][1].strip()
        datetime = f'{date} {time}'
        location = d[0][2].strip()
        descricoes = d[1]

        general_description = ' '.join([" ".join(descricao.split()) for descricao in descricoes])

        trackingCode = TrackingCode(datetime, location, general_description)
        trackingCodes.append(trackingCode)

    return trackingCodes


def store_tracking_code(tracking_codes):
    for t in tracking_codes:
        t.save()
