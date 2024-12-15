import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

sns.set(style='dark')

# Mapping untuk memudahkan pembacaan
season_mapping = {1: 'Musim Semi', 2: 'Musim Panas', 3: 'Musim Gugur', 4: 'Musim Dingin'}
weather_mapping = {1: 'Cerah/Sedikit Berawan', 2: 'Berawan/Berkabut', 3: 'Hujan Ringan/Salju', 4: 'Cuaca Ekstrim'}

def create_sewa_sepeda_workingday(df):
    return df.groupby(by="workingday")["cnt"].sum()

def create_sewa_sepeda_weathersit(df):
    return df.groupby(by="weathersit")["cnt"].sum().reset_index()

all_df = pd.read_csv("day.csv")

# Ubah nilai numerik season dan weathersit ke string untuk memudahkan
all_df['season'] = all_df['season'].map(season_mapping)
all_df['weathersit'] = all_df['weathersit'].map(weather_mapping)

with st.sidebar:
    st.header("Selamat Datang")
    st.text("Penyewaan Sepeda Berkualitas by Ariel Gibranu")
    st.image("sepeda.jpg")
    st.caption('Ariel Gibranu (c) 2024')


    # Opsi untuk memilih musim (Sekarang menggunakan mapping)
    season_options = ['Semua Musim'] + list(season_mapping.values())
    selected_season = st.selectbox('Pilih Musim', season_options)




st.header('Analisis Data Bike Sharing Dataset :sparkles:')



# Filtering Dataframe berdasarkan musim yang dipilih
if selected_season == 'Semua Musim':
    filtered_df = all_df
else:
    filtered_df = all_df[all_df['season'] == selected_season]

# --- Visualisasi 1: Berdasarkan Hari Kerja (Setelah Filtering) ---
st.subheader("Jumlah Penyewaan Sepeda Berdasarkan Hari Kerja")

by_workingday = create_sewa_sepeda_workingday(filtered_df) # Gunakan filtered_df disini

fig_workingday, ax_workingday = plt.subplots(figsize=(8, 6))
by_workingday.plot(kind='bar', ax=ax_workingday, color=["skyblue", "skyblue"])
ax_workingday.set_title('Jumlah Penyewaan Sepeda Berdasarkan Hari Kerja')
ax_workingday.set_xlabel('Hari Kerja')
ax_workingday.set_ylabel('Jumlah Total Penyewaan')
ax_workingday.set_xticklabels(['Weekend/Libur', 'Hari Kerja'], rotation=0)

for p in ax_workingday.patches:
    ax_workingday.annotate(format(p.get_height(), '.0f'),
                            (p.get_x() + p.get_width() / 2., p.get_height()),
                            ha='center', va='center',
                            xytext=(0, 4),
                            textcoords='offset points')
st.pyplot(fig_workingday)

# --- Visualisasi 2: Berdasarkan Kondisi Cuaca (Setelah Filtering) ---
st.subheader("Jumlah Penyewaan Sepeda Berdasarkan Kondisi Cuaca")

by_weathersit = create_sewa_sepeda_weathersit(filtered_df) # Gunakan filtered_df disini

fig_weather, ax_weather = plt.subplots(figsize=(10, 6)) # Buat figure dan axes sendiri
sns.barplot(x='weathersit', y='cnt', data=by_weathersit, order=list(weather_mapping.values()), palette=["skyblue", "skyblue", "skyblue", "skyblue"], ax=ax_weather) # Menggunakan ax_weather
ax_weather.set_title('Jumlah Penyewaan Sepeda Berdasarkan Kondisi Cuaca')
ax_weather.set_xlabel('Kondisi Cuaca')
ax_weather.set_ylabel('Jumlah Penyewaan')
ax_weather.tick_params(axis='x', rotation=0)


for p in ax_weather.patches:
    ax_weather.annotate(format(p.get_height(), '.0f'),
                        (p.get_x() + p.get_width() / 2., p.get_height()),
                        ha='center', va='center',
                        xytext=(0, 4),
                        textcoords='offset points')

st.pyplot(fig_weather) # Tampilkan figure yang benar