from threading import Thread

l=[0]
def thread(ar):
    l[0]=sum(ar)
    return l[0]

a=input('')
a=list(map(int,a.split(' ')))
p=Thread(target=thread,args=(a,))
z=0
p.start()
p.join()
print(l[0])