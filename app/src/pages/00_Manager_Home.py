import logging
logger = logging.getLogger(__name__)
import streamlit as st
from modules.nav import SideBarLinks 

# Set layout of the page
st.set_page_config(layout='wide')

# Display Sidebar
SideBarLinks()

# Display main title with manager's first name from session state
st.title(f"Welcome, Manager  {st.session_state['first_name']}!")

# Add spacing between elements
st.write('')
st.write('')

# Display section header
st.write('### What would you like to do today?')

# Button that navigates to the Costs page
if st.button('View and Manage: COSTS', 
             type='primary',
             use_container_width=True):
    st.switch_page('pages/01_Costs.py')

# Button that navigates to the Sales page
if st.button('View and Manage: SALES', 
             type='primary',
             use_container_width=True):
    st.switch_page('pages/02_Sales.py')

# Button that navigates to the Employees page
if st.button('View and Manage: EMPLOYEES',
             type='primary',
             use_container_width=True):
    st.switch_page('pages/03_Employees.py')

# Button that navigates to the Suppliers page
if st.button('View and Manage: SUPPLIERS',
             type='primary',
             use_container_width=True):
    st.switch_page('pages/04_Suppliers.py')

# Button that navigates to the Equipment page 
if st.button('View and Mange: MANAGERS',
             type='primary',
             use_container_width=True):
    st.switch_page('pages/09_Equipment.py')
