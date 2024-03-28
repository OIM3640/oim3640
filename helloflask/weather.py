import urllib.request
import json
from config import OPENWEATHERMAP_APIKEY


def get_temp(city):
    APIKEY = OPENWEATHERMAP_APIKEY
    country_code = "us"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city},{country_code}&APPID={APIKEY}&units=imperial"

    with urllib.request.urlopen(url) as f:
        response_text = f.read().decode("utf-8")
        response_data = json.loads(response_text)

    return response_data["main"]["temp"]
