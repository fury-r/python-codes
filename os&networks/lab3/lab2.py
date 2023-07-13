import os
def os_Concurrent(a):
    d=os.fork()
    s=p=0
    for i in a:
        if d==0:
            s+=i
            os.exit(0)
           
        elif d>1: p*=i
        print(f"Parent Calculated Product {p}\nChild Calculatef sum {s}")

a=input("Enter numbers ")
l=list(map(int,a.split(" ")))
os_Concurrent(l)