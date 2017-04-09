import requests, random, string, urllib, sys, copy
from Argument import Argument

#use the cookies
cookies = {"PHPSESSID":"ao3pmpu53mi5nh2fgrkbdffjd6", "security_level": "0"}

#First get the url
total_url = input("What is the url? ")

#Split it into the total url and the arguments
url, get_args = total_url.split("?")

#Get the valid request
valid_request = requests.get(url+"?"+get_args, cookies=cookies)

print(valid_request.text)

#Split it into each argument
arg_list = get_args.split("&")

arg_list = list(map(lambda x: Argument(x.split("=")[0], "=".join(x.split("=")[1:])), arg_list))

while True:
    #Randomly change characters of the args and try it
    new_args = copy.deepcopy(arg_list)
    for arg in new_args:
        arg.change()

    new_args = "&".join(list(map(str, new_args)))
    new_request = requests.get(url+"?"+new_args, cookies=cookies)

    #print(url+"?"+new_args, file=sys.stderr)

    if ((not new_request.ok) or "error" in new_request.text.lower()):
        print("Error on: " + url+"?"+new_args)
        #quit()
