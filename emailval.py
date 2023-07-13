import re

val=re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
while True:
    a=input("enter an email address ")

    z=val.search(a)
    if(z):
        print("valid")
        break
    else:
        print("invalid")