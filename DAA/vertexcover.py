

from unittest import result
from cv2 import sort

def changeList(graph,cover):
    result=[]
    for i in graph:
        inner1=[i[0],[]]

        for j in i[1]:
            if j!=cover[-1]:
                inner1[1].append(j)
        result.append(inner1)
    return result
        
    
def vertexCover(graph):
    nodes=[i[0] for i in graph]
    cover=[]
    sorted_graph=sorted(graph,key=lambda item:len(item[1]),reverse=True)

    while len(nodes)>0 and len(cover)<len(graph) and len(sorted_graph)>0:
        cover.append(sorted_graph[0][0])
        nodes=[i for i in nodes if i not in sorted_graph[0][1]]
        sorted_graph.pop(0)
        graph1=list(filter(lambda item: len(item[1])!=0,changeList(sorted_graph,cover)))
        sorted_graph=sorted(graph1,key=lambda item:len(item[1]),reverse=True)
    print(cover)

graph=[
    ['A',['B','C']],
    ['B',['A','E']],
    ['C',['E','D','A']],
    ['D',['C','E','F','G']],
    ['E',['C','D','F']],
    ['F',['D','E']],
    ['G',['D']]

]

graph1=[
    ['A',['B']],
    ['B',['A']],
    ['C',['A','E']],
    ['D',['F','G']],
    ['E',['C','F']],
    ['F',['E','D']],
    ['G',['D']]

]
vertexCover(graph)