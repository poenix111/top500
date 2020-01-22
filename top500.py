from bs4 import BeautifulSoup
import requests


class ScrapTop500:
    def __init__(self):
        self.url = "https://www.top500.org/lists/top500/"


    def getTop(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.text, 'html.parser')
        print(soup)

scrap = ScrapTop500()

scrap.getTop()

        
        