from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI() # app is the instance of the fastapi object

@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.get("/greet")
def greet():
    return {"message": "welcome manu"}

@app.get("/greet/{name}")
def greet_name(name: str, age: Optional[int] = None):
    return {"message": f"hello {name} and my age is {age}"}


class Student(BaseModel):
    name: str
    age: int
    roll: int

@app.post("/create_student")
def create_student(student: Student):
    return{
        "name": student.name,
        "age": student.age,
        "roll": student.roll
    }