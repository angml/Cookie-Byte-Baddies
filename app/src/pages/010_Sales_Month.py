import streamlit as st
import pandas as pd
import requests
from datetime import datetime

# --- Page config & styling ---
st.set_page_config(layout="wide")

st.markdown("""
    <style>
        .stApp { background-color: #f3e8ff; }
        .block-container { background-color: #f3e8ff; }
        html, body, [class*="css"] { color: #2d2d2d; }
        h1, h2, h3, h4 { color: #6a0dad; }
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
""", unsafe_allow_html=True)

# --- Header ---
st.title("📆 Sales by Month")
st.write("Select a year and month to view sales.")

# --- Month & Year selectors ---
today = datetime.today()
year = st.selectbox("Year", options=list(range(today.year, today.year - 5, -1)), index=0)
month = st.selectbox("Month", options=range(1, 13), format_func=lambda m: datetime(2000, m, 1).strftime('%B'))

# --- Button to fetch data ---
if st.button("🔍 Get Sales for Selected Month", type='primary', use_container_width=True):
    try:
        url = f"http://api:4000/sales/sales/month/{year}/{month}"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        if isinstance(data, list) and data:
            df = pd.DataFrame(data, columns=["SalesID", "Date", "TotalSales"])
            df["Date"] = pd.to_datetime(df["Date"])
            st.success(f"Sales data for {datetime(year, month, 1).strftime('%B %Y')}:")
            st.dataframe(df)
        else:
            st.warning("No sales found for this month.")
    except requests.exceptions.RequestException as e:
        st.error("Failed to fetch sales data.")
        st.text(f"Error: {e}")
