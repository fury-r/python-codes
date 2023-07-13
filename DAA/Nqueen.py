def check(row,col,arr):
    z=col
    c=0
    while c<len(arr):
        if  arr[c][z]:
            return True
        c+=1
    x=row
    y=col
    c=0
    while x>0 and y>0:
        x-=1
        c=x
        y-=1       
    while y<len(arr) and c<len(arr):
        if   arr[c][y] :
            return True
        y+=1
        c+=1
    x=row
    y=col
    c=0  
    while x>0 and y<len(arr):
        x-=1
        c=x
        y+=1 
    while c<len(arr):
        if  y<len(arr) and arr[c][y] :
            return True
        y-=1
        if y<0:
            y=0
        c+=1 
def Nqueen(n):
    if n==2 or n==3:return False
    chess=[[ 0 for j in range(0,n)] for i in  range(0,n)]
    x,y=0,0
    while x<n:
        if y<n:    
            p= check(x,y,chess)
            
            if not p:
                chess[x][y]=1
                x+=1
                y=0
            else:
                y+=1
        if y>=n:
            x-=1
            y=chess[x].index(1)
            chess[x][y]=0
            y=y+1
    for i in chess:
        print(f"{i}")
print(Nqueen(int(input('N queen '))))
