import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout = 'wide')

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

st.title(f"Welcome Baker, {st.session_state['first_name']}.")
st.write('')
st.write('')
st.write('### What would you like to do today?')

if st.button("View Menu Item Inventory", 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/51_Baker_MenuItems_Stock.py')

if st.button("View Ingredients and Update Inventory", 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/52_Ingredients_View.py')

if st.button("View Materials and Update Inventory", 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/53_BakerMaterial.py')