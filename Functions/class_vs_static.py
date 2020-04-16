from datetime import date

class Demo():
    def __init__(self,name,age):
        self.name=name
        self.age=age

    @classmethod
    def getAge(cls,name,birth_year):
        print(name+"'s age is "+str(date.today().year-birth_year))

    @staticmethod
    def get_std_format(name,age):
        return (name+"'s age is " +str(age))


print(Demo.getAge("Swapnil",1991))
print(Demo.get_std_format("Swapnil",1991))
