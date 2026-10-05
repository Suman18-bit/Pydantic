from pydantic import BaseModel, Field, EmailStr
from typing import List, Optional, Dict, Annotated,model_validator,computed_field
import json 
import os

class Patient(BaseModel):
    name: Annotated[str, Field(..., max_length=100, description="The name of the patient")]
    age: Annotated[int, Field(..., gt=0, strict=True, description="Age must be a positive integer")]
    weight: Annotated[float, Field(..., gt=0, strict=True, description="Weight must be a positive number")]
    height: Annotated[float, Field(..., gt=0, strict=True, description="Height must be a positive number")]
    married: Annotated[bool, Field(..., strict=True, description="Whether the patient is married")]
    allergies: Annotated[Optional[List[str]], Field(None, description="List of allergies")]
    address: Annotated[Dict[str, str], Field(..., description="The address of the patient")]
    disease: str = Field(..., description="The disease of the patient")
    contact_number: Optional[Dict[str, str]] = Field(None, description="The contact number of the patient")
    Email: Optional[EmailStr] = Field(None, description="The email address of the patient")
    LinkedIn: Optional[str] = Field(None, description="The LinkedIn profile of the patient")
    Emergency_contact: Optional[Dict[str, str]] = Field(None, description="Emergency contact details")


    @computed_field
    @property

    def bmi(self) -> float:
        bmi = self.weight / (self.height ** 2)
        return round(bmi, 2)
