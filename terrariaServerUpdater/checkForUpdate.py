import requests
import re
from bs4 import BeautifulSoup

URL = 'https://terraria.org/'


def checkForUpdate(url) -> (str, int):
    page = requests.get(url)

    # print(page.text)

    soup = BeautifulSoup(page.content, 'html.parser')

    links = soup.findAll('a')

    server_href = None

    for link in links:
        if link.text == "PC Dedicated Server":
            server_href = link['href']

    if server_href is None:
        print("Cannot find link for PC Dedicated Server. Website layout may have been changed.")
        return None

    versionNumber = re.search("(?<=terraria-server-)[0-9]*", server_href)

    return server_href, int(versionNumber.group())
