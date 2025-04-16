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


# Initialize session state
if "form_step" not in st.session_state:
    st.session_state.form_step = 1
    st.session_state.new_order = {}
    st.session_state.order_details_list = []

def next_step():
    st.session_state.form_step += 1

def reset_form():
    st.session_state.form_step = 1
    st.session_state.new_order = {}
    st.session_state.order_details_list = []

# PAGE 1 — Add Multiple Item Sets
if st.session_state.form_step == 1:
    st.markdown("---")
    st.subheader("➕ Add an Order")

    with st.form("add_item_form", clear_on_submit=True):
        suppliers_unique = df['Supplier'].drop_duplicates()
        suppliername = st.selectbox("Select Supplier", suppliers_unique)

        manager_fname = st.text_input("Manager First Name", value="Mandy", disabled=True)
        manager_lname = st.text_input("Manager Last Name", value="Manager", disabled=True)

        ingredient_name = st.text_input("Ingredient Name")
        ingredient_qty = st.number_input("Ingredient Quantity", min_value=0)
        material_name = st.text_input("Material Name")
        material_qty = st.number_input("Material Quantity", min_value=0)
        equipment_name = st.text_input("Equipment Name")
        equipment_qty = st.number_input("Equipment Quantity", min_value=0)

        add_another = st.form_submit_button("Add Item to Order")

        if add_another:
            # Save supplier/manager info once
            st.session_state.SupplierName = suppliername
            st.session_state.ManagerFirstName = manager_fname
            st.session_state.ManagerLastName = manager_lname

            item = {
                "IngredientName": ingredient_name,
                "IngredientQuantity": ingredient_qty,
                "MaterialName": material_name,
                "MaterialQuantity": material_qty,
                "EquipmentName": equipment_name,
                "EquipmentQuantity": equipment_qty
            }
            st.session_state.order_details_list.append(item)
            st.success("Item added to order.")

    # Show all added items
    if st.session_state.order_details_list:
        st.write("🧾 **Current Items in Order:**")
        for idx, item in enumerate(st.session_state.order_details_list, 1):
            st.write(f"{idx}. {item['IngredientName']} ({item['IngredientQuantity']}), "
                     f"{item['MaterialName']} ({item['MaterialQuantity']}), "
                     f"{item['EquipmentName']} ({item['EquipmentQuantity']})")

        if st.button("Next: Add Order Info"):
            # Calculate total quantity
            total_qty = sum(
                item["IngredientQuantity"] +
                item["MaterialQuantity"] +
                item["EquipmentQuantity"]
                for item in st.session_state.order_details_list
            )
            st.session_state.new_order = {
                "SupplierName": st.session_state.SupplierName,
                "ManagerFirstName": st.session_state.ManagerFirstName,
                "ManagerLastName": st.session_state.ManagerLastName,
                "OrderQuantity": total_qty
            }
            next_step()

# PAGE 2 — Finalize and Submit Order
elif st.session_state.form_step == 2:
    st.subheader("🧾 Finalize Order Info")

    with st.form("finalize_form"):
        total = st.number_input("Order Total", min_value=0.0, format="%.2f")

        order_date = st.date_input("Order date", value=datetime.now().date(), disabled=True)
        order_time = st.time_input("Order time", value=datetime.now().time(), disabled=True)

        delivery_date = st.date_input("Delivery date", value=datetime.now().date())
        delivery_time = st.time_input("Delivery time", value=datetime.now().time())

        submitted = st.form_submit_button("Submit Order")

        if submitted:
            order_datetime_str = datetime.combine(order_date, order_time).strftime('%Y-%m-%d %H:%M:%S')
            delivery_datetime_str = datetime.combine(delivery_date, delivery_time).strftime('%Y-%m-%d %H:%M:%S')

            full_order_payload = {
                **st.session_state.new_order,
                "OrderTotal": total,
                "DateOrdered": order_datetime_str,
                "DeliveryDate": delivery_datetime_str,
                "OrderDetails": st.session_state.order_details_list
            }

            try:
                post_url = 'http://api:4000/o/orders/full-multi'  # Backend must handle list of details
                response = requests.post(post_url, json=full_order_payload)
                response.raise_for_status()

                order_id = response.text.split(":")[-1].strip()
                st.session_state['order_id'] = order_id

                st.success(f"✅ Order #{order_id} successfully created!")
                reset_form()

            except requests.exceptions.RequestException as e:
                st.error("❌ Failed to add new order.")
                st.text(f"Error: {e}")
