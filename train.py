import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import joblib
import mlflow
import mlflow.sklearn

# Update train.py (ADD THIS LINE)
mlflow.set_tracking_uri("file:./mlruns")
mlflow.set_experiment("loan_prediction_experiment")

# Generate dataset
np.random.seed(42)

data_size = 200

df = pd.DataFrame({
    "ApplicantIncome": np.random.randint(2000, 10000, data_size),
    "CoapplicantIncome": np.random.randint(0, 5000, data_size),
    "LoanAmount": np.random.randint(50, 300, data_size),
})

df["Loan_Status"] = (
    (df["ApplicantIncome"] + df["CoapplicantIncome"]) > 7000
).astype(int)

# Features
X = df[["ApplicantIncome", "CoapplicantIncome", "LoanAmount"]]
y = df["Loan_Status"]

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Start MLflow tracking
with mlflow.start_run():

    model = LogisticRegression()
    model.fit(X_train, y_train)

    accuracy = model.score(X_test, y_test)

    # Log parameters
    mlflow.log_param("model_type", "LogisticRegression")

    # Log metrics
    mlflow.log_metric("accuracy", accuracy)

    # Log model
    mlflow.sklearn.log_model(model, "model")

    print(f"Model trained with accuracy: {accuracy}")

# Save model locally too
joblib.dump(model, "model/model.pkl")
