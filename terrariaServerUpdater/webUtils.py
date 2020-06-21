import requests
import re
from bs4 import BeautifulSoup


def check_for_update(url: str) -> (str, int):
    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')

    links = soup.findAll('a')

    server_href = None

    for link in links:
        if link.text == "PC Dedicated Server":
            server_href = link['href']

    if server_href is None:
        raise ValueError(
            "Cannot find link for PC Dedicated Server download. Website layout or url may have been changed.")

    version_number = re.search("(?<=terraria-server-)[0-9]*", server_href)

    return url + server_href, int(version_number.group())

def download_url(url, save_path, chunk_size=128):
    r = requests.get(url, stream=True)
    with open(save_path, 'wb') as fd:
        for chunk in r.iter_content(chunk_size=chunk_size):
            fd.write(chunk)