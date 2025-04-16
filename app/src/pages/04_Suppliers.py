import streamlit as st
import requests
import pandas as pd
from modules.nav import SideBarLinks

st.set_page_config(layout="wide")
SideBarLinks()

st.markdown(
    """
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
        #MainMenu, footer {visibility: hidden;}
    </style>
    """,
    unsafe_allow_html=True
)

st.title("📦 All Suppliers")

BASE_URL = "http://api:4000/s/suppliers"

def fetch_suppliers_df():
    response = requests.get(BASE_URL)
    print(response)
    data = response.json()
    print(data)
    return pd.DataFrame(data)


def update_supplier(supplier_id, supplier_name, contact_name, phone):
    payload = {
        "SupplierName": supplier_name,
        "ContactName": contact_name,
        "Phone": phone
    }
    response = requests.put(f"{BASE_URL}/{supplier_id}", json=payload)
    return response.status_code == 200

def delete_supplier(supplier_id):
    response = requests.delete(f"{BASE_URL}/{supplier_id}")
    return response.status_code == 200

def add_supplier(supplier_name, contact_name, phone):
    payload = {
        "SupplierName": supplier_name,
        "ContactName": contact_name,
        "Phone": phone
    }
    response = requests.post(BASE_URL, json=payload)
    return response.status_code in (200, 201)


st.subheader("📋 Current Suppliers")
suppliers_df = fetch_suppliers_df()
if not suppliers_df.empty:
    st.dataframe(suppliers_df)
else:
    st.info("No suppliers found.")

st.markdown("---")
st.subheader("➕ Add New Supplier")
with st.form("add_supplier_form"):
    supplier_name = st.text_input("Supplier Name")
    contact_name = st.text_input("Contact Name")
    phone = st.text_input("Phone Number")
    submitted = st.form_submit_button("Add Supplier")
    if submitted:
        if supplier_name and contact_name and phone:
            if add_supplier(supplier_name, contact_name, phone):
                st.success("Supplier added successfully!")
                st.experimental_rerun()
            else:
                st.error("Failed to add supplier.")
        else:
            st.error("Please fill in all fields.")

st.markdown("---")
st.subheader("🔧 Manage Suppliers")

for idx, row in suppliers_df.iterrows():
    with st.expander(f"{row['Name']} (ID: {row['ID']})"):
        col1, col2 = st.columns(2)

        with col1:
            new_name = st.text_input("New Supplier Name", value=row['Name'], key=f"name_{idx}")
            new_email = st.text_input("New Email ", value=row['Email'], key=f"email_{idx}")
            new_phone = st.text_input("New Phone Number", value=row['Phone'], key=f"phone_{idx}")
            if st.button("Update Supplier", key=f"update_{idx}"):
                if update_supplier(row['SupplierID'], new_name, new_email, new_phone):
                    st.success("Supplier updated successfully!")
                    st.experimental_rerun()
                else:
                    st.error("Failed to update supplier.")

        with col2:
            if st.button("Delete Supplier", key=f"delete_{idx}"):
                if delete_supplier(row['SupplierID']):
                    st.success("Supplier deleted successfully!")
                    st.experimental_rerun()
                else:
                    st.error("Failed to delete supplier.")
