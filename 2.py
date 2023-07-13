m=[]
n=[]
o=[]
for i in range(0,5):
    b=input('enter string '+str(i+1)+' ' )
    if(len(b)>=1 and len(b)<=4):
        m.append(b)
    elif(len(b)>=5 and len(b)<=7):
        n.append(b)
    elif(len(b)>=10):
        o.append(b)
    else:
        print("empty")
c=m[0]+n[0]
print('list1 '+str(m))
print('list2 '+str(n))
print('list3 '+str(o))
print("list 1 has"+str(len(m)))
print("list 2 has"+str(len(n)))
print("list 3 has"+str(len(o)))