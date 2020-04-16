class Employee():
    def __init__(self,first,last):
        self.first=first
        self.last=last
        
    @property
    def email(self):
        return f"{self.first}.{self.last}@gmail.com"
    @property
    def full_name(self):
        return (self.first+" "+self.last)

    @full_name.setter
    def full_name(self,message):
        first,last=message.split()
        self.first=first
        self.last=last

    def printall(self):
        print(self.first,self.last,self.full_name)

e=Employee("Swapnil","Karwa")
print(e.first)
print(e.last)
print(e.full_name)
print(e.user_name)
print(e.email)
e.full_name = "Pooja Mantri"
print(e.first)
print(e.last)
print(e.full_name)
print(e.user_name)
print(e.email)

e.first="Sagar"
print(e.first)
print(e.last)
print(e.user_name)