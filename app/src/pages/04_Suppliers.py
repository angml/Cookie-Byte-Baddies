import streamlit as st
import requests

st.set_page_config(layout='wide')
st.title("🍪 All Suppliers")

BASE_URL = "http://localhost:8502"  

# Add new supplier form
st.subheader("➕ Add New Supplier")
with st.form("add_supplier_form"):
    name = st.text_input("Supplier Name")
    phone = st.text_input("Phone Number")
    email = st.text_input("Email Address")
    
    submitted = st.form_submit_button("Add Supplier")
    
    if submitted:
        if name and phone and email:
            new_supplier = {
                "Name": name,
                "Phone": phone,
                "Email": email
            }
            res = requests.post(BASE_URL, json=new_supplier)
            if res.status_code == 201:
                st.success("Supplier added successfully.")
            else:
                st.error(f"Failed to add supplier: {res.text}")
        else:
            st.error("Please fill in all fields.")

st.divider()

# Fetch and display suppliers
response = requests.get(BASE_URL)

try:
    response.raise_for_status()

    if "application/json" not in response.headers.get("Content-Type", ""):
        st.error("Server did not return JSON data.")
        st.stop()

    suppliers = response.json()

except requests.exceptions.HTTPError as http_err:
    st.error(f"HTTP error occurred: {http_err}")
    st.stop()
except requests.exceptions.JSONDecodeError as json_err:
    st.error(f"JSON decode error: {json_err}")
    st.stop()
except Exception as e:
    st.error(f"Unexpected error: {e}")
    st.stop()

# Display suppliers in expandable sections
for supplier in suppliers:
    with st.expander(f"{supplier['Name']} (ID: {supplier['ID']})"):
        st.write(f"**Phone:** {supplier['Phone']}")
        st.write(f"**Email:** {supplier['Email']}")

        # Update contact information
        col1, col2 = st.columns(2)

        with col1:
            update_phone = st.text_input(f"New phone for {supplier['Name']}", key=f"update_phone_{supplier['ID']}")
            update_email = st.text_input(f"New email for {supplier['Name']}", key=f"update_email_{supplier['ID']}")
            if st.button(f"Update Contact Info for {supplier['Name']}", key=f"update_{supplier['ID']}"):
                if update_phone and update_email:
                    update_data = {"Phone": update_phone, "Email": update_email}
                    res = requests.put(f"{BASE_URL}/{supplier['ID']}", json=update_data)
                    if res.status_code == 200:
                        st.success(f"Supplier {supplier['Name']} updated successfully!")
                    else:
                        st.error(f"Failed to update supplier: {res.text}")
                else:
                    st.error("Please provide both phone and email.")

        with col2:
            if st.button(f"Terminate Contract for {supplier['Name']}", key=f"delete_{supplier['ID']}"):
                res = requests.delete(f"{BASE_URL}/{supplier['ID']}")
                if res.status_code == 200:
                    st.success(f"Supplier {supplier['Name']} contract terminated successfully!")
                else:
                    st.error(f"Failed to terminate supplier contract: {res.text}")
