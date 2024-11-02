import pickle
import streamlit as st
import pandas as pd
from sklearn.preprocessing import StandardScaler

# Judul Aplikasi
st.title("Aplikasi Prediksi Penyakit Anemia")

# Memuat Model
# Pastikan Anda memiliki file model yang tersimpan sebagai 'model.pkl'
try:
    with open("model.pkl", "rb") as file:
        model = pickle.load(file)
except FileNotFoundError:
    st.error("Model file not found. Make sure 'model.pkl' is in the directory.")

# Input Data
st.sidebar.header("Input Parameter")

def user_input_features():
    gender = st.sidebar.selectbox("Gender", (0, 1))
    hemoglobin = st.sidebar.number_input("Hemoglobin")
    mch = st.sidebar.number_input("MCH")
    mchc = st.sidebar.number_input("MCHC")
    mcv = st.sidebar.number_input("MCV")
    result = st.sidebar.selectbox("Result", (0, 1))
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
        y_pred = model.predict(input_scaled)
        st.subheader("Hasil Prediksi")
        st.write("Anemia" if y_pred[0] == 1 else "Non-anemia")
    except Exception as e:
        st.error(f"Error during prediction: {e}")
