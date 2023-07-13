import sys


class Graph():
    def __init__(self,vertices):
        self.vertex=vertices
        self.graph=[[0 for column in range(vertices)] for row  in range(vertices)]

    def  display(self,parent):
        for i in range(1,self.vertex):
            print(chr(65+parent[i]),chr(65+i),self.graph[i][parent[i]])
    def min_key(self,key,mst):
        min=sys.maxsize
        for v in range(self.vertex):
            if key[v]<min and mst[v]==False:
                min=key[v]
                min_index=v
        return min_index
    
    def prims(self):
        key=[sys.maxsize]*self.vertex
        parent=[None]*self.vertex
        key[0]=0
        mst=[False]*self.vertex
        parent[0]=-1
        for out in range(self.vertex):
            #print(parent,key,mst,parent)

            u=self.min_key(key,mst)
            mst[u]=True
            for v in range(self.vertex):
                if self.graph[u][v]>0 and mst[v] ==False and key[v]>self.graph[u][v]:
                    key[v]=self.graph[u][v]
                    parent[v]=u

        self.display(parent)

graph=Graph(6)
#adjacency matrix
graph.graph = [[0,7,8,0,0,0],
[7,0,3,6,0,0],
[8,3,0,4,3,0,0],
[0,6,4,0,2,5],
[0,0,3,2,0,2],
[0,0,0,0,2,0]]
 
graph.prims()
