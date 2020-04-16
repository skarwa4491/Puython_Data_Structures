class Hello:
    def __init__(self):
        self.a=10
        self._b=20
        self.__c=30

    def public_method(self):
        print(self.__c)
        print("inside pubic method")

    def __private_method(self):
        print("this is private method")



hh=Hello()
hh.public_method()