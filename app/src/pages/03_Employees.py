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

# Fetch employees and return as a DataFrame
def fetch_employees_df():
    try:
        response = requests.get(BASE_URL)
        response.raise_for_status()
        data = response.json()
        if isinstance(data, list) and data:
            return pd.DataFrame(data)
    except:
        pass
    return pd.DataFrame()

# Add employee via POST
def add_employee(data):
    try:
        response = requests.post(BASE_URL, json=data)
        response.raise_for_status()
        return response.status_code == 201
    except:
        return False

# Show employee DataFrame
st.subheader("📋 Current Employees")
employees_df = fetch_employees_df()
if not employees_df.empty:
    st.dataframe(employees_df)
else:
    st.info("No employees found.")

# Form to add a new employee
st.markdown("---")
st.subheader("➕ Add New Employee")

with st.form("add_employee_form"):
    emp_id = st.number_input("Employee ID", min_value=1, step=1)
    first = st.text_input("First Name")
    last = st.text_input("Last Name")
    position = st.selectbox("Position", ["Cashier", "Baker"])
    wage = st.number_input("Wage", min_value=0.0, format="%.2f")
    hours = st.number_input("Hours Worked", min_value=0.0, format="%.2f")
    manager_id = st.number_input("Manager ID", min_value=1, step=1)
    submitted = st.form_submit_button("Add Employee")

    if submitted:
        if not all([emp_id, first.strip(), last.strip(), position, wage, hours, manager_id]):
            st.error("❌ Please fill in all fields before submitting.")
        else:
            new_emp = {
                "ID": int(emp_id),
                "FirstName": first.strip(),
                "LastName": last.strip(),
                "Position": position,
                "Wage": float(wage),
                "HoursWorked": float(hours),
                "ManagerID": int(manager_id)
            }
            if add_employee(new_emp):
                st.success("✅ Employee added! Refresh to see updated table.")
            else:
                st.error("❌ Failed to add employee. Please check your data or backend.")

