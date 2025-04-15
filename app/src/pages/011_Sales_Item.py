import streamlit as st
import pandas as pd
import requests

# --- Page config & styling ---
st.set_page_config(layout="wide")

st.markdown("""
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
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# --- Header ---
st.title("🍽️ Sales by Menu Item")
st.write("Select a menu item from the dropdown to view its total revenue.")

# --- Get menu items from /m/menu-items ---
try:
    menu_response = requests.get("http://api:4000/m/menu-items")
    menu_response.raise_for_status()
    menu_data = menu_response.json()

    # Extract just the item names
    menu_item_names = [item["Name"] for item in menu_data]

    # Dropdown to select item
    selected_item = st.selectbox("Select Menu Item", options=menu_item_names)

    # When button clicked, get revenue for selected item
    if st.button("💰 View Total Revenue", type="primary", use_container_width=True):
        try:
            revenue_url = f"http://api:4000/sales/sales/menuitem/{selected_item}"
            revenue_response = requests.get(revenue_url)
            revenue_response.raise_for_status()
            result = revenue_response.json()

            st.success(f"Total Revenue for '{result['MenuItem']}':")
            st.metric(label="💵 Revenue", value=f"${result['TotalRevenue']:.2f}")
        except requests.exceptions.RequestException as e:
            st.error("Failed to fetch revenue.")
            st.text(f"Error: {e}")

except requests.exceptions.RequestException as e:
    st.error("Could not load menu items.")
    st.text(f"Error: {e}")
