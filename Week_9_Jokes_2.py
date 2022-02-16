# DSC 510
# Week 9
# Programming Assignment Week 9.1
# Author Michael Ersevim
# 8/5/2021

'''Purpose of code is to use and API request to retreive Chuck Norris jokes for a user
and present it in a nice looking format, then ask if they'd like to see another one
'''


import json
import requests

url = "https://api.chucknorris.io/jokes/random"

json_file = requests.get(url, verify=False)
json_object = json.loads(json_file.text)

json_formated_str = json.dumps(json_object, indent=2)
print(json_formated_str)
