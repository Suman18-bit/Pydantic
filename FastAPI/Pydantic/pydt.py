from pydantic import BaseModel 

class Pydantic_object_Patient(BaseModel): #the object blueprint for the patient data
    name: str
    age: int

def insert_patient(patient: Pydantic_object_Patient): # the function that accapts only the Pydantic_object_Patient type object as an argument
    print(patient.name)
    print(patient.age)
    print("Patient data insertion successfully done.")

patient_info = {
    "name": "Suman Seth",
    "age": 25
}

patient1 = Pydantic_object_Patient(**patient_info)  # creating an instance of the Pydantic_object_Patient class

insert_patient(patient1)
