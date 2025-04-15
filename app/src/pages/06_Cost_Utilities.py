import streamlit as st
import requests
import pandas as pd
from datetime import date

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

st.title("Utilities Costs")
st.write("Here are the cost details for Utilities:")

# Fetch costs
def fetch_utilities_costs():
    try:
        response = requests.get('http://api:4000/costs/type/utilities')
        response.raise_for_status()
        if response.text.strip():
            data = response.json()
            if isinstance(data, list) and data:
                return pd.DataFrame(data, columns=["CostID", "Type", "PaymentDate", "PaymentAmount"])
    except:
        pass
    return pd.DataFrame()

df = fetch_utilities_costs()
st.dataframe(df)

# Form to add new utilities cost
st.markdown("---")
st.subheader("Add a New Utilities Cost")

with st.form("add_utilities_cost"):
    payment_date = st.date_input("Payment Date", value=date.today())
    payment_amount = st.number_input("Payment Amount ($)", min_value=0.0, format="%.2f")
    submitted = st.form_submit_button("Submit")

    if submitted:
        new_cost_data = {
            "Type": "utilities",
            "PaymentDate": payment_date.strftime('%Y-%m-%d'),
            "PaymentAmount": payment_amount,
        }

        try:
            post_url = 'http://api:4000/costs/cost'
            post_response = requests.post(post_url, json=new_cost_data)
            post_response.raise_for_status()

            st.success("New utilities cost added successfully! Please refresh the page to see the updated table.")

        except requests.exceptions.RequestException as e:
            st.error("Failed to add new utilities cost.")
            st.text(f"Error: {e}")
