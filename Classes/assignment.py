class Restaurant():
    def __init__(self,name,ctype):
        self.name=name
        self.ctype=ctype
        self.number_serve=0

    def open_restaurant(self):
        print(self.name+" "+"is now open")

    def desc_restaurant(self):
        print(self.name+" restaurant is of type " +self.ctype )

    def set_number_served(self,number):
        self.number_serve+=number

class ince_cream_stand(Restaurant):
    def __init__(self,name,ctype):
        super().__init__(name,ctype)
        self.flavors = ["butter-skotch","Vanila","red-velvet"]

    def display_flavors(self):
        print("avialable flavors at ice-cream stand are below")
        for flavor in self.flavors:
            print("\t"+flavor)



amul=ince_cream_stand("Rajmandir","ice_cream_stand")
amul.display_flavors()


