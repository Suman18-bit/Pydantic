from pydantic import BaseModel, Field, EmailStr
from typing import List, Optional, Dict, Annotated,model_validator
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
    contact_number: Optional[Dict[str, str]] = Field(None, description="The contact number of the patient")
    Email: Optional[EmailStr] = Field(None, description="The email address of the patient")
    LinkedIn: Optional[str] = Field(None, description="The LinkedIn profile of the patient")
    Emergency_contact: Optional[Dict[str, str]] = Field(None, description="Emergency contact details")

    @model_validator(mode='after')
    def valid_emergency_contact(cls, model):
        if model.age <60 and "emergency" not in model.contact_number:
            raise ValueError("Emergency contact is only required for patients aged 60 and above.")
        return model

# ✅ Define a single constant for the file path
FILE_PATH = r"L:\EDU\FastAPI\Pydantic\patients_data.json"

def insert_patients(patient: Patient):
    patient_dict = patient.dict()

    # Load existing data if file exists
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, "r") as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                data = []
    else:
        data = []

    # Append new patient
    data.append(patient_dict)

    # Save back to JSON
    with open(FILE_PATH, "w") as file:
        json.dump(data, file, indent=4)

    print("✅ Patient data insertion successfully done.")
