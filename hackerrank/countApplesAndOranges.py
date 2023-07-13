def countApplesAndOranges(s,t,a,b,apples,oranges):
    l=[[a+i  for i in apples if a+i>=s  and a+i<=t],[b+i for i in oranges if b+i>=s  and b+i<=t]]
    print (l[0],l)
    print(l[1])
    return 0


print(countApplesAndOranges(7,10,4,12,[2,3,-4],[3,-2,-4]))