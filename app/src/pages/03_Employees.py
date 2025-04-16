import streamlit as st
import requests
from logging import getLogger

st.set_page_config(layout='wide')
st.title("🍪 All Employees")

BASE_URL = "http://api:4000/e/employees"

def fetch_employees():
    try:
        response = requests.get(BASE_URL, timeout=5)
        response.raise_for_status()
        if "application/json" not in response.headers.get("Content-Type", ""):
            st.error("Server did not return JSON data.")
            st.write("DEBUG:", response.text)
            return []
        data = response.json()
        print(data)
        if isinstance(data, list):
            return data
        else:
            st.error("Unexpected API response format.")
            st.write("DEBUG:", data)
            return []
    except Exception as e:
        st.error(f"Could not fetch employees: {e}")
        return []

def add_employee(data):
    try:
        res = requests.post(BASE_URL, json=data, timeout=5)
        if res.status_code == 201:
            st.success("Employee added successfully.")
            st.experimental_rerun()
        else:
            try:
                st.error(f"Failed to add employee: {res.json()}")
            except Exception:
                st.error(f"Failed to add employee: {res.text}")
    except Exception as e:
        st.error(f"Error adding employee: {e}")

def update_wage(emp_id, wage):
    try:
        res = requests.put(f"{BASE_URL}/{emp_id}", json={"Wage": wage}, timeout=5)
        if res.status_code == 200:
            st.success("Wage updated.")
            st.experimental_rerun()
        else:
            try:
                st.error(f"Failed to update wage: {res.json()}")
            except Exception:
                st.error(f"Failed to update wage: {res.text}")
    except Exception as e:
        st.error(f"Error updating wage: {e}")

def delete_employee(emp_id):
    try:
        res = requests.delete(f"{BASE_URL}/{emp_id}", timeout=5)
        if res.status_code == 200:
            st.success("Employee terminated.")
            st.experimental_rerun()
        else:
            try:
                st.error(f"Error terminating employee: {res.json()}")
            except Exception:
                st.error(f"Error terminating employee: {res.text}")
    except Exception as e:
        st.error(f"Error terminating employee: {e}")

employees = fetch_employees()

# Add new employee form
st.subheader("➕ Add New Employee")
with st.form("add_employee_form"):
    emp_id = st.number_input("Employee ID", min_value=1, step=1)
    first = st.text_input("First Name")
    last = st.text_input("Last Name")
    position = st.text_input("Position")
    wage = st.number_input("Wage", min_value=0.0, format="%.2f")
    hours = st.number_input("Hours Worked", min_value=0.0, format="%.2f")
    manager_id = st.number_input("Manager ID", min_value=1, step=1)
    submitted = st.form_submit_button("Add Employee")
    if submitted:
        if all([emp_id, first, last, position, wage, hours, manager_id]):
            new_emp = {
                "ID": int(emp_id),
                "FirstName": first,
                "LastName": last,
                "Position": position,
                "Wage": float(wage),
                "HoursWorked": float(hours),
                "ManagerID": int(manager_id)
            }
            add_employee(new_emp)
        else:
            st.error("Please fill in all fields.")

st.divider()

print("employees")
if employees:
    for emp in employees:
        with st.expander(f"{emp.get('FirstName', '')} {emp.get('LastName', '')} (ID: {emp.get('ID', '')})"):
            st.write(emp)
            col1, col2 = st.columns(2)
            with col1:
                # Ensure Wage is a float for the number_input
                try:
                    wage_value = float(emp.get('Wage', 0.0))
                except Exception:
                    wage_value = 0.0
                # new_wage = st.number_input(
                #     f"Update Wage for {emp.get('ID', '')}",
                #     value=wage_value,
                #     step=0.01,
                #     format="%.2f",
                #     key=f"wage_input_{emp.get('ID', '')}"
                # )
                # if st.button("Update Wage", key=f"update_btn_{emp.get('ID', '')}"):
                #     update_wage(emp.get('ID', ''), new_wage)
            # with col2:
            #     if st.button("Terminate", key=f"delete_btn_{emp.get('ID', '')}"):
            #         delete_employee(emp.get('ID', ''))
else:
    st.info("No employees found.")
