import requests, random, string, urllib, sys

#use the cookies
cookies = {"PHPSESSID":"ao3pmpu53mi5nh2fgrkbdffjd6", "security_level": "0"}

#First get the url
total_url = input("What is the url? ")

#Split it into the total url and the arguments
url, get_args = total_url.split("?")

#Get the valid request
valid_request = requests.get(url+"?"+get_args, cookies=cookies)

print(valid_request.text)

while True:
    #Randomly change characters of the args and try it
    new_args = list(get_args)
    new_args[random.randint(0, len(new_args)-1)] = urllib.parse.quote(random.choice(string.punctuation))

    new_args = "".join(new_args)
    new_request = requests.get(url+"?"+new_args, cookies=cookies)

    if ((not new_request.ok) or "error" in new_request.text.lower()):
        print("Error on: " + url+"?"+new_args)
        #quit()
        #print(url+"?"+new_args, file=sys.stderr)
