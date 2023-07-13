import sys
g =  [[0,7,8,0,0,0],
[7,0,3,6,0,0],
[8,3,0,4,3,0,0],
[0,6,4,0,2,5],
[0,0,3,2,0,2],
[0,0,0,0,2,0]]
visited=[0 for i in g]
e=0
visited[0]=1
while e<len(g)-1:
    x,y=0,0
    min=sys.maxsize
    for i in range(len(g)):
        if visited[i]:
            for j in range(len(g)):
                if not visited[j] and g[i][j] and min>g[i][j]:
                    min=g[i][j]
                    x=i
                    y=j
    e+=1
    visited[y]=True
    print(chr(65+x),chr(65+y),min)