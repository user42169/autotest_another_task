import json
from endpoints.get_regions_by_country_code_and_page_endpoint import getRegionsByCountryCodeAndPage

res = getRegionsByCountryCodeAndPage(country_code='en', page='2')
body = res.json()

assert res.status_code == 200
assert body['error']['message'] == 'Параметр \'country_code\' может быть одним из следующих значений: ru, kg, kz, cz'

if (body['error']['message'] == 'Параметр \'country_code\' может быть одним из следующих значений: ru, kg, kz, cz'):
    print('Negative get regions with custom page size succesfull')
else:
    print('Negative get regions with custom page size failure')