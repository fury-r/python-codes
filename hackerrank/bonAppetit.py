def bonAppetit(bill,k,b):
    l=sum(bill[:k]+bill[k+1:])
    a=int(l/2)
    if(a>b):print(a-b) 
    elif(a<b):print( b-a)
    else: print('Bon Appetit')
    return 0 
print(bonAppetit([3,10,2,9],1,12))