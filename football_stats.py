import urllib
from bs4 import BeautifulSoup

url = "https://www.cbssports.com/nfl/stats/playersort/nfl/year-2019-season-regular-category-touchdowns"
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page.read())


nfltable = soup.find_all("table", attrs={"class":"data"})[0]

nfltrs = nfltable.find_all('tr', attrs={"valign":"top"})

Ranking = 1
for tr in nfltrs:
    if Ranking <=20:
        i=0
        Player = None
        Position = None
        Team = None
        Touchdowns = None
        for td in tr:
            if i == 0:
                Player = td.get_text()
            if i == 1:
                Position= td.get_text()
            if i == 2:
                Team = td.get_text()
            if i == 6:
                Touchdowns = td.get_text()
            i= i+1
        print("Ranking: {}, Player Name: {}, Position: {}, Team: {}, Total Touchdowns: {}".format(Ranking, Player, Position, Team, Touchdowns))
    Ranking = Ranking + 1
