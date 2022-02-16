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

from requests.packages.urllib3.exceptions import InsecureRequestWarning #suppresses the HTTPS warnings
requests.packages.urllib3.disable_warnings(InsecureRequestWarning) #suppresses the HTTPS warnings

print("Welcome to the great repository of random Chuck Norris jokes!") #initial

def get_joke(): #the JSON joke generator
    url = "https://api.chucknorris.io/jokes/random" #the API site
    json_file = requests.get(url, verify=False) #uses GET and assigns to var
    json_object = json.loads(json_file.text) #JSON parser
    json_formated_str = json.dumps(json_object, indent=2) #dump string file
    PYTHONWARNINGS = "ignore:Unverified HTTPS request" #keeps the https error quiet
    print("") #prints a blank line for a less cluttered look
    print(json_object["value"],"  Ha Ha Ha Ha!! ") #prints random joke, which has the key 'value' in the JSON object
    print("") #prints a blank line for a less cluttered look
    main() #calls the main for another potential joke request

def main(): #the main input/response handler
    ans = str(input("Enter a 'Y' to hear a Chuck Norris joke OR enter any other key to quit: ")) #asks for input
    if ans == 'Y' or ans == 'y': #either Y will get another joke
        get_joke() #calls the joke generator
    else:
        print("We hope you enjoyed these jokes!") #A departing message

if __name__ == "__main__": #good practice to use this setup
    main()