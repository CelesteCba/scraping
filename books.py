import requests
from bs4 import BeautifulSoup
import pandas as pd

print("Bienvenido a mi súper programa de scrapping")
print("Menu \n 1.Nombre de la Editorial \n 2.Rango de Precio \n 3.Filtrar una cantidad de registros \n 4.Salir")
print("Elija una opción:")
choice = int(input())
notFound = False
titulos = list()
precios = list()
editoriales = list()

if choice < 4:
    url = 'https://www.librenta.com/7t4013'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    valor1 = 0
    valor2 = 0
    cant = 0
    nombre = None

    if choice == 1 or choice == 2 or choice == 3:
        if choice == 1:
            print("Ingrese el nombre de la editorial:")
            nombre = input()
        elif choice == 2:
            print("Ingrese el precio mínimo:")
            valor1 = int(input())
            print("Ingrese el precio máximo:")
            valor2 = int(input())
        elif choice == 3:
            print("Ingrese la cantidad de registros:")
            cant = int(input())

        for book in soup.find_all("a", class_="ui-search-item__group__element shops__items-group-details ui-search-link")[: cant if cant > 0 else None]:
            price = book.parent.parent.find("div", class_="ui-search-price__second-line shops__price-second-line").find("span", class_="price-tag-fraction").getText(strip=True)
            pageBook = requests.get(book.get("href"))
            soupBook = BeautifulSoup(pageBook.content, 'lxml')
            for publish in soupBook.find_all("div", class_="ui-vip-core") if soupBook.find("div", class_="ui-pdp") is None else soupBook.find_all("div", class_="ui-pdp"):
                for feature in publish.find_all("td", class_="andes-table__column andes-table__column--left ui-pdp-specs__table__column")[3:4]:
                    if nombre is not None and feature.getText(strip=True) == nombre:
                        print(publish.find("h1", class_="ui-pdp-title").getText(strip=True))
                        print("$" + price)
                        print(feature.getText(strip=True))
                        titulos.append(publish.find("h1", class_="ui-pdp-title").getText(strip=True))
                        precios.append("$" + price)
                        editoriales.append(feature.getText(strip=True))
                    elif (valor1 != 0 or valor2 != 0) and (valor1 < int(str(price).replace(".", "")) < valor2):
                        print(publish.find("h1", class_="ui-pdp-title").getText(strip=True))
                        print("$" + price)
                        print(feature.getText(strip=True))
                        titulos.append(publish.find("h1", class_="ui-pdp-title").getText(strip=True))
                        precios.append("$" + price)
                        editoriales.append(feature.getText(strip=True))
                    elif cant > 0:
                        print(publish.find("h1", class_="ui-pdp-title").getText(strip=True))
                        print("$" + price)
                        print(feature.getText(strip=True))
                        titulos.append(publish.find("h1", class_="ui-pdp-title").getText(strip=True))
                        precios.append("$" + price)
                        editoriales.append(feature.getText(strip=True))
                    else:
                        notFound = True
    if notFound:
        print("No encontramos un resultado que se ajuste a su búsqueda.")
    else:
        df = pd.DataFrame({"Títulos": titulos, "Precios": precios, "Editoriales": editoriales}, index=list(range(1, len(titulos) + 1)))
        df.to_csv('libros.csv')

else:
    print("Muchas gracias por utilizar nuestro software.")