import json
from endpoints.get_regions_with_custom_page_size_endpoint import getRegionsWithCustomPageSize

res = getRegionsWithCustomPageSize(country_code='ru', page_size='2')
assert res.status_code == 200
body = res.json()
assert body['error']['message'] == 'Параметр \'page_size\' может быть одним из следующих значений: 5, 10, 15'

if (body['error']['message'] == 'Параметр \'page_size\' может быть одним из следующих значений: 5, 10, 15' and res.status_code == 200):
    print('Negative get regions with custom page size succesfull')
else:
    print('Negative get regions with custom page size failure')

res = getRegionsWithCustomPageSize(country_code='kz', page_size='16')
body = res.json()

assert res.status_code == 200
assert body['error']['message'] == 'Параметр \'page_size\' может быть одним из следующих значений: 5, 10, 15'

if (body['error']['message'] == 'Параметр \'page_size\' может быть одним из следующих значений: 5, 10, 15' and res.status_code == 200):
    print('Negative get regions with custom page size succesfull')
else:
    print('Negativve get regions with custom page size failure')