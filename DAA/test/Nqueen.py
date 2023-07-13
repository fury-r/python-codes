def isSafe(row,col,chess):
    x,y=row,col
    n=len(chess)
    #vertical check
    for i in range(n): 
        if chess[i][col]:
            return False
    while x>0 and y>0:
        x-=1
        y-=1
    #right diagonal
    while x<n and y<n:
        if chess[x][y]:
            return False
        x+=1
        y+=1
    x,y=row,col
    while x>0 and y<n:
        x-=1
        y+=1
    #left diagonal
    while x<n and y>0:
        if y<n and chess[x][y]:
            return False
        x+=1
        y-=1
    return True
def nqueen(n):
    chess=[[0 for i in range(n)] for i in range(n)]
    print(chess)
    row,col=0,0
    while row<n:
        if row<0:
            print(False)
            return 0
        if col<n:
            p=isSafe(row,col,chess)
            if p:
                chess[row][col]=1
                row+=1
                col=0
            else:
                col+=1
        if col>=n:
            print("Backtracking -1")
            row-=1
            if row>=0 and 1 in chess[row] :
                col=chess[row].index(1)
                chess[row][col]=0
                col+=1


    for i in chess:
        print(" ".join([str(j) for j in i]))
nqueen(3)