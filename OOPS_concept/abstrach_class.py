class grandparent():
    def __init__(self):
        print("this is grand parent")


class Parent1(grandparent):
    def __init__(self):
        print("This is parent1")



class parent_2(grandparent):
    def __init__(self):
        print("This is parent_2")


class child(parent_2,Parent1):
    def __init__(self):
        print("this is child class")

    def display(self):
        super().display()
        print("this is child display")


c=child()
c.display()
print(child.__mro__)