def deco(func):
    def wrap():
        print("******")
        func()
        print("******")
    return wrap
def decorate(func):
    def wrap(*args,**kwargs):
        print("******")
        func(*args,**kwargs)
        print("******")
    return wrap    
@deco
def hello():
    print('hello')
@decorate
def hello2(greeting,emoji=":-("):
    print(greeting,emoji)
hello()

hello2("bye")