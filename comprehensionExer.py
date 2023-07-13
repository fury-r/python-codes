#Exercise
my_list=['a','b','c','d','e','a','b','d']
my_list1=list(set([char for char in (my_list) if(my_list.count(char)>1)]))
print(my_list1)