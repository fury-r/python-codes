def minEdit(s1,s2):
    s1="#"+s1
    s2="#"+s2
    matrix=[[0 for i in range(len(s2))] for i in range(len(s1))]
    for i in range(len(s2)):
        matrix[0][i]=i
    for i in range(len(s2)):
        matrix[i][0]=i        
    for i in range(1,len(s1)):
        for j in range(1,len(s2)):

            if s1[i]==s2[j]:
                matrix[i][j]=matrix[i-1][j-1]
            else:
                matrix[i][j]=min([matrix[i-1][j]+1,matrix[i][j-1]+1,matrix[i-1][j-1]+2])

    print(matrix[-1][-1])
    print(matrix) 
minEdit('intention','execution')