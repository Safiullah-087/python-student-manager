import json

books = [
    {"title": "Python", "price": 500},
    {"title": "AI", "price": 1000}
]

# Save to books.json
with open("books.json", "w") as file:
    json.dump(books, file)

print("Books saved successfully!")

# Load from books.json
with open("books.json", "r") as file:
    books = json.load(file)

print("\nBook Titles:")

for book in books:
    print(book["title"])