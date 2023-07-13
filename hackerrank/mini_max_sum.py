
def mini_max_sum(arr):
    l=[]
    for i in range(0,len(arr)):
        l1=list(arr)
        l1.pop(i)
        l+=[l1]
    l=[sum(i) for i in l]
    l.sort()
    return f"{l[0]} {l[-1]}" 
print(mini_max_sum([1,2,3,4,5]))