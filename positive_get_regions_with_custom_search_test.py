import json
from endpoints.get_regions_with_custom_search_endpoint import getRegionsWithCustomSearch

res = getRegionsWithCustomSearch(q='новосибирск')
body = res.json()

assert res.status_code == 200
assert body['total'] == 22
assert body['items'][0]['id'] == 1

if (body['items'][0]['id'] == 1 and body['total'] == 22 and res.status_code == 200):
    print('Positive get regions with custom search succesfull')
else:
    print('Positive get regions with custom search failure')

res = getRegionsWithCustomSearch(q='казахстан')
body = res.json()

assert res.status_code == 200
assert body['total'] == 22

if (body['total'] == 22 and res.status_code == 200):
    print('Positive get regions with custom search succesfull')
else:
    print('Positive get regions with custom search failure')