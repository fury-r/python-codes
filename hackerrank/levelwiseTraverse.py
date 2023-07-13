def preorderTree(root,data,level):
    if root:
        data.append([root.info,level])
        
        preorderTree(root.left,data,level+1)
        preorderTree(root.right,data,level+1)
        return data

def levelOrder(root):
    data=preorderTree(root,[],1)
    #print(data,'ddddddddddddd')
    val=list(map(lambda item:str(item[0]),sorted(data,key=lambda item:item[1])))
    print(" ".join(val))
    return " ".join(val)