import requests
from pprint import pprint
from dotenv import load_dotenv
import os


# # response = requests.get("https://oim.108122.xyz/words/random")

# # print(response.json())

# response = requests.get(
#     "https://oim.108122.xyz/mass",
#     headers={"X-Token": "zhizhi"},
# )
# data = response.json()

# # print(data['name'])       # 'Massachusetts'
# # print(data['governor'])   # 'Maura Healey'

# print(len(data))
# print(data.keys())

# towns = data["data"]
# print(type(towns))  # do this for explore the data structure

# # pprint(towns)
# # print(len(towns))
# pprint(towns[0])  # print the first town




# # POST: send a message (1-140 characters)
# requests.post('https://oim.108122.xyz/message',
#               json={'message': 'Hello from Zhi! I hope you enjoyed this API demo.'},
#               headers={'X-Token': 'zhizhi'})

# # GET: read all messages
# data = requests.get('https://oim.108122.xyz/messages').json()
# for msg in data:
#     print(msg)


load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")

url = (f'https://api.openweathermap.org/data/2.5/weather?q=Boston&appid={API_KEY}&units=imperial')

print(url)
data = requests.get(url).json()
print(f"Boston: {data['main']['temp']}°F")
# Can you modify the code to get weather information for any city? (Hint: you can use input() function to get user input)
