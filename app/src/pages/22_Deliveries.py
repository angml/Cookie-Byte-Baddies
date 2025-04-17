import logging
logger = logging.getLogger(__name__)
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px
from modules.nav import SideBarLinks
import requests
from datetime import datetime

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

          .stTabs [role="tab"] {
            padding: 0.75em 2em;
            font-size: 1rem;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Sip Happens' Orders")

#data frame
def fetch_supplierOrders():
    try:
        response = requests.get('http://api:4000/o/orders/supplier')
        response.raise_for_status()
        if response.text.strip():
            data = response.json()
            if isinstance(data, list) and data:
                return pd.DataFrame(data)
    except:
        pass
    return pd.DataFrame()

df = fetch_supplierOrders()
df = df.rename(columns={
    "ID": "Order ID",
    "OrderQuantity": "Order Quantity",
    "DeliveryDate": "Delivery Date",
    "Delivered": "Status"})

df["Status"] = df["Status"].map({1: "Yes", 0: "No"})
df = df[["Status","Order ID","Order Quantity","Delivery Date"]]
st.dataframe(df)

tab1, tab2 = st.tabs(["Update Delivery Status", "View Order Details"])

with tab1:
    st.subheader("🔁Update Delivery Status")
    with st.form("update_status_form"):
        selected_id = st.selectbox("Select Order ID to Update", df['Order ID'])
        selected = df[df['Order ID'] == selected_id]

        updated_delivery_date = st.date_input("Delivery Date", value=datetime.now())
        updated_delivery_time = st.time_input("Delivery time", value=datetime.now().time())
        updated_status = st.checkbox("Delivered?", value=False)

        submitted = st.form_submit_button("Update Order Status")
        if submitted:
            supplier_name = "Sanchez & Sons Sweet Deliveries"
            delivery_datetime_str = datetime.combine(updated_delivery_date, updated_delivery_time).strftime('%Y-%m-%d %H:%M:%S')
            updated_info = {
                "OrderID": int(selected["Order ID"].values[0]),
                "DeliveryDate": delivery_datetime_str,  
                "DeliveryStatus": updated_status,
                "SupplierName": supplier_name
            }
            try:
                put_url = 'http://api:4000/o/orders'
                put_response = requests.put(put_url, json=updated_info)
                put_response.raise_for_status()

                st.success(f"Order ID: {int(selected['Order ID'].values[0])} status updated successfully!")

            except requests.exceptions.RequestException as e:
                st.error("Failed to update.")
                st.text(f"Error: {e}")
with tab2:
    st.subheader("View Order Details")

    with st.form("view_order_details_form"):
        view_id = st.selectbox("Select Order ID to View Details", df["Order ID"])
        submitted = st.form_submit_button("Get Details")
        if submitted:
            def fetch_details():
                try:
                    response = requests.get(f'http://api:4000/o/orders/{view_id}')
                    response.raise_for_status()
                    if response.text.strip():
                        data = response.json()
                        if isinstance(data, list) and data:
                            return pd.DataFrame(data)
                except:
                    pass
                return pd.DataFrame()

            df = fetch_details()
            df = df.rename(columns={
                "ID": "Order ID", 
                "IngredientQuantity": "Ingredient Qty",
                "MaterialQuantity": "Material Qty",
                "EquipmentQuantity": "Equipment Qty",
                "IngredientName": "Ingredient",
                "MaterialName": "Material",
                "EquipmentName": "Equipment"})
            
            df= df[["Order ID","Ingredient",  "Ingredient Qty","Material" , "Material Qty",
                    "Equipment", "Equipment Qty"  ]]
            st.dataframe(df)



            
