class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


l=[]
def search(root,mov):
    if mov==0:
        l.append(root.info)
        if root.left :search(root.left,0)
    elif  mov==1:
        l.append(root.info)
        if root.right:search(root.right,1)
    return 0
    
def topView(root):
    l.append(root.info)
    if root.left:search(root.left,0)
    if root.right:search(root.right,1)
    x=' '.join(map(str,l))
    print(x,l)
    
    
    


tree = BinarySearchTree()
t = input()

arr = list(map(int, t.split(' ')))
print(arr)
for i in arr:
    tree.create(i)

topView(tree.root)