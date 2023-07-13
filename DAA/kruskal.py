
class Graph:
    def __init__(self,vertices):
        self.v=vertices
        self.graph=[]
    def addEdge(self,u,v,w):
        self.graph.append([u,v,w])
    
    def find(self,parent,i):
        if parent[i]==self.v[i]:
            return i
        return self.find(parent,parent[i])
    def union(self,parent,rank,x,y):
        xroot=self.find(parent,x)
        yroot=self.find(parent,y)
        if rank[xroot]==rank[yroot]:
            parent[xroot]=yroot
        elif rank[xroot]>parent[yroot]:
            parent[yroot]=xroot
        else:
            parent[yroot]=xroot
            rank[xroot]+=1
    def kruskal(self):
        result=[]
        i=0
        e=0
        self.graph=sorted(self.graph,key=lambda item:item[2])

        parent=[i for i in self.v]
        rank=[0 for i in range(0,len(self.v))]
        while e<len(self.v)-1:
            u,v,w=self.graph[i]
            i+=1
            x=self.find(parent,self.v.index(u))
            y=self.find(parent,self.v.index(v))
            if x!=y:
                e+=1
                print(u,v,w)
                result.append([u,v,w])
                self.union(parent,rank,self.v.index(u),self.v.index(v))
        print("edges of mst")
        for u,v,w in result:
            print(f"{u}--->{v} weight {w}")
""" n=int(input('No of edges '))
g=Graph(input().split(" ")) """
g=Graph(['A','B','C','D','E','F'])
print(g.v)
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

g.kruskal()