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
    thefinalurl=resp["links"]["article_link"]
    print(thefinalurl)
    input("prese enter to access:")
    webbrowser.open(thefinalurl)
 
main()
