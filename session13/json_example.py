import urllib.request
import json
from config import OPENWEATHERMAP_APIKEY
import pprint

APIKEY = OPENWEATHERMAP_APIKEY
city = 'Wellesley'
country_code = 'us'
url = f'https://api.openweathermap.org/data/2.5/weather?q={city},{country_code}&APPID={APIKEY}&units=metric'

# print(url)

with urllib.request.urlopen(url) as f:
    response_text = f.read().decode('utf-8')
    # print(response_text)
    response_data = json.loads(response_text)

print(response_data)