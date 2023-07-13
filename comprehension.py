#list,set,dictionary comprehension
mylist=[]
for char in 'hello world':
    mylist.append(char)
#print(mylist)

#Using comprehension
#list
my_list2=[char for char in 'hello']
print(my_list2)
quick_list=[num for  num   in range(100)]
my_list3=[num*2 for  num   in range(100)]
my_list4=[num for  num   in range(100) if num%2==0]
#print(quick_list)
#print(my_list3)
#print(my_list4)

#set
my_list2={char for char in 'hello'}
#print(my_list2)
quick_list={num for  num   in range(100)}
my_list3={num*2 for  num   in range(100)}
my_list4={num for  num   in range(100) if num%2==0}
#print(quick_list)
#print(my_list3)
#print(my_list4)

#dictionary
simple_dict={
    'a':1,
    'b':2
}
my_dict={key:value**2 for key,value in simple_dict.items()}
my_dict2=my_dict={key:value**2 for key,value in simple_dict.items() if value%2==0}
my_dict3={num:num**2 for num in  [1,2,3] }
print(my_dict)
print(my_dict2)
print(my_dict3)











