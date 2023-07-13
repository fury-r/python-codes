def remove_edges(graph,cover):
    result=[]
    for i in graph:
        sub=[i[0],[]]
        for j in i[1]:
            if j not in cover:
                sub[1].append(j)
        if len(sub[1])>0:
            result.append(sub)
    return result

def vertexCover(graph):
    sorted_graph=sorted(graph,key=lambda item:len(item[1]),reverse=True)
    cover=[]
    while len(sorted_graph)>0:
        print(sorted_graph,cover)

        cover.append(sorted_graph[0][0])
        sorted_graph.pop(0)
        sorted_graph=sorted(remove_edges(sorted_graph,cover),key=lambda item:len(item[1]),reverse=True)
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