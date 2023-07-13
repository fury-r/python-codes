num1=int(input("enter first number "))
num2=int(input("enter second number "))
if(num1%num2==0):
    print("First number is divisble by  second "+str(num1/num2))
else:
    print(str(num1)+" is not divisble by "+str(num2)+ ": "+str(num1/num2))
if(num2%num1==0):
    print("Second number is divisble by  first "+str(num2/num1))
else:
    print(str(num1)+" is not divisble by "+str(num2)+ ": "+str(num1/num2))