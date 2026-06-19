import requests

users = requests.get(
    "https://jsonplaceholder.typicode.com/users"
).json()

while True:

    print("\n1 Show All Users")
    print("2 Search User")
    print("3 Exit")

    choice = input("Enter Choice: ")

    if choice == "1":

        for user in users:

            print(user["name"])

    elif choice == "2":

        search = input(
            "Enter Name: "
        ).lower()

        found = False

        for user in users:

            if search in user["name"].lower():

                print(user["name"])
                print(user["email"])

                found = True

        if not found:

            print("User Not Found")

    elif choice == "3":

        break