class Graph:
    def __init__(self,vertices):
        self.vertices=vertices
        self.edges=[]
    def addEdge(self,u,v,w):
        self.edges.append([u,v,w])
    def find(self,parent,i):
        if parent[i]==self.vertices[i]:return i
        return self.find(parent,parent[i])
    def union(self,parent,rank,x,y):
        xroot=self.find(parent,self.vertices.index(x))
        yroot=self.find(parent,self.vertices.index(y))
        if rank[xroot]==rank[yroot]:
            parent[xroot]=yroot
        elif rank[xroot]>rank[yroot]:
            parent[yroot]=xroot
        else:
            parent[yroot]=xroot
            rank[xroot]+=1
    def solve(self):
        parent=[i for i in self.vertices]
        rank=[0]*len(self.vertices)
        self.edges=sorted(self.edges,key=lambda item:item[2])
        e,i=0,0
        result=[]
        while e<len(self.vertices)-1:
            u,v,w=self.edges[i]
            x=self.find(parent,self.vertices.index(u))
            y=self.find(parent,self.vertices.index(v))
            i+=1
            if x!=y:
                result.append([u,v,w])
                e+=1
                self.union(parent,rank,u,v)
        for i in result:
            print(i)
g=Graph(['A','B','C','D','E','F'])
""" for i in range(0,n):
    
    g.addEdge(input('Start '),input('END '),input("Weight ")) """
g.addEdge('A','F',7)
g.addEdge('A','C',3)
g.addEdge('F','C',8)
g.addEdge('A','B',5)
g.addEdge('A','B',10)
g.addEdge('C','B',6)
g.addEdge('C','D',3)
g.addEdge('B','D',2)
g.addEdge('B','E',4)
g.addEdge('D','E',2)
g.solve()