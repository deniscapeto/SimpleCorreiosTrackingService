import aiohttp

class CorreiosHttpClient:

    urlPrefix = 'https://www2.correios.com.br/sistemas/rastreamento/ctrl/ctrlRastreamento.cfm'
    acao = 'track'
    objetos = 'PU524124388BR'
    btnPesq = 'Buscar'

    async def get_correios_tracking_events(self, tracking_code):
        async with aiohttp.ClientSession() as session:
            payload = f"acao=track&objetos={tracking_code}&btnPesq=Buscar"
            headers = { 'Content-Type': 'application/x-www-form-urlencoded' }
            url = self.urlPrefix
            async with session.post(url, json=payload, headers=headers) as resp:
                print(resp.status)
                return await resp.text()