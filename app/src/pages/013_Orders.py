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
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Order History")

#data frame
def fetch_orders():
    try:
        response = requests.get('http://api:4000/o/orders')
        response.raise_for_status()
        if response.text.strip():
            data = response.json()
            if isinstance(data, list) and data:
                return pd.DataFrame(data)
    except Exception as e:
        print("Error fetching orders:", e)
    return pd.DataFrame()

df = fetch_orders()

#rename columns
df = df.rename(columns={
    "ID": "Order ID",
    "Name": "Supplier",
    "OrderQuantity": "Order Quantity",
    "OrderTotal": "Order Total",
    "DateOrdered": "Order Date",
    "DeliveryDate": "Delivery Date"})

#show only the date portion
df["Order Date"] = pd.to_datetime(df['Order Date']).dt.date
df['Delivery Date'] = pd.to_datetime(df['Delivery Date']).dt.date

#establish order
df = df[["Order ID", "Supplier", "Order Quantity", "Order Total", "Order Date", "Delivery Date"]]
st.dataframe(df)

#input new orders
st.markdown("---")
st.subheader("➕ Add a Order")
with st.form("add_order_form"):
    suppliers_unique= df['Supplier'].drop_duplicates()
    suppliername = st.selectbox("Select Supplier", suppliers_unique)

    manager_fname = st.text_input("Manager First Name", value="Mandy", disabled=True)
    manager_lname= st.text_input("Manager Last Name", value="Manager", disabled=True)
   
    quantity= st.number_input("Order Quantity", min_value=0, step=1)
    total= st.number_input("Order Total", min_value=0.0, format="%.2f")
   
    order_date = st.date_input("Order date", value= datetime.now().date())
    order_time = st.time_input("Order time", value=datetime.now().time())
    order_datetime = datetime.combine(order_date, order_time)
    
    delivery_date = st.date_input("Delivery date", value= datetime.now().date())
    delivery_time = st.time_input("Delivery time", value=datetime.now().time())
    delivery_datetime = datetime.combine(delivery_date, delivery_time)
   
    submitted = st.form_submit_button("Make Order")

    if submitted:
        # Basic Validation: Check if all required fields are filled
        if quantity== 0 or total == 0.0:
            st.error("Please fill in Order Quantity and Total.")
        if delivery_datetime < order_datetime:
            st.error("Delivery date/time cannot be before order date/time.")
        else:
            # Convert the datetime objects to a string with 'YYYY-MM-DD HH:MM:SS' format before sending them
            order_datetime_str = order_datetime.strftime('%Y-%m-%d %H:%M:%S')
            delivery_datetime_str = delivery_datetime.strftime('%Y-%m-%d %H:%M:%S')

            new_order = {
                "SupplierName": suppliername,
                "ManagerFirstName": manager_fname,
                "ManagerLastName": manager_lname,
                "OrderQuantity": quantity,
                "OrderTotal": total,
                "DateOrdered": order_datetime_str,
                "DeliveryDate": delivery_datetime_str
            }
        try:
            post_url = 'http://api:4000/o/orders'
            post_response = requests.post(post_url, json=new_order)
            post_response.raise_for_status()

            st.success(f"New order added successfully! Please refresh the page to see the updated table.")

        except requests.exceptions.RequestException as e:
            st.error("Failed to add new order.")
            st.text(f"Error: {e}")

    








