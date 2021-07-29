import endpoints.base
import requests
import json
from urllib import request

def getRegionsByCountryCodeAndPage(country_code='ru', page=2):
    res = requests.get(endpoints.base.baseUrl + 'regions?country_code=' + country_code + '&page=' + page)
    return res
