import streamlit as st
import joblib
import pandas as pd

@st.cache_resource
def load_model():
    return joblib.load("churn_model.pkl")

model=load_model()

st.title("CUSTOMER CHURN PREDICTION")

#CUSTOMER DETAILS
st.subheader("Customer Details")
gender=st.selectbox("Gender",["Male","Female"])
senior=st.selectbox("SeniorCitizen",["Yes","No"])
partner=st.selectbox("Partner",["Yes","No"])
dependents=st.selectbox("Dependents",["Yes","No"])

if senior=="Yes":
    senior=1
else:
    senior=0

st.subheader("Phone Services")
#PHONE SERVICES
phone=st.selectbox("PhoneService",["Yes","No"])
mul_lines=st.selectbox("MultipleLines",["Yes","No","No phone service"])

st.subheader("Internet Services")
#INTERNET SERVICES
internet=st.selectbox("InternetService",["DSL","Fiber optic","No internet service"])
online_security=st.selectbox("OnlineSecurity",["Yes","No","No internet service"])
online_backup=st.selectbox("OnlineBackup",["Yes","No","No internet service"])
device_protection=st.selectbox("DeviceProtection",["Yes","No","No internet service"])
tech_support=st.selectbox("TechSupport",["Yes","No","No internet service"])
streaming_tv=st.selectbox("StreamingTV",["Yes","No","No internet service"])
streaming_movies=st.selectbox("StreamingMovies",["Yes","No","No internet service"])

st.subheader("Billing Information")
#CONTRACT AND BILLING
tenure=st.number_input("Tenure",min_value=0,step=1)
contract=st.selectbox("Contract",["Month-to-month","One year","Two year"])
paperless_bill=st.selectbox("PaperlessBilling",["Yes","No"])
payment_method=st.selectbox("PaymentMethod",["Electronic check","Mailed check","Bank transfer (automatic)","Credit card (automatic)"])
monthly_charges=st.number_input("MonthlyCharges",min_value=0)
total_charges=st.number_input("TotalCharges",min_value=0,value=tenure*monthly_charges)

if st.button("PREDICT"):
    input_df=pd.DataFrame({"tenure":[tenure],"Contract":[contract],"PaperlessBilling":[paperless_bill],"PaymentMethod":[payment_method],"MonthlyCharges":[monthly_charges],"TotalCharges":[total_charges],
                           "InternetService":[internet],"OnlineSecurity":[online_security],"OnlineBackup":[online_backup],"DeviceProtection":[device_protection],"TechSupport":[tech_support],"StreamingTV":[streaming_tv],"StreamingMovies":[streaming_movies],
                           "PhoneService":[phone],"MultipleLines":[mul_lines],
                           "gender":[gender],"Partner":[partner],"SeniorCitizen":[senior],"Dependents":[dependents]})
    #st.write(input_df.dtypes)
    prob=model.predict_proba(input_df)[0][1]
    threshold=0.4
    if prob>=threshold:
        prediction="Churn"
    else:
        prediction="Stay"

    st.header("Prediction")
    st.write(f"Prediction :{prediction}")
    st.write(f"Churn Probability :{prob:.2%}")

    if prob>=0.8:
        risk="High"
    elif prob>=0.6:
        risk="Medium"
    else:
        risk="Low"
    
    st.write(f"Risk Level : {risk}")
    