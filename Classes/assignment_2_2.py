class User():

    def __init__(self,**kwargs):
        self.user_info={}
        for key,value in kwargs.items():
            self.user_info[key]=value
    def describer_user(self):
        for k,v in self.user_info.items():
            print(k,v)

class Admin(User):

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)


class Privilages:
    def __init__(self,*args):
        self.role=args
        


user=Admin(
    first="Swapnil",
    last="Karwa",
    user_name="skarwa4491",
    role=Privilages("can_add","can_edit","can_Delete")
)

user_2= Admin(
    first="Pooja",
    last="Manti",
    user_name="pamntri0507",
    role=Privilages("can_add","can_edit"))

