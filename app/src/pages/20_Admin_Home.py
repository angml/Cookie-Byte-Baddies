import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
import requests

st.set_page_config(layout = 'wide')

SideBarLinks()

st.title('Welcome, Supplier Sally')
st.write('')
st.write('')
st.write('### What would you like to do today?')

if st.button('Ingredients', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/21_Ingredients.py')

if st.button('Supplies', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/21_ML_Model_Mgmt.py')

if st.button('Materials', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/23_ViewMaterials.py')