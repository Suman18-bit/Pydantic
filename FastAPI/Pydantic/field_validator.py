from pydantic import BaseModel, EmailStr, Field ,field_validator
from typing import Dict, List, Optional, Annotated
import json
import os

class Patient(BaseModel):
    name: Annotated[str, Field(..., max_length=100, description="The name of the patient")]
    age: Annotated[int, Field(..., gt=0, strict=True, description="Age must be a positive integer")]
    weight: Annotated[float, Field(..., gt=0, strict=True, description="Weight must be a positive number")]
    married: Annotated[bool, Field(..., strict=True, description="Whether the patient is married")]
    allergies: Annotated[Optional[List[str]], Field(None, description="List of allergies")]
    address: Annotated[Dict[str, str], Field(..., description="The address of the patient")]
    disease: str = Field(..., description="The disease of the patient")
    contact_number: Optional[str] = Field(None, description="The contact number of the patient")
    Email: Optional[EmailStr] = Field(None, description="The email address of the patient")
    LinkedIn: Optional[str] = Field(None, description="The LinkedIn profile of the patient")


    @field_validator('Email')
    @classmethod
    def valid_email(cls, v):
        valid_domains = ["gmail.com", "yahoo.com", "outlook.com"]
        domain_name = v.split('@')[-1]
        if domain_name not in valid_domains:
            raise ValueError(f"Email domain must be one of {valid_domains}")
        return v

    @field_validator('name')
    @classmethod
    def valid_name(cls,v):
        return v.upper()

    @field_validator('contact_number')
    @classmethod
    def valid_contact_number(cls, v):
        if v is not None and (not v.isdigit() or len(v) != 10):
            raise ValueError("Not a valid contact number. It must be a 10-digit number.")
        return v
    
    @field_validator('age',mode='after')
    @classmethod
    def valid_age(cls,v):
        if v < 0 or v > 120:
            raise ValueError("Age must be between 0 and 120.")
        return v
    
    @field_validator('weight',mode='after')
    @classmethod
    def valid_weight(cls,v):
        if v < 0 or v > 500:
            raise ValueError("Weight must be between 0 and 500.")
        return v
     



FILE_PATH = r"L:\EDU\FastAPI\Pydantic\patients_data.json"

def insert_patients(patient: Patient):
    patient_dict = patient.dict()

    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, "r") as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                data = []
    else:
        data = []

    data.append(patient_dict)

    # Save back to JSON
    with open(FILE_PATH, "w") as file:
        json.dump(data, file, indent=4)

    print("✅ Patient data insertion successfully done.")

data = {
    "name": "Suman Seth",
    "age": 25,
    "weight": 70.5,
    "married": False,
    "allergies": ["pollen", "dust"],
    "address": {"street": "Bayal", "city": "Nandigram", "state": "West Bengal", "zip": "721632"},
    "disease": "Flu",
    "contact_number": "45545",
    "Email": "suman@gmail.com",
    "LinkedIn": "https://linkedin.com/in/suman"
}

patient = Patient(**data)
insert_patients(patient)


def show_patient(name: str):
    if not os.path.exists(FILE_PATH):
        print("No patient data found.")
        return

    with open(FILE_PATH, "r") as file:
        try:
            data = json.load(file)
        except json.JSONDecodeError:
            print("Data file is corrupted.")
            return

    for patient in data:
        if patient["name"].lower() == name.lower():
            print("🩺 Patient found:", patient)
            return
    print(f"No patient found with the name: {name}")

    
show_patient("Suman Seth")


