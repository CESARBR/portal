"""
Esse modulo recupera os convenios do Portal da Transparencia
"""
import json
import exceptions
import urllib3

def get_contracts(convenente):
    """  Para recuperar os convenios do Portal da CGU e necessario um parametro "pagina" (!?)
    Assim para recuperar todos os convenios, e necessario incrementar pagina ate nao retornar
    nenhum convenio. """

    http = urllib3.PoolManager()

    url = 'http://www.transparencia.gov.br/api-de-dados/convenios'


    fields = {
        'convenente': convenente,
    }

    pagina = 1

    convenios = []
    while True:
        fields['pagina'] = pagina
        response = http.request('GET', url, fields=fields)
        if response.status != 200:
            raise exceptions.RequestError(response.status)

        data = json.loads(response.data.decode('utf-8'))
        if data == []:
            break
        convenios += data
        pagina += 1
    return convenios
