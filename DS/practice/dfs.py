def dfs(arr,root=None):
    visited,notvisted=[],{i[0] for i in arr}
    stack=[]
    root=  arr[0][0] if root==None else root 

    visited.append(root)
    stack.append(root)
    notvisted.remove(root)
    while len(notvisted)>0:
        if len(stack)==0:
            stack=[i for i in visited]
        l=stack.pop(-1)
        for i in arr:
            if i[0]==l:
                c=0
                for j in i[1]:
                    if j not in visited and c==0:
                        visited.append(j)
                        stack.append(j)
                        notvisted.remove(j)
                        c+=1
    print(visited)
arr=[[0,[1,3]],[1,[0,2,3,5,6]],[2,[1,3,4,5]],[3,[0,1,2,4]],[4,[2,3,6]],[5,[1,2]],[6,[1,4]]]
dfs(arr)
            
