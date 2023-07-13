import os
import time
l=[1,2,3,4,5,6]
def con(l):
    s,p=0,1

    a=os.fork()

    for i in l:
        if a==0:
            s+=i
            print('sum ',s)
            time.sleep(1)
        elif a>1:
            p*=i
            print('product ',p )
            time.sleep(1)
    print(f'parent {p} child {s}')
con(l)
