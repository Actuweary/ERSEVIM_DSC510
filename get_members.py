# Author Michael Ersevim - on behalf of First Church Glastonbury
# 9/07/2021
'''Purpose of code is to find the services for the current Sunday, find the people who signed up
for it, alphabetize it, save as a PDF and send it to the Ushers before the days' services
'''
from datetime import datetime

import requests, json

def ppl(): #this is the url for the people who signed up for a PARTICULAR service via SignUpGenius
    url_ppl = 'https://api.signupgenius.com/v2/k/signups/report' \
              '/filled/33061226/?user_key=a1pJUEl3RlhwUEtuYzI0U050aXAwQT09' #Needs f-string for signupID as variable 33061226
    json_file_ppl = requests.get(url_ppl)   #uses GET and assigns to var
    json_object_ppl = json.loads(json_file_ppl.text)  # JSON parser #
    print("Reort date:",datetime.today().strftime('%Y-%m-%d'))
    print("People attending:")
    #print(json_object_ppl)
    for j in range(len(json_object_ppl['data']["signup"])): #loop through everyone who signed up for that service
        print(json_object_ppl["data"]["signup"][j]["lastname"],", ",json_object_ppl["data"]["signup"][j]["firstname"]
          ," / ",json_object_ppl["data"]["signup"][j]["item"]," / Comment: ",json_object_ppl["data"]["signup"][j]["comment"],sep="")# / ID: ",
              #json_object_ppl["data"]["signup"][j]["slotitemid"],sep="")



def PrintTen(string): #makes date string look neat and comparable
    print (string[:10])

def find_services(): #this url lsts the services which have been posted that people can sign up for. Need the right date and ID(s) to use in the people list
    url_svc = 'https://api.signupgenius.com/v2/k/signups/created/all/?user_key=a1pJUEl3RlhwUEtuYzI0U050aXAwQT09'
    json_file_svc = requests.get(url_svc)   #uses GET and assigns to var
#    print(json_file_svc.status_code) # if <> "200", possibly send alert to me?
    json_object_svc = json.loads(json_file_svc.text)  # JSON parser
    print("Today's date:",datetime.today().strftime('%Y-%m-%d'))
    print("Services:")
    print("Date         ID#       Title")
    print("--------------------------------------------------------------------------------")

    #This "for j..." below gives the entire list of signup services of ALL types
    #for j in range(len(json_object_svc['data'])):
    #    print(json_object_svc["data"][j]["startdatestring"][:10],json_object_svc["data"][j]["signupid"],json_object_svc["data"][j]["title"],sep="  ")

    for j in range(len(json_object_svc['data'])):
        if(json_object_svc["data"][j]["startdatestring"][:10]) == '2021-12-12' and 'Worship' in (json_object_svc["data"][j]["title"]):
            print(json_object_svc["data"][j]["signupid"], json_object_svc["data"][j]["title"], sep="  ")
        else:
            pass

def main(): #the main input/response handler
    #ppl()
    find_services()
    #print_nicely()
    #send PDFs

if __name__ == "__main__": #good practice to use this setup
    main()