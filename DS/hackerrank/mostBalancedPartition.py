def Balance(parent,files_size):
    diff=[]
    count=1
    for x in range(1,len(parent)):
        index=range(len(parent))
        ind=list(index)
        ind.remove(count)
        edge1 = [i for i in ind if parent[i]!=count]
        edge2 = [i for i in index if i not in edge1]
        print(edge1,edge2)
        filtered_list = list(filter(lambda i: parent[i] not in edge2, edge1 ))
        print(filtered_list,'filter')
        for i in edge1:
            if i not in filtered_list:
                edge2.append(i)
        print(edge1,edge2,'after')
        count+=1
        partiton1=[]
        for i in filtered_list:
           partiton1.append(files_size[i])
        partition2 =[]
        for j in edge2:
           partition2.append(files_size[j])
        
        diff.append(abs(sum(partiton1)-sum(partition2)))
    print(min(diff))
Balance([-1,0,1,2],[4,1,3,4])