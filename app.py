""" from fastapi import FastAPI
import joblib
import numpy as np

app = FastAPI()

model = joblib.load("model/model.pkl")

@app.get("/")
def home():
    return {"message": "ML API is running"}

@app.post("/predict")
def predict(income: float, age: int):
    data = np.array([[income, age]])
    prediction = model.predict(data)[0]
    
    return {
        "income": income,
        "age": age,
        "prediction": int(prediction)
    } """

#Better API structure (clean code)

from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI(title="Loan Prediction API")

# Load model
model = joblib.load("model/model.pkl")

# Input schema
""" class LoanRequest(BaseModel):
    income: float
    age: int """
class LoanRequest(BaseModel):
    income: float
    coapplicant_income: float
    loan_amount: float

# Health check
@app.get("/")
def home():
    return {"status": "API is running"}

# Prediction endpoint
@app.post("/predict")
def predict(request: LoanRequest):
    try:
        # data = np.array([[request.income, request.age]])
        data = np.array([
    [request.income, request.coapplicant_income, request.loan_amount]
])
        prediction = model.predict(data)[0]

        return {
            "input": {
                "income": request.income,
                "coapplicant_income": request.coapplicant_income,
                "loan_amount": request.loan_amount
            },
            "prediction": int(prediction),
            "status": "success"
        }

    except Exception as e:
        return {
            "error": str(e),
            "status": "failed"
        }