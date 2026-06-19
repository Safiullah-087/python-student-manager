import requests

username = input(
    "Enter GitHub Username: "
)

url = f"https://api.github.com/users/{username}"

response = requests.get(url)

if response.status_code == 200:

    user = response.json()

    print("\nName:", user["name"])

    print(
        "Followers:",
        user["followers"]
    )

    print(
        "Following:",
        user["following"]
    )

    print(
        "Public Repos:",
        user["public_repos"]
    )

    print(
        "Created At:",
        user["created_at"]
    )

else:

    print("User Not Found")