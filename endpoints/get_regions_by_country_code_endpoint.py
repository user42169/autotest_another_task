import endpoints.base
import requests
import json
from urllib import request

def getRegionsByCountryCode(country_code='ru'):
    res = requests.get(endpoints.base.baseUrl + 'regions?country_code=' + country_code)
    print(res.text)
    return res
