from bs4 import BeautifulSoup
import requests
import pandas as pd
url = 'https://vandal.elespanol.com/reportaje/random-las-30-peliculas-mas-taquilleras-de-la-historia-y-su-recaudacion'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

#Peliculas
peli = soup.find_all('h2', class_='titulo2')
print(peli)

peliculas = list()

contador = 0
for i in peli:
    if contador < 30:
        peliculas.append(i.text)
    else:
        break
    contador += 1
df = pd.DataFrame({'Ranking Peliculas mas taquilleras': peliculas}, index=list(range(1,31)))
print(df)




