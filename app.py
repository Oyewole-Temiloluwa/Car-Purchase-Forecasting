import streamlit as st
import joblib
import numpy as np

scaler = joblib.load('scaler.pkl')
model = joblib.load('model.pkl')

st.title('Customer Car Price Estimator')

st.divider()

st.caption('''This app is for getting proce estimation for customer 
            so a price with the price range given can be advised for the customer''')

age = st.number_input('Enter the age', min_value=18, max_value=90, value=40, step=1)
salary = st.number_input('Enter your annual salary', min_value=1000, max_value=999999999, step=5000, value=30000)
networth = st.number_input('Enter the net worth', min_value=0, max_value=9999999999, step=1000, value = 100000)

X = [age, salary, networth]

calculatebutton = st.button('Calculate')

st.divider()

if calculatebutton:
    st.balloons()
    X_array = np.array(X)
    X_scaled = scaler.transform([X_array])

    
    prediction = model.predict(X_scaled)

    st.write(f'Prediction is {prediction[0]:,.2f}')
    st.write('Advise cars in the similar values')
else:
    st.write('Please enter the values and press the calculate button')
