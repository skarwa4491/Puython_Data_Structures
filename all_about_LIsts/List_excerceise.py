guest_list=["Pooja","Sagar","Subhash"]

for each_item in guest_list:
    print(f"you are invited for dinner {each_item}")

print("Unfortunately Subhash cannot make it to dinner")

guest_list[guest_list.index("Subhash")]="Mantri Pariwar"

for each_item in guest_list:
    print(f"you are invuited to dinner {each_item}")

guest_list.insert(0,"Renuka JIJI")
guest_list.insert(int(len(guest_list)/2),"Shilpa JIJI")
guest_list.extend(["Sarla JIJI","Umesh JIJAJI"])

for each_item in guest_list:
    print(f"you all are invited for dinner {each_item}")

print(guest_list)



