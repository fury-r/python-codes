import sys
def brackets(arr,k_table,main):
    if  len(arr)>2:
        bracket=arr.index("A"+str(k_table[main.index(arr[0])][main.index(arr[len(arr)-1])]))
        new=[arr[:bracket+1],arr[bracket+1:]]    
        if new!=arr and new[1]!=arr and new[0]!=arr:
            if(len(new[0])>1):
                new[0]=brackets(new[0],k_table,main)
            if len(new[1])>1: 
                new[1]=brackets(new[1],k_table,main)
            
        return new
    else:
        return arr

def mcm(arr):
    matrix=[[0 for j in range(len(arr)-1)] for i in range(len(arr)-1)]
    k_table=[[0 for j in range(len(arr)-1)] for i in range(len(arr)-1)]
    arr.append(arr.pop(0))
    for v in range(1,len(arr)):
        i,j=0,v
        while i<len(arr)-1 and j<len(arr)-1:
            min_val,min_index=sys.maxsize,0
            for k in range(i,j):
                m=matrix[i][k]+matrix[k+1][j]+(arr[i-1]*arr[k]*arr[j])
                if m<min_val:
                    min_index=k
                    min_val=m
            matrix[i][j]=min_val
            k_table[i][j]=min_index+1
            i+=1
            j+=1
    print("\n".join(["     ".join([str(j) for j in i]) for i in k_table[:len(arr)-2]]))
    print("\n".join(["     ".join([str(j) for j in i]) for i in matrix[:len(arr)-2]]))
    data= [ "A"+str(i+1) for i in range(len([arr.pop(-1)]+arr)-1)]
    print(brackets(data,k_table,data))

#mcm([40,20,30,10,30])
mcm([30,35,15,5,10,20,25])



import sys

def brackets(arr,k_table,main):
    print(main.index(arr[len(arr)-1]))
    if  len(arr)>2:
        bracket=arr.index("A"+str(k_table[main.index(arr[0])+1][main.index(arr[len(arr)-1])+1]))
        new=[arr[:bracket+1],arr[bracket+1:]]    
        if new!=arr and new[1]!=arr and new[0]!=arr:
            if(len(new[0])>1):
                new[0]=brackets(new[0],k_table,main)
            if len(new[1])>1: 
                new[1]=brackets(new[1],k_table,main)
            
        return new
    else:
        return arr
def mcm(p):
    matrix={k+1:{l+1:0 for l in range(0,len(p)-1)} for k in range(len(p)-1)}
    r={k+1:{l+1:0 for l in range(0,len(p)-1)} for k in range(len(p)-1)}

    for i in range(1,len(p)):
        x,y=1,i+1
        while x<len(p)-1 and y<len(p):
            min_index=0
            min_value=sys.maxsize

            for k in range(x,y):
                value=matrix[x][k]+matrix[k+1][y]+p[x-1]*p[k]*p[y]
                print(matrix[x][k],matrix[k+1][y],p[x-1],p[k],p[y],'for',x,y,value)
                if value<min_value:
                    min_value=value
                    min_index=k
            matrix[x][y]=min_value
            r[x][y]=min_index
    
            x+=1
            y+=1
    data= ["A"+str(i+1) for i in range(len(p)-1)]
    for k,v in r.items():
        print(v)
    print(brackets(data,r,data))

   
mcm([30,35,15,5,10,20,25])