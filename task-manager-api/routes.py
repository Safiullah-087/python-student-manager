from fastapi import APIRouter
from models import Task

router = APIRouter()

tasks = []

@router.get("/tasks")
def get_tasks():
    return tasks

@router.get("/tasks/{task_id}")
def get_task(task_id: int):

    for task in tasks:

        if task["id"] == task_id:
            return task

    return {"message": "Task not found"}

@router.post("/tasks")
def add_task(task: Task):

    tasks.append(task.model_dump())

    return {
        "message": "Task Added"
    }


@router.delete("/tasks/{task_id}")
def delete_task(task_id: int):

    for task in tasks:

        if task["id"] == task_id:

            tasks.remove(task)

            return {
                "message": "Deleted"
            }

    return {
        "message": "Task not found"
    }

@router.put("/tasks/{task_id}")
def update_task(task_id: int, updated_task: Task):

    for index, task in enumerate(tasks):

        if task["id"] == task_id:

            tasks[index] = updated_task.model_dump()

            return {
                "message": "Updated"
            }

    return {
        "message": "Task not found"
    }

