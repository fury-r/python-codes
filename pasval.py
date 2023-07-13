#atleast 8 char
#contain any letters,numbers, $%#@
import re

pattern=re.compile(r"([a-zA-z0-9]).([@$%#])")
while True:
    a=input("Enter  password ")

    if(len(a)>=8):
        p=pattern.search(a)
        if(p):
            print("successfull")
            break
        else:
            print("password should have a special character")
    else:
        print("password should be atleast 8 char long")


        