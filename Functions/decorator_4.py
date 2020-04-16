def decor_outer(exper):
    def decor(func):
        def inner():
            x=func()
            return x+exper
        return inner
    return decor

@decor_outer(" Swapnil")
def simple_text():
    return "good morning"

print(simple_text() )