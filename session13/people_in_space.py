import urllib.request
import json
import pprint

url = "http://api.open-notify.org/astros.json"

with urllib.request.urlopen(url) as f:
    response_text = f.read().decode('utf-8')
    # print(response_text)
    # print(type(response_text))
    data = json.loads(response_text)
    # print(data)
    # print(type(data))
    pprint.pprint(data)

# Can you print number of people in the space?
# print(data['number'])

print(len(data['people'])) # because the value to key 'people' is a list

# Can you print all the names?
for astronaut in data['people']:
    print(astronaut['name']) # the type of astronaut is dict