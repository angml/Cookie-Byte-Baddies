import logging
logger = logging.getLogger(__name__)
import pandas as pd
import streamlit as st
from streamlit_extras.app_logo import add_logo
import world_bank_data as wb
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px
from modules.nav import SideBarLinks
import requests

from modules.nav import SideBarLinks



st.set_page_config(layout="wide")

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

# Styling
st.markdown(
    """
    <style>
        .stApp {
            background-color: #f3e8ff;
        }
        .block-container {
            background-color: #f3e8ff;
        }
        html, body, [class*="css"]  {
            color: #2d2d2d;
        }
        h1, h2, h3, h4 {
            color: #6a0dad;
        }
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
    """,
    unsafe_allow_html=True
)


st.title("Costs Page")
st.write("Select a cost type to view details:")

if st.button("Labor", type="primary", use_container_width=True):
    st.switch_page("pages/05_Cost_Labor.py")  

if st.button("Utilities", type="primary", use_container_width=True):
    st.switch_page("pages/06_Cost_Utilities.py")  

if st.button("Supplies", type="primary", use_container_width=True):
    st.switch_page("pages/07_Cost_Supply.py")  

if st.button("View All Costs by Date", type="primary", use_container_width=True):
    st.switch_page("pages/08_Cost_Dates.py")



# --- Chart section ---
st.markdown("---")
st.subheader("📈 Monthly Cost Trends by Type")

# Define base URL for each type
base_url = "http://api:4000/costs/type"

# Reusable function for monthly line chart
def get_monthly_line_chart(cost_type, color, title):
    try:
        response = requests.get(f"{base_url}/{cost_type.lower()}")
        response.raise_for_status()
        data = response.json()
        if not data:
            return None

        df = pd.DataFrame(data, columns=["CostID", "Type", "PaymentDate", "PaymentAmount", "ManagerID"])
        df["PaymentDate"] = pd.to_datetime(df["PaymentDate"])
        df["Month"] = df["PaymentDate"].dt.to_period("M").astype(str)

        monthly_totals = df.groupby("Month")["PaymentAmount"].sum().reset_index()

        fig = px.line(
            monthly_totals,
            x="Month",
            y="PaymentAmount",
            markers=True,
            title=title,
            labels={"Month": "Month", "PaymentAmount": "Total Cost ($)"}
        )

        fig.update_traces(line_color=color)
        fig.update_layout(
            template="plotly_white",
            height=300,
            yaxis_tickprefix="$",
            margin=dict(l=10, r=10, t=30, b=30)
        )

        return fig

    except Exception as e:
        st.error(f"Error loading {cost_type} data: {e}")
        return None

# Create columns for the 3 graphs
col1, col2, col3 = st.columns(3)

with col1:
    fig1 = get_monthly_line_chart("labor", "#9b5de5", "Labor Costs")
    if fig1:
        st.plotly_chart(fig1, use_container_width=True)

with col2:
    fig2 = get_monthly_line_chart("supplies", "#00bbf9", "Supplies Costs")
    if fig2:
        st.plotly_chart(fig2, use_container_width=True)

with col3:
    fig3 = get_monthly_line_chart("utilities", "#00f5d4", "Utilities Costs")
    if fig3:
        st.plotly_chart(fig3, use_container_width=True)
