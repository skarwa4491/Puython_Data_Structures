responses={}
polling_active=True
while polling_active:
    name=input("\n whats your name")
    poll=input("\n whtas your poll")

    responses[name]=poll

    repeat=input("would you like to let another man response (yes/no)")
    if repeat=="no":
        polling_active=False

print("\n ---- POll results----")
count_yes=0
count_no=0
for response in responses.values():
    if response=="yes":
        count_yes+=1
    else:
        count_no+=1

print(count_yes)
print(count_no)

