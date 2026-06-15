
students = []

while True:
    print("\n--- Student Record Manager ---")
    print("1 Add Student")
    print("2 View Students")
    print("3 Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        students.append(name)
        print("Student added!")

    elif choice == "2":
        if len(students) == 0:
            print("No students found")
        else:
            print("\nStudent List:")
            for s in students:
                print(s)

    elif choice == "3":
        print("Exiting program...")
        break

    else:
        print("Invalid choice")

