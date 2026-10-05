from pydantic import BaseModel, Field, EmailStr
from typing import List, Optional, Dict, Annotated,model_validator,computed_field
import json 
import os

#nested model for address and emergency contact
 #--------------------------------------------------------------------------------
class Address(BaseModel):
    street: Annotated[str, Field(..., max_length=100, description="Street address")]
    city: Annotated[str, Field(..., max_length=50, description="City name")]
    state: Annotated[str, Field(..., max_length=50, description="State name")]
    pin_code: Annotated[str, Field(..., max_length=10, description="ZIP code")]
    country: Annotated[str, Field(..., max_length=50, description="Country name")]

class EmergencyContact(BaseModel):
    name: Annotated[str, Field(..., max_length=100, description="Emergency contact name")]
    relationship: Annotated[str, Field(..., max_length=50, description="Relationship to the patient")]
    phone_number: Annotated[str, Field(..., max_length=15, description="Emergency contact phone number")]
    email: Optional[EmailStr] = Field(None, description="Emergency contact email address")
#--------------------------------------------------------------------------------


class Patient(BaseModel):
    name: Annotated[str, Field(..., max_length=100, description="The name of the patient")]
    age: Annotated[int, Field(..., gt=0, strict=True, description="Age must be a positive integer")]
    weight: Annotated[float, Field(..., gt=0, strict=True, description="Weight must be a positive number")]
    height: Annotated[float, Field(..., gt=0, strict=True, description="Height must be a positive number")]
    married: Annotated[bool, Field(..., strict=True, description="Whether the patient is married")]
    allergies: Annotated[Optional[List[str]], Field(None, description="List of allergies")]
    address: Annotated[Address, Field(..., description="The address of the patient")]
    disease: str = Field(..., description="The disease of the patient")
    contact_number: Optional[Dict[str, str]] = Field(None, description="The contact number of the patient")
    Email: Optional[EmailStr] = Field(None, description="The email address of the patient")
    LinkedIn: Optional[str] = Field(None, description="The LinkedIn profile of the patient")
    Emergency_contact: Optional[EmergencyContact] = Field(None, description="Emergency contact details")


def insert(
    name: str,
    age: int,
    weight: float,
    height: float,
    married: bool,
    allergies: Optional[List[str]],
    address: Address,
    disease: str,
    contact_number: Optional[Dict[str, str]],
    Email: Optional[EmailStr],
    LinkedIn: Optional[str],
    Emergency_contact: Optional[EmergencyContact]
) -> Patient:
    patient = Patient(
        name=name,
        age=age,
        weight=weight,
        height=height,
        married=married,
        allergies=allergies,
        address=address,
        disease=disease,
        contact_number=contact_number,
        Email=Email,
        LinkedIn=LinkedIn,
        Emergency_contact=Emergency_contact
    )
    return patient

data = {
    "name": "John Doe",
    "age": 30,
    "weight": 70.5,
    "height": 1.75,
    "married": True,
    "allergies": ["Peanuts", "Shellfish"],
    "address": {
        "street": "123 Main St",
        "city": "Anytown",
        "state": "Anystate",
        "pin_code": "12345",
        "country": "USA"
    },
    "disease": "Hypertension",
    "contact_number": {
        "home": "+1-555-555-5555",
        "work": "+1-555-555-5556"
    },
    "Email": "johndoe@example.com"
}

patient = Patient(**data)

inserted_patient = insert(patient.name, patient.age, patient.weight, patient.height, patient.married, patient.allergies, patient.address, patient.disease, patient.contact_number, patient.Email, patient.LinkedIn, patient.Emergency_contact)

temp = patient.model_dump()

temp2 = patient.model_dump_json(indent=4)

temp3 = patient.model_dump(include={'name', 'age', 'weight', 'height', 'married', 'allergies', 'address', 'disease', 'contact_number', 'Email', 'LinkedIn', 'Emergency_contact'}) #which one to include in the dump

temp4 = patient.model_dump(exclude={'contact_number', 'Email', 'LinkedIn', 'Emergency_contact'}) #which one to exclude in the dump

temp5 = patient.model_dump(exclude_unset=True) #exclude unset values


