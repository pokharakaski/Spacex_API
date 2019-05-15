#!/usr/bin/python



###
#This actually works
#call
#https://api.spacexdata.com/v3/launches/latest
#display mission name
#display launch date
#any other piece of info
#tell user user to press entero to access ...
#dealer's choice to opne one link provide by response
###




import requests
import pprint
import webbrowser


def main():
    theurl = r"https://api.spacexdata.com/v3/launches/latest"
    print(theurl)
    resp=requests.get(theurl)
    resp=resp.json()
    missionname = resp["mission_name"]
    launch_date_local=resp["launch_date_local"]
    print("mission name is:",missionname)
    print("launch_date_local:", launch_date_local)
    #pprint.pprint(resp)
    thefinalurl=resp["links"]["article_link"]
    print(thefinalurl)
    input("prese enter to access:")
    webbrowser.open(thefinalurl)
    #bookno = input("Which book are you searching on (1-5)?")
    #bookurl = "https://www.anapioficeandfire.com/api/books/" + bookno
    #print(bookurl)
    #resp = requests.get(bookurl)
    #  pprint.pprint(resp.json())
    #resp = resp.json()

    #with open(resp['name'] + ".txt", 'a') as gotbook:
     #   for character in resp['characters']:
      #      charprofile = requests.get(character)
       #     charprofile = charprofile.json()
        #    print(charprofile['name'])
         #   print(charprofile['name'], sep=' ', file=gotbook)

####
main()
