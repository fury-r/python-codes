
def Linear(arr,size):
    result=[None]*size
    table={}
    
    for i in arr:
        location=0

        z=0
        index=(2*i+3)%size
        if result[index]==None:
            result[index]=i
        else:
            z=0
            x=0
            location=index
            while result[location]!=None:
                location=(location+z)%10
                z+=1
                x+=1
                if z>size:
                    z=0
                if x==size*2:
                    location=''
                    break
            result[location]=i
        table[i]={'index':location}
    print(table)
    print(result)
def Quadratic(arr,size):
    result=[None]*size
    table={}
    
    for i in arr:
        location=0

        z=0
        index=(2*i+3)%size
        if result[index]==None:
            result[index]=i
        else:
            z=0
            x=0
            location=index
            while result[location]!=None:
                location=(location+(z*z))%10
                z+=1
                x+=1
                if z>size:
                    z=0
                if x==size*2:
                    location=''
                    break
            result[location]=i
        table[i]={'index':location}
    print(table)
    print(result)
Quadratic([3,2,9,6,11,13,7,12],10)