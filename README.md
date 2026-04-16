# Loan Prediction ML API

This project demonstrates deployment of a machine learning model using FastAPI.

## Features
- REST API for predictions
- Input validation using Pydantic
- Trained ML model (Logistic Regression)
- Clean and structured responses

## Tech Stack
- Python
- FastAPI
- Scikit-learn
- Joblib

## API Endpoint

POST /predict

Request:
{
  "income": 50000,
  "age": 30
}

Response:
{
  "prediction": 1,
  "status": "success"
}

## Run Locally

pip install -r requirements.txt
uvicorn app:app --reload