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
    "CompanyName": "Supplier",
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

st.subheader("Input New Order")
with st.form("create_order_form"):
    supplier_name = st.selectbox("Select Supplier", df['Supplier'])
    selected = df[df['Supplier'] == supplier_name]
    manager_fname = st.text_input("Manager First Name", value = "Mandy", disabled=True)
    manager_lname = st.text_input("Manager Last Name", value= "Manager", disabled=True)
    order_total = st.number_input("Order Total", min_value=0.0, step=0.01, format="%.2f")
    order_quantity = st.number_input("Order Quantity", min_value=1, step=1)
    date_ordered = st.date_input("Date Ordered", value=datetime.today())
    delivery_date = st.date_input("Delivery Date")

    submit_order = st.form_submit_button("Submit Order")

if submit_order:
    date_ordered_str = date_ordered.strftime('%Y-%m-%d %H:%M:%S')
    delivery_date_str = date_ordered.strftime('%Y-%m-%d %H:%M:%S')

    new_order = {
        "CompanyName": supplier_name,
        "ManagerFirstName": manager_fname,
        "ManagerLastName": manager_lname,
        "OrderTotal": order_total,
        "OrderQuantity": order_quantity,
        "DateOrdered": date_ordered_str,
        "DeliveryDate": delivery_date_str}

    try:
        post_res = requests.post("http://api:4000/o/orders", json=new_order)
        post_res.raise_for_status()
        st.success("Order created successfully!")

    except requests.exceptions.RequestException as e:
            st.error("Failed to add new order information.")
            st.text(f"Error: {e}")





   


