# Customer Churn Prediction System

## Overview

This project predicts whether a telecom customer is likely to churn (leave the service) based on customer demographics, services subscribed, contract details, and billing information.

The project covers the complete machine learning workflow:

* Exploratory Data Analysis (EDA)
* Data Preprocessing
* Feature Engineering
* Model Training
* Model Evaluation
* Cross Validation
* Threshold Tuning
* Model Interpretation
* Streamlit Deployment

---

## Problem Statement

Customer churn is a major business problem for telecom companies. Acquiring a new customer is often more expensive than retaining an existing one.

The objective of this project is to identify customers who are likely to churn so that the company can take proactive retention measures.

---

## Dataset

Telco Customer Churn Dataset

Target Variable:

* Churn (Yes / No)

Features Used:

* Customer Information
* Service Information
* Internet Services
* Contract Details
* Billing Information

Total Features: 18

---

## Machine Learning Workflow

### Data Preprocessing

* Handled missing values
* Converted data types
* One-Hot Encoding for categorical features
* Standard Scaling for numerical features
* Pipeline-based preprocessing

### Models Evaluated

* Logistic Regression
* Decision Tree
* Random Forest

### Model Selection

Logistic Regression was selected as the final model after comparing:

* Accuracy
* Precision
* Recall
* Cross Validation Performance
* Business Requirements

### Threshold Tuning

Instead of using the default threshold of 0.5, a threshold of 0.4 was chosen to improve churn detection and reduce false negatives.

---

## Final Model Performance

Final Model: Logistic Regression

Threshold: 0.4

Metrics:

- Accuracy: 0.77
- Precision: 0.56
- Recall: 0.66

Reason for Selection:

The objective was to identify customers likely to churn. Since missing a potential churn customer is more costly than incorrectly flagging a non-churn customer, recall was prioritized. Logistic Regression provided stable cross-validation performance and better business alignment compared to the other evaluated models.



## Deployment

The trained model was deployed using Streamlit.

Features:

* User-friendly input form
* Churn probability prediction
* Risk categorization
* Real-time inference

---

## Project Structure

├── app.py

├── churn_model.pkl

├── requirements.txt

├── README.md

---

## Installation

```bash
pip install -r requirements.txt
```

---

## Run Locally

```bash
python -m streamlit run app.py
```
---

## Live Demo Link

https://customer-churn-prediction-yash1912.streamlit.app/

---

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-Learn
* Joblib
* Streamlit

---

## Future Improvements

* XGBoost implementation
* Advanced model comparison
* FastAPI deployment
* Docker containerization
* Cloud deployment

---

## Author

Yaswanth

AI & Data Science Student
