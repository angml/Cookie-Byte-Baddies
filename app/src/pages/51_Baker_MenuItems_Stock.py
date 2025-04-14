import streamlit as st
import requests
from modules.nav import SideBarLinks

# Setup sidebar
SideBarLinks()

st.write("# Cafe Menu Stock Tracker")

# Fetch the categories to filter by 
categories_response = requests.get('http://api:4000/m/categories')
categories = ["All"]
if categories_response.status_code == 200:
    category_data = categories_response.json()
    categories += [c['value'] for c in category_data]

# Dropdown to select the category
selected_category = st.selectbox("Select Category", categories)

# Get the menu items for the selected category (filtered by category)
menu_url = f'http://api:4000/m/menu-items/category/{selected_category}' if selected_category != "All" else 'http://api:4000/m/menu-items'
menu_response = requests.get(menu_url)

# Check if response was a success
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

    # Show data in a table
    st.write("### Menu Item Stock Information")
    st.table(menu_table)

    # Update stock number
    st.write("### Update Stock")
    selected_item = st.selectbox("Select Item to Update", [item['Name'] for item in menu_items])
    new_stock = st.number_input("Enter New Stock Level", min_value=0, step=1)
    
    if st.button("Update Stock"):
        # Make API call to update the stock level for the selected item 
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
    
## DELETING A MENU ITEM 
st.write("### Delete a Menu Item")
item_to_delete = st.selectbox("Select Item to Delete", [item['Name'] for item in menu_items])

if st.button("Delete Item"):
    # Get the item ID
    selected_item_obj = next(item for item in menu_items if item['Name'] == item_to_delete)
    item_id = selected_item_obj['ItemID']

    # Call the DELETE API
    delete_url = f'http://api:4000/m/menu-items/delete/{item_id}'
    delete_response = requests.delete(delete_url)

    if delete_response.status_code == 200:
        st.success(f"'{item_to_delete}' has been deleted.")
    elif delete_response.status_code == 404:
        st.error("Item not found.")
    else:
        st.error("Something went wrong while deleting the item.")
        
## CREATING A NEW MENU ITEM
st.subheader("Add a New Menu Item")

# Input fields for the new menu item
name = st.text_input("Item Name")
price = st.number_input("Price", min_value=0.0, step=0.1)
stock = st.number_input("Stock", min_value=0, step=1)
shelf_life = st.text_input("Shelf Life")

# Dropdown for status
status = st.selectbox("Status", ["Available", "Unavailable"])

# Fetch categories (this assumes you've already fetched categories as shown earlier)
category_response = requests.get('http://api:4000/m/categories')
category_options = [cat['value'] for cat in category_response.json()] if category_response.status_code == 200 else []
category = st.selectbox("Select Category", category_options)

# Form submission button
if st.button("Add Menu Item"):
    # Basic Validation: Check if all required fields are filled
    if not name or not shelf_life or category == "":
        st.error("Please fill in all the fields. Item Name, Shelf Life, and Category are required.")
    elif price <= 0 or stock < 0:
        st.error("Please enter a valid price (greater than 0) and a non-negative stock quantity.")
    else:
        # stuff to send to back end
        item_data = {
            "Name": name,
            "Status": status,
            "Price": price,
            "Category": category,
            "Stock": stock,
            "ShelfLife": shelf_life
        }

        # Make POST request to the API to create the menu item
        response = requests.post("http://api:4000/m/menu-items/create", json=item_data)

        # Handle API response
        if response.status_code == 201:
            st.success(f"New menu item '{name}' added successfully!")
        elif response.status_code == 400:
            st.error("Invalid input. Please check the entered data.")
        elif response.status_code == 500:
            st.error("Server error. Please try again later.")
        else:
            st.error(f"Failed to add item. Status code: {response.status_code}")




