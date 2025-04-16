import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout = 'wide')

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

st.title(f"Welcome, Manager  {st.session_state['first_name']}!")
st.write('')
st.write('')
st.write('### What would you like to do today?')

if st.button('View and Manage: COSTS', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/01_Costs.py')

if st.button('View and Manage: SALES', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/02_Sales.py')

if st.button('View and Manage: EMPLOYEES',
             type = 'primary',
             use_container_width = True):
  st.switch_page('pages/03_Employees.py')

if st.button('View and Manage: Suppliers',
            type = 'primary',
            use_container_width = True):
  st.switch_page('pages/04_Suppliers.py')

if st.button('View and Add: Ingredients',
            type = 'primary',
            use_container_width = True):
  st.switch_page('pages/09_Ingredient_Add.py')

if st.button('View and Add: Materials',
            type = 'primary',
            use_container_width = True):
  st.switch_page('pages/010_EditMaterials.py')