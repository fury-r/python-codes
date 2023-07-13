import os
import sys
def os_fork():
    a=os.fork()
    b=os.fork()
    status=0
    if a==0:
        print(f"child PID: {os.getpid()}")
        status=os._exit(0)
    elif b==0:

        print(f"child PID: {os.getpid()}")
        status=os._exit(1)

    print('1st wait')
    a=os.wait()
    print(a,os.WEXITSTATUS(status))
    print('2nd wait')
    a=os.wait()
    print(a,os.WEXITSTATUS(status))
    return sys.exit(0)

os_fork()