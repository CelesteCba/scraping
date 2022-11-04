from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://argentina.as.com/resultados/futbol/argentina/clasificacion/'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

#Equipos
eq = soup.find_all('span', class_='nombre-equipo')
print(eq)

equipos = list()

contador = 0
for i in eq:
    if contador < 20:
        equipos.append(i.text)
    else:
        break
    contador += 1
#print(equipos, len(equipos))

#Puntaje
pt = soup.find_all('td', class_='destacado')
print(pt)

puntaje = list()

contador = 0
for i in pt:
    if contador < 20:
        puntaje.append(i.text)
    else:
        break
    contador += 1
#print(puntaje, len(puntaje))
df = pd.DataFrame({'Nombre': equipos, 'Puntos':puntaje},index=list(range(1,21)))
print(df)

