class Node:
    def __init__(self,data):
        self.right=None
        self.left=None
        self.data=data
class BST:
    def __init__(self):
        self.root=None
    def insert(self,root,data):
        if not self.root:
            self.root=Node(data)
            return self.root
        elif not root:
            return Node(data)
        elif data>root.data:
            root.right=self.insert(root.right,data)
        elif data<root.data:
            root.left=self.insert(root.left,data)
        return root
    def Preorder(self,root,pos):
        if root:
            print(root.data,pos)
            self.Preorder(root.left,'left')
            self.Preorder(root.right,'right')

    def Inorder(self,root,pos):
        if root:
            self.Inorder(root.left,'left')
            print(root.data,pos)
            self.Inorder(root.right,'right')
    def PostOrder(self,root,pos):
        if root:
            self.PostOrder(root.left,'left')
            self.PostOrder(root.right,'right')
            print(root.data,pos)
c=BST()
c.root=c.insert(c.root,2)
c.root=c.insert(c.root,1)
c.root=c.insert(c.root,3)
c.root=c.insert(c.root,4)
print('Preorder')
c.Preorder(c.root,'root')
print('Inorder')

c.Inorder(c.root,'root')
print('PostOrder')

c.PostOrder(c.root,'root')