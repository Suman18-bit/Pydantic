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

