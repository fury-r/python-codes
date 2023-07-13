import operator
ops = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.truediv,  
    '%' : operator.mod,
    '^' : operator.xor,
}
def QuadraticProbing(arr,size,hash='k%mod'):
    table=[None]*10
    if 'm' in hash:
        hash[hash.index('m')]=size
    table_structure={}
    op=None
    for i in arr:
        location=2*i+3

        location%=10
        index=location

        if not table[location]:
            table[location]=i
        else:
            z=0
            x=0
            while table[index]!=None:
                if z>size:
                    z=0
                index=(location+(z*z))%size         
                z+=1
                x+=1
                if x==(10*2):
                    break
            if not table[index]:table[index]=i
        table_structure[i]={
            'key':i,
            'location':index
        }
    print(table)
def LinearProbing(arr,size,hash='k%mod'):
    table=[None]*10
    if 'm' in hash:
        hash[hash.index('m')]=size
    table_structure={}
    op=None
    for i in arr:
        location=2*i+3
        location%=10
        index=location

        if not table[location]:
            table[location]=i
        else:
            z=0
            x=0
            while table[index]!=None:
                if z>size:
                    z=0
                index=(location+(z))%size
                
                z+=1
                x+=1
                if x==(10*2):
                    break
            if not table[index]:table[index]=i          
        table_structure[i]={
            'key':i,
            'location':index
        }
    print(table)
QuadraticProbing([3,2,9,6,11,13,7,12],10,'2*k+3')
LinearProbing([3,2,9,6,11,13,7,12],10,'2*k+3')