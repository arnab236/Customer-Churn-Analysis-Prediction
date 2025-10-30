#Gender -> 1 Female 0 Male
#Churn -> 1 Yes 0 No
# Scaler is exported as scaler.pkl
# Model is exported as model.pkl
# Order of the X-> 'Age, 'Gender', 'Tenure', 'MonthlyCharges'


import joblib
import streamlit as st
import numpy as np

scaler = joblib.load('scaler.pkl')
model = joblib.load('model.pkl')


st.title("Customer Churn Prediction")
st.divider()

st.write("Please provide the following details to predict if the customer is likely to churn or not.")

st.divider()

age = st.number_input("Age", min_value=10, max_value=100, value=30)

tenure = st.number_input("Enter Tenure (in months)", min_value=0, max_value=130, value=10)

monthly_charges = st.number_input("Enter Monthly Charges", min_value=30.0, max_value=150.0)

gender = st.selectbox("Gender", options=["Male", "Female"])

st.divider()

predictButton = st.button("Predict!")

if predictButton:
    gender_selected = 1 if gender == "Female" else 0
    X = [age, gender_selected, tenure, monthly_charges]
    X_array = np.array(X)
    X_scaled = scaler.transform([X_array])
    prediction = model.predict(X_scaled)[0]
    predicted ="Churn"  if prediction == 1 else "Not Churn"
    st.balloons()
    st.subheader(f"The customer is likely to: {predicted}")
    st.write(f"Predicted : {predicted}")
