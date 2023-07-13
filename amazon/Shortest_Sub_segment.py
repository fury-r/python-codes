import re
def Shortest_Sub_segment(p,k):
    l=[i for i in k if re.search(i,p,re.IGNORECASE)]
    print(l)
    a=p.split(' ')
    q=set(a)
    return q.intersection(l)
print(Shortest_Sub_segment('This is a test. This is a programming test. This is a programming test in any language.',['4','this','a','test','programming']))