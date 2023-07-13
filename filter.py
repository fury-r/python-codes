my_list=[1,2,3,4] #immutable
def check_even(item):
    return item%2==0

print(list(filter(check_even,my_list)))
print(my_list) #list is not changed