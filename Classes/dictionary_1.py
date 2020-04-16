alien_0={"color":'green',"points":5}
print(alien_0["color"])
print(alien_0["points"])

#adding a key value pair to dictionary

alien_0["x_position"]=0
alien_0["y_position"]=0
alien_0["speed"]="medium"
#modifying values in dictionary:

alien_0["color"]="red"
if alien_0["speed"]=="slow":
    x_increament=1;
elif alien_0["speed"]=="medium":
    x_increament=2;
else:
    y_increament=3

alien_0["x_position"]=alien_0["x_position"]+1;

print("new Xposition of alien_0",alien_0["x_position"])

# removing the elements from dictionary:
del alien_0["points"]

print(alien_0)