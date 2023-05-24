import requests
from bs4 import BeautifulSoup

requests.get('https://immo-soluce.web.app/auth')

def requette(b):
    immo = requests.get(b).text
    return immo

immo = requette('https://immo-soluce.web.app/auth')
soup = BeautifulSoup(immo, 'html.parser')
print(soup.prettify())
print(soup.title)
print(soup.a)
print(soup.title.string)
print(soup.title.parent.name)
print(soup.p)
print(soup.get_text())


"""def liens():
    url = []
    numero_page = 1
    for i in range(1, 100):
        i = f"https://immo-soluce.web.app/auth={numero_page}"
        numero_page += 1
        url.append(i)
    print(url)"""


