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
    def fill_gas_tank(self):
        print("Gas tank will be filled")

class Battery():

    def __init__(self,battery_size=70):
        self.battery_size=battery_size

    def describe_battery(self):
        print("this has battery_size "+ str(self.battery_size))

class electric_car(car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery=Battery()

    def fill_gas_tank(self):
        print("Electric cars dont have gas tank")





ec=electric_car("toyota","zest","2020")
print(ec.get_name())
ec.battery.describe_battery()

ec2=electric_car("toyota","zest","2020")
ec2.battery=Battery(80)
print(ec2.get_name())
ec2.battery.describe_battery()

