# create environment for windows
# python -m venv myenv
# activate environment
# myenv\Scripts\activate
# pip install streamlit scikit-learn pandas numpy
# streamlit run app.py


import pickle
import streamlit as st
import numpy as np
import pandas as pd

st.title('🏠 House Price Prediction App')

# load model
model = pickle.load(open('lr_model.pkl','rb'))

# input features
Square_Footage = st.number_input('Square Footage', min_value=500, max_value=10000, value=1500)
Num_Bedrooms = st.number_input('Number of Bedrooms', min_value=1, max_value=10, value=3)
Num_Bathrooms = st.number_input('Number of Bathrooms', min_value=1, max_value=10, value=2)
Year_Built = st.number_input('Year Built', min_value=1900, max_value=2026, value=2010)
Lot_Size = st.number_input('Lot Size', min_value=0.0, max_value=20.0, value=1.0)
Garage_Size = st.number_input('Garage Size', min_value=0, max_value=5, value=1)
Neighborhood_Quality = st.number_input('Neighborhood Quality', min_value=1, max_value=10, value=5)

# define dataframe
input_features = pd.DataFrame({
    'Square_Footage': [Square_Footage],
    'Num_Bedrooms': [Num_Bedrooms],
    'Num_Bathrooms': [Num_Bathrooms],
    'Year_Built': [Year_Built],
    'Lot_Size': [Lot_Size],
    'Garage_Size': [Garage_Size],
    'Neighborhood_Quality': [Neighborhood_Quality]
})

# prediction
if st.button('Predict'):
    prediction = model.predict(input_features)
    st.success(f'🏠 Predicted House Price: ₹ {prediction[0]:,.2f}')