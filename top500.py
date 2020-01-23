from bs4 import BeautifulSoup
from database import DbTop500
import requests


class ScrapTop500:
    def __init__(self):
        self.url = "https://www.top500.org/lists/top500"
        self.urlBase = "https://www.top500.org"
        self.tableHeads = ["Rank", "Site", "System",
                           "Cores", "Rmax (TFlop/s)", "Power(kW)"]

        self.db = DbTop500()
        self.db.create_database()

    def getTop(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.text, 'html.parser')
        squares = soup.find('ul', {"id": "squarelist"})
        links = squares.find_all('a')
        listaComparativas = []
        for ref in links:
            save = str(ref['href']).replace('lists', 'list')
            listaComparativas.append(save)

        # print(listaComparativas)
        return listaComparativas

    def getTables(self):
        pages = [1, 2, 3, 4, 5]
        listaComparativas = self.getTop()
        for p in listaComparativas:
            print(p)
            date = p.split('/')
            year = date[2]
            mon = date[3]
            for num in pages:
                urlAux = self.urlBase + p
                params = {"page": str(num)}
                print(urlAux)
                response = requests.get(urlAux, params=params)
                soup = BeautifulSoup(response.text, 'html.parser')
                table = soup.find(
                    'table', {'class': "table table-condensed table-striped"})
                body = table.find_all('tr')
                saltar = False
                # lista500Top = []

                for b in body:
                    if not saltar:
                        saltar = True
                        continue

                    b = b.find_all("td")

                    site = b[1].find('a').text
                    pais = b[1].text[len(site):]
                    print(pais)
                    example = {
                        "rank": b[0].text,
                        "site": site,
                        "pais": pais,
                        "system": b[2].text,
                        "cores": int(b[3].text.replace(',','')),
                        "rmax": float(b[4].text.replace(',','')),
                        "rpeak": float(b[5].text.replace(',','')),
                        "power": int(b[6].text.replace(',','')) if (b[6].text != '') else None,
                        'año': int(year),
                        'mes': int(mon)
                    }
                    self.db.insert(example)
                    #lista500Top.append(example)


if __name__ == '__main__':
    scrap = ScrapTop500()
    scrap.getTables()
