import aiohttp
from aiohttp.client_exceptions import ClientResponseError
from bs4 import BeautifulSoup

from scts.tracking.adapters.correios.exceptions import CorreiosException
from scts.tracking.domain.models import TrackingEvent


class CorreiosHttpClient:

    urlPrefix = 'https://www2.correios.com.br/sistemas/rastreamento/ctrl/ctrlRastreamento.cfm'
    acao = 'track'
    objetos = 'PU524124388BR'
    btnPesq = 'Buscar'

    async def get_tracking_events(self, tracking_code):
        async with aiohttp.ClientSession() as session:
            payload = f"acao=track&objetos={tracking_code}&btnPesq=Buscar"
            headers = {'Content-Type': 'application/x-www-form-urlencoded'}
            url = self.urlPrefix

            try:
                async with session.post(url, json=payload, headers=headers) as resp:
                    resp.raise_for_status()
                    print(resp.status)
                    return await resp.text()

            except ClientResponseError as exc:
                raise CorreiosException(exc)


async def get_correios_tracking_events(tracking_code):

    html_response = await CorreiosHttpClient().get_tracking_events(tracking_code)

    tracking_events = extract_tracking_events(html_response, tracking_code)

    return tracking_events


def extract_tracking_events(html, tracking_code):
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

    tracking_events = get_tracking_events_from_list(events, tracking_code)

    return tracking_events


def get_tracking_events_from_list(events, tracking_code):
    tracking_events = []

    for d in events:
        date = d[0][0].strip()
        time = d[0][1].strip()
        datetime = f'{date} {time}'
        location = d[0][2].strip()
        descricoes = d[1]

        general_description = ' '.join([" ".join(descricao.split()) for descricao in descricoes])

        tracking_event = TrackingEvent(tracking_code, datetime, location, general_description)
        tracking_events.append(tracking_event)

    return tracking_events
