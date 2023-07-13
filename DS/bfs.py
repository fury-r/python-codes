def bfs(arr,root):
    queue=[]
    root= arr[0][0] if not root else root
    nodes=[i[0] for i in arr]
    queue.append(root)
    visted=[root]
    notvisted=set(nodes)
    while True:
        if len(notvisted)==0:
            break
        elif len(queue)>0:
            a=queue.pop(0)
            if a not in queue:
                if a in notvisted:
                    notvisted.remove(a)
                for i in arr:
                    if i[0]==a:
                        for j in i[1]:
                            if j not in visted :
                                queue.append(j)
                                visted.append(j)
                                notvisted.remove(j)

        else:
            queue=list(visted)
    print(visted)
arr=[[0,[1,3]],[1,[0,2,3,5,6]],[2,[1,3,4,5]],[3,[0,1,2,4]],[4,[2,3,6]],[5,[1,2]],[6,[1,4]]]
bfs(arr,None)