import pandas as pd
import numpy as np
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder
import joblib
import streamlit as st
model= joblib.load ('pss1_modell.pkl')
def encode_feature(value, column_name):
    le = LabelEncoder()
    le.fit(tablets_data[column_name])
    return le.transform([value])[0]
st.header ('Dissolution Rate Prediction in ML Model')
import streamlit as st
import pandas as pd

# Upload the file
uploaded_file = st.file_uploader("Upload your Excel file", type=["xlsx"])

# Check if file is uploaded
if uploaded_file is not None:
    tablets_data = pd.read_excel(uploaded_file, engine="openpyxl")
    
    # Optional: Show preview
    st.success("File uploaded successfully!")
    st.write(tablets_data.head())
else:
    st.warning("Please upload an Excel file to continue.")



tablets_data = pd.read_excel(file_path, engine="openpyxl") 

Drug_Form=st.selectbox('Select Drug Form', tablets_data ['Drug Form'].unique())
Particle_Size=st.slider('Select Particle Size', 8.0, 10.0)
Lipophilicity_Index=st.slider('Select Lipophilicity Index', 0.8, 1.0)
Disintegrant=st.slider('Select Disintegrant (%)', 8.0, 10.0)
Binder=st.slider('Select Binder (%)', 2.0,3.0)
Filler_Type=st.selectbox('Select Filler Type', tablets_data ['Filler Type'].unique())
Surfactant=st.slider('Select Surfactant (%)', 0.0, 0.5)
Tablet_Hardness=st.slider('Select Tablet Hardness (kg/cm²)', 3.0, 8.0)
Lubricant=st.slider('Select Lubricant (%)', 0.3, 1.0)
Porosity=st.slider('Select Porosity (%)', 5, 15)
Coating_Thickness=st.slider('Select Coating Thickness (%)', 1.5 , 3.0)
Granulation_Type=st.selectbox('Select Granulation Type', tablets_data ['Granulation Type'].unique())
Compression_Force=st.slider('Select Compression Force (kN)', 7.0,15.0)
Drying_Temperature =st.slider('Select Drying Temperature (°C)', 55.0,63.0)
Mixing_Time=st.slider('Select Mixing Time (minutes)', 10.0, 18.0)
Fluid_Volume=st.slider('Select Fluid Volume (mL)', 120.0, 300.0)
Gastric_Emptying_Rate=st.selectbox('Select Gastric Emptying Rate', tablets_data ['Gastric Emptying Rate'].unique())
 




if st.button("Predict"):
    input_data_model= pd.DataFrame(
        [[Particle_Size,Drug_Form, Lipophilicity_Index, Disintegrant, Binder,
        Filler_Type, Surfactant, Tablet_Hardness, Lubricant, Porosity,
        Coating_Thickness, Granulation_Type, Compression_Force, Drying_Temperature,
        Mixing_Time, Fluid_Volume, Gastric_Emptying_Rate
    ]],
      columns=[
        'Particle Size (µm)','Drug Form', 'Log P (Lipophilicity Index)', 'Disintegrant (%)',
        'Binder (%)', 'Filler Type', 'Surfactant (%)', 'Tablet Hardness (kg/cm²)',
        'Lubricant (%)', 'Porosity (%)', 'Coating Thickness (%)', 'Granulation Type',
        'Compression Force (kN)', 'Drying Temperature (°C)', 'Mixing Time (minutes)',
        'Fluid Volume (mL)', 'Gastric Emptying Rate'
    ])
    input_data_model['Drug Form'].replace(['Amorphous','Crystalline'],[1,2],inplace=True)
    input_data_model['Filler Type'].replace(['Water-Soluble (MCC, Lactose)', 'Water-Insoluble (e.g., DCP)'],[1,2], inplace=True)
    input_data_model['Granulation Type'].replace(['Wet Granulation' ,'Dry Granulation'],[1,2], inplace=True)
    input_data_model['Gastric Emptying Rate'].replace(['Fast' ,'Slow'],[1,2], inplace=True)
    
   
   
   
   
    st.write(input_data_model)
 



    tablets_rate = model.predict(input_data_model)
    st.markdown(f"### 📊 Predicted Dissolution Rate: **{tablets_rate[0]:.2f}**")


