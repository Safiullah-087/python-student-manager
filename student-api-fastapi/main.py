from fastapi import FastAPI
from pydantic import BaseModel

class Student(BaseModel):

    id: int
    name: str
    age: int

app = FastAPI()
@app.get("/")
def home():
    return {"message": "Hello Safi"}

students = [
    {
        "id": 1,
        "name": "Ali",
        "age": 20
    },
    {
        "id": 2,
        "name": "Ahmed",
        "age": 21
    }
]
@app.get("/students")
def get_students():
    return students

@app.get("/students/{id}")
def get_student(id: int):

    for student in students:

        if student["id"] == id:
            return student

    return {"message": "Not Found"}

@app.post("/students")
def add_student(student: Student):

    students.append(student.dict())

    return {
        "message": "Student Added"
    }

@app.delete("/students/{id}")
def delete_student(id: int):

    for student in students:

        if student["id"] == id:

            students.remove(student)

            return {
                "message": "Deleted"
            }

    return {
        "message": "Student Not Found"
    }