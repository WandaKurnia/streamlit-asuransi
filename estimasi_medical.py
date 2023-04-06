import pickle
import streamlit as st

model = pickle.load(open('estimasi_medical.sav','rb'))

st.title('Estimasi Biaya Medis Dalam US Dolar')

age = st.number_input('Input Umur')
sex = st.number_input('Input Jenis Kelamin(F = 2 or M = 1)')
bmi = st.number_input('Input BMI')
children = st.number_input('Input Jumlah Anak Berdasarkan Asuransi')
smoker = st.number_input('Apakah Anda Perokok? (N = 2 or Y = 1)')

predict =''

if st.button('Estimasi Asuransi'):
    predict = model.predict(
        [[age, sex, bmi, children, smoker]]
    )
    st.write('Estimasi biaya medis dalam Dolar : ', predict)
    st.write('Estimasi biaya medis dalam IDR (Juta): ', predict*15000)
 