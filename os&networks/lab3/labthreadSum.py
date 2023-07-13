
from threading import Thread
arr=[1,2,3]
p=[0]
def thread(arr):
    print('Inside thread')
    print(sum(arr))
    p[0]=sum(arr)
    return 0
def create_thread():
    print('Main')
    x=Thread(target=thread,args=(arr,))

    x.start()
    x.join()
    print(p[0])
create_thread()
