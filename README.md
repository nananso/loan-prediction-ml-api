![Python](https://img.shields.io/badge/Python-3.10-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-API-green)
![MLflow](https://img.shields.io/badge/MLflow-Tracking-orange)
![Render](https://img.shields.io/badge/Deployed-Render-purple)

# 🚀 Loan Prediction ML API

A production-ready Machine Learning API that predicts loan approval using Logistic Regression. This project demonstrates an end-to-end MLOps pipeline: model training, experiment tracking with MLflow, and deployment using FastAPI.

## 🔗 Live Demo

👉 https://loan-prediction-ml-api.onrender.com/docs

Try it: Open `/docs`, expand `POST /predict`, click “Try it out”, and send the sample request.

---

## 📌 Features

* 🔍 Predict loan approval using ML model
* ⚡ FastAPI for high-performance API
* 📊 MLflow for experiment tracking
* ☁️ Deployed on Render (public access)
* 🧠 Scikit-learn model (Logistic Regression)

---

## 🧪 API Endpoint

### GET `/`

Returns API status:

```json
{
  "message": "Loan Prediction API is running"
}
```

### POST `/predict`

#### Request Body:

```json
{
  "income": 5000,
  "coapplicant_income": 2000,
  "loan_amount": 150
}
```

#### Response:

```json
{
  "prediction": 1,
  "status": "success"
}
```

---

## 🛠️ Tech Stack

* Python
* FastAPI
* Scikit-learn
* Pandas
* MLflow
* Uvicorn
* Render

---

## 📊 Model Info

* Algorithm: Logistic Regression
* Accuracy: 0.95
* Features Used:

  * Income
  * Coapplicant Income
  * Loan Amount

---

## 📈 Experiment Tracking

MLflow was used to:

* Track model experiments
* Log accuracy metrics
* Manage model artifacts

---

## ⚙️ Run Locally

```bash
git clone https://github.com/nananso/loan-prediction-ml-api.git
cd loan-prediction-ml-api

pip install -r requirements.txt

python train.py

uvicorn app:app --reload
```

---

## 📁 Project Structure

```
├── app.py
├── train.py
├── requirements.txt
├── README.md
├── model.pkl
```

---

## 👨‍💻 Author

Uchenna I Nsoha

---

## ⭐ If you like this project

Give it a star ⭐ on GitHub
