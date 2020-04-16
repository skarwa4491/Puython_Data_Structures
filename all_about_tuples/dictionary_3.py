favorite_language={
    "Sarah":"c",
    "maria":"java",
    "Swapnil":"Python",
    "Karwa":"Java"
}

friends=[
    "Swapnil",
    "Karwa"
]

for name in friends:
    print(name.capitalize())

    if name in favorite_language.keys():
        print("Hi there i see your fav language is ",favorite_language[name].capitalize())

print("****************************")

for name in sorted(favorite_language.keys(), reverse=True):
    print(name)
