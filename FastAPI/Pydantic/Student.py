from pydantic import BaseModel, EmailStr, Field
from typing import Dict, Optional
import json
import os

class Student(BaseModel):
    name: str = Field(..., description="The name of the student")
    age: int = Field(..., gt=0, lt=120, description="The age of the student")
    email: Optional[EmailStr] = None
    mobile: str = Field(..., description="The mobile number of the student")
    address: Dict[str, str] = Field(..., description="The address of the student")
    course: str = Field(..., description="The course of the student")

FILE_PATH = r"L:\EDU\FastAPI\Pydantic\students_data.json"

def insert_student(student: Student):
    student_dict = student.dict()

    # Load existing data if file exists
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, "r") as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                data = []
    else:
        data = []

    # Append new student
    data.append(student_dict)

    # Save back to JSON
    with open(FILE_PATH, "w") as file:
        json.dump(data, file, indent=4)

    print("✅ Student data insertion successfully done.")

def show_student(name: str):
    if not os.path.exists(FILE_PATH):
        print("No student data found.")
        return

    with open(FILE_PATH, "r") as file:
        try:
            data = json.load(file)
        except json.JSONDecodeError:
            print("Data file is corrupted.")
            return

    for student in data:
        if student["name"].lower() == name.lower():
            print("🎓 Student found:", student)
            return
    print(f"No student found with the name: {name}")

choice = input("Do you want to insert a new student? (yes/no): ").strip().lower()
if choice == "yes":
    print("Enter student details:")
    name = input("Name: ")
    age = int(input("Age: "))
    email = input("Email (optional): ")
    mobile = input("Mobile: ")
    print("Enter address details:")
    address = {
        "street": input("Street: "),
        "city": input("City: "),
        "state": input("State: "),
        "zip": Optional[int](input("Zip: ") or None)
    }
    course = input("Course: ")

    student = Student(
        name=name,
        age=age,
        email=email if email else None,
        mobile=mobile,
        address=address,
        course=course
    )
    insert_student(student)

choice = input("Do you want to see a student? (yes/no): ").strip().lower()
if choice == "yes":
    student_name = input("Enter the name of the student to show details: ")
    show_student(student_name)
