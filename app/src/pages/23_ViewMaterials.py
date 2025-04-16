import pandas as pd
import logging
logger = logging.getLogger(__name__)
import streamlit as st
from modules.nav import SideBarLinks
import requests
import altair as alt

logger = logging.getLogger(__name__)

st.set_page_config(layout = 'wide')

SideBarLinks()

st.title('The Materials Page')

# Gets the Material list 
def get_mat_list():
    try:
        response = requests.get('http://web-api:4000/m/materials')
        response.raise_for_status()
        if response.text.strip():
            data = response.json()
            if isinstance(data, list) and data:
                return pd.DataFrame(data)
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching materials: {e}")
    return pd.DataFrame()

df = get_mat_list()

# Display the material list
st.subheader("Materials List")
if not df.empty:
    st.dataframe(df)
else:
    st.write("No Materials available.")

# Update inventory number
response = requests.get('http://web-api:4000/m/materials')
mat_items = response.json()

st.write("### Update Inventory of a Material")
selected_material = st.selectbox("Select Material to Update", [item['Name'] for item in mat_items])
new_inventory = st.number_input("Enter New Inventory Number", min_value=0, step=1)
    
if st.button("Update Inventory"):
    # Get the selected item's ID 
    mat_to_update = next(item for item in mat_items if item['Name'] == selected_material)
    item_id = mat_to_update['ID']
       
    update_url = f'http://web-api:4000/m/materials/update-inventory/{item_id}'
    response = requests.put(update_url, json={"Inventory": new_inventory})
      
    if response.status_code == 200:
        st.success(f"Inventory for {selected_material} updated successfully!")
        st.rerun()
    else:
        st.error(f"Failed to update Inventory for {selected_material}. Please try again. Status: {response.status_code}")