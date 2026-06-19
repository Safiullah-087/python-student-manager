import requests

response = requests.get(
    "https://jsonplaceholder.typicode.com/users"
)

print(response.status_code)

data = response.json()

print(data)