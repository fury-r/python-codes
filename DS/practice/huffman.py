class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class Huffman:
    def __init__(self):
        self.root=None
        self.code=''
    def insert(self,s):
        data=set(s)
        queue=[[s.count(i),i] for i in data]
        table={

        }
        queue.sort()
        temp=list(queue)
        print(queue,'ieee')
        for i in range(0,len(queue)):
            if len(queue)>=2:
                print(queue)
                a=queue.pop(0)
                b=queue.pop(0)
                c=0
                root=self.root
                if not root:
                    c=a[0]+b[0]

                    n=Node(c)
                    n.left=Node(a[1])
                    n.right=Node(b[1])
                    self.root=n
                else:
                    c=a+b[0]

                    n=Node(c)
                    n.right=Node(b[1])
                    n.left=self.root
                    self.root=n
                queue=[c]+queue
        bits=len(set(data))*8
        for i in temp:
            self.getNode(self.root,i[1],'')
            table[i[1]]={
                'freq':i[0],
                'code':self.code,
                'size':len(self.code)*i[0]
            }
            self.code=''
        for k,v in table.items():
            bits+=v['size']+v['freq']
        print(bits,table)
    def getNode(self,root,find,str):
            if root.data==find:
                self.code=str
            if root.right: self.getNode(root.right,find,str+'1')

            if root.left: self.getNode(root.left,find,str+'0')
T=Huffman()
T.insert('BCAADDDCCACACAC')

