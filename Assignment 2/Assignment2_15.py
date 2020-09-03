import re

pwd=input("Enter password for validation")

Flag=True
while Flag:
    if(len(pwd)<6 or len(pwd)>16):
        break
    elif not re.search("[a-z]",pwd):
        break
    elif not re.search("[A-Z]",pwd):
        break
    elif not re.search("[0-9]",pwd):
        break
    elif not re.search("[$#@]",pwd):
        break
    elif not re.search("\S",pwd):
        break
    else:
        print("Valid password")
        Flag=False
if Flag:
    print("NOt valid Password ")