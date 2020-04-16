def ouuter():
    x=3
    def inner():
        y=4
        result=x+y
        return result
    return inner

a=ouuter()
print(a.__name__)
print(a())