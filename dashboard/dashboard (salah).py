import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')

def create_sewa_sepeda_workingday(df):
    sewa_sepeda_workingday = df.groupby(by="workingday").size() 
    return sewa_sepeda_workingday

def create_sewa_sepeda_weathersit(df):
    sewa_sepeda_weathersit = df.groupby(by="weathersit").size() 
    return sewa_sepeda_weathersit

all_df = pd.read_csv("dashboard/day.csv")

by_workingday = create_sewa_sepeda_workingday(all_df).reset_index(name='count')
by_weathersit = create_sewa_sepeda_weathersit(all_df).reset_index(name='count')



with st.sidebar:
    st.header("Selamat Datang")
    st.text("Penyewaan Sepeda")
    st.image("dashboard/sepeda.jpg")
    st.caption('Ariel Gibranu (c) 2024')




st.header('Analisis Data Bike Sharing Dataset :sparkles:')



st.subheader("Jumlah Penyewaan Sepeda Berdasarkan Hari Kerja")


colors = ["#90CAF9", "#90CAF9"]




plt.figure(figsize=(8, 6))
ax = sns.barplot(x='workingday', y='count', data=by_workingday, palette=colors) 
plt.title('Jumlah Penyewaan Sepeda Berdasarkan Hari Kerja')
plt.xlabel('Hari Kerja')
plt.ylabel('Jumlah Penyewaan')
plt.xticks([0, 1], ['Weekend/Libur', 'Hari Kerja'])

for p in ax.patches:
    ax.annotate(format(p.get_height(), '.0f'), 
                (p.get_x() + p.get_width() / 2., p.get_height()), 
                ha='center', va='center', 
                xytext=(0, 4), 
                textcoords='offset points')

st.pyplot(plt)



st.subheader("Jumlah Penyewaan Sepeda Berdasarkan Kondisi Cuaca")


colors = ["#90CAF9", "#D3D3D3", "#D3D3D3", "#D3D3D3"]

plt.figure(figsize=(10, 6))
ax = sns.barplot(x='weathersit', y='count', data=by_weathersit, order=[1, 2, 3, 4], palette=colors)
plt.title('Jumlah Penyewaan Sepeda Berdasarkan Kondisi Cuaca')
plt.xlabel('Kondisi Cuaca')
plt.ylabel('Jumlah Penyewaan')
plt.xticks([0, 1, 2, 3], ['Cerah/Sedikit Berawan', 'Berawan/Berkabut', 'Hujan Ringan/Salju', 'Cuaca Ekstrim'])

for p in ax.patches:
    ax.annotate(format(p.get_height(), '.0f'), 
                (p.get_x() + p.get_width() / 2., p.get_height()), 
                ha='center', va='center', 
                xytext=(0, 4), 
                textcoords='offset points')

st.pyplot(plt)