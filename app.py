import streamlit as st
import pandas as pd
import pickle
from sklearn.preprocessing import StandardScaler
from sklearn.naive_bayes import BernoulliNB

# Judul Aplikasi
st.title("Aplikasi Prediksi Penyakit Anemia")

# Memuat Model
# Pastikan model telah disimpan sebagai 'naive_bayes_model.pkl'
try:
    with open("naive_bayes_model.pkl", "rb") as file:
        model = pickle.load(file)
except FileNotFoundError:
    st.error("Model file not found. Make sure 'naive_bayes_model.pkl' is in the directory.")

# Input Data
st.sidebar.header("Masukkan Parameter")

def user_input_features():
    gender = st.sidebar.selectbox("Gender (0: Pria, 1: Wanita)", (0, 1))
    hemoglobin = st.sidebar.number_input("Hemoglobin", min_value=0.0, max_value=20.0, value=13.5)
    mch = st.sidebar.number_input("MCH", min_value=0.0, max_value=50.0, value=30.0)
    mchc = st.sidebar.number_input("MCHC", min_value=0.0, max_value=40.0, value=33.0)
    mcv = st.sidebar.number_input("MCV", min_value=0.0, max_value=100.0, value=90.0)
    
    data = {
        "Gender": gender,
        "Hemoglobin": hemoglobin,
        "MCH": mch,
        "MCHC": mchc,
        "MCV": mcv
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
        # Prediksi dengan model Naive Bayes
        y_pred = model.predict(input_scaled)
        st.subheader("Hasil Prediksi")
        st.write("Anemia" if y_pred[0] == 1 else "Non-anemia")
    except Exception as e:
        st.error(f"Error during prediction: {e}")
