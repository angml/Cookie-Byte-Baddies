import streamlit as st
import requests

st.set_page_config(layout='wide')
st.title("🍪 All Suppliers")

BASE_URL = "http://api:4000/s/suppliers"

def fetch_suppliers():
    try:
        response = requests.get(BASE_URL, timeout=5)
        response.raise_for_status()
        if "application/json" not in response.headers.get("Content-Type", ""):
            st.error("Server did not return JSON data.")
            st.write("DEBUG:", response.text)
            return []
        return response.json()
    except Exception as e:
        st.error(f"Could not fetch suppliers: {e}")
        return []

def add_supplier(data):
    try:
        res = requests.post(BASE_URL, json=data, timeout=5)
        if res.status_code == 201:
            st.success("Supplier added successfully.")
            st.experimental_rerun()
        else:
            try:
                st.error(f"Failed to add supplier: {res.json()}")
            except Exception:
                st.error(f"Failed to add supplier: {res.text}")
    except Exception as e:
        st.error(f"Error adding supplier: {e}")

def update_supplier(supplier_id, phone, email):
    try:
        res = requests.put(f"{BASE_URL}/{supplier_id}", json={"Phone": phone, "Email": email}, timeout=5)
        if res.status_code == 200:
            st.success("Supplier updated successfully.")
            st.experimental_rerun()
        else:
            try:
                st.error(f"Failed to update supplier: {res.json()}")
            except Exception:
                st.error(f"Failed to update supplier: {res.text}")
    except Exception as e:
        st.error(f"Error updating supplier: {e}")

def delete_supplier(supplier_id):
    try:
        res = requests.delete(f"{BASE_URL}/{supplier_id}", timeout=5)
        if res.status_code == 200:
            st.success("Supplier contract terminated successfully.")
            st.experimental_rerun()
        else:
            try:
                st.error(f"Failed to terminate supplier: {res.json()}")
            except Exception:
                st.error(f"Failed to terminate supplier: {res.text}")
    except Exception as e:
        st.error(f"Error terminating supplier: {e}")

# Add new supplier form
st.subheader("➕ Add New Supplier")
with st.form("add_supplier_form"):
    supplier_id = st.number_input("Supplier ID", min_value=1, step=1)
    name = st.text_input("Supplier Name")
    phone = st.text_input("Phone Number")
    email = st.text_input("Email Address")
    submitted = st.form_submit_button("Add Supplier")
    if submitted:
        if all([supplier_id, name, phone, email]):
            new_supplier = {
                "ID": supplier_id,
                "Name": name,
                "Phone": phone,
                "Email": email
            }
            add_supplier(new_supplier)
        else:
            st.error("Please fill in all fields.")

st.divider()

suppliers = fetch_suppliers()
if suppliers:
    for supplier in suppliers:
        with st.expander(f"{supplier['Name']} (ID: {supplier['ID']})"):
            st.write(supplier)
            col1, col2 = st.columns(2)
            with col1:
                update_phone = st.text_input(
                    f"New phone for {supplier['Name']}",
                    value=supplier['Phone'],
                    key=f"update_phone_{supplier['ID']}"
                )
                update_email = st.text_input(
                    f"New email for {supplier['Name']}",
                    value=supplier['Email'],
                    key=f"update_email_{supplier['ID']}"
                )
                if st.button("Update Contact Info", key=f"update_{supplier['ID']}"):
                    if update_phone and update_email:
                        update_supplier(supplier['ID'], update_phone, update_email)
                    else:
                        st.error("Please provide both phone and email.")
            with col2:
                if st.button("Terminate Contract", key=f"delete_{supplier['ID']}"):
                    delete_supplier(supplier['ID'])
