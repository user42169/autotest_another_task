import json
from endpoints.get_regions_endpoint import getRegions

res = getRegions()
body = res.json()

assert res.status_code == 200
assert body['total'] == 22

if (body['total'] == 22 and res.status_code == 200):
    print('Positive get regions succesfull')
else:
    print('Positive get regions failure')