from functools import reduce

#sqaure 
my_list=[1,2,3,4,5]
print(list(map(lambda item: item**2,my_list)))

#List_sorting

li=[(0,2),(4,3),(9,9),(10,-1)]
li.sort(key=lambda x:x[1])
print(li)
  for i in queries:
        l=numbers[i[0]-1:i[1]]
        c=l.count(0)
        s=sum(l)+(i[2]*c)
        result.append(s)