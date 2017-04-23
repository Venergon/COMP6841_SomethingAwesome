import requests, random, string, urllib, sys, copy
from SeenLines import SeenLines
from Argument import Argument

#Ask if it should show unimportant changed lines
show_unimportant = input("Show unimportant changed lines? (y/n): ")
while show_unimportant not in ["y", "n"]:
    show_unimportant = input("Please enter either y or n: ")


if show_unimportant == "y":
    show_unimportant_flag = True
else:
    show_unimportant_flag = False

#Set up the list of seen lines
seen = SeenLines()

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

for line in valid_request.text.split("\n"):
    seen.add(line, arg_list)

while True:
    #Randomly change characters of the args and try it
    new_args = copy.deepcopy(arg_list)
    for arg in new_args:
        arg.change()

    new_args_str = "&".join(list(map(str, new_args)))
    new_request = requests.get(url+"?"+new_args_str, cookies=cookies)

    #print(url+"?"+new_args, file=sys.stderr)

    #if ((not new_request.ok) or "error" in new_request.text.lower()):
    #    print("Error on: " + url + "?" + new_args_str)
    #    #quit()
    #else:

    #Check if each line is new, if it is then print it out
    for line in new_request.text.split("\n"):
        if not seen.contains(line, new_args):
            new_args_str = "&".join(list(map(lambda x: x.unescape_str(), new_args)))
            if seen.show(line, new_args, show_unimportant_flag) is not None:
                print("<{}?{}>{}".format(url, new_args_str, seen.show(line, new_args, show_unimportant_flag)))
            seen.add(line, new_args)
