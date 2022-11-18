import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.librenta.com/7t4013'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')


tit = soup.find_all('h2', class_='ui-search-item__title shops__item-title')
titulos = list()

contador = 0
for i in tit:
    if contador < 50:
        titulos.append(i.text)
    else:
        break
    contador += 1

urls = soup.find_all('a', class_='ui-search-item__group__element shops__items-group-details ui-search-link')
urls = [i.get('href') for i in urls]
contador = 0
for i in urls:
    if contador < 50:
        urls.append
    else:
        break
    contador += 1
#print(urls)

prec = soup.find_all('span', class_='price-tag-fraction')
precios = list()

contador = 0
for i in prec:
    if contador < 50:
        precios.append(i.text)
    else:
        break
    contador += 1
#print(precios)

df = pd.DataFrame({"títulos":titulos,"url":urls,"precios":precios},index=list(range(1,51)))
print(df)

df.to_csv('libros_de_novelas.csv')





