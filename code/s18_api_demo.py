import requests
from pprint import pprint


# response = requests.get("https://oim.108122.xyz/words/random")

# print(response.json())

response = requests.get(
    "https://oim.108122.xyz/mass",
    headers={"X-Token": "zhizhi"},
)
data = response.json()

# print(data['name'])       # 'Massachusetts'
# print(data['governor'])   # 'Maura Healey'

print(len(data))
print(data.keys())

towns = data["data"]
print(type(towns))  # do this for explore the data structure

# pprint(towns)
print(len(towns))
