
class Graph:
    def __init__(self,v):
        self.vertex=v
        self.edges=[]
    def add_edge(self,f,t,w):
        self.edges.append([f,t,w])
    def find(self, parent, i):
        print(parent,i,self.vertex[i])
        if parent[i] ==self.vertex[i]:
            return i
        
        return self.find(parent, parent[i])
    def apply_union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot]+=1
    def kruskal(self):
        result=[]
        i,j=0,0
        print(self.edges)
        self.edges=sorted(self.edges,key=lambda item:item[2])
        print(self.edges)
        parent,rank=[],[]
        for z in self.vertex:
            parent.append(z)
            rank.append(0)
        while j<len(self.vertex)-1:
            u,v,w=self.edges[i]
            i+=1
            x=self.find(parent,self.vertex.index(u))
            y=self.find(parent,self.vertex.index(v))
            print(x,y)
            if x!=y:
                j+=1
                result.append([u,v,w])
                self.apply_union(parent,rank,x,y)
        for u,v,w in result:
            print(u,v,w)
 
g = Graph(['A','B','C','D','E','F'])
#from,to,weight
g.add_edge('A', 'F', 7)
g.add_edge('A', 'C', 3)
g.add_edge('F', 'C', 8)
g.add_edge('A', 'B', 5)
g.add_edge('A', 'B', 10)
g.add_edge('B', 'C', 6)
g.add_edge('C', 'D', 3)
g.add_edge('E', 'D', 2)
g.add_edge('E', 'B', 4)
g.add_edge('D', 'B', 2)
# g = Graph([1,2,3,4,5,8])
# g.add_edge(3,3,5)
# g.add_edge(1,3,5)
# g.add_edge(3,4,12)
# g.add_edge(1,2,3)
# g.add_edge(2,4,4)
# g.add_edge(2,5,3)
# g.add_edge(2,5,2)
# g.add_edge(4,5,9)
# g.add_edge(5,8,1)
# g.add_edge(4,8,15)
# g.add_edge(4,8,8)

g.kruskal()