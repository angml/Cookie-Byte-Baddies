import pandas as pd
import logging
logger = logging.getLogger(__name__)
import streamlit as st
from modules.nav import SideBarLinks
import requests
import altair as alt

logger = logging.getLogger(__name__)

st.set_page_config(layout = 'wide')

SideBarLinks()


st.markdown("""
    <style>
        .stApp { background-color: #f3e8ff; }
        .block-container { background-color: #f3e8ff; }
        html, body, [class*="css"] { color: 2d2d2d; }
        h1, h2, h3, h4 { color: #6a0dad; }
        button {
            background-color: #9b5de5 !important;
            color: white !important;
            border: 2px solid white !important;
            border-radius: 6px !important;
        }
        .stDataFrame {
            background-color: #ffc0cb !important;
            border: 1px solid #ffaad4;
            border-radius: 6px;
            padding: 6px;  
        }
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

st.title('Ingredients Page')

# Gets the ingredient list
def get_ing_list():
    try:
        response = requests.get('http://web-api:4000/i/ingredients')
        response.raise_for_status()
        if response.text.strip():
            data = response.json()
            if isinstance(data, list) and data:
                return pd.DataFrame(data)
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching ingredients: {e}")
    return pd.DataFrame()

df = get_ing_list()

# Display the ingredient list
st.subheader("📋 Ingredients List")
if not df.empty:
    st.dataframe(df)
else:
    st.write("No ingredients available.")


st.write("### 📈 Top 10 Ingredients with the Highest Burn Rate")

response = requests.get("http://web-api:4000/i/ingredients/burnrate/top")

# Makes a bar chart of high burn rates
if response.status_code == 200:
    data = response.json()
    df = pd.DataFrame(data)

    df["BurnRate"] = pd.to_numeric(df["BurnRate"], errors="coerce")

    df = df.sort_values(by="BurnRate", ascending=False)

    chart = alt.Chart(df).mark_bar(color="#6a0dad").encode(
        x=alt.X(
            "BurnRate:Q", 
            title="Burn Rate", 
            scale=alt.Scale(domain=[0, df["BurnRate"].max()]),
            axis=alt.Axis(grid=True, gridColor='gray', gridOpacity=1, gridWidth=1.5)
        ),
        y=alt.Y("IngredientName:N", sort='-x', title="Ingredient"),
        tooltip=["IngredientName", "BurnRate"]
    ).properties(
        width=700,
        height=400,
    ).configure_view(
        fill="#f3e8ff"
    ).configure(
        background="#f3e8ff"
    )

    st.altair_chart(chart, use_container_width=True)

else:
    st.error("Failed to fetch burn rate data")


st.write("### 📉 Top 10 Ingredients with the Lowest Burn Rate")

response = requests.get("http://web-api:4000/i/ingredients/burnrate/bottom")

# Makes a bar chart with the lowest burn rate
if response.status_code == 200:
    data = response.json()
    df_bottom = pd.DataFrame(data)

    df_bottom["BurnRate"] = pd.to_numeric(df_bottom["BurnRate"], errors="coerce")

    df_bottom = df_bottom.sort_values(by="BurnRate", ascending=True)

    bottom_chart = alt.Chart(df_bottom).mark_bar(color="#6a0dad").encode(
        x=alt.X(
            "BurnRate:Q", 
            title="Burn Rate", 
            scale=alt.Scale(domain=[0, df_bottom["BurnRate"].max()]),
            axis=alt.Axis(grid=True, gridColor='gray', gridOpacity=1, gridWidth=1.5)
        ),
        y=alt.Y("IngredientName:N", sort='x', title="Ingredient"),
        tooltip=["IngredientName", "BurnRate"]
    ).properties(
        width=700,
        height=400,
    ).configure_view(
        fill="#f3e8ff"
    ).configure(
        background="#f3e8ff"
    )

    st.altair_chart(bottom_chart, use_container_width=True)

else:
    st.error("Failed to fetch lowest burn rate data")



# Update inventory number
response = requests.get('http://web-api:4000/i/ingredients')
ing_items = response.json()


st.write("### ➕ Update Inventory of an Ingredient")
selected_ingredient = st.selectbox("Select Ingredient to Update", [item['IngredientName'] for item in ing_items])
new_inventory = st.number_input("Enter New Inventory Number", min_value=0, step=1)


# Updates the inventory of a selected ingredient
if st.button("Update Inventory"):
    # Get the selected item's ID 
    inv_to_update = next(item for item in ing_items if item['IngredientName'] == selected_ingredient)
    item_id = inv_to_update['IngredientID']
       
    update_url = f'http://web-api:4000/i/ingredients/update-inventory/{item_id}'
    response = requests.put(update_url, json={"Inventory": new_inventory})
      
    if response.status_code == 200:
        st.success(f"Inventory for {selected_ingredient} updated successfully!")
        st.rerun()
    else:
        st.error(f"Failed to update Inventory for {selected_ingredient}. Please try again. Status: {response.status_code}")