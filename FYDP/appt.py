import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
import joblib
import streamlit as st

# Load model
model = joblib.load('pss_modell.pkl')

# Title
st.header('Dissolution Rate Prediction in ML Model')

# Load dataset
file_path = r"c:\Users\fatim\Downloads\dissolution_rate_samples.xlsx"
tablets_data = pd.read_excel(file_path, engine="openpyxl")

# Encoding function
def encode_feature(value, column_name):
    le = LabelEncoder()
    le.fit(tablets_data[column_name])
    return le.transform([value])[0]

# User Inputs
Drug_Form = st.selectbox('Select Drug Form', tablets_data['Drug Form'].unique())
Particle_Size = st.slider('Select Particle Size', 8.0, 10.0)
Lipophilicity_Index = st.slider('Select Lipophilicity Index', 8.0, 10.0)
Disintegrant = st.slider('Select Disintegrant (%)', 8.0, 10.0)
Binder = st.slider('Select Binder (%)', 2.0, 3.0)
Filler_Type = st.selectbox('Select Filler Type', tablets_data['Filler Type'].unique())
Surfactant = st.slider('Select Surfactant (%)', 0.0, 0.5)
Tablet_Hardness = st.slider('Select Tablet Hardness (kg/cm²)', 3.0, 8.0)
Lubricant = st.slider('Select Lubricant (%)', 0.3, 1.0)
Porosity = st.slider('Select Porosity (%)', 0.3, 1.0)
Coating_Thickness = st.slider('Select Coating Thickness (%)', 1.5, 3.0)
Granulation_Type = st.selectbox('Select Granulation Type', tablets_data['Granulation Type'].unique())
Compression_Force = st.slider('Select Compression Force (kN)', 7.0, 15.0)
Drying_Temperature = st.slider('Select Drying Temperature (°C)', 55.0, 63.0)
Mixing_Time = st.slider('Select Mixing Time (minutes)', 10.0, 18.0)
Fluid_Volume = st.slider('Select Fluid Volume (mL)', 120.0, 3000.0)
Gastric_Emptying_Rate = st.selectbox('Select Gastric Emptying Rate', tablets_data['Gastric Emptying Rate'].unique())

# Encode categorical variables
Drug_Form_enc = encode_feature(Drug_Form, 'Drug Form')
Filler_Type_enc = encode_feature(Filler_Type, 'Filler Type')
Granulation_Type_enc = encode_feature(Granulation_Type, 'Granulation Type')
Gastric_Emptying_Rate_enc = encode_feature(Gastric_Emptying_Rate, 'Gastric Emptying Rate')

# Predict on button click
if st.button("Predict"):
    input_data_model = pd.DataFrame([[
        Particle_Size, Drug_Form_enc, Lipophilicity_Index, Disintegrant, Binder,
        Filler_Type_enc, Surfactant, Tablet_Hardness, Lubricant, Porosity,
        Coating_Thickness, Granulation_Type_enc, Compression_Force, Drying_Temperature,
        Mixing_Time, Fluid_Volume, Gastric_Emptying_Rate_enc
    ]], columns=[
        'Particle Size (µm)', 'Drug Form', 'Log P (Lipophilicity Index)', 'Disintegrant (%)',
        'Binder (%)', 'Filler Type', 'Surfactant (%)', 'Tablet Hardness (kg/cm²)',
        'Lubricant (%)', 'Porosity (%)', 'Coating Thickness (%)', 'Granulation Type',
        'Compression Force (kN)', 'Drying Temperature (°C)', 'Mixing Time (minutes)',
        'Fluid Volume (mL)', 'Gastric Emptying Rate'
    ])

    st.write("Input Data:")
    st.write(input_data_model)

    tablets_rate = model.predict(input_data_model)
    st.markdown(f"### 📊 Predicted Dissolution Rate: **{tablets_rate[0]:.2f}**")

