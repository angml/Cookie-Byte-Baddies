import streamlit as st
import pandas as pd
import requests
import os

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

st.title("All Costs by Date")
st.write("Below are all labor, supplies, and utilities costs sorted from oldest to newest.")

# Define cost types
cost_types = ["labor", "supplies", "utilities"]
all_data = []

# Fetch each cost type
for cost_type in cost_types:
    try:
        response = requests.get(f"http://api:4000/costs/type/{cost_type}")
        response.raise_for_status()
        data = response.json()
        all_data.extend(data)
    except Exception as e:
        st.warning(f"Failed to fetch {cost_type} data. Error: {e}")

# Convert to DataFrame

if all_data:
    df = pd.DataFrame(all_data, columns=["CostID", "Type", "PaymentDate", "PaymentAmount"])
    df["PaymentDate"] = pd.to_datetime(df["PaymentDate"])
    df = df.sort_values(by="PaymentDate", ascending=True)
    st.dataframe(df)

    # --- Update Cost Form ---
    st.markdown("---")
    st.subheader("✏️ Update a Cost Record by CostID")

    cost_id = st.selectbox("Select a CostID to update", df["CostID"].unique())
    row = df[df["CostID"] == cost_id].iloc[0]

    with st.form("update_cost_form"):
        new_type = st.selectbox(
            "New Cost Type",
            options=["labor", "supplies", "utilities"],
            index=["labor", "supplies", "utilities"].index(row["Type"].lower())
        )

        new_date = st.date_input("New Payment Date", value=row["PaymentDate"])

        new_amount = st.number_input(
            "New Payment Amount",
            min_value=0.0,
            format="%.2f",
            value=float(row["PaymentAmount"])
        )

        submitted = st.form_submit_button("Submit Update")

        if submitted:
            update_payload = {
                "Type": new_type,
                "PaymentDate": new_date.strftime("%Y-%m-%d"),
                "PaymentAmount": new_amount
            }

            try:
                update_url = f"http://api:4000/costs/id/{cost_id}"  # ✅ FIXED: now updates by ID
                response = requests.put(update_url, json=update_payload)
                response.raise_for_status()
                st.success("Cost updated successfully! Please refresh the page to see changes.")
            except requests.exceptions.RequestException as e:
                st.error("Failed to update cost record.")
                st.text(f"Error: {e}")
else:
    st.warning("No cost data found.")
