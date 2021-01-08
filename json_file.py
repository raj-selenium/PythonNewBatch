"""
import requests


response = requests.get('http://api.zippopotam.us/us/90210')

print(response.text)
dict1 = response.json()


for key in dict1.keys():
    print(key, "--->", dict1.get(key))

for place in dict1.get("places"):
    for k in place:
        print(k,"-->",place[k])

"""

import json

with open("response.json") as f:
    dict1 = json.load(f)
    print(json.load.__doc__)
    print(dict1["places"][0]["place name"])

json_str = '{"places":["Chennai","Delhi","Mumbai"]}'

dict2 = json.loads(json_str)
print(dict2["places"][2])

with open("mydata.json", "w") as f:
    json.dump(dict2, f)