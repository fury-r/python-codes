def runningMedian(a,o):
    new=[]
    median=[]
    for i in a:
        new.append(float(i))
        mid=len(new)//2
        new=sorted(new)
        if len(new)==1:
            print(new[0])
            median.append(new[0])
        elif(len(new)%2==1):
            print(new[mid])
            median.append(new[mid])
        elif (len(new)%2==0):
            print((new[mid]+new[mid-1])/2)
            median.append((new[mid]+new[mid-1])/2)
        #print(median[-1]==o[a.index(new[-1])])
    return median
f=open('./testcase/median.txt','r')
g=[ float(i)  for i in f.read().splitlines()]
f.close()
f=open("./testcase/medianOutput.txt",'r')
o=[ float(i)  for i in f.read().splitlines()]
f.close()
runningMedian(g,o)