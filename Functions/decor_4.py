def decor(func):
    def inner(*args):
        list=args
        if(0 in list[1:]):
            print("dovide by zero")
            return None
        else:
            return func(*args)
    return inner

@decor
def div(a,b):
    return a/b

@decor
def div2(a,b,c):
    return a/b/c

print(div.__name__)

print(div2(4,2,0))