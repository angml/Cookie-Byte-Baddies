import logging
import streamlit as st
import requests
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks


# Setup logger
logger = logging.getLogger(__name__)

# Image URL mapping for menu items
image_mapping = {
    "Croissant": 'assets/croissant.jpeg',
    "Blueberry Muffin": 'assets/blueberry_muffin.jpg',
    "Turkey & Swiss Sandwich": 'assets/turkey_and_swiss.jpg',
    "Caprese Panini": 'assets/caprese.jpg',
    "Tiramisu": 'assets/tiramisu.jpg',
    "Cherry Pie": 'assets/cherry_pie.jpg',
    "Avocado Toast": 'assets/avo_toast.jpg'
    # Add more items and their image URLs here...
}

unavailable_overlay_image = 'assets/sold_out.png' 


# Setup sidebar
SideBarLinks()

# Display the header
st.write("# 'Sip Happens' Menu")

# --- Drop Down Menu for Categories ---
try:
    categories_response = requests.get('http://api:4000/m/categories')
    categories_response.raise_for_status()
    category_data = categories_response.json()
    categories = ["All"] + [c['value'] for c in category_data]
except Exception as e:
    logger.error(f"Failed to load categories: {e}")
    categories = ["All"]

# Dropdown to filter menu by category
selected_category = st.selectbox("Filter by Category", categories)

# --- Adjust API Endpoint Based on Category ---
if selected_category == "All":
    menu_url = 'http://api:4000/m/menu-items'
else:
    menu_url = f'http://api:4000/m/menu-items/category/{selected_category}'

# Make API call to fetch filtered menu items
try:
    menuItems = requests.get(menu_url).json()

    # Separate available and unavailable items
    available_items = []
    unavailable_items = []

    if isinstance(menuItems, list):
        for item in menuItems:
            # Get item details
            name = item.get('Name', 'N/A')
            price = item.get('Price', 'N/A')
            availability = item.get('Status', 'Unavailable')
            image_url = image_mapping.get(name, None)

            # Add items to respective lists based on availability
            if availability == 'Available':
                available_items.append((name, price, availability, image_url))
            else:
                unavailable_items.append((name, price, availability, image_url))

        # --- Display Available Items ---
        st.markdown("<h3 style='color: blue;'>Available Items</h3>", unsafe_allow_html=True)

        for item in available_items:
            name, price, availability, image_url = item

            # Use columns for a more organized layout
            col1, col2 = st.columns([3, 1])  # The left column will take 3 parts, the right one 1 part

            with col1:  # item descriptions
                st.markdown(f"### {name}")
                st.markdown(f"**Price:** ${price}")
                st.markdown(f"**Status:** {availability}")

            with col2:  # image
                if image_url:
                    st.image(image_url, caption=name, width=150)

            st.markdown("---")  # Adds a horizontal line for separation

        # --- Display Unavailable Items ---
        st.markdown("<h3 style='color: grey;'>Unavailable Items</h3>", unsafe_allow_html=True)

        for item in unavailable_items:
            name, price, availability, image_url = item

            # Use columns for a more organized layout
            col1, col2 = st.columns([3, 1])  # The left column will take 3 parts, the right one 1 part

            with col1:  # item descriptions
                st.markdown(f"### <span style='color: grey;'>{name}</span>", unsafe_allow_html=True)
                st.markdown(f"**Price:** <span style='color: grey;'>{price}</span>", unsafe_allow_html=True)
                st.markdown(f"**Status:** <span style='color: red;'>{availability}</span>", unsafe_allow_html=True)

            with col2:  # image (also greyed out)
                if image_url:
                    st.image(image_url, caption=name, width=150)

            st.markdown("---")  # Adds a horizontal line for separation

    else:
        st.write("API did not return a valid list of menu items.")

except requests.exceptions.RequestException as e:
    st.write("Could not connect to database to retrieve menu items.")
    logger.error(f"Error fetching data from API: {e}")
