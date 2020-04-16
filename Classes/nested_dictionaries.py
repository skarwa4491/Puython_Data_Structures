alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens=[alien_0,alien_1,alien_2]

for alien_number in range(1,31):
    new_alien= {'color': 'red', 'points': 15}
    aliens.append(new_alien)

for alien in aliens[0:3]:
    if(alien["color"]=="green"):
        alien["color"]="red"
        alien["points"]=15
    elif(alien["color"]=="yellow"):
        alien['color']="red"
        alien["points"] = 15

for name in aliens:
    print(name)