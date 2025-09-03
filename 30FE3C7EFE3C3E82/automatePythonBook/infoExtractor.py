import pyperclip 
import sys #sys.argv
import re

# Get text off clipboard

text = str(pyperclip.paste())

# find phone numbers and email addresses

# emailRegex = re.compile(r'''(
# .*@[a-zA-z].[a-zA-z]                    
# )''', re.VERBOSE)

print(text)

print("++++++++++++++++++++++++++++++=")

#gets emails

emailRegex = re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z]+\.[a-zA-z]{2,}')
# breakdown: matching name to be any char or number
# after @: email service name can be within a-zA-Z range, put + to allow more than one character
# \. is used to escape the dot character
# after \.: domain name can be within a-zA-Z range but needs to have at least 2 characters


#gets phone numbers
phoneRegex = re.compile(r'''
    (\d{3}|\(\d{3}\))?              #area code ( 209 or (209) )
    (\s|-|\.)?                      #separator (" ", -, .)
    (\d{3})                         #first 3 digits
    (\s|-|\.)                       #separator
    (\d{4})                         #last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?  #extension
    ''', re.VERBOSE)

#everything is split into groups for easy grabbing

# for groups in phoneRegex.findall(text):
#     print(groups)
#     print(groups[0], groups[2], groups[4])

matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[0],groups[2], groups[4]])
    if groups[7] != '':
        phoneNum += ' x' + groups[7]
    matches.append(phoneNum)

for groups in emailRegex.findall(text):
    matches.append(groups)
    
#copy to clipboard

if (len(matches)> 0):
    # pyperclip.copy('\n'.join(matches))
    print("Copied to clipboard:")
    print('\n'.join(matches))
else:
    print("No phone numbers or email addresses found.")


