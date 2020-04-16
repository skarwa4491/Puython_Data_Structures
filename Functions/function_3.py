def build_dict(first,last,**user_info):
    profile={}
    profile["first"]=first
    profile["last"]=last
    for key, value in user_info.items():
        profile[key]=value

    return profile

def make_pizza(size,*toppings):
    print("Making pizza of size "+str(size)+
          "- and toppings as below")
    for item in toppings:
        print("\t"+item)



user_info=build_dict('albert', 'einstein',
station='princeton',
field='physics')

print(user_info)

make_pizza(12,'mushrooms', 'green peppers', 'extra cheese')