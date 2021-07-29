import endpoints.base
import requests
import json
from urllib import request

def getRegions():
    res = requests.get(endpoints.base.baseUrl + 'regions')

    return res
