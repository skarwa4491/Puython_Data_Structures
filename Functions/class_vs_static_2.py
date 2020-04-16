def outerfunc(text):
    text=text
    def inner_func():
        print(text)

    return inner_func


myfunc=outerfunc("Swapnil")
print(myfunc)
