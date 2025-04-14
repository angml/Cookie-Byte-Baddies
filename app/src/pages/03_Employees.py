import streamlit as st
import requests

st.set_page_config(layout='wide')
st.title("🍪 All Employees")

BASE_URL = "http://localhost:8502"  

st.subheader("➕ Add New Employee")
with st.form("add_employee_form"):
    first = st.text_input("First Name")
    last = st.text_input("Last Name")
    
    # 🔽 Dropdown for Position
    position = st.selectbox("Position", ["Cashier", "Baker"])
    
    wage = st.number_input("Wage", min_value=0.0, format="%.2f")
    hours = st.number_input("Hours Worked", min_value=0.0, format="%.2f")
    manager_id = st.number_input("Manager ID", min_value=1, step=1)
    
    submitted = st.form_submit_button("Add Employee")
    
    if submitted:
        new_emp = {
            "FirstName": first,
            "LastName": last,
            "Position": position,
            "Wage": wage,
            "HoursWorked": hours,
            "ManagerID": manager_id
        }
        res = requests.post(f"{BASE_URL}/employees", json=new_emp)
        if res.status_code == 201:
            st.success("Employee added successfully.")
        else:
            st.error(f"Failed to add employee: {res.text}")


st.divider()


response = requests.get(f"{BASE_URL}/employees")

try:
    response.raise_for_status()

    if "application/json" not in response.headers.get("Content-Type", ""):
        st.error("Server did not return JSON data.")
        st.stop()

    employees = response.json()

except requests.exceptions.HTTPError as http_err:
    st.error(f"HTTP error occurred: {http_err}")
    st.stop()
except requests.exceptions.JSONDecodeError as json_err:
    st.error(f"JSON decode error: {json_err}")
    st.stop()
except Exception as e:
    st.error(f"Unexpected error: {e}")
    st.stop()

positions = {}
for emp in employees:
    pos = emp['Position']
    positions.setdefault(pos, []).append(emp)

for position, emp_group in positions.items():
    st.subheader(f"Position: {position}")
    for emp in emp_group:
        with st.expander(f"{emp['FirstName']} {emp['LastName']} (ID: {emp['ID']})"):
            st.write(f"Wage: ${emp['Wage']}")
            st.write(f"Hours Worked: {emp['HoursWorked']}")
            st.write(f"Manager ID: {emp['ManagerID']}")

            col1, col2 = st.columns(2)

            with col1:
                new_wage = st.number_input(
                    f"Update Wage for {emp['ID']}",
                    value=emp['Wage'],
                    key=f"wage_{emp['ID']}"
                )
                if st.button("Update Wage", key=f"update_{emp['ID']}"):
                    update_data = {"Wage": new_wage}
                    res = requests.put(f"{BASE_URL}/employees/{emp['ID']}", json=update_data)
                    if res.status_code == 200:
                        st.success("Wage updated.")
                    else:
                        st.error(f"Failed to update wage: {res.text}")

            with col2:
                if st.button("Terminate", key=f"delete_{emp['ID']}"):
                    res = requests.delete(f"{BASE_URL}/employees/{emp['ID']}")
                    if res.status_code == 200:
                        st.success("Employee terminated.")
                    else:
                        st.error(f"Error terminating employee: {res.text}")