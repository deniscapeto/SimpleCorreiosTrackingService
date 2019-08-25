import aiohttp

class CorreiosHttpClient:

    urlPrefix = 'https://www2.correios.com.br/sistemas/rastreamento/ctrl/ctrlRastreamento.cfm'
    acao = 'track'
    objetos = 'AA100833276BR'
    btnPesq = 'Buscar'

    async def get_correios_tracking_events(self):
        async with aiohttp.ClientSession() as session:
            async with session.get(f'{self.urlPrefix}?acao={self.acao}&objetos={self.objetos}&btnPesq={self.btnPesq}') as resp:
                print(resp.status)
                return await resp.text()