import time
import threading

def thread():
    print('Inside thread')
    for i in range(20,25):
        print(i)
        time.sleep(5)
def create_thread():
    x=threading.Thread(target=thread)
    x.start()
    print('Inside Main')
    for i in range(0,4):
        print(i)
        time.sleep(4)
create_thread()
