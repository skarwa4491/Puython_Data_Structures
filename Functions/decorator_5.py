class Decor():
    def __init__(self,func):
        print(1)
        print(func.__name__)
        self.func=func

    def __call__(self):
        print(2)
        str1=self.func()
        print(str1)
        print("hahaha")
        return(str1+"haha")
@Decor
def simple_msg():
    return "good morning "


simple_msg()