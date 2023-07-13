class Superlist(list):
    def __init__(self, li):
        self.li=li
    def __getitem__(self,i):
        return self.li[i]
  
    def __len__(self):
        c=0
        for i in self.li:
           c=c+1 
        return c
    def p(self):
        return self.li

l=Superlist([1,2,3,4,5,6])
print(l.__len__())
l[3]
l.append(3)
l.append(2)
print(l.p())