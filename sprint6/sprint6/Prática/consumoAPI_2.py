import requests
import json

# https://covid19-brazil-api-docs.vercel.app/

url = 'https://covid19-brazil-api.now.sh/api/report/v1'
r = requests.get(url)
casos_covid = r.json()
content = json.loads(r.content)


url = 'https://covid19-brazil-api.now.sh/api/report/v1/brazil/uf/sp'
r = requests.get(url)
dados_SP = r.json()

import requests
import json
url = 'https://covid19-brazil-api.now.sh/api/report/v1/brazil/20210820'
r = requests.get(url).json()
for item in r['data']:
    if item['uf'] == 'SP':
        print(item)

import requests
import json
url = 'https://covid19-brazil-api.now.sh/api/report/v1/countries'
consulta = requests.get(url).json()
resultado = []
for pais in consulta['data']:
    resultado.append((pais['country'], pais['confirmed']))