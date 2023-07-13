def dfs(arr,n):
    stack=[]
    root= arr[0][0] if not n else n
    nodes=[i[0] for i in arr]
    stack.append(root)
    notvisted=set()
    visited=set()
    l=[]
    visited.add(root)
    while len(visited)<len(arr):   
        if len(stack)>0:
            a=stack.pop(-1)
            if a not in stack:
                if a in notvisted  and a not in visited:
                    notvisted.remove(a)
                for i in arr:
                    if i[0]==a:
                        c=0
                        for j in i[1]:
                            if j not in visited:notvisted.add(j)
                            if j not in visited and c==0:
                                stack.append(j)
                                l.append(j)
                                visited.add(j)
                                c=1
                                notvisted.remove(j)
                            elif j not in visited and j not in  notvisted:
                                notvisted.add(j)
        else:
            stack=list(visited)
    print(l)
arr=[[0,[1,3]],[1,[0,2,3,5,6]],[2,[1,3,4,5]],[3,[0,1,2,4]],[4,[2,3,6]],[5,[1,2]],[6,[1,4]]]
dfs(arr,None)