import logging
logger = logging.getLogger(__name__)
import pandas as pd
import streamlit as st
from streamlit_extras.app_logo import add_logo
import world_bank_data as wb
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px
from modules.nav import SideBarLinks
import requests

# Set page config
st.set_page_config(layout="wide")

# Show appropriate sidebar links for the role of the currently logged in user
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
        html, body, [class*="css"] {
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

# Title
st.title("View Sales Transactions")

if st.button('📆 View: Sales by Month', type='primary', use_container_width=True):
    st.switch_page('pages/010_Sales_Month.py')

if st.button('🍪 View: Sales by Item', type='primary', use_container_width=True):
    st.switch_page('pages/011_Sales_Item.py')

st.markdown("---")

st.write("Below is a list of all sales transactions:")

# API endpoint for sales data
url = 'http://api:4000/sales/sales'

# Fetch sales data
try:
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

    if isinstance(data, list) and data:
        df = pd.DataFrame(data, columns=["SalesID", "Date", "TotalSales"])
        df["Date"] = pd.to_datetime(df["Date"])
        df = df.sort_values(by="Date", ascending=True)
        st.dataframe(df)
    else:
        st.warning("No sales data found.")
except requests.exceptions.RequestException as e:
    st.error("Failed to fetch sales data.")
    st.text(f"Error: {e}")
