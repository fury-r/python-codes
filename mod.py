from collections import Counter,defaultdict,OrderedDict
import array,pdb #pdb is a debugger

l=[1,2,3,4,5,6,7]
print(Counter(l))
d=defaultdict(int,{'a':1,'ab':2})
print(d['b'])
d1=OrderedDict()
d1[1]=10
d1[2]=20

d2=OrderedDict()
d2[1]=10
d2[2]=20
print(d1==d2)

def add(num1,num2):
    pdb.set_trace()
    return num1+num2
print(add(2,3))