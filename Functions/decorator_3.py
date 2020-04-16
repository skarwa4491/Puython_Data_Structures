def uppercase(func):
    print(func.__name__)
    def inner():
        x=func()
        return x.upper()
    return inner

def split_code(func):
    print(func.__name__)
    def wrapper():
        x=func()
        return x.split(" ")
    return wrapper


@split_code
@uppercase
def ordinary():
    return "Good Morning"


print(ordinary())