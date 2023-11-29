#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    response = requests.get("https://www.lamb-of-god.com/tour/")
    soup = BeautifulSoup(response.content, "html.parser")
    locs = soup.select('div')
    for loc in locs:
        print(loc)