fav_places={

    "Swapnil":["USA","CANADA","Mexico"],
    "Pooja":["Ahmednagar","SwitzerLand","Belgium"]

}
for person,placess in fav_places.items():
    print(person+" "+"your fav places are below")

    for place in placess:
        print("\t", end="")
        print(place)