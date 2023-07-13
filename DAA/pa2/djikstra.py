import sys


class Graph:
    def __init__(self,vertices):
      self.vertices=vertices
      self.n=len(vertices)
      self.graph=[]

    def printSolution(self,dist):
        for i in range(self.n):
            print(i,dist[i])
    
    def getMin(self,dist,spt):
        min=sys.maxsize
        for i in range(self.n):
            if dist[i]<min and spt[i]==False:
                min=dist[i]
                min_index=i
        return min_index
    
    def djikstra(self,source):
        dist=[sys.maxsize]*self.n
        spt=[False]*self.n
        dist[self.vertices.index(source)]=0

        for i in self.vertices:
            x=self.getMin(dist,spt)
            spt[x]=True

            for y in range(0,self.n):
                if self.graph[x][y]>0 and spt[y]==False and dist[y]>self.graph[x][y]+dist[x]:
                    dist[y]=dist[x]+self.graph[x][y]

        self.printSolution(dist)


g=Graph(["1",'2','3','4','5','6','7','8','9'])
g.graph= [[0, 4, 0, 0, 0, 0, 0, 8, 0],
		[4, 0, 8, 0, 0, 0, 0, 11, 0],
		[0, 8, 0, 7, 0, 4, 0, 0, 2],
		[0, 0, 7, 0, 9, 14, 0, 0, 0],
		[0, 0, 0, 9, 0, 10, 0, 0, 0],
		[0, 0, 4, 14, 10, 0, 2, 0, 0],
		[0, 0, 0, 0, 0, 2, 0, 1, 6],
		[8, 11, 0, 0, 0, 0, 1, 0, 7],
		[0, 0, 2, 0, 0, 0, 6, 7, 0]
		];
g.djikstra('1')