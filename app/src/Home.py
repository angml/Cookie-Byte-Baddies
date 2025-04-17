##################################################
# This is the main/entry-point file for the 
# sample application for your project
##################################################

import logging
import streamlit as st
from modules.nav import SideBarLinks

# Logging setup
logging.basicConfig(format='%(filename)s:%(lineno)s:%(levelname)s -- %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# streamlit supports regular and wide layout (how the controls
# are organized/displayed on the screen).
st.set_page_config(page_title="CookieByte Login", layout="wide")

# Auth state
st.session_state['authenticated'] = False

# Sidebar nav
SideBarLinks(show_home=True)

# --------------------------------------
#           MAIN PAGE CONTENT
# --------------------------------------

# --- Hero Section ---
st.markdown("""
    <div style='text-align: center; padding: 3rem 1rem; background: linear-gradient(90deg, #1b0b6e 0%, #9985ff 100%); border-radius: 15px;'>
        <h1 style='font-size: 3rem; margin-bottom: 0.5rem; color: white;'>🍪 CookieByte</h1>
        <h3 style='margin-top: 0; color: white;'>Where Cafes Run Smoothly</h3>
    </div>
""", unsafe_allow_html=True)

st.write("## 👋 Hi there!")
st.markdown("### Choose a role to log in as:")

st.divider()

# --- Buttons Section ---
# Split into two columns
col1, col2 = st.columns(2, gap="large")

with col1:
    if st.button("🙋🏾 Manager Mandy - 'Sip Happens Cafe'", use_container_width=True, type='primary'):
        st.session_state['authenticated'] = True
        st.session_state['role'] = 'Manager'
        st.session_state['first_name'] = 'Mandy'
        logger.info("Logging in as Manager Mandy")
        st.switch_page('pages/00_Manager_Home.py')

    if st.button("👩🏿‍🍳 Baker Pearl - The finest baker", use_container_width=True, type='primary'):
        st.session_state['authenticated'] = True
        st.session_state['role'] = 'baker'
        st.session_state['first_name'] = 'Pearl'
        st.switch_page('pages/50_Baker_Home.py')

    if st.button("🚚 Sally Supplier - Delivery Driver", use_container_width=True, type='primary'):
        st.session_state['authenticated'] = True
        st.session_state['role'] = 'supplier'
        st.session_state['first_name'] = 'Sally'
        st.switch_page('pages/20_Supplier_Home.py')

with col2:
    if st.button("💁🏾‍♂️ Connor Cashier - Frontline Worker", use_container_width=True, type='primary'):
        st.session_state['authenticated'] = True
        st.session_state['role'] = 'cashier'
        st.session_state['first_name'] = 'Connor'
        st.switch_page('pages/60_Cashier_Home.py')

    if st.button("🧁 Customer Carl - Regular Customer", use_container_width=True, type='primary'):
        st.session_state['authenticated'] = True
        st.session_state['role'] = 'customer'
        st.session_state['first_name'] = 'Carl'
        st.switch_page('pages/40_Customer_Home.py')

st.divider()

st.markdown("<small style='color: gray;'>Tip: These roles are mock profiles used for demonstration purposes.</small>", unsafe_allow_html=True)
