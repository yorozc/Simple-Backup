# Take a list of websites and separate the http and https
# take input from clipboard 
# separate into two lists and then write each list to a file

import re, pyperclip

# grab input from clipboard
websites = pyperclip.paste()
# print(websites)

# regex for http
links = re.compile(r'https?://\w.+')

# separate links
http = []
https = []
for link in links.findall(websites):
    if link[4] == "s":
        https.append(link)
    else:
        http.append(link)

print(http)
print("++++++++")
print(https)

print("+++++++++")

# put list of links into file

with open("httpVshttps.txt", "w") as f:
    f.write("=====http=====\n")
    for link in http:
        f.write(link+"\n")
        

with open("httpVshttps.txt", "a") as f:
    f.write("====https====\n")
    for link in https:
        f.write(link+"\n")


