import requests

url = 'https://ftp.debian.org/debian/tools/loadlin.txt'
response = requests.get(url)
response.raise_for_status() 
with open('teste.txt','wb') as f:
    f.write(response.content)


