import streamlit as st
import pandas as pd
import mysql.connector
import folium
from streamlit_folium import st_folium

# ---------------------------------------------------------------------------------------------
# Layout
st.set_page_config(page_title="Gestão de Frota", layout="wide", initial_sidebar_state="collapsed", page_icon="🚛")

with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

car1, card2, card3 = st.columns(3)

col1, = st.columns(1)

# ---------------------------------------------------------------------------------------------
conn = mysql.connector.connect(
    host="srv1073.hstgr.io", 
    user="u771906953_barreto", 
    password="MQPj3:6GY_hFfjA", 
    database="u771906953_barreto" 
)

query = "SELECT * FROM u771906953_barreto.localizacoes"
df = pd.read_sql(query, conn)

df["lat"] = df["lat"].astype(float)
df["lon"] = df["lon"].astype(float)


total_amigos = df.shape[0]

# ---------------------------------------------------------------------------------------------

m = folium.Map(location=[df["lat"].mean(), df["lon"].mean()], zoom_start=2.5,tiles="CartoDB dark_matter")


for _, row in df.iterrows():
    folium.Marker(
        location=[row["lat"], row["lon"]],
        popup=f"{row['pessoa']}",
        tooltip=f"{row['pessoa']}",
        icon=folium.Icon(color="blue", icon="user"),
    ).add_to(m)


with col1:
    st.write("🌍 Onde Estão meus amigos?")
    st_folium(m, width=None, height=500)

with car1:
    st.metric("Total de Amigos",f'❤️ {total_amigos}')

# ---------------------------------------------------------------------------------------

# Adicionando uma borda personalizada ao layout
borda = """
            <style>
            [Data-testid="stColumn"]
            {
            background-color: #252629;
            border-radius: 15px;
            padding: 10px;
            text-align: center;
            opacity: 100%;
            box-shadow: 5px 5px 10px 0px rgba(0, 0, 0, 0.5); 
            }
            </style>
            """
st.markdown(borda, unsafe_allow_html=True)

# ----------------------------------------------------------------------------------

style2 = """
            <style>
            [Data-testid="stHeader"]
            {
            display: none;
            }
            </style>
            """
st.markdown(style2, unsafe_allow_html=True) 
