
"""
list are like arrays which start from index 0
list are not of generic type in python , as variables don't have data types.
"""
movies=["Holy brain","the life of a brain","the meaning of life"]

#accessing item at specific index:
print(movies[0])

#printing length of list which is last_index+1
cast=["brad","Tom","peteer","Jhonny"]
print(len(cast))

#appending a item to list, it appends the item to end of list

cast.append("Nicolas")
print(cast)

#popping the item to pist , pop function pop's out mentioned object from list and returnds the popped object
#by default item is popped from right.
print(cast.pop())
print(cast.pop(1))
print(cast)

#remove - it is same as pop , istead it accepts the name of object to remove, and returns nothing

print(cast.remove("brad"))
print(cast)
#del method accepts the index postion of list and removes the element from provided index:
del(cast[0])
print(cast)
#extend method appends the another list to existing list

cast.extend(["brad","Tom","Nicolas"])
print(cast)

#insert it accepts 2 parameters object and index number and inserts the object at specified index

cast.insert(1,"Shahrukh")
print(cast)


mixed_list=["Shahrukh",2018,"jab tak hai jaan"]
print(mixed_list)
print(id(mixed_list))