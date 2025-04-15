import pandas as pd
import logging
logger = logging.getLogger(__name__)
import streamlit as st
from modules.nav import SideBarLinks
import requests

logger = logging.getLogger(__name__)

st.set_page_config(layout = 'wide')

SideBarLinks()

st.title('App Administration Page')

st.write('\n\n')
st.write('## Ingredients List Management')

# Gets the ingredient list with inventory and expiry date
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
st.subheader("Ingredients List")
if not df.empty:
    st.dataframe(df)
else:
    st.write("No ingredients available.")

# ------------------------------------------------------------------------------------------------------

# # Adds a new ingredient
# st.markdown("---")
# st.subheader("Add a New Ingredient")

# with st.form("add_new_ing"):
#     ing_name = st.text_input("Ingredient Name")
#     inventory = st.number_input("Inventory", min_value=0)
#     expiry_days = st.number_input("Shelf Life (Days Fresh)", min_value=1)
#     price = st.number_input("Price", min_value=0.0, format="%.2f")
#     burn_rate = st.number_input("Burn Rate", min_value=0.0, format="%.2f")
#     submitted = st.form_submit_button("Submit")

#     if submitted and ing_name:
#         new_ing_data = {
#             "IngredientName": ing_name,
#             "Inventory": inventory,
#             "Expiry": expiry_days,
#             "Price": price,
#             "BurnRate": burn_rate,
#         }

#         try:
#             post_url = 'http://api:4000/i/ingredients'
#             post_response = requests.post(post_url, json=new_ing_data)
#             post_response.raise_for_status()

#             st.success("New ingredient added successfully!")
#             st.experimental_rerun() 

#         except requests.exceptions.RequestException as e:
#             st.error("Failed to add new ingredient.")
#             st.text(f"Error: {e}")

## CREATING A NEW MENU ITEM
st.subheader("Add a New Ingredient")

# Input fields for the new menu item

name = st.text_input("Ingredient Name")
price = st.number_input("Price", min_value=0.0, step=0.1)
inventory = st.number_input("Inventory Count", min_value=0, step=1)
expiry = st.number_input("Expiry", min_value=0, step=1)
burn_rate = st.number_input("Burn Rate", min_value=0.0, step=0.1)

# Form submission button
if st.button("Add Ingredient"):
    # Basic Validation: Check if all required fields are filled
    if name == "":
        st.error("Please fill in Ingredient Name")
    elif price <= 0 or inventory < 0:
        st.error("Please enter a valid price (greater than 0) and a non-negative inventory quantity.")
    else:
        # stuff to send to back end
        item_data = {
            "IngredientName": name,
            "Price": price,
            "Inventory Count" : inventory,
            "Expiry" : expiry,
            "Burn Rate" : burn_rate
        }

        # Make POST request to the API to create the menu item
        response = requests.post("http://web-api:4000/i/ingredients/create", json=item_data)
        

        # Handle API response
        if response.status_code == 201:
            st.success(f"New ingredient '{name}' added successfully!")
        elif response.status_code == 400:
            st.error("Invalid input. Please check the entered data.")
        elif response.status_code == 500:
            st.error("Server error. Please try again later.")
        else:
            st.error(f"Failed to add ingredient. Status code: {response.status_code}")




# -------------------------------------------------------------------------------------------------------

# Updates the inventory for a specific ingredient
st.markdown("---")
st.subheader("Update Inventory for Ingredient")

with st.form("update_inventory"):
    ingredient_id_to_update = st.selectbox("Select Ingredient to Update Inventory", df["IngredientID"])
    new_inventory = st.number_input("New Inventory Quantity", min_value=0)
    update_submitted = st.form_submit_button("Update Inventory")

    if update_submitted:
        update_data = {
            "IngredientID": ingredient_id_to_update,
            "Inventory": new_inventory,
        }

        try:
            update_url = f'http://api:4000/ingredients'
            update_response = requests.put(update_url, json=update_data)
            update_response.raise_for_status()

            st.success("Inventory updated successfully!")
            st.experimental_rerun() 

        except requests.exceptions.RequestException as e:
            st.error("Failed to update inventory.")
            st.text(f"Error: {e}")


# st.title("Ingredient Burn Rate Chart")

# response = requests.get("http://localhost:5000/ingredients/burnrate")
# if response.status_code == 200:
#     data = response.json()
#     df = pd.DataFrame(data)
#     st.line_chart(df, x="Ingredient Name", y="Burn Rate")
# else:
#     st.error("Failed to fetch data")

import pandas as pd
import logging
import streamlit as st
from modules.nav import SideBarLinks
import requests

logger = logging.getLogger(__name__)

st.set_page_config(layout='wide')

SideBarLinks()

st.title('App Administration Page')

st.write('\n\n')
st.write('## Ingredients List Management')

# Gets the ingredient list with inventory and expiry date
def get_ing_list():
    try:
        response = requests.get('http://web-api:4000/i/ingredients')  # Corrected URL
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
st.subheader("Ingredients List")
if not df.empty:
    st.dataframe(df)
else:
    st.write("No ingredients available.")

# ------------------------------------------------------------------------------------------------------

# Add a New Ingredient Form
st.subheader("Add a New Ingredient")

name = st.text_input("Ingredient Name")
price = st.number_input("Price", min_value=0.0, step=0.1)
inventory = st.number_input("Inventory Count", min_value=0, step=1)
expiry = st.number_input("Expiry", min_value=0, step=1)
burn_rate = st.number_input("Burn Rate", min_value=0.0, step=0.1)

# Form submission button
if st.button("Add Ingredient"):
    # Basic Validation: Check if all required fields are filled
    if name == "":
        st.error("Please fill in Ingredient Name")
    elif price <= 0 or inventory < 0:
        st.error("Please enter a valid price (greater than 0) and a non-negative inventory quantity.")
    else:
        item_data = {
            "IngredientName": name,  # Corrected key
            "Price": price,
            "Inventory": inventory,
            "Expiry": expiry,
            "BurnRate": burn_rate
        }

        try:
            response = requests.post("http://web-api:4000/i/ingredients/create", json=item_data)  # Corrected URL
            if response.status_code == 201:
                st.success(f"New ingredient '{name}' added successfully!")
            else:
                st.error(f"Failed to add ingredient. Status code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            st.error(f"Failed to add ingredient. Error: {e}")

# -------------------------------------------------------------------------------------------------------

# Updates the inventory for a specific ingredient
st.markdown("---")
st.subheader("Update Inventory for Ingredient")

with st.form("update_inventory"):
    ingredient_id_to_update = st.selectbox("Select Ingredient to Update Inventory", df["IngredientID"])
    new_inventory = st.number_input("New Inventory Quantity", min_value=0)
    update_submitted = st.form_submit_button("Update Inventory")

    if update_submitted:
        update_data = {
            "IngredientID": ingredient_id_to_update,
            "Inventory": new_inventory,
        }

        try:
            update_url = f'http://web-api:4000/i/ingredients'  # Corrected URL
            update_response = requests.put(update_url, json=update_data)
            update_response.raise_for_status()

            st.success("Inventory updated successfully!")
            st.experimental_rerun() 
        except requests.exceptions.RequestException as e:
            st.error("Failed to update inventory.")
            st.text(f"Error: {e}")
