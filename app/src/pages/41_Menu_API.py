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
st.write("# Accessing 'Sip Happens' Menu (Rest API test)")

# Make API call to fetch menu items
try:
    menuItems = requests.get('http://api:4000/m/menu-items').json()

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
            
            # Add items to respective lists
            if availability == 'Available':
                available_items.append((name, price, availability, image_url))
            else:
                unavailable_items.append((name, price, availability, image_url))

        # Display available items
        st.markdown("<h3 style='color: blue;'>Available Items</h3>", unsafe_allow_html=True)
        
        for item in available_items:
            name, price, availability, image_url = item
            
            # Use columns for a more organized layout
            col1, col2 = st.columns([3, 1])  # The left column will take 3 parts, the right one 1 part
            
            # Display item
            with col1: # item descriptions
                st.markdown(f"### {name}")
                st.markdown(f"**Price:** ${price}")
                st.markdown(f"**Status:** {availability}")
            
            with col2: # image
                if image_url:
                    st.image(image_url, caption=name, width=150)  # Adjust the width as needed

            st.markdown("---")  # Adds a horizontal line for separation

        # Display unavailable items at the bottom
        st.markdown("<h3 style='color: grey;'>Unavailable Items</h3>", unsafe_allow_html=True)

        for item in unavailable_items:
            name, price, availability, image_url = item
            
            # Use columns for a more organized layout
            col1, col2 = st.columns([3, 1])  # The left column will take 3 parts, the right one 1 part
            
            # Display item with greyed-out style
            with col1: # item descriptions
                st.markdown(f"### <span style='color: grey;'>{name}</span>", unsafe_allow_html=True)
                st.markdown(f"**Price:** <span style='color: grey;'>{price}</span>", unsafe_allow_html=True)
                st.markdown(f"**Status:** <span style='color: red;'>{availability}</span>", unsafe_allow_html=True)
            
            with col2: # image (also greyed out)
                if image_url:
                    st.image(image_url, caption=name, width=150)  # Adjust the width as needed

            st.markdown("---")  # Adds a horizontal line for separation

    else:
        st.write("API did not return a valid list of menu items.")

except requests.exceptions.RequestException as e:
    st.write("Could not connect to database to retrieve menu items.")
    logger.error(f"Error fetching data from API: {e}")
