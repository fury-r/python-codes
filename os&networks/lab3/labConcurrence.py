import os

import time
def os_Concurrent(a):
    d=os.fork()
    s,p=0,1
    for i in a:
        if d==0:
            s+=i
            print(f'sum {s}')
            time.sleep(1)
           
        elif d>1: 
            p*=i
            print(f'product {p}')
            time.sleep(1)
        print(f"Parent Calculated Product {p}\nChild Calculatef sum {s}")
    print(p,s)
a=input("Enter numbers ")
l=list(map(int,a.split(" ")))
os_Concurrent(l)