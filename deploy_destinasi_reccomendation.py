# Deploy Destinasi Wisata Demoghrapic Recommendation

# ==========================================
import pandas as pd
import streamlit as st

# ==========================================
st.title('''
    REKOMENDASI DESTINASI WISATA KOTA JAKARTA, YOGYAKARTA, BANDUNG, SEMARANG dan SURABAYA
         BERDASARKAN DEMOGRAPICH RECOMMENDATION   
''')

# Menampilkan DataFrame
df = pd.read_csv('MASUKAN FILE PATH df_destinasi_wisata.csv YANG TELAH DISIMPAN PADA PERANGKAT')

# sidebar
st.sidebar.header("Masukkan kriteria destinasi yang anda inginkan :")
kota = st.sidebar.selectbox('City', [None, 'Jakarta', 'Yogyakarta', 'Bandung', 'Semarang', 'Surabaya'])
kategori = st.sidebar.selectbox('Category', [None, 'Budaya', 'Taman Hiburan', 'Cagar Alam', 'Bahari', 'Pusat Perbelanjaan', 'Tempat Ibadah'])
maxharga = st.sidebar.slider('Price', min_value=0, max_value=900000, value=500000)

if kota is not None:
    df = df[df['City'] == kota]
if kategori is not None:
    df = df[df['Category'] == kategori]
if maxharga is not None:
    df = df[df['Price'] <= maxharga]

df = df.sort_values('Score', ascending=False).reset_index(drop=True)
df = df[['City', 'Category', 'Price', 'Place_Name', 'Description']]
   
st.dataframe(df, width=999999999)