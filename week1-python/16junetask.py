import json
import os

FILE_NAME = "students.json"


# Load data automatically
if os.path.exists(FILE_NAME):
    with open(FILE_NAME, "r") as file:
        students = json.load(file)
else:
    students = []


def save_data():
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)


while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        semester = input("Enter Semester: ")

        student = {
            "name": name,
            "age": age,
            "semester": semester
        }

        students.append(student)
        save_data()
        print("Student added successfully!")

    elif choice == "2":
        if len(students) == 0:
            print("No students found.")
        else:
            print("\nStudent List:")
            for student in students:
                print(
                    f"Name: {student['name']}, "
                    f"Age: {student['age']}, "
                    f"Semester: {student['semester']}"
                )

    elif choice == "3":
        search_name = input("Enter student name to search: ")

        found = False

        for student in students:
            if student["name"].lower() == search_name.lower():
                print("\nStudent Found:")
                print(f"Name: {student['name']}")
                print(f"Age: {student['age']}")
                print(f"Semester: {student['semester']}")
                found = True
                break

        if not found:
            print("Student not found.")

    elif choice == "4":
        delete_name = input("Enter student name to delete: ")

        found = False

        for student in students:
            if student["name"].lower() == delete_name.lower():
                students.remove(student)
                save_data()
                print("Student deleted successfully!")
                found = True
                break

        if not found:
            print("Student not found.")

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")