import json
from endpoints.get_regions_by_country_code_and_page_endpoint import getRegionsByCountryCodeAndPage

res = getRegionsByCountryCodeAndPage(country_code='ru', page='2')
body = res.json()

assert res.status_code == 200
assert body['total'] == 22

if (body['total'] == 22):
    print('Positive get regions with custom page size succesfull')
else:
    print('Positive get regions with custom page size failure')

res = getRegionsByCountryCodeAndPage(country_code='kz', page='1')
assert res.status_code == 200
body = res.json()
assert body['total'] == 22

if (body['total'] == 22 and res.status_code == 200):
    print('Positive get regions with custom page size succesfull')
else:
    print('Positive get regions with custom page size failure')