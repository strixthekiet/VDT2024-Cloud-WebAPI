from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import json
import motor.motor_asyncio
from bson import ObjectId
app = FastAPI(title="Nguyen Don The Kiet's Submission for VDT2024 Cloud WebAPI", version="0.1", description="This is a simple API for managing students' information")
import os
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
mongo_url = os.getenv('MONGO_URL')
print(f"Connected to MongoDB at {mongo_url}")
client = motor.motor_asyncio.AsyncIOMotorClient(f"mongodb://{mongo_url}:27017/")

student_collection = client.vdt24.get_collection("students")


@app.get("/")
def Welcome():
    res = "Welcome to Strix's Submission for VDT2024 Cloud WebAPI"
    return res

@app.get("/students")
async def get_students():
    students = await student_collection.find().to_list(100)
    response = []
    for student in students:
        response.append(
            {
                "id" : student["id"], # Convert ObjectId to string to avoid "Object of type ObjectId is not JSON serializable
                "name" : student["Name"],
                "gender" : student["Gender"],
                "university" : student["University"],
             }
        )
    return response


@app.get("/students/{student_id}")
async def get_student(student_id: int):
    student = await student_collection.find_one({"id": student_id})

    if student:
        return {
            "id" : student["id"],
            "name" : student["Name"],
            "gender" : student["Gender"],
            "university" : student["University"],
            "yearOB" : student["YearOB"],
            "email" : student["Email"],
            "phoneNb" : student["PhoneNb"],
            "country" : student["Country"]
        }
    return {"message": "Student not found"}


@app.post("/students")
async def create_student( req_json: dict):
    # find the latest student id
    student = await student_collection.find_one(sort=[("id", -1)])
    new_id = 1
    if student:
        new_id = student["id"] + 1
    student = {
        "Name": req_json["name"],
        "University": req_json["university"],
        "Email": req_json["email"],
        "PhoneNb": req_json["phoneNb"],
        "YearOB": req_json["yearOB"],
        "Country": req_json["country"],
        "Gender" : req_json["gender"],
        "id": new_id
    }
    result = await student_collection.insert_one(student)
    return {"message": "Student has been created"}


@app.delete("/students/{student_id}")
async def delete_student(student_id: int):
    student = await student_collection.find_one({"id": student_id})
    if student is None:
        return {"message": "Student not found"}

    result = await student_collection.delete_one({"id": student_id})
    if result.deleted_count == 1:
        return {"message": "Student has been deleted"}
    return {"message": "Student not found"}


@app.put("/students/{student_id}")
async def update_student(student_id: int, req_json: dict):
    student = await student_collection.find_one({"id": student_id})
    if student is None:
        return {"message": "Student not found"}

    await student_collection.update_one({"id": student_id}, {"$set":
        {
            "Name": req_json["name"],
            "University": req_json["university"],
            "Email": req_json["email"],
            "PhoneNb": req_json["phoneNb"],
            "YearOB": req_json["yearOB"],
            "Country": req_json["country"],
            "Gender" : req_json["gender"]
            }})
    return {"message": "Student has been updated"}

    # await student_collection.update_one(
    #     {"_id": ObjectId(student_id)},
    #     {"$set": {
    #         "Name": req_json["name"],
    #         "University": req_json["university"],
    #         "Email": req_json["email"],
    #         "PhoneNb": req_json["phoneNb"],
    #         "YearOB": req_json["yearOB"],
    #         "Country": req_json["country"],
    #         "Gender" : req_json["gender"]
    #     }})
    # return {"message": "Student has been updated"}
