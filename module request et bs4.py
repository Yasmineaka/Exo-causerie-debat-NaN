import requests
from bs4 import BeautifulSoup




requests.get('https://google.com')
#nom = requests.get('https://google.com')


def requette(b):
    nombre = requests.get(b).text
    return nombre

nom = requette('https://google.com')
soup = BeautifulSoup(nom, 'html.parser')
#print(soup.prettify())
print(soup.title)