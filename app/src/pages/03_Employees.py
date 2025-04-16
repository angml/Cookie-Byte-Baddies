import streamlit as st
import requests
import pandas as pd
from modules.nav import SideBarLinks

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

st.title("🍪 All Employees")

BASE_URL = "http://api:4000/e/employees"

# Utility functions
def fetch_employees_df():
    response = requests.get(BASE_URL)
    data = response.json()
    if isinstance(data, list) and data:
        return pd.DataFrame(data)
    return pd.DataFrame(data)

def get_clean_employees_df():
    df = fetch_employees_df()
    return df.rename(columns={
        'ID': 'Employee ID',
        'FirstName': 'First Name',
        'LastName': 'Last Name',
        'Position': 'Position',
        'Wage': 'Hourly Wage',
        'HoursWorked': 'Hours Worked',
        'ManagerID': 'Manager ID'
    })

def update_employee_wage(employee_id, new_wage):
    response = requests.put(f"{BASE_URL}/{employee_id}", json={"Wage": new_wage})
    return response.status_code == 200

def delete_employee(employee_id):
    response = requests.delete(f"{BASE_URL}/{employee_id}")
    return response.status_code == 200

# Fetch cleaned employee data once
employees_df = get_clean_employees_df()

# Display Employees Table
st.subheader("📋 Current Employees")
if not employees_df.empty:
    st.dataframe(employees_df)
else:
    st.info("No employees found.")

st.markdown("---")
st.subheader("➕ Add New Employee")

with st.form("add_employee_form"):
    employee_id = st.number_input("Employee ID", min_value=1, step=1)
    first_name = st.text_input("First Name")
    last_name = st.text_input("Last Name")
    position = st.selectbox("Position", ['Cashier', 'Baker'])
    wage = st.number_input("Wage", min_value=0.0, format="%.2f")
    hours_worked = st.number_input("Hours Worked", min_value=0.0, format="%.2f")
    manager_id = st.text_input("Manager ID", value = 1, disabled = True)
    submitted = st.form_submit_button("Add Employee")

    if submitted:
        if all([employee_id, first_name, last_name, position, wage, hours_worked, manager_id]):
            new_employee = {
                "ID": employee_id,
                "FirstName": first_name,
                "LastName": last_name,
                "Position": position,
                "Wage": wage,
                "HoursWorked": hours_worked,
                "ManagerID": 1
            }
            response = requests.post(BASE_URL, json=new_employee)
            if response.status_code == 201:
                st.success("Employee added successfully!")
            else:
                st.error("Failed to add employee.")
        else:
            st.error("Please fill in all fields.")

st.markdown("---")
st.subheader("🔧 Update or Terminate Employee")

# Update or Delete Employee
for idx, row in employees_df.iterrows():
    with st.expander(f"Employee {row['First Name']} {row['Last Name']} (ID: {row['Employee ID']})"):
        col1, col2 = st.columns(2)

        with col1:
            try:
                current_wage = float(row['Hourly Wage']) if row['Hourly Wage'] is not None else 0.0
            except ValueError:
                current_wage = 0.0
            
            new_wage = st.number_input(
                f"New wage for {row['First Name']} {row['Last Name']}",
                value=current_wage,
                min_value=0.0,
                format="%.2f",
                key=f"wage_{row['Employee ID']}_{idx}"
            )
            if st.button(f"Update Wage for {row['First Name']} {row['Last Name']}", key=f"update_wage_{row['Employee ID']}_{idx}"):
                if update_employee_wage(row['Employee ID'], new_wage):
                    st.success(f"Wage for {row['First Name']} {row['Last Name']} updated!")
                else:
                    st.error(f"Failed to update wage for {row['First Name']} {row['Last Name']}.")

        with col2:
            if st.button(f"Terminate Contract for {row['First Name']} {row['Last Name']}", key=f"delete_{row['Employee ID']}_{idx}"):
                if delete_employee(row['Employee ID']):
                    st.success(f"Contract for {row['First Name']} {row['Last Name']} terminated!")
                else:
                    st.error(f"Failed to terminate contract for {row['First Name']} {row['Last Name']}.")
