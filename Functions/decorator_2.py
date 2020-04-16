def decorate(func):
    def inner(x,y):
        if(y==0):
            return("cannot divide")
        return func(x,y)
    return inner

@decorate
def div(x,y):
    return x/y

print(div(4,2))