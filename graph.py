def adj(matrix):
    r,c=(len(matrix)),len(matrix[0])
    for  i in range(r):
        for j in range(c):
            print(matrix[i][j], end=' ')
        print()
a,b=map(int,input().split())
matrix=[[0]*a for i in  range(a)]
for i in range(b):
    c,a=map(str,input().split())
    print()
    c=ord(c)-ord('A')
    a=ord(a)-ord('A')
    matrix[c][a]=1
    print(matrix)
adj(matrix)