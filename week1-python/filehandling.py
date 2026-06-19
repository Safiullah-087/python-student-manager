name = input("Enter student name: ")
with open("students.txt", "w") as file:
    file.write(name)

print("Student saved successfully!")

with open("students.txt", "r") as file:
    data = file.read()

print("Students:")

with open("students.txt", "w") as file:
    file.write("Ali\n")
    file.write("Ahmed\n")
    file.write("Sara\n")

with open("students.txt", "r") as file:
    data = file.read()

print("Students:")
print(data)

with open("students.txt", "w") as file:
    for i in range(3):
        name = input("Enter student name: ")
        file.write(name + "\n")

with open("students.txt", "r") as file:
    data = file.read()

print("\nStudents:")
print(data)

