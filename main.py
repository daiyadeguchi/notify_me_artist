#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup

urls = {
    "lamb of god": "https://www.songkick.com/artists/127504-lamb-of-god/calendar",
    "julian lage": "https://www.songkick.com/artists/988278-julian-lage/calendar",
    "metallica": "https://www.songkick.com/artists/331163-metallica/calendar",
    "ffdp": "https://www.songkick.com/artists/577269-five-finger-death-punch/calendar",
    "slipknot": "https://www.songkick.com/artists/1012485-slipknot/calendar",
    "jason mraz": "https://www.songkick.com/artists/336656-jason-mraz/calendar",
    }

if __name__ == '__main__':
    result = {}
    for key in urls:
        response = requests.get(urls[key])
        soup = BeautifulSoup(response.content, "html.parser")
        locs = soup.select('.primary-detail')
				# TODO too much for loops
        for loc in locs:
            for japan in ["JPN", "Japan", "Tokyo"]:
                if(japan in str(loc)):
                    result = {key: True}

        print(result)
