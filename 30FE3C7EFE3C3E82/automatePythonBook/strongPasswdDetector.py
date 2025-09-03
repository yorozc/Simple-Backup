#! python3
# strongPasswdDetector.py - Checks whether or not the password inserted is strong

import re

# check if  >=8 char, has both a-zA-Z, at least one \d

def passwordChecker(passwd):
    validPasswd = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$')
    passwdTest = validPasswd.search(passwd)

    if passwdTest is not None:
        return f"Valid password: {passwdTest.group()}"
    else: 
        return f"Not a valid password: {passwd}"



passwd1 = 'notValid'

print(passwordChecker(passwd1))

passwd2 = 'tesTing8'

print(passwordChecker(passwd2))