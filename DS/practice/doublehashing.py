def doublehashing(arr,size):
    result=[None]*size
    table={}
    flag=0

    for i in arr:
        index=(2*i+3)%size
        location=(3*i+1)%size
        if not  result[index]:
            result[index]=i
        else:
            l=index
            x=0
            z=0
            while result[l]!=None:
                l=(index+(location*x))%size
                x+=1
                z+=1
                if x>size:
                    x=0
                if z>=size*10:
                    flag=1
                    l=None
                    break
            if l:
                result[l]=i
                table[i]={
                    'key':i,
                    'index':l
                }
    if flag==1:print('hashing function is not good')
    print(['-' if not i else i for i in result])
doublehashing([3,2,9,6,11,13,7,12],10)