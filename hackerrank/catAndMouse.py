def catAndMouse(x,y,z):
    a=b=0
    if(x>z): a=x-z
    else:a=z-x
    if(y>z):b=y-z
    else:b=z-y
    if(a<b):return 'Cat A'
    elif(b<a): return 'Cat B'
    else: return 'Mouse C'

print(catAndMouse(1,3,2))