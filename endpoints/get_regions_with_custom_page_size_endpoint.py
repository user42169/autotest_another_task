import endpoints.base
import requests
import json
from urllib import request

def getRegionsWithCustomPageSize(country_code='ru', page_size=1):
    res = requests.get(endpoints.base.baseUrl + 'regions?country_code=' + country_code + '&page_size=' + page_size)
    return res