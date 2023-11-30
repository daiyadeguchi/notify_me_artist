#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    response = requests.get("https://www.songkick.com/artists/127504-lamb-of-god/calendar")
    soup = BeautifulSoup(response.content, "html.parser")
    locs = soup.select('.primary-detail')
    result = {}
    for loc in locs:
        for japan in ["JPN", "Japan", "Tokyo"]:
            if(japan in loc):
                result = {"LoG": True}

