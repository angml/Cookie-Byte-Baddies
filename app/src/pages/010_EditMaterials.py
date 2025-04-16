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

st.title('Materials Page')

# Gets the Material list 
def get_mat_list():
    try:
        response = requests.get('http://web-api:4000/m/materials')
        response.raise_for_status()
        if response.text.strip():
            data = response.json()
            if isinstance(data, list) and data:
                return pd.DataFrame(data)
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching materials: {e}")
    return pd.DataFrame()

df = get_mat_list()

# Display the material list
st.subheader("📋 Materials List")
if not df.empty:
    st.dataframe(df)
else:
    st.write("No Materials available.")



# Add new Material title
st.subheader("➕ Add a New Material")

# Input fields for the new matierial
name = st.text_input("Name")
price = st.number_input("Price", min_value=0.0, step=0.1)
inventory = st.number_input("Inventory", min_value=0, step=1)
burn_rate = st.number_input("Burn Rate", min_value=0.0, step=0.1)

# Button that adds a new material
if st.button("Add Material"):
    # All fields should have a value
    if not name or price is None or inventory is None or burn_rate is None:
        st.error("Please fill out all fields before submitting. Thank you!")
    # Must have a real price and burn rate greater than zero. We are allowed to have a 0 for inventory
    # to represent when we run out of an item :)
    elif price <= 0.0 or burn_rate <= 0:
        st.error("Please enter a valid price or burn rate number (greater than 0). Thank you!")
    else:
        # stuff to send to back end
        item_data = {
            "Name": name,
            "Price": price,
            "Inventory" : inventory,
            "BurnRate" : burn_rate
        }

        # Makes a POST request to the API to create the material
        response = requests.post("http://web-api:4000/m/materials/create", json=item_data)
        
        # Handles either a success or error response
        if response.status_code == 201:
            st.success(f"New material '{name}' added successfully!")
            # refreshes the page automatically!
            st.rerun()
        elif response.status_code == 400:
            st.error("Invalid input. Please check the entered data.")
        elif response.status_code == 500:
            st.error("Server error. Please try again later.")
        else:
            st.error(f"Failed to add material. Status code: {response.status_code}")


# Makes a title for burn rate
st.write("### 📈 Top 10 Materials with the Highest Burn Rate")

response = requests.get("http://web-api:4000/m/materials/burnrate/top")

# Makes a burn rate bar chart
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
        y=alt.Y("Name:N", sort='-x', title="Ingredient"),
        tooltip=["Name", "BurnRate"]
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

# Makes a title for burn rate
st.write("### 📉 Top 10 Materials with the Lowest Burn Rate")

response = requests.get("http://web-api:4000/m/materials/burnrate/bottom")

# Makes a burn rate chart
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
            axis=alt.Axis(grid=True, gridColor="gray", gridOpacity=1, gridWidth=1.5)
        ),
        y=alt.Y("Name:N", sort='x', title="Ingredient"),
        tooltip=["Name", "BurnRate"]
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