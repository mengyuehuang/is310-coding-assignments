import apikey

with open('C:\\Users\\98768\\Desktop\\is310\\api-getting-data\\apikeys.txt', 'r') as file:
    first_line = file.readline().strip()

apikey.save("dpla_key", first_line)
dpla_api_key = apikey.load("dpla_key")
#print(dpla_api_key)


import requests
url = 'https://api.dp.la/v2/items?q=kittens&api_key='
response = requests.get(url + dpla_api_key)

#print(response.status_code)
#print(response.json())

dpla_data = response.json()


import json
with open('api-getting-data/data/dpla_kittens.json', 'w') as f:
    json.dump(dpla_data, f)

#print(dpla_data.keys())
    
#print('dataProvider', dpla_data['docs'][0]['dataProvider'])
#print('isShownAt', dpla_data['docs'][0]['isShownAt'])
#print('sourceResource', dpla_data['docs'][0]['sourceResource'])
    
print('object', dpla_data['docs'][0]['object'])


from dpla.api import DPLA
dpla = DPLA(first_line)

# Now make your search
response = dpla.search(q="kittens")
#print(response.items[0])