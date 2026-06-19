import json
import os

class Student:

    def __init__(self, name, age, semester):
        self.name = name
        self.age = age
        self.semester = semester

    def to_dict(self):
        return {
            "name": self.name,
            "age": self.age,
            "semester": self.semester
        }


class StudentManager:

    def __init__(self):
        self.students = []
        self.load_data()

    def add_student(self):

        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        semester = input("Enter Semester: ")

        student = Student(name, age, semester)

        self.students.append(student)

        self.save_data()

        print("Student Added!")

    def view_students(self):

        if len(self.students) == 0:
            print("No Students Found")

        else:

            for student in self.students:

                print(
                    student.name,
                    student.age,
                    student.semester
                )

    def search_student(self):

        name = input("Enter Name: ")

        for student in self.students:

            if student.name.lower() == name.lower():

                print("Student Found")

                print(student.name)
                print(student.age)
                print(student.semester)

                return

        print("Student Not Found")

    def delete_student(self):

        name = input("Enter Name: ")

        for student in self.students:

            if student.name.lower() == name.lower():

                self.students.remove(student)

                self.save_data()

                print("Deleted Successfully")

                return

        print("Student Not Found")

    def save_data(self):

        data = []

        for student in self.students:
            data.append(student.to_dict())

        with open("students.json", "w") as file:
            json.dump(data, file, indent=4)

    def load_data(self):

        if os.path.exists("students.json"):

            with open("students.json", "r") as file:

                data = json.load(file)

                for item in data:

                    student = Student(
                        item["name"],
                        item["age"],
                        item["semester"]
                    )

                    self.students.append(student)


manager = StudentManager()

while True:

    print("\n1 Add Student")
    print("2 View Students")
    print("3 Search Student")
    print("4 Delete Student")
    print("5 Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        manager.add_student()

    elif choice == "2":
        manager.view_students()

    elif choice == "3":
        manager.search_student()

    elif choice == "4":
        manager.delete_student()

    elif choice == "5":
        break