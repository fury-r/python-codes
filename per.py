from time import time

def performance(func):
    def wrap(*args,**kwargs):
        t1=time()
        r=func(*args,**kwargs)
        t2=time()
        print (f"it took {t2-t1}s")
        return r
    return wrap

    return wrap()

@performance
def loadtime():
    for i in range(100000000):
        i*5
loadtime()