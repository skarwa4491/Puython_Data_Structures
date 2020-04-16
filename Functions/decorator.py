def decor(a):
    def outer(func):
        print(func.__name__)
        def inner(x,y):
            if(x==0 or y==0):
                return "adding 0 will return same number"
            else:
                return func(x,y) + a
        return inner
    return outer

@decor(8)
def add1(x,y):
    return x+y

print(add1(0,4))
