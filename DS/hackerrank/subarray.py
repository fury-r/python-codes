
def findSum(numbers, queries):
    print(numbers,queries)
    result=[]
    result=list(map(lambda i:sum(numbers[i[0]-1:i[1]])+((numbers[i[0]-1:i[1]].count(0))*i[2]),queries))      for i in queries:
      for i in queries:
        l=numbers[i[0]-1:i[1]]
        c=l.count(0)
        s=sum(l)+(i[2]*c)
        result.append(s)