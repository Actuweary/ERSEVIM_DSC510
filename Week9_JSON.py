# DSC 510
# Week 9
# Programming Assignment Week 9.1
# Author Michael Ersevim
# 8/5/2021

'''Purpose of code is to use and API request to retreive Chuck Norris jokes for a user
and present it in a nice looking format, then ask if they'd like to see another one
'''

import requests
import json
r = requests.get('https://api.chucknorris.io/jokes/random')
json.loads(r.data.decode('utf-8'))


#headers = {'cache-control': 'no-cache'}
#response = requests.request("GET", url, verify=False)  # , headers=headers)
#js = json.loads(response)
#print(json.dumps(response, indent=2))

#print(response.text)