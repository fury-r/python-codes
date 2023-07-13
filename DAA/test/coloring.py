
from re import I


def graphcolor(arr):
    color=['r','g','b']

    final=[]
    for i in range(0,2):
        c=i
        graph={i:None for i in arr.keys()}
        for k,v in arr.items():
            while True in [True if color[c]==graph[x] else False for  x in v]:
                c+=1
                if c>=len(color):c=0 
            graph[k]=color[c]
        final.append(graph)
    print(final)
arr={
    'A':['B','C','D'],
    'B':['C','A','D'],
    'C':["E","A",'B'],
    'D':['A','B','E'],
    'E':['C','D'],
}
graphcolor(arr)