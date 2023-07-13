import os,sys
def os_fork():
    a=os.fork()
    b=os.fork()
    x=z=0
    status=0
    if a==0:
        print(f"child PID: {os.getpid()}")
        z=os._exit(0)
    elif b==0:
        print(f"child PID: {os.getpid()}")
        
        x=os._exit(1)
    print('1st wait')
    a=os.wait()
    print(a,os.WEXITSTATUS(status),x,z)
    print('2nd wait')
    a=os.wait()
    print(a,os.WEXITSTATUS(status))
    return os._exit(0)

os_fork()