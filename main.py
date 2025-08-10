from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def blogs():
    return {
        "data": {
            "Name": "Junaed",
            "Designation": "Trainee - Software Engineer",
            "Salary": 8000,
            "Company": "ADN Diginet"
        }
    }
