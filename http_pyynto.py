import urllib.request
import json


def search_indexes():
    with urllib.request.urlopen('https://raw.githubusercontent.com/theikkila/postinumerot/master/postcode_map_light.json') as response:
        data = response.read()

    zipcodes = json.loads(data)
    return zipcodes
