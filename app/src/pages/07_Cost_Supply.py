import streamlit as st
import requests
import pandas as pd
from datetime import date

# Set up the page
st.set_page_config(layout="wide")

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

st.title("Supplies Costs")
st.write("Here are the cost details for Supplies:")

# --- Fetch costs ---
def fetch_supply_costs():
    try:
        response = requests.get('http://api:4000/costs/type/supplies')
        response.raise_for_status()
        if response.text.strip():
            data = response.json()
            if isinstance(data, list) and data:
                return pd.DataFrame(data, columns=["CostID", "Type", "PaymentDate", "PaymentAmount"])
    except:
        pass
    return pd.DataFrame()

df = fetch_supply_costs()
st.dataframe(df)

# --- Form to add new supply cost ---
st.markdown("---")
st.subheader("Add a New Supply Cost")

with st.form("add_supply_cost"):
    payment_date = st.date_input("Payment Date", value=date.today())
    payment_amount = st.number_input("Payment Amount ($)", min_value=0.0, format="%.2f")
    submitted = st.form_submit_button("Submit")

    if submitted:
        new_cost_data = {
            "Type": "supplies",
            "PaymentDate": payment_date.strftime('%Y-%m-%d'),
            "PaymentAmount": payment_amount,
        }

        try:
            post_url = 'http://api:4000/costs/cost'
            post_response = requests.post(post_url, json=new_cost_data)
            post_response.raise_for_status()

            st.success("New supply cost added successfully! Please refresh the page to see the updated table.")

        except requests.exceptions.RequestException as e:
            st.error("Failed to add new supply cost.")
            st.text(f"Error: {e}")
