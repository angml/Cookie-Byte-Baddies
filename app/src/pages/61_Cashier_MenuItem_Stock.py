import streamlit as st
import requests
from modules.nav import SideBarLinks

# Setup sidebar
SideBarLinks()

st.write("# Cafe Menu Stock Tracker for Front Line")

# Fetch the categories to filter by (API stuff...)
categories_response = requests.get('http://api:4000/m/categories')
categories = ["All"]
if categories_response.status_code == 200:
    category_data = categories_response.json()
    categories += [c['value'] for c in category_data]

# Dropdown to select category
selected_category = st.selectbox("Select Category", categories)

# Get the menu items for the selected category (filtered by category)
menu_url = f'http://api:4000/m/menu-items/category/{selected_category}' if selected_category != "All" else 'http://api:4000/m/menu-items'
menu_response = requests.get(menu_url)

# Check if the response is successful
if menu_response.status_code == 200:
    menu_items = menu_response.json()

    # Display table headers
    st.markdown("### Menu Items Stock Overview")
    st.write("Here you can track the stock levels for each menu item.")

    # Create a table with ItemID, Name, Stock, and Status
    menu_table = []
    for item in menu_items:
        item_id = item.get('ItemID', 'N/A')
        name = item.get('Name', 'N/A')
        stock = item.get('Stock', 'N/A')
        status = item.get('Status', 'N/A')
        menu_table.append([name, stock, status])

    # Show the data in a table
    st.write("### Menu Item Stock Information")
    st.table(menu_table)

    # Update stock
    st.write("### Update Stock")
    selected_item = st.selectbox("Select Item to Update", [item['Name'] for item in menu_items])
    new_stock = st.number_input("Enter New Stock Level", min_value=0, step=1)
    
    if st.button("Update Stock"):
        # Make API call to update the stock level for selected item
        item_to_update = next(item for item in menu_items if item['Name'] == selected_item)
        item_id = item_to_update['ItemID']
        
        update_url = f'http://api:4000/m/menu-items/update-stock/{item_id}'
        response = requests.put(update_url, json={"Stock": new_stock})
        
        if response.status_code == 200:
            st.success(f"Stock for {selected_item} updated successfully!")
        else:
            st.error(f"Failed to update stock for {selected_item}. Please try again.")
else:
    st.error("Failed to retrieve menu items.")
