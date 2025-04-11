import streamlit as st
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks

SideBarLinks()

st.write("# About CookieByte")

st.markdown (
    """
    This is a demo app for CS 3200 Course Project.  

    CookieByte is a user-friendly app designed to optimize 
    cafe operations for customers, employees, and suppliers.
    By streamlining operations and improving data visibility, 
    CookieByte helps cafes reduce waste, boost sales, and increase profitability

    Stay tuned for more information and features to come!
    """
        )
