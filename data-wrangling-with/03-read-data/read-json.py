import json

filename = "../data/chp03/data-text.json"

json_data = open(filename).read()
data = json.loads(json_data)

for item in data:
    print(item)