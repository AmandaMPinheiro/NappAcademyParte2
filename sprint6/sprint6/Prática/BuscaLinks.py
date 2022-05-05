from bs4 import BeautifulSoup
from urllib import request
import requests
import mechanicalsoup

url = 'https://www.nappsolutions.com.br/'
# Primeira forma
data = request.urlopen(url).read().decode()
soup = BeautifulSoup(data, "html.parser")
print(soup.title)
soup.find_all('a')
lista_de_links = soup.find_all('a')

# Segunda forma
from bs4 import BeautifulSoup
import requests
url = 'https://www.nappsolutions.com.br/'
request1 = requests.get(url)
soup2 = BeautifulSoup(request1.text, "html.parser")
print(soup2.title)
lista_de_links = soup2.find_all('a')
status_list = []
for link in lista_de_links:
    try:
        r = requests.get(link['href'])
        status_list.append((r.status_code, link['href']))
    except:
        continue

# Terceira forma
browser = mechanicalsoup.StatefulBrowser()
browser.open(url)
print(browser.page.title)
lista_de_links = browser.page.find_all('a')

lista_links_encontrados = []

for link in lista_de_links:
    lista_links_encontrados.append(link.attrs.get('href',''))


lista = []
