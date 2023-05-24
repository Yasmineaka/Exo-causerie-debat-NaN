import requests

from bs4 import BeautifulSoup






n =requests.get('https://jumia.ci')
soup = BeautifulSoup(n.text, 'html.parser')
data = []
articles = soup.select('article.prd._fb.col.c-prd')
for article in articles:
    dico = {
        "image": article.select('img.img')[0].attrs['data-src'],
        "titre": article.select('h3.name')[0].text,
        "prix": article.select('div.prc')[0].text,
    }
    link = 'https://www.jumia.ci' + article.select('a.core') [0].attrs['href']
    
   

print(link)