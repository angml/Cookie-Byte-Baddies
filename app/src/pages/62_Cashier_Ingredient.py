import pandas as pd
import logging
logger = logging.getLogger(__name__)
import streamlit as st
from modules.nav import SideBarLinks
import requests

logger = logging.getLogger(__name__)

st.set_page_config(layout = 'wide')

SideBarLinks()

st.title('Ingredients Page')

# Gets the ingredient list with all values but the IngredientID
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


# Update inventory number
response = requests.get('http://web-api:4000/i/ingredients')
ing_items = response.json()


st.write("### Update Inventory of an Ingredient")
selected_ingredient = st.selectbox("Select Ingredient to Update", [item['IngredientName'] for item in ing_items])
new_inventory = st.number_input("Enter New Inventory Number", min_value=0, step=1)
    
if st.button("Update Inventory"):
    # Get the selected item's ID 
    inv_to_update = next(item for item in ing_items if item['IngredientName'] == selected_ingredient)
    item_id = inv_to_update['IngredientID']
       
    update_url = f'http://web-api:4000/i/ingredients/update-inventory/{item_id}'
    response = requests.put(update_url, json={"Inventory": new_inventory})
      
    if response.status_code == 200:
        st.success(f"Inventory for {selected_ingredient} updated successfully!")
        st.rerun()
    else:
        st.error(f"Failed to update Inventory for {selected_ingredient}. Please try again. Status: {response.status_code}")