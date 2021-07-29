import json
from endpoints.get_regions_with_custom_page_size_endpoint import getRegionsWithCustomPageSize

res = getRegionsWithCustomPageSize(country_code='ru', page_size='5')
body = res.json()

assert res.status_code == 200
assert body['total'] == 22

if (body['total'] == 22):
    print('Positive get regions with custom page size succesfull')
else:
    print('Positive get regions with custom page size failure')
    print(body)

res = getRegionsWithCustomPageSize(country_code='kz', page_size='5')
body = res.json()

assert res.status_code == 200
assert body['total'] == 22

if (body['total'] == 22 and res.status_code == 200):
    print('Positive get regions with custom page size succesfull')
else:
    print('Positive get regions with custom page size failure')