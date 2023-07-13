from functools import reduce
def accumalator(acc,item):
    return acc+ item

my_list=[1,2,3,4,5,6,7]
print(reduce(accumalator,my_list,0))