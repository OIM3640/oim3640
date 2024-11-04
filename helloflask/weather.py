import json
import os
import urllib.request
import pprint

from dotenv import load_dotenv

load_dotenv()
APIKEY = os.getenv("OPENWEAHTER_API_KEY")


def get_temp(city):
    city = city.replace(" ", "%20")
    country_code = "us"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city},{country_code}&APPID={APIKEY}&units=metric"

    # print(url)  # Open this URL in your browser to see the data

    with urllib.request.urlopen(url) as response:
        response_text = response.read().decode("utf-8")
        weather_data = json.loads(response_text)

    # pprint.pprint(weather_data)

    # How do we get current temperature?
    temp = weather_data["main"]["temp"]
    return temp


# get_weather("New York")
