import logging
logger = logging.getLogger(__name__)
import streamlit as st
from modules.nav import SideBarLinks
import requests

st.set_page_config(layout = 'wide')

SideBarLinks()

st.title('App Administration Page')

st.write('\n\n')
st.write('## Model 1 Maintenance')

st.button("Ingredients", 
            type = 'primary', 
            use_container_width=True)

