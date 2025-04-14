# Idea borrowed from https://github.com/fsmosca/sample-streamlit-authenticator

# This file has function to add certain functionality to the left side bar of the app

import streamlit as st

#### ------------------------ General ------------------------
def HomeNav():
    st.sidebar.page_link("Home.py", label="Home", icon="🏠")


def AboutPageNav():
    st.sidebar.page_link("pages/30_About.py", label="About", icon="🧠")


#### ------------------------ Examples for Role of pol_strat_advisor ------------------------
def ManagerHomeNav():
    st.sidebar.page_link(
        "pages/00_Manager_Home.py", label="Manager Home", icon="👤"
    )


def CostsNav():
    st.sidebar.page_link(
        "pages/01_Costs.py", label="Costs", icon="🏦"
    )


def SalesNav():
    st.sidebar.page_link("pages/02_Sales.py", label="Sales", icon="🗺️")


## ------------------------ Examples for Role of usaid_worker ------------------------
def ApiTestNav():
    st.sidebar.page_link("pages/12_API_Test.py", label="Test the API", icon="🛜")


def PredictionNav():
    st.sidebar.page_link(
        "pages/11_Prediction_Worker.py", label="Regression Prediction", icon="📈"
    )


def ClassificationNav():
    st.sidebar.page_link(
        "pages/13_Classification.py", label="Classification Demo", icon="🌺"
    )


#### ------------------------ System Admin Role ------------------------
def AdminPageNav():
    st.sidebar.page_link("pages/20_Admin_Home.py", label="System Admin", icon="🖥️")
    st.sidebar.page_link(
        "pages/21_ML_Model_Mgmt.py", label="ML Model Management", icon="🏢"
    )
    
#### ------------------------ Manager Role ------------------------
def ManagerPageNav():
    st.sidebar.page_link("pages/00_Manager_Home.py", label="Manager Home", icon="🖥️")
    st.sidebar.page_link(
        "pages/01_Costs.py", label="Management Costs Page", icon="💰"
    )
    st.sidebar.page_link(
        "pages/02_Sales.py", label="Management Sales Page", icon="🧾"
    )
    
#### ------------------------ Customer Role ------------------------
def CustomerHomeNav():
    st.sidebar.page_link("pages/40_Customer_Home.py", label="Customer Home", icon="💁🏾")
    
def MenuApiNav():
    st.sidebar.page_link("pages/41_Menu_API.py", label="Menu", icon="☕️")
    
#### ------------------------ Baker Role ------------------------
def BakerHomeNav():
    st.sidebar.page_link("pages/50_Baker_Home.py", label="Baker Home", icon="👩🏿‍🍳")
    
def BakerStockNav():
    st.sidebar.page_link("pages/51_Baker_MenuItem_Stock.py", label="Stock Tracker", icon="📈")
    
#### ------------------------ Cashier Role ------------------------
def CashierHomeNav():
    st.sidebar.page_link("pages/60_Cashier_Home.py", label="Cashier Home", icon="🍵")
    
def CashierStockNav():
    st.sidebar.page_link("pages/61_Cashier_MenuItem_Stock.py", label="Stock Tracker", icon="📈")

# --------------------------------Links Function -----------------------------------------------
def SideBarLinks(show_home=False):
    """
    This function handles adding links to the sidebar of the app based upon the logged-in user's role, which was put in the streamlit session_state object when logging in.
    """
    
    st.markdown("""
    <style>
        /* Sidebar container background */
        [data-testid="stSidebar"] {
            background: linear-gradient(180deg, #1b0b6e 0%, #4e1489 100%);
            color: white;
        }

        /* Sidebar header and text */
        [data-testid="stSidebar"] * {
            color: white !important;
        }

        /* Sidebar buttons */
        [data-testid="stSidebar"] button {
            background-color: #ba59eb !important;
            color: white !important;
            border: none;
            border-radius: 8px;
        }

        /* Sidebar page links */
        [data-testid="stSidebar"] a {
            color: white !important;
            text-decoration: none;
        }
    </style>
""", unsafe_allow_html=True)



    # add a logo to the sidebar always
    st.sidebar.image("assets/cookiebyte_logo.png", width=150)

    # If there is no logged in user, redirect to the Home (Landing) page
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False
        st.switch_page("Home.py")

    if show_home:
        # Show the Home page link (the landing page)
        HomeNav()

    # Show the other page navigators depending on the users' role.
    if st.session_state["authenticated"]:

        # Show World Bank Link and Map Demo Link if the user is a political strategy advisor role.
        if st.session_state["role"] == "Manager":
            ManagerPageNav()
            CostsNav()
            SalesNav()

        # If the user role is usaid worker, show the Api Testing page
        if st.session_state["role"] == "usaid_worker":
            PredictionNav()
            ApiTestNav()
            ClassificationNav()

        # If the user is an administrator, give them access to the administrator pages
        if st.session_state["role"] == "administrator":
            AdminPageNav()
            
        # If the user is a customer, give them access to the customer pages (menu)
        if st.session_state["role"] == "customer":
            CustomerHomeNav()
            MenuApiNav()
            
        # If the user is a baker, give them access to the baker pages
        if st.session_state["role"] == "baker":
            BakerHomeNav()
            #BakerStockNav()
            
        # If the user is a baker, give them access to the baker pages
        if st.session_state["role"] == "cashier":
            CashierHomeNav()
            #CashierStockNav()
                

    # Always show the About page at the bottom of the list of links
    AboutPageNav()

    if st.session_state["authenticated"]:
        # Always show a logout button if there is a logged in user
        if st.sidebar.button("Logout"):
            del st.session_state["role"]
            del st.session_state["authenticated"]
            st.switch_page("Home.py")