import requests
import xmltodict

cep = '13617028'

url = 'http://viacep.com.br/ws/' + cep + '/json/'
r = requests.get(url)
endereco_json = r.json()

url = 'http://viacep.com.br/ws/' + cep + '/xml/'
r = requests.get(url)
endereco_xmldata = xmltodict.parse(r.content)


url = 'http://viacep.com.br/ws/' + cep + '/piped/'
r = requests.get(url)

endereco_piped = r.content

logradouro = endereco_json['logradouro']
if 'Avenida' in logradouro:
    print('Endereço possui "Avenida"!')
else: 
    print('Endereço não possui "Avenida"!')