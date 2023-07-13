def graphrecoloring(graph):
    result=[]
    colors=['Red','Blue','Green']
    c=0
    for i in range(0,2):
        c=i
        graphcolor={i:None for i in graph.keys()}
        for k,v in graph.items():
            while True  in [ True for j in v if graphcolor[j]==colors[c]]:
                c+=1
            graphcolor[k]=colors[c]   
            c=0
        result.append(graphcolor) 
    print(result)
arr={
    'A':['B','C','D'],
    'B':['C','A','D'],
    'C':["E","A",'B'],
    'D':['A','B','E'],
    'E':['C','D'],
}
graphrecoloring(arr)  