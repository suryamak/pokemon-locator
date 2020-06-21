import requests
import sys
from bs4 import BeautifulSoup

try:
    num = sys.argv[1]
    if int(num) > 493:
        raise Exception()
    version = sys.argv[2]

    poke = ''
    method = ''

    url = "https://www.serebii.net/pokedex-dp/{}.shtml".format(num)
    r = requests.get(url, headers={'User-agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(r.text, 'html.parser')
    # print(str(soup.find('title').next_element))
    poke = str(soup.find('title').next_element).split(num)[1].strip()
    tr_filter = soup.find_all("tr")
    for tr in tr_filter:
        version_tag = tr.find_all("td", {"class" : "{}".format(version)})
        if len(version_tag):
            for td in version_tag:
                location_tag = td.parent.find("td", {"class", "fooinfo"})
                if location_tag:
                    method = str(location_tag.contents[0]).strip()
                    break

    print()
    print(poke.upper())
    print('{}:  '.format(version), method)
    
except:
    print("Invalid command line arguments")