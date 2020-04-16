"""
what is decorators.?
will accepet a function add some functionality to it and return it , without hampering
original function's functionality

decorator are of two types:
1.function_decorator
2.class_decorator
"""

def div_decorate(func):

    print(func.__name__)
    def inner(x,y):
        print(x,y)
        if y==0:
            return "can't be divided by zer0"

        return func(x,y)
    return inner

@div_decorate
def div(a,b):

    return a/b


print(div(4,2))





