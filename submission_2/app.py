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
except FileNotFoundError:
    model_and_scaler = joblib.load('submission_2/model.joblib')

# Fungsi untuk membuat selectbox dengan tampilan Ya/Tidak tetapi mengembalikan nilai 0/1
def selectbox_ya_tidak(label):
    mapping = {"No": 0, "Yes": 1}
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

curricular_units_1st_sem_grade = st.number_input("Curricular Unit 1st Grade", min_value=0.0, max_value=26.0, value=5.0)
curricular_units_1st_sem_approve = st.number_input("Curricular Unit 1st Approved", min_value=0.0, max_value=20.0, value=10.0)
curricular_units_2nd_sem_grade = st.number_input("Curricular Unit 2nd Grade", min_value=0.0, max_value=20.0, value=10.0)
curricular_units_2nd_sem_approve = st.number_input("Curricular Unit 2nd Approved", min_value=0.0, max_value=20.0, value=10.0)

tuition_fees_up_to_date = selectbox_ya_tidak("Tuition fees up to date ?")
scholarship_holder = selectbox_ya_tidak("Scholarship Holder ?")
application_mode = selectbox_application_method("Application Mode")
gender = selectbox_male_female("Gender")
age_at_enrollment = st.number_input("Age at Enrollment", min_value=17, max_value=100, value=20)
debtor = selectbox_ya_tidak("Debtor ?")


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


# Prediksi dan tampilkan hasil
if st.button("Predict Dropout"):
    result = predict_dropout(user_data, model_and_scaler)
    if result[0] == 1:
        st.error("Mahasiswa kemungkinan akan dropout.")
    else:
        st.success("Mahasiswa kemungkinan tidak akan dropout.")