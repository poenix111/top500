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
            print (p)
            date = p.split('/')
            year = date[2]
            mon = date[3]
            for num in pages:
                urlAux = self.urlBase + p
                params = {"page": str(num)}
                print(urlAux)
                response = requests.get(urlAux, params=params)
                soup = BeautifulSoup(response.text, 'html.parser')
                table = soup.find('table', {'class':"table table-condensed table-striped"})
                body = table.find_all('tr')
                saltar = False
                lista500Top = []                
               
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
                    "pais":pais,
                    "system": b[2].text,
                    "cores": b[3].text,
                    "rmax":b[4].text,
                    "rpeak": b[5].text,
                    "power":b[6].text,
                    'año' : year,
                    'mes' : mon
                    }
                    lista500Top.append(example)    
                    print(lista500Top)
                   
                    
                    
                
                
scrap = ScrapTop500()

scrap.getTables()
