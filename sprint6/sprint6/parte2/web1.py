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
request1 = requests.get(url)
soup2 = BeautifulSoup(request1.text, "html.parser")
print(soup2.title)
lista_de_links = soup2.find_all('a')

# Terceira forma
browser = mechanicalsoup.StatefulBrowser()
browser.open(url)
print(browser.page.title)
lista_de_links = browser.page.find_all('a')


for link in lista_de_links:
    print(link.attrs.get('href',''))
