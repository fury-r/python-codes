

class Node:
	
	def __init__(self):
		self.children = [None]*26
		self.isWordEnd = False

class Trie:
	
    def __init__(self):
        self.root = self.getNode()

    def getNode(self):
        return Node()

    def ascii(self,ch):
        print(ord(ch)-ord('a'),ch)
        return ord(ch)-ord('a')

    def insert(self,a):
        print(a)
        root = self.root
        length = len(a)
        for level in range(length):
            index = self.ascii(a[level])

            if not root.children[index]:
                root.children[index] = self.getNode()
            root = root.children[index]

        root.isWordEnd = True

    def search(self, a):
        root = self.root
        length = len(a)
        for level in range(length):
            index = self.ascii(a[level])
            if not root.children[index]:
                return False
            root = root.children[index]

        return root.isWordEnd


key = ["big",'bigger']


t = Trie()

for a in key:
	t.insert(a)

print(f'check The output {t.search("bigger")}')


