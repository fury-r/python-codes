class Node:
    def __init__(self,data):
        self.data=''
        self.freq=data
        self.left=None
        self.right=None
class Huffman:
    def __init__(self):
        self.root=None
        self.code=''
    def encodeData(self,data,direct):
        main=set(data)
        queue=[[data.count(i),i] for  i in main]
        queue.sort()
        l=list(queue)
        original=len(data)*8
        for  i in range (0,len(queue)):
            if len(queue)>=2:
                a=queue.pop(0)
                b=queue.pop(0)
                if self.root==None:
                    z=a[0]+b[0]
                    if direct:
                        print(a,b)
                        self.root=Node(z)
                        self.root.left=Node(a[0])
                        self.root.left.data=a[1] 

                        self.root.right=Node(b[0])  
                        self.root.right.data=b[1]
                    else: 
                        self.root=Node(z)
                        self.root.left=Node(a[0])
                        self.root.left.data=a[1] 

                        self.root.right=Node(b[0])  
                        self.root.right.data=b[1]

                    queue=[z]+queue
                else:
                    z=a+b[0]
                    new_node=Node(z)
                    if direct:

                        new_node.left=self.root
                        new_node.right=Node(b[0])
                        new_node.right.data=b[1]
                    else:
                        new_node.right=self.root
                        new_node.left=Node(b[0])
                        new_node.left.data=b[1]
                    self.root=new_node
                    queue=[z]+queue

        d={}
        for i in l:
            a=self.getNode(self.root,i[1],'')
            d[i[1]]={
                    'freq':i[0],
                    'code':self.code,
                    'size':len(self.code)*i[0]
                }
                
        print(d)
        bits=0
        bits=len(main)*8
        for k,v in d.items():
            bits+=v['size']+v['freq']   
        print(f'Original Size  {original} bits.')     
  
        print(f'Size Reduced to {bits} bits.')     
    def show_data(self,root,pos):
        if root:
            print(f'{root.data} freq {root.freq}, location: {pos}')
            self.show_data(root.left,'left')
            self.show_data(root.right,'right')
    def getNode(self,root,find,str):
            if root.data==find:
                self.code=str
            if root.right: self.getNode(root.right,find,str+'1')

            if root.left: self.getNode(root.left,find,str+'0')

p=Huffman()
#right
#p.encodeData('BCAADDDCCACACAC',True)
#left
p.encodeData('BCAADDDCCACACAC',False)

p.show_data(p.root,'root')
