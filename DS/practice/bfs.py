def bfs(arr,root=None):
    visited,notvisted=[],{i[0] for i in arr}
    queue=[]
    root=  arr[0][0] if root==None else root 
    visited.append(root)
    queue.append(root)
    notvisted.remove(root)
    while len(notvisted)>0:
        if len(queue)==0:
            queue=visited
        l=queue.pop(0)
        for i in arr:
            if i[0]==l:
                for j in i[1]:
                    if j not in visited :
                        visited.append(j)
                        queue.append(j)
                        notvisted.remove(j)
    print(visited)
arr=[[0,[1,3]],[1,[0,2,3,5,6]],[2,[1,3,4,5]],[3,[0,1,2,4]],[4,[2,3,6]],[5,[1,2]],[6,[1,4]]]
bfs(arr)
            
