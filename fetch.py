import requests
import json
import sys

try:
    poke = sys.argv[1]
    if len(sys.argv) > 2:
        game = sys.argv[2]
    else:
        game = None

    url = "https://pokeapi.co/api/v2/pokemon/{}/".format(poke)
    r = requests.get(url)
    print()
    print(r.json()['name'].upper())
    r = requests.get(url + 'encounters')
    for i in range(0, len(r.json())):
        for j in range(0, len(r.json()[i]['version_details'])):
            if not game or r.json()[i]['version_details'][j]['version']['name'] == game:
                print(r.json()[i]['version_details'][j]['version']['name'], r.json()[i]['version_details'][j]['encounter_details'][0]['method']['name'], r.json()[i]['location_area']['name'])
    print()
except:
    print("Invalid command line arguments")