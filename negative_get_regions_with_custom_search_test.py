import json
from endpoints.get_regions_with_custom_search_endpoint import getRegionsWithCustomSearch

res = getRegionsWithCustomSearch(q='')

assert res.status_code == 500

if (res.status_code == 500):
    print('Negative get regions with custom page size succesfull')
else:
    print('Negativve get regions with custom page size failure')

res = getRegionsWithCustomSearch(q='a')
body = res.json()

assert res.status_code == 200
assert body['error']['message'] == 'Параметр \'q\' должен быть не менее 3 символов'

if (body['error']['message'] == 'Параметр \'q\' должен быть не менее 3 символов' and res.status_code == 200):
    print('Negative get regions with custom page size succesfull')
else:
    print('Negative get regions with custom page size failure')

res = getRegionsWithCustomSearch(q='a&country_code=r&page=1&page_size=5')
body = res.json()

assert res.status_code == 200
assert body['error']['message'] == 'Параметр \'q\' должен быть не менее 3 символов'

if (body['error']['message'] == 'Параметр \'q\' должен быть не менее 3 символов' and res.status_code == 200):
    print('Negative get regions with custom page size succesfull')
else:
    print('Negative get regions with custom page size failure')