import sys
def Prims(graph,vertices):
    edges=0
    visited=[0 for i in graph]
    visited[0]=1
    while (edges<vertices-1):
        min=sys.maxsize
        x,y=0,0
        for i in range(vertices):
            if visited[i]:
                con=graph[i]
                for j in range(vertices): 
                    if not visited[j] and con[j] and min>con[j]:
                        min=con[j]
                        x,y=i,j
        print(f"{chr(65+x)}-{chr(65+y)}-{min}")
        edges+=1   
        visited[y]=True    
          
graph = [[0,7,8,0,0,0],
[7,0,3,6,0,0],
[8,3,0,4,3,0,0],
[0,6,4,0,2,5],
[0,0,3,2,0,2],
[0,0,0,0,2,0]]
 
Prims(graph,len(graph))