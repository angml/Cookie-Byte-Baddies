import logging
logger = logging.getLogger(__name__)
import pandas as pd
import streamlit as st
from streamlit_extras.app_logo import add_logo
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px
from modules.nav import SideBarLinks
import requests

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

st.title("Current Equipment")

#data frame
def fetch_equipment():
    try:
        response = requests.get('http://api:4000/eq/equipment')
        response.raise_for_status()
        if response.text.strip():
            data = response.json()
            if isinstance(data, list) and data:
                return pd.DataFrame(data, columns=["ID", "Name", "Price", "Lifespan"])
    except:
        pass
    return pd.DataFrame()

df = fetch_equipment()
st.dataframe(df)

# to input and update new equipment 
st.markdown("---")

tab1, tab2 = st.tabs(["Add", "Update"])
with tab1:
    st.subheader("➕ Add a New Equipment")
    with st.form("add_equipment_form"):
        name = st.text_input("Equipment Name")
        price = st.number_input("Price", min_value=0.0, format="%.2f")
        lifespan = st.number_input("Equipment Lifespan", min_value=0, step=1)
        submitted = st.form_submit_button("Add Equipment")

        if submitted:
            # Basic Validation: Check if all required fields are filled
            if not name or lifespan == 0 or price == 0:
                st.error("Please fill in all fields. Name, Price, and Lifespan are required.")
            else:
                new_equipment = {
                    "Name": name,
                    "Price": price,
                    "Lifespan": lifespan
                }

            try:
                post_url = 'http://api:4000/eq/equipment'
                post_response = requests.post(post_url, json=new_equipment)
                post_response.raise_for_status()

                st.success(f"New equipment {name} added successfully! Please refresh the page to see the updated table.")

            except requests.exceptions.RequestException as e:
                st.error("Failed to add new equipment information.")
                st.text(f"Error: {e}")
with tab2:
    # Update stock number
    st.subheader("🔁Update Equipment Information")
    with st.form("update_equipment_form"):
        selected_id = st.selectbox("Select Equipment ID to Update", df['ID'])
        selected = df[df['ID'] == selected_id]
        
        updated_name= st.text_input("Enter New Name")
        updated_price = st.number_input("Enter New Price", min_value=0.0, format="%.2f")
        updated_lifespan = st.number_input("Enter New Lifespan", min_value = 0, step=1)

        submitted = st.form_submit_button("Update Equipment Info")
        if submitted:
            updated_info = {
                "ID": int(selected["ID"].values[0]),
                "Name": updated_name,  
                "Price": float(updated_price),
                "Lifespan": int(updated_lifespan)
            }
            try:
                put_url = 'http://api:4000/eq/equipment'
                put_response = requests.put(put_url, json=updated_info)
                put_response.raise_for_status()

                st.success(f"Equipment ID: {int(selected['ID'].values[0])} updated successfully!")

            except requests.exceptions.RequestException as e:
                st.error("Failed to update.")
                st.text(f"Error: {e}")




            










