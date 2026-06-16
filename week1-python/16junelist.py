students = []

while True:
    print("\n===== Student Manager =====")
    print("1. Add Student")
    print("2. Remove Student")
    print("3. View Students")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        students.append(name)
        print("Student added successfully!")

    elif choice == "2":
        name = input("Enter student name to remove: ")

        if name in students:
            students.remove(name)
            print("Student removed successfully!")
        else:
            print("Student not found!")

    elif choice == "3":
        if len(students) == 0:
            print("No students available.")
        else:
            print("\nStudent List:")
            for student in students:
                print(student)

    elif choice == "4":
        print("Exiting...")
        break

    else:
        print("Invalid choice. Try again.")