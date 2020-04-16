class car():
    def __init__(self, make, model, year):

        self.make=make
        self.model=model
        self.year=year
        self.odmeter=0

    def get_name(self):
        long_name=self.year+" "+self.make+" "+self.model
        return long_name.title()
    def read_meter(self):
        print(self.get_name()+" "+"has "+str(self.odmeter)+" meter running")

    def update_readings(self,number,mileage):
        if mileage >= self.odmeter:
            self.odmeter=number
        else:
            print("you can't rollback the odmeter")


