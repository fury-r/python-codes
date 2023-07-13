def finiteAutomata(graph,str):
    start=0
    for i in range(len(str)):
        start=graph[start][str[i]]
    if start==list(graph.keys())[-1]:
        print("Accept String")
    else:
        print("Reject string")

graph={
    0:{
        'a':1,'b':0,'c':0

    },
    1:{
        'a':2,'b':1,'c':1

    },
    2:{
        'a':1,'b':2,'c':2

    }
}

finiteAutomata(graph,'bcaabcaaabac')
#finiteAutomata(graph,'bcaabcaaabaca')