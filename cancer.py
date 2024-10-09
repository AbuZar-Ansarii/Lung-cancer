import streamlit as st
import pickle
import numpy as np

model = pickle.load(open('lung_cancer_model.pkl','rb'))


st.title("LUNG CANCER DETECTOR")

user_input = []

Gender = st.selectbox("Select Gender",["","Male","Female"])
if Gender == "Male":
    user_input.append(1)
elif Gender == "female":
    user_input.append(0)

Age = st.number_input("Enter Your Age",min_value=0,max_value=130)
user_input.append(Age)

Smoking = st.selectbox("Smoking",["","Yes","No"])
if Smoking == "No":
    user_input.append(1)
elif Smoking == "Yes":
    user_input.append(2)

Yellow_finger = st.selectbox("Yellow Fingers",["","Yes","No"])
if Yellow_finger == "No":
        user_input.append(1)
elif Yellow_finger == "Yes":
    user_input.append(2)

Anxiety = st.selectbox("Anxiety",["","Yes","No"])
if Anxiety == "No":
    user_input.append(1)
elif Anxiety == "Yes":
    user_input.append(2)

Peer_pressure = st.selectbox("Peer Pressure",["","Yes","No"])
if Peer_pressure == "No":
    user_input.append(1)
elif Peer_pressure == "Yes":
    user_input.append(2)

Chronic_disease = st.selectbox("Chronic Disease",["","Yes","No"])
if Chronic_disease == "No":
    user_input.append(1)
elif Chronic_disease == "Yes":
    user_input.append(2)
Fatigue = st.selectbox("Fatigue",["","Yes","No"])
if Fatigue == "No":
    user_input.append(1)
elif Fatigue == "Yes":
    user_input.append(2)
Allergy = st.selectbox("Allergy",["","Yes","No"])
if Allergy == "No":
    user_input.append(1)
elif Allergy == "Yes":
    user_input.append(2)

Wheezing = st.selectbox("Wheezing",["","Yes","No"])
if Wheezing == "No":
    user_input.append(1)
elif Wheezing == "Yes":
    user_input.append(2)

Alcohol_Consuming = st.selectbox("Alcohol Consuming",["","Yes","No"])
if Alcohol_Consuming == "No":
    user_input.append(1)
elif Alcohol_Consuming == "Yes":
    user_input.append(2)

Coughing = st.selectbox("Coughing",["","Yes","No"])
if Coughing == "No":
    user_input.append(1)
elif Coughing == "Yes":
    user_input.append(2)

Shortness_Of_Breath = st.selectbox("Shortness Of Breath",["","Yes","No"])
if Shortness_Of_Breath == "No":
    user_input.append(1)
elif Shortness_Of_Breath == "Yes":
    user_input.append(2)

Swallowing = st.selectbox("Swallowing",["","Yes","No"])
if Swallowing == "No":
    user_input.append(1)
elif Swallowing == "Yes":
    user_input.append(2)

Chest_pain = st.selectbox("Chest Pain",["","Yes","No"])
if Chest_pain == "No":
    user_input.append(1)
elif Chest_pain == "Yes":
    user_input.append(2)


button = st.button("Predict")
if button:
    if len(user_input) != 15:
        st.header("Please Fill All Options")
    else:
        reshaped_input = np.array(user_input).reshape(1,15)
        result = model.predict(reshaped_input)[0]
        if result == 1:
            st.header("-- Lung Cancer Detected --")
            st.header("-- Visit Doctor --")
        else:
            st.header("-- congratulation --")
            st.header("-- Cancer Not Detected --")




