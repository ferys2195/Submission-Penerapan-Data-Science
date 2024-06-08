import streamlit as st
import pandas as pd
import joblib
from sklearn.preprocessing import StandardScaler


# 10. Buat aplikasi Streamlit yang menggunakan model dan scaler yang telah disimpan
def predict_dropout(data, model_and_scaler):
    model = model_and_scaler['model']
    scaler = model_and_scaler['scaler']
    data_scaled = scaler.transform(data)
    prediction = model.predict(data_scaled)
    return prediction

st.title("Student Dropout Prediction")

# Load model dan scaler yang sudah disimpan
try:
    model_and_scaler = joblib.load('model.joblib')
    st.write("Model loaded successfully!")
except FileNotFoundError:
    model_and_scaler = joblib.load('submission_2/model.joblib')
    st.write("Model loaded successfully!")

# Fungsi untuk membuat selectbox dengan tampilan Ya/Tidak tetapi mengembalikan nilai 0/1
def selectbox_ya_tidak(label):
    mapping = {"Tidak": 0, "Ya": 1}
    selected = st.selectbox(label, list(mapping.keys()))
    return mapping[selected]

def selectbox_male_female(label):
    mapping = {"Female": 0, "Male": 1}
    selected = st.selectbox(label, list(mapping.keys()))
    return mapping[selected]

def selectbox_application_method(label):
    mapping = {
        "1st phase - general contingent": 1,
        "Ordinance No. 612/93": 2,
        "1st phase - special contingent (Azores Island)": 5,
        "Holders of other higher courses": 7,
        "Ordinance No. 854-B/99": 10,
        "International student (bachelor)": 15,
        "1st phase - special contingent (Madeira Island)": 16,
        "2nd phase - general contingent": 17,
        "3rd phase - general contingent": 18,
        "Ordinance No. 533-A/99, item b2) (Different Plan)": 26,
        "Ordinance No. 533-A/99, item b3 (Other Institution)": 27,
        "Over 23 years old": 39,
        "Transfer": 42,
        "Change of course": 43,
        "Technological specialization diploma holders": 44,
        "Change of institution/course": 51,
        "Short cycle diploma holders": 53,
        "Change of institution/course (International)": 57
    }
    selected = st.selectbox(label, list(mapping.keys()))
    return mapping[selected]

# Input lainnya
curricular_units_1st_sem_grade = st.number_input("Nilai Mata Kuliah Semester 1", min_value=0.0, max_value=26.0, value=5.0)
curricular_units_1st_sem_approve = st.number_input("Nilai Lulus Mata Kuliah Semester 1", min_value=0.0, max_value=20.0, value=10.0)
curricular_units_2nd_sem_grade = st.number_input("Nilai Mata Kuliah Semester 2", min_value=0.0, max_value=20.0, value=10.0)
curricular_units_2nd_sem_approve = st.number_input("Nilai Lulus Mata Kuliah Semester 2", min_value=0.0, max_value=20.0, value=10.0)
# Menggunakan fungsi untuk selectbox dengan tampilan Ya/Tidak
tuition_fees_up_to_date = selectbox_ya_tidak("Biaya Kuliah Terbayar")
scholarship_holder = selectbox_ya_tidak("Penerima Beasiswa")
application_mode = selectbox_application_method("Metode Pendaftaran yang digunakan")
gender = selectbox_male_female("Jenis Kelamin")
age_at_enrollment = st.number_input("Usia Saat Pendaftaran", min_value=17, max_value=100, value=20)
debtor = selectbox_ya_tidak("Status Debitur")


features = [
    'Curricular_units_2nd_sem_approved',
    'Curricular_units_2nd_sem_grade',
    'Curricular_units_1st_sem_approved',
    'Curricular_units_1st_sem_grade',
    'Tuition_fees_up_to_date',
    'Scholarship_holder',
    'Application_mode',
    'Gender',
    'Age_at_enrollment',
    'Debtor'
]


# Mengumpulkan input dari pengguna
user_data = pd.DataFrame([[application_mode,
                           debtor,
                           tuition_fees_up_to_date,
                           gender,
                           scholarship_holder,
                           age_at_enrollment,
                           curricular_units_1st_sem_approve,
                           curricular_units_1st_sem_grade,
                           curricular_units_2nd_sem_approve,
                           curricular_units_2nd_sem_grade,
                          ]],
                         columns=features)



# Tampilkan data input pengguna
st.write("### Data Input Pengguna")
st.write(user_data)

# Prediksi dan tampilkan hasil
if st.button("Predict Dropout"):
    result = predict_dropout(user_data, model_and_scaler)
    if result[0] == 1:
        st.error("Mahasiswa kemungkinan akan dropout.")
    else:
        st.success("Mahasiswa kemungkinan tidak akan dropout.")