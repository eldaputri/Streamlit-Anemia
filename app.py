import pickle
import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler

# Judul Aplikasi
st.title("Aplikasi Prediksi Penyakit Anemia")

# Input Data
import os
os.system('pip install scikit-learn')

import streamlit as st
from sklearn.model_selection import train_test_split  # Import yang sebelumnya menyebabkan error
import pandas as pd

# Sidebar for input parameters
st.sidebar.header("Input Parameter")

def user_input_features():
    gender = st.sidebar.selectbox("Gender", (0, 1))
    hemoglobin = st.sidebar.number_input("Hemoglobin")
    mch = st.sidebar.number_input("MCH")
    mchc = st.sidebar.number_input("MCHC")
    mcv = st.sidebar.number_input("MCV")
    result = st.sidebar.selectbox("Result", (0, 1))
    
    # Creating a dictionary of user inputs
    data = {
        'gender': gender,
        'hemoglobin': hemoglobin,
        'mch': mch,
        'mchc': mchc,
        'mcv': mcv,
        'result': result
    }
    features = pd.DataFrame(data, index=[0])
    return features

# Display user input features
df = user_input_features()
st.write(df)
