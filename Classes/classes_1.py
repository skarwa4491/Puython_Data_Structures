class Dog():
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def sit(self):
        print(self.name.title() +" "+ "is now sitting")

my_dog=Dog("Sheru",4)
yourDog=Dog("TOMMY","8")


print(my_dog.name +" "+yourDog.name)
