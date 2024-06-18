import pickle
import streamlit as st
import pandas as pd
import zipfile
from io import BytesIO
import os
import tempfile

# path_to_file = "prediksi_harga_rumah_smg.sav"  
# model = pickle.load(open(path_to_file, 'rb'))

filename = 'prediksi_harga_rumah_smg.zip'
with zipfile.ZipFile(filename, 'r') as zip_ref:
    # List all the contents of the zip file
    file_list = zip_ref.namelist()
        
    with tempfile.TemporaryDirectory() as temp_dir:
        # Extract all files to the temporary directory
        zip_ref.extractall(temp_dir)
            
        # Load pickle files from the extracted contents
        for file_name in file_list:
            file_path = os.path.join(temp_dir, file_name)
            # with open(file_path, 'rb') as f:
            model = joblib.load(file_path)

# Membuat sidebar
test = st.sidebar.radio("Menu", ["Beranda", "Data","Labelling", "Prediksi", "Kontak"])

# Halaman Beranda
if test == "Beranda":
    st.header("Halo semuanya selamat datang :wave:")
    st.markdown("#### Ini merupakan website yang dapat memprediksi harga rumah di Kota Semarang sesuai dengan kriteria yang diinginkan oleh calon pembeli.")
    
    st.markdown("###### ")
    st.image('Poster Peta Kota Semarang.png')
    st.markdown("###### ")
    
    st.markdown("#### Dengan adanya website ini, diharapkan dapat membantu para calon pembeli dalam menentukan harga rumah yang sesuai dan memenuhi kriteria rumah impiannya.")
    st.markdown("#### Selamat mencoba!")

# Halaman Data
if test == "Data":
    st.header("Data Bersih")
    st.write("Berikut merupakan data yang digunakan dalam prediksi harga rumah di Kota Semarang.") 
    data = pd.read_csv("df_cleaning.csv")
    st.write(data)
    st.write("Sumber Data : Rumah123.com (Kota Semarang) per Maret 2024")


# Halaman Labelling
if test == "Labelling":
    st.subheader("Labelling")
    st.markdown("##### Untuk variabel 'Jenis Rumah' dan 'Lokasi' merupakan variabel kategorik sehingga harus dikonversi kedalam variabel numerik agar dapat di prediksi")
    st.markdown("###### Variabel jenis rumah")
    st.text("0 = jenis rumah biasa")
    st.text("1 = jenis rumah featured")
    st.text("2 = jenis rumah premier")

    st.markdown("###### ")
    st.markdown("###### Variabel lokasi")
    st.text("0 = Banyumanik, Semarang")
    st.text("1 = Candisari, Semarang")
    st.text("2 = Gajah Mungkur, Semarang")
    st.text("3 = Gayamsari, Semarang")
    st.text("4 = Genuk, Semarang")
    st.text("5 = Gunung Pati, Semarang")
    st.text("6 = Mijen, Semarang")
    st.text("7 = Ngaliyan, Semarang")
    st.text("8 = Pedurungan, Semarang")
    st.text("9 = Semarang Barat, Semarang")
    st.text("10 = Semarang Selatan, Semarang")
    st.text("11 = Semarang Tengah, Semarang")
    st.text("12 = Semarang Timur, Semarang")
    st.text("13 = Semarang Utara, Semarang")
    st.text("14 = Tembalang, Semarang")


# Halaman Prediksi
if test == "Prediksi":
    st.subheader("Prediksi harga rumah di Kota Semarang")
    
    # Membuat kolom prediksi
    col1, col2 = st.columns(2)

    with col1:
        Jenis_Rumah = st.number_input('Input Jenis Rumah')
    with col2:
        Lokasi = st.number_input('Input Lokasi')
    with col1:
        KT = st.number_input('Input Jumlah Kamar Tidur')
    with col2:
        KM = st.number_input('Input Jumlah Kamar Mandi')
    with col1:
        Garasi = st.number_input('Input Garasi (menampung berapa mobil)')
    with col2:
        LT = st.number_input('Input Luas Tanah (m2)')
    with col1:
        LB = st.number_input('Input Luas Bangunan (m2)')

    predict = ''

    
    if st.button("Prediksi Harga Rumah (miliar)"):
        predict = model.predict(
            [[Jenis_Rumah, Lokasi, KT, KM, Garasi, LT, LB]]
        )
        st.write("Berikut merupakan prediksi harga rumah sesuai dengan kriteria dalam satuan miliar : ", predict)
    
    
    
# Halaman Kontak
if test == "Kontak":
    st.subheader("Hai, mari terhubung! :wave:")
    col1, col2 = st.columns(2)
    with col1:
        st.image('ciss.png')
    with col2:
        st.write("Nama     : Fransisca Mulya Sari")
        st.write("LinkedIn : https://www.linkedin.com/in/fransisca-mulya-sari-a51853260/")
        st.write("Github   : https://github.com/FransiscaaMS")
        st.write("Email    : fransiscaams@gmail.com")
    
