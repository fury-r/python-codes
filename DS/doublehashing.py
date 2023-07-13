def DoubleHashing(arr,size):
    table=[None]*10
    table_structure={}
    flag=0
    for i in arr:
        v,u=0,0
        u=((2*i)+3)%size
        index=u

        if not table[u]:
            table[u]=i
        else:
            z=0
            x=0
            v=((3*i)+1)%size
            while table[index]!=None:
                if z>size:
                    z=0
                index=(u+(v*z))%size         
                z+=1
                x+=1
                if x==(10*2):
                    flag=1
                    break
            if not table[index]:table[index]=i
        table_structure[i]={
            'key':i,
            'u':u,
            'v':v,
            'location':index
        }
    table=['-' if i==None  else i for i in table]
    print(f'Table:{table_structure}\n\nFinal Output:{table}')
    if flag:print('Hash Function is Not Proper')

DoubleHashing([3,2,9,6,11,13,7,12],10)