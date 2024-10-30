import pickle
import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler

# Judul Aplikasi
st.title("Aplikasi Prediksi Penyakit Anemia")

# Input Data
st.sidebar.header("Input Parameter")
def user_input_features():
  gender = st.sidebar.selectbox("Gender"(0, 1))
  hemogolobin = st.number_input("Hemogologi")
  mch =
  mchc = 
  mcv = 
  result =
