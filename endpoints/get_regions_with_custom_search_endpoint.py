import endpoints.base
import requests
import json
from urllib import request

def getRegionsWithCustomSearch(q='rus'):
    res = requests.get(endpoints.base.baseUrl + 'regions?q=' + q)
    return res


