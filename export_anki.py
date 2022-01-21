import requests
import json 
import urllib.request
from urllib.error import URLError
from progress.bar import IncrementalBar


def request(action, **params):
    return {'action': action, 'params': params, 'version': 6}

def invoke(action, **params):
    requestJson = json.dumps(request(action, **params)).encode('utf-8')
    try:
        response = json.load(urllib.request.urlopen(urllib.request.Request('http://localhost:8765', requestJson)))

        if len(response) != 2:
            raise Exception('response has an unexpected number of fields')
        if 'error' not in response:
            raise Exception('response is missing required error field')
        if 'result' not in response:
            raise Exception('response is missing required result field')
        if response['error'] is not None:
            raise Exception(response['error'])
        return response['result']
    except URLError:
        print("ANKI NOT ONLINE !")


blacklist = ['API_TEST', 'Custom Study Session', 'Default']
decks = invoke('deckNames') 
for entry in blacklist:
    decks.remove(entry)
print("Exporting:")
print(decks)
path_to_packages = "C:/Users/paulb/git/DHBW_WI_Anki/"
API_base = {
    "action": "exportPackage",
    "version": 6,
    "params": {
        "deck": "Default",
        "path": "/data/Deck.apkg",
        "includeSched": False
    }
}
bar = IncrementalBar('Exporting Decks...', max=len(decks))
for deck in decks:
    API_base["params"]["deck"] = str(deck)
    API_base["params"]["path"] = path_to_packages +  str(deck) + ".apkg"
    result = invoke(API_base["action"],  **API_base["params"])
    bar.next()
bar.finish()
