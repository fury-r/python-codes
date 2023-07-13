import sys,random

num1=int(sys.argv[1])
num2=int(sys.argv[2])
r=random.randint(num1, num2)
while True:
    a=int(input('guess a number between 1 to 10: '))
    if(num1<a<num2):
        if(a==r):
            print("You are a genius ")
            break
