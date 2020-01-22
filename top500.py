from bs4 import BeautifulSoup
import requests


class ScrapTop500:
    def __init__(self):
        self.url = "https://www.top500.org/lists/top500"
        self.urlBase = "https://www.top500.org"
        self.tableHeads = ["Rank", "Site", "System", "Cores", "Rmax (TFlop/s)", "Power(kW)"]

    def getTop(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.text, 'html.parser')
        squares = soup.find('ul', {"id": "squarelist"})
        links = squares.find_all('a')
        listaComparativas = []
        for ref in links:
            save = str(ref['href']).replace('lists','list')
            listaComparativas.append(save)

        # print(listaComparativas)
        return listaComparativas

    def getTables(self):
        pages = [1, 2, 3, 4, 5]
        listaComparativas = self.getTop()
        for p in listaComparativas:
            for num in pages:
                urlAux = self.urlBase + p
                params = {"page": str(num)}
                print(urlAux)
                response = requests.get(urlAux, params=params)
                soup = BeautifulSoup(response.text, 'html.parser')
                table = soup.find('table', {'class':"table table-condensed table-striped"})
                body = soup.find_all('tbody')
                print(table)
                exit()
                
scrap = ScrapTop500()

scrap.getTables()
