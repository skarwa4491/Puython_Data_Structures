"""
using conditional statementrs to check if object is a list

"""

movies = [
"The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91,
["Graham Chapman",
["Michael Palin", "John Cleese", "Terry Gilliam", "Eric Idle", "Terry Jones"]]]


print(movies[4][1][2])
for each_irem in movies:
    print(each_irem)
print ("*********************************************")
#solution2
for each_item in movies:
    if(isinstance(each_item,list)):
        for each_item_nest in each_item:
            print(each_item)
    else:
        print(each_item)


