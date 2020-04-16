users = {
    "Skarwa4491": {
        "First_name": "Swapnil",
        "Last_name": "Karwa",
        "Location": "India"
    },

    "Pooja0507": {

        "First_name": "Pooja",
        "Last_name": "Mantri",
        "Location": "Ahmednagar"

    }

}

for user_name, user_info in users.items():
    print(user_name + "-", end=" ")
    print(user_info["First_name"] + " " + user_info["Last_name"])
