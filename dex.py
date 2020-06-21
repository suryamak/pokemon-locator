import requests
from bs4 import BeautifulSoup

def lookup():

    with open('mons.txt', 'wb') as mons:
        url = "https://www.serebii.net/pokemon/all.shtml"
        r = requests.get(url, headers={'User-agent': 'Mozilla/5.0'})
        soup = BeautifulSoup(r.text, 'html.parser')
        tr_filter = soup.find_all("tr")
        for i in range(2, len(tr_filter)):
            if i % 2 == 0:
                td_filter = tr_filter[i].find_all('td')
                mons.write(('"' + str(td_filter[3].next_element.next_element.next_element).strip().lower() + '" : ' + str(td_filter[0].next_element).strip().split('#')[1] + ',\n').encode('utf-8'))
                # print(str(td_filter[0].next_element).strip().split('#')[1], str(td_filter[3].next_element.next_element.next_element).strip())

lookup()