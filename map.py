my_list=[1,2,3] #immutable
def multiply_by2(item):
    return item*3
print(list(map(multiply_by2,my_list)))
y=list(map(multiply_by2,my_list))
print(y)
print(my_list) #list is not changed