from pydantic import BaseModel, Field

class Task(BaseModel):
    id: int
    title: str = Field(min_length=1)
    description: str = Field(min_length=5)
    completed: bool = False