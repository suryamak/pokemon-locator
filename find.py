import requests
import sys
from bs4 import BeautifulSoup

from lookup import games, all_mons

def find(mon, gen, dex, version):
    url = "https://www.serebii.net/{}/{}{}".format(dex, str(all_mons[mon]).zfill(3) if gen < 8 else mon, '.shtml' if gen < 8 else '')
    r = requests.get(url, headers={'User-agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(r.text, 'html.parser')
    tr_filter = soup.find_all("tr")
    for tr in (tr_filter[::-1] if gen < 5 else tr_filter):
        version_tag = tr.find_all("td", {"class" : "{}".format(version)})
        if len(version_tag):
            for td in version_tag:
                location_tag = td.parent.find("td", {"class", "fooinfo"})
                if location_tag:
                    method = str(location_tag.contents[0]).strip()
                    return method

try:
    poke = sys.argv[1]
    version = sys.argv[2]

    method = find(poke.lower(), games[version][0], games[version][1], games[version][2])

    print()
    print(poke.upper())
    print('{}:  '.format(version), method)

except:
    print("Invalid command line arguments")