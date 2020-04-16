class decor():
    def __init__(self,func):
        self.func=func
    def __call__(self, *args, **kwargs):
        num=args
        if(0 in num[1:]):
            return "cannot be dividd by 0"
        else:
            return self.func(*args,**kwargs)

@decor
def div(a,b):
    return a/b
@decor
def div1(a,b,c):
    return(a/b/c)

print(div1(16,4,2))