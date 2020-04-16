favorite_language={
    "Sarah":"c",
    "maria":"java",
    "Swapnil":"Python",
    "Karwa":"Java"
}

for person,language in favorite_language.items():
    print(person +" "+ language)

if "Swapnil" in favorite_language.keys():
    print("user is present")
else:
    "user is not present in keys"