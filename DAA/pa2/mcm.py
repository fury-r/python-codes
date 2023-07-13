import sys

def brackets(arr,k_table,main):
    print(arr)
    if len(arr)>2:
        bracket=arr.index("A"+str(k_table[main.index(arr[0])+1][main.index(arr[len(arr)-1])]))
        print(bracket,'bracket',"A"+str(k_table[main.index(arr[0])+1][main.index(arr[-1])]+1),arr[:bracket+1],arr[bracket+1:])
        new=[arr[:bracket+1],arr[bracket+1:]]
        print(new)
        if len(new[0])>1:
            new[0]=brackets(new[0],k_table,main)
        if len(new[1])>1:
            new[1]=brackets(new[1],k_table,main)
        return new
    else:
        return arr
def mcm(p):
    matrix={k+1:{v+1:0 for v in range(len(p)-1)} for k in range(len(p)-1)}
    k_table={k+1:{v+1:0 for v in range(len(p)-1)} for k in range(len(p)-1)}
    for i in range(1,len(p)):
        x,y=1,i+1
        while x<len(p)-1 and y<len(p):
            print(x,y)
            min_size=sys.maxsize
            min_index=None
            for k in range(x,y):
                e=matrix[x][k]+matrix[k+1][y]+(p[x-1]*p[k]*p[y])
                if e<min_size:
                    min_size=e
                    min_index=k
            matrix[x][y]=min_size
            k_table[x][y]=min_index
            x+=1
            y+=1
    data=['A'+str(i+1) for i in range(len(p)-1)]

    print(data)
    for k,v in k_table.items():
        print(k,v)
    print(brackets(data,k_table,data))

   
mcm([30,35,15,5,10,20,25])