import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

sns.set(style='dark')

def create_sewa_sepeda_workingday(df):
    return df.groupby(by="workingday")["cnt"].sum()

def create_sewa_sepeda_weathersit(df):
    return df.groupby(by="weathersit")["cnt"].sum()

all_df = pd.read_csv("day.csv")

by_workingday = create_sewa_sepeda_workingday(all_df)
by_weathersit = create_sewa_sepeda_weathersit(all_df).reset_index(name='count')

with st.sidebar:
    st.header("Selamat Datang")
    st.text("Penyewaan Sepeda Berkualitas by Ariel Gibranu")
    st.image("sepeda.jpg")
    st.caption('Ariel Gibranu (c) 2024')

st.header('Analisis Data Bike Sharing Dataset :sparkles:')

st.subheader("Jumlah Penyewaan Sepeda Berdasarkan Hari Kerja")

# Visualisasi
fig_workingday, ax_workingday = plt.subplots(figsize=(8, 6))
by_workingday.plot(kind='bar', ax=ax_workingday, color=["skyblue", "skyblue"]) # Warna berbeda
ax_workingday.set_title('Jumlah Penyewaan Sepeda Berdasarkan Hari Kerja')
ax_workingday.set_xlabel('Hari Kerja')
ax_workingday.set_ylabel('Jumlah Total Penyewaan')
ax_workingday.set_xticklabels(['Weekend/Libur', 'Hari Kerja'], rotation=0)  # Label yang lebih deskriptif

# kasih label diatas biar jelas jumlahnya
for p in ax_workingday.patches:
    ax_workingday.annotate(format(p.get_height(), '.0f'),
                        (p.get_x() + p.get_width() / 2., p.get_height()),
                        ha='center', va='center',
                        xytext=(0, 4),
                        textcoords='offset points')
st.pyplot(fig_workingday)




st.subheader("Jumlah Penyewaan Sepeda Berdasarkan Kondisi Cuaca")

colors = ["skyblue", "skyblue", "skyblue", "skyblue"]

plt.figure(figsize=(10, 6))
ax = sns.barplot(x='weathersit', y='count', data=by_weathersit, order=[1, 2, 3, 4], palette=colors)
plt.title('Jumlah Penyewaan Sepeda Berdasarkan Kondisi Cuaca')
plt.xlabel('Kondisi Cuaca')
plt.ylabel('Jumlah Penyewaan')
plt.xticks([0, 1, 2, 3], ['Cerah/Sedikit Berawan', 'Berawan/Berkabut', 'Hujan Ringan/Salju', 'Cuaca Ekstrim'])


# kasih label diatas biar jelas jumlahnya
for p in ax.patches:
    ax.annotate(format(p.get_height(), '.0f'),
                (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='center', va='center',
                xytext=(0, 4),
                textcoords='offset points')

st.pyplot(plt)