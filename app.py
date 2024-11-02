import streamlit as st
import pandas as pd
import numpy as np
from sklearn.naive_bayes import BernoulliNB
from sklearn.preprocessing import StandardScaler
import pickle

# Judul Aplikasi
st.title("Aplikasi Prediksi Penyakit Anemia Menggunakan Naive Bayes")

# Memuat Model
# Pastikan Anda memiliki file model yang tersimpan sebagai 'naive_bayes_model.pkl'
try:
    with open("naive_bayes_model.pkl", "rb") as file:
        model = pickle.load(file)
except FileNotFoundError:
    st.error("Model file not found. Make sure 'naive_bayes_model.pkl' is in the directory.")

# Input Parameter dari Pengguna
st.sidebar.header("Input Parameter")

def user_input_features():
    gender = st.sidebar.selectbox("Gender (0 = Female, 1 = Male)", (0, 1))
    hemoglobin = st.sidebar.number_input("Hemoglobin Level (g/dL)")
    mch = st.sidebar.number_input("MCH (Mean Corpuscular Hemoglobin)")
    mchc = st.sidebar.number_input("MCHC (Mean Corpuscular Hemoglobin Concentration)")
    mcv = st.sidebar.number_input("MCV (Mean Corpuscular Volume)")
    result = st.sidebar.selectbox("Result (0 = Non-Anemia, 1 = Anemia)", (0, 1))
    
    data = {
        "Gender": gender,
        "Hemoglobin": hemoglobin,
        "MCH": mch,
        "MCHC": mchc,
        "MCV": mcv,
        "Result": result
    }
    features = pd.DataFrame(data, index=[0])
    return features

# Menyiapkan input fitur dari pengguna
input_df = user_input_features()

# Preprocessing: Standarisasi
scaler = StandardScaler()
input_scaled = scaler.fit_transform(input_df)

# Prediksi
if st.button("Prediksi"):
    try:
        # Melakukan prediksi
        y_pred = model.predict(input_scaled)
        st.subheader("Hasil Prediksi")
        st.write("Anemia" if y_pred[0] == 1 else "Non-anemia")
    except Exception as e:
        st.error(f"Error during prediction: {e}")
