from fastapi import FastAPI, HTTPException, Path, Query
import json

app = FastAPI()

def load_data():
    try:
        with open('Data.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        return {}

@app.get("/")
def hello():
    return {"message": "Hello World........!"}

@app.get('/about')
def about():
    return {"message": "This is a FastAPI application."}

@app.get('/view')
def view():
    data = load_data()
    if not data:
        raise HTTPException(status_code=404, detail="Data file is empty or not found.")
    return data

@app.get('/patients/{patient_id}')
def view_patient(patient_id: str = Path(..., description = "ID of the patient to see the patient details",example = "P001")):
    data = load_data()
    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code = 404, detail = f"Patient ID {patient_id} not found")
@app.get('/sort')
def sort_patients(sort_by:str = Query(...,description = "Field to sort the patients by", examples = ["name", "age","bmi"]), Order:str = Query('asc',description = "Order of sorting, can be Ascending or Descending order", examples = ["asc","/","desc"])):
    valid_fields = ['height','weight','age','bmi']

    if sort_by not in valid_fields:
        raise HTTPException(status_code = 400, detail = f"{sort_by} in not a valid field to sort")
    
    if Order not in ['asc','desc']:
        raise HTTPException(status_code = 400, detail = f"{Order} is not a valid order, it should be either 'asc' or 'desc'")

    data = load_data()

    return sorted(data.values(), key = lambda x: x.get(sort_by, 0), reverse = True if Order == 'desc' else False)