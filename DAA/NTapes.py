import math
def NTapes(data,n):
    increasing_order={k:v for k,v in  sorted(data.items(),key=lambda item:item[1])}
    tapes={
        i:[]
        for i in range (1,n+1)
    }
    main={ i:0
        for i in range (1,n+1)
    }
    c=1
    for k,v in increasing_order.items():
       if c>n:
           c=1
       tapes[c].append(v)
       c+=1
    c=1
    for k,v in tapes.items():
        s=0
        for  i in  range(0,len(v)+1):
            s=sum(v[:i])+s
 
        main[c]=s
        c+=1
    print(f'Tapes:{tapes}\nSum:{main}')
    main={ k:v for k,v in  sorted(main.items(),key=lambda item:item[1])}
    #print(f'Minimun {main[list(main)[0]]}')
    retrieval_time=sum([ v for k,v in main.items()])
    print(f'Total retrival time {retrieval_time}')
    divide= n if n>1 else len(increasing_order)
    print(f'MRT {retrieval_time/divide}')
 
    print(f'MRT rounded up {math.ceil(retrieval_time/divide)}')
 
# data={
#     'L1':10,
#     'L2':20,
#     'L3':45,
#     'L4':70,
#     'L5':1,
#     'L6':3,
#     'L7':7,
#     'L8':54,
#     'L9':23,
#     'L10':67,
 
# }
data={}
n=int(input('Number of tapes '))
l=int(input('Number of programs '))
for i in range(1,l+1):
    p=int(input(f'{i}: '))
    data[p]=p
 
NTapes(data,n)
