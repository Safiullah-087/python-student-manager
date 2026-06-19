class Student:
    def __init__(self, name, age, semester):
        self.name = name
        self.age = age
        self.semester = semester

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Semester: {self.semester}")

student1 = Student("Safi", 21, 6)

student1.display()