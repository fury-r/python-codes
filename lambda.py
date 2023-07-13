#lambda expressions
from functools import reduce #reduce you have to import using this
my_list=[1,2,4,5]
print(list(map(lambda item: item*2,my_list)))
print(list(filter(lambda item: item%2==0,my_list)))
print(reduce(lambda  acc,item: acc+item,my_list,0))

