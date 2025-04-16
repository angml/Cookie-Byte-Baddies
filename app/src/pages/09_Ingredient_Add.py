import pandas as pd
import logging
logger = logging.getLogger(__name__)
import streamlit as st
from modules.nav import SideBarLinks
import requests

logger = logging.getLogger(__name__)

# Page config and styling
st.set_page_config(layout = 'wide')

SideBarLinks()

st.markdown("""
    <style>
        .stApp { background-color: #f3e8ff; }
        .block-container { background-color: #f3e8ff; }
        html, body, [class*="css"] { color: 2d2d2d; }
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

# Header
st.title('Ingredient Page')

# Gets the ingredient list
def get_ing_list():
    try:
        response = requests.get('http://web-api:4000/i/ingredients')
        response.raise_for_status()
        if response.text.strip():
            data = response.json()
            if isinstance(data, list) and data:
                return pd.DataFrame(data)
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching ingredients: {e}")
    return pd.DataFrame()

df = get_ing_list()

# Display the ingredient list
st.subheader("📋 Ingredient List")
if not df.empty:
    st.dataframe(df)
else:
    st.write("No ingredients available.")

# Add new Ingredient title
st.subheader("➕ Add a New Ingredient")

# Input fields for the new ingredient
name = st.text_input("Ingredient Name")
price = st.number_input("Price", min_value=0.0, step=0.1)
inventory = st.number_input("Inventory Count", min_value=0, step=1)
expiry = st.number_input("Days Until Expiry", min_value=0, step=1)
burn_rate = st.number_input("Burn Rate", min_value=0.0, step=0.1)

# Button that adds a new ingredient
if st.button("Add Ingredient"):
    # All fields should have a value
    if not name or price is None or inventory is None or not expiry or burn_rate is None:
        st.error("Please fill out all fields before submitting. Thank you!")
    # Must have a real price and burn rate greater than zero. We are allowed to have a 0 for inventory
    # to represent when we run out of an item :)
    elif price <= 0.0 or burn_rate <= 0:
        st.error("Please enter a valid price or burn rate number (greater than 0). Thank you!")
    else:
        # stuff to send to back end
        item_data = {
            "IngredientName": name,
            "Price": price,
            "Inventory" : inventory,
            "Expiry" : expiry,
            "BurnRate" : burn_rate
        }

        # Makes a POST request to the API to create the ingredient
        response = requests.post("http://web-api:4000/i/ingredients/create", json=item_data)
        
        # Handles either the success or error response
        if response.status_code == 201:
            st.success(f"New ingredient '{name}' added successfully!")
            # refreshes the page automatically!
            st.rerun()
        elif response.status_code == 400:
            st.error("Invalid input. Please check the entered data.")
        elif response.status_code == 500:
            st.error("Server error. Please try again later.")
        else:
            st.error(f"Failed to add ingredient. Status code: {response.status_code}")