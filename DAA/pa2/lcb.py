def lcb(arr1,arr2):
    matrix=[[0 for j in range(len(arr2)+1)]  for i in range(len(arr1)+1)]
    for i in range(1,len(matrix)):
        for j in range(1,len(matrix[i])):
            print(i,j)
            if arr1[i-1]==arr2[j-1]:
                matrix[i][j]=matrix[i-1][j-1]+1
            elif arr1[i-1]!=arr2[j-1]:
                matrix[i][j]=max(matrix[i-1][j],matrix[i][j-1])
    f=''
    x,y=len(arr1)-1,len(arr2)-1
    while x>-1 and y>-1:
        if arr1[x]==arr2[y]:
            f+=arr1[x]
            x-=1
            y-=1
        else:
            p=[matrix[x][y-1],matrix[x-1][y]]
            if p[0]==p[1]:
                y-=1
            elif p[0]>p[1]:
                y=y-1
            else:
                x=x-1
        
    print(f[::-1])        
lcb(["A","B","C","B","D","A","B"],['B',"D","C","A","B","A"])