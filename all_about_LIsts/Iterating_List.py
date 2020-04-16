"""
covered for loop and while loop to iterate the list
"""

fav_movies=["The holy grill","the life of brain"]
# using for loop
for each_movies in fav_movies:
    print(each_movies)

# using while loop:
count=0
while(count<len(fav_movies)):
    print(fav_movies[count])
    count+=1;