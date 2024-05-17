from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI(title="Nguyen Don The Kiet's Submission for VDT2024 Cloud WebAPI", version="0.1", description="This is a simple API for managing students' information")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def Welcome():
    return "Welcome to Strix's Submission for VDT2024 Cloud WebAPI"

@app.get("/students")
async def get_students():
    students = [
        {"id": 1, "gender": "male", "name": "John Doe", "school": "SMK Taman Desa"},
        {"id": 2, "gender": "fs", "name": "Jane Doe", "school": "SMK Taman Desa"},
        {"id": 2, "gender": "fs", "name": "Jane Doe", "school": "SMK Taman Desa"}
    ]
    return students
             

@app.get("/students/{student_id}")
async def get_student(student_id: int):
    return {"name": "John Doe", "school": "SMK Taman Desa", "email": "test@asd.com", "phone_nb": "0123456789", "birth_yr": 2000}


@app.post("/students")
async def create_student( name: str = Query(description="Student's name", min_length=3, max_length=50), 
                         school: str = Query(description="Student's school", min_length=3, max_length=50),
                         email: str = Query(description="Student's email", min_length=3, max_length=50, pattern="[^@]+@[^@]+\.[^@]+"),
                         phone_nb: str = Query(description="Student's phone number", min_length=9, max_length=10, pattern="^[0-9]*$"),
                         birth_yr: int = Query(description="Student's birth year", ge=1999, le=2005)
                         ):
    return {"message": "Student has been created"}

@app.delete("/students/{student_id}")
async def delete_student(student_id: int):
    return {"message": "Student has been deleted"}

@app.put("/students/{student_id}")
async def update_student(student_id: int):
    return {"message": "Student has been updated"}
