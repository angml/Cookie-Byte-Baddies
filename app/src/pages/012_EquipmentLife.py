import logging
logger = logging.getLogger(__name__)
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px
from modules.nav import SideBarLinks
import requests
from datetime import datetime, timedelta

st.set_page_config(layout="wide")
SideBarLinks()

# Styling
st.markdown(
    """
    <style>
        .stApp {
            background-color: #f3e8ff;
        }
        .block-container {
            background-color: #f3e8ff;
        }
        html, body, [class*="css"]  {
            color: #2d2d2d;
        }
        h1, h2, h3, h4 {
            color: #6a0dad;
        }
        button {
            background-color: #9b5de5 !important;
            color: white !important;
            border: 2px solid white !important;
            border-radius: 6px !important;
        }
        .stDataFrame {
            background-color: #ffc0cb !important;
            border: 1px solid #ffaad4;
            border-radius: 6px;
            padding: 6px;
        }
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Equipment Lifecycle")
#data frame
st.header("Top 10 Oldest Equipment")
def fetch_oldest():
    try:
        response = requests.get('http://api:4000/eq/equipment/oldest')
        response.raise_for_status()
        if response.text.strip():
            data = response.json()
            if isinstance(data, list) and data:
                return pd.DataFrame(data)
    except:
        pass
    return pd.DataFrame()

df = fetch_oldest()
df = df.rename(columns={
    "ID": "Equipment ID",
    "Name": "Name",
    "Lifespan": "Lifespan (yrs)",
    "DeliveryDate": "Date Acquired"})

df["Date Acquired"]= pd.to_datetime(df['Date Acquired'])
df['end_date'] = df['Date Acquired'] + df['Lifespan (yrs)'].apply(lambda x: timedelta(days=round(x * 365.25)))
df['time_left'] = df['end_date'] - datetime.now()

df['Months Left'] = round(df['time_left'].dt.days/ 30.44)

df["Date Acquired"]= df["Date Acquired"].dt.date

st.dataframe(df[["Equipment ID", "Name","Lifespan (yrs)","Date Acquired", "Months Left"]])

st.header("Top 10 Equipment with the Shortest Lifespans")
def fetch_shortest():
    try:
        response = requests.get('http://api:4000/eq/equipment/short')
        response.raise_for_status()
        if response.text.strip():
            data = response.json()
            if isinstance(data, list) and data:
                return pd.DataFrame(data)
    except:
        pass
    return pd.DataFrame()

df = fetch_shortest()
df = df.rename(columns={
    "ID": "Equipment ID",
    "Name": "Name",
    "Lifespan": "Lifespan (yrs)",
    "DeliveryDate": "Date Acquired"})

df["Date Acquired"]= pd.to_datetime(df['Date Acquired'])
df['end_date'] = df['Date Acquired'] + df['Lifespan (yrs)'].apply(lambda x: timedelta(days=round(x * 365.25)))
df['time_left'] = df['end_date'] - datetime.now()

df['Months Left'] = round(df['time_left'].dt.days/ 30.44)

df["Date Acquired"]= df["Date Acquired"].dt.date

st.dataframe(df[["Equipment ID", "Name","Lifespan (yrs)","Date Acquired", "Months Left"]])


