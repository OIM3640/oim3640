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
print(data['number'])

# Can you print all the names?
# print(data['people'][0]['name'])

astronauts = data['people']  # this is a list
for astronaut in astronauts:
    name = astronaut['name']
    craft = astronaut['craft']
    print(f'{name} in {craft}')
