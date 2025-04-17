# Idea borrowed from https://github.com/fsmosca/sample-streamlit-authenticator

# This file has function to add certain functionality to the left side bar of the app

import streamlit as st

#### ------------------------ General ------------------------
def HomeNav():
    st.sidebar.page_link("Home.py", label="Home", icon="🏠")


def AboutPageNav():
    st.sidebar.page_link("pages/30_About.py", label="About", icon="🧠")

#### ------------------------ Manager Role ------------------------
def ManagerPageNav():
    st.sidebar.page_link("pages/00_Manager_Home.py", label="Manager Home", icon="🖥️")
    st.sidebar.page_link(
        "pages/01_Costs.py", label="Management Costs Page", icon="💰"
    )
    st.sidebar.page_link(
        "pages/02_Sales.py", label="Management Sales Page", icon="🧾"
    )
    st.sidebar.page_link(
        "pages/03_Employees.py", label="Employees Page", icon="💁🏾‍♂️"
    )
    st.sidebar.page_link(
        "pages/04_Suppliers.py", label="Suppliers Page", icon="🚛"
    )
    st.sidebar.page_link(
        "pages/09_Equipment.py", label="Equipment Page", icon="🥄"
    )
    st.sidebar.page_link(
        "pages/013_Orders.py", label="Orders Page", icon="📦"
    )
    st.sidebar.page_link(
        "pages/09_Ingredient_Add.py", label="Ingredients Page", icon="🧈"
    )
    st.sidebar.page_link(
        "pages/010_EditMaterials.py", label="Materials Page", icon="🥣"
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
    st.sidebar.page_link("pages/51_Baker_MenuItems_Stock.py", label="Stock Tracker", icon="📈")
    
def BakerIngredientsNav():
    st.sidebar.page_link("pages/52_Ingredients_View.py", label="Ingredient Inventory", icon="🍫")
    
def BakerMaterialsNav():
    st.sidebar.page_link("pages/53_BakerMaterial.py", label="Material Inventory", icon="🥣")
    
#### ------------------------ Cashier Role ------------------------
def CashierHomeNav():
    st.sidebar.page_link("pages/60_Cashier_Home.py", label="Cashier Home", icon="🍵")
    
def CashierStockNav():
    st.sidebar.page_link("pages/61_Cashier_MenuItem_Stock.py", label="Stock Tracker", icon="📈")
    
def CashierIngredientsNav():
    st.sidebar.page_link("pages/62_Cashier_Ingredient.py", label="Ingredient Inventory", icon="🍫")
    
def CashierMaterialsNav():
    st.sidebar.page_link("pages/63_CashierMaterial.py", label="Material Inventory", icon="🥣")
    
#### ------------------------ Supplier Role ------------------------
def SupplierHomeNav():
    st.sidebar.page_link("pages/20_Supplier_Home.py", label="Supplier Home", icon="🚛")
    
def SupplierIngredientsNav():
    st.sidebar.page_link("pages/21_Ingredients.py", label="Ingredients Page", icon="🧈")
    
def SupplierDeliveriesNav():
    st.sidebar.page_link("pages/22_Deliveries.py", label="Deliveries Page", icon="📦")
    
def SupplierMaterialsNav():
    st.sidebar.page_link("pages/23_ViewMaterials.py", label="Materials Page", icon="🥄")
    

# --------------------------------Links Function -----------------------------------------------
def SideBarLinks(show_home=False):
    """
    This function handles adding links to the sidebar of the app based upon the logged-in user's role, which was put in the streamlit session_state object when logging in.
    """
    
#     st.markdown("""
#     <style>
#         /* Sidebar container background */
#         [data-testid="stSidebar"] {
#             background: linear-gradient(180deg, #1b0b6e 0%, #4e1489 100%);
#             color: white;
#         }

#         /* Sidebar header and text */
#         [data-testid="stSidebar"] * {
#             color: white !important;
#         }

#         /* Sidebar buttons */
#         [data-testid="stSidebar"] button {
#             background-color: #ba59eb !important;
#             color: white !important;
#             border: none;
#             border-radius: 8px;
#         }

#         /* Sidebar page links */
#         [data-testid="stSidebar"] a {
#             color: white !important;
#             text-decoration: none;
#         }
#     </style>
# """, unsafe_allow_html=True)


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

        # If the user is a customer, give them access to the customer pages (menu)
        if st.session_state["role"] == "customer":
            CustomerHomeNav()
            MenuApiNav()
            
        # If the user is a baker, give them access to the baker pages
        if st.session_state["role"] == "baker":
            BakerHomeNav()
            BakerStockNav()
            BakerIngredientsNav()
            BakerMaterialsNav()
            
        # If the user is a baker, give them access to the baker pages
        if st.session_state["role"] == "cashier":
            CashierHomeNav()
            CashierStockNav()
            CashierIngredientsNav()
            CashierMaterialsNav()
            
        # If the user is a supplier, give them access to the supplier pages
        if st.session_state["role"] == "supplier":
            SupplierHomeNav()
            SupplierDeliveriesNav()
            SupplierIngredientsNav()
            SupplierMaterialsNav()
            
        if st.session_state["role"] == "Manager":
            ManagerPageNav()
            

                

    # Always show the About page at the bottom of the list of links
    AboutPageNav()

    if st.session_state["authenticated"]:
        # Always show a logout button if there is a logged in user
        if st.sidebar.button("Logout"):
            del st.session_state["role"]
            del st.session_state["authenticated"]
            st.switch_page("Home.py")