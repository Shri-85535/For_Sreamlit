import streamlit as st
import pandas as pd
import numpy as np
import random
import plotly.express as px

# Set page config
st.set_page_config(page_title="City AI Core", layout="wide")

# Custom sci-fi styling with neon/glassmorphism
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@500&display=swap');

        html, body, [class*="css"]  {
            font-family: 'Orbitron', sans-serif;
            background-color: #0f0f23;
            color: #c7f5ff;
        }
        .stApp {
            background: linear-gradient(135deg, #0f0f23 60%, #1c1c2e);
            color: #c7f5ff;
        }
        h1, h2, h3, h4 {
            color: #00f7ff;
            text-shadow: 0 0 8px #00f7ff;
        }
        .block-container {
            padding-top: 2rem;
        }
        .cool-table {
            border-collapse: collapse;
            width: 100%;
            background-color: #0f0f23;
            color: #c7f5ff;
            font-size: 16px;
        }
        .cool-table th {
            background-color: #1c1c2e;
            color: #00f7ff;
            padding: 10px;
            border: 1px solid #00f7ff;
        }
        .cool-table td {
            background-color: #141622;
            color: #c7f5ff;
            padding: 10px;
            text-align: center;
            border: 1px solid #333;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("""
    <h1 style='text-align: center;'>🛰️ CITY AI CORE</h1>
    <h4 style='text-align: center; color:#9be7ff;'>Real-time Traffic Intelligence Powered by Adaptive Learning</h4>
""", unsafe_allow_html=True)

# Sidebar
zones = ["Zone A - Market", "Zone B - School", "Zone C - Hospital", "Zone D - Residential", "Zone E - Highway"]
selected_zone = st.sidebar.selectbox("🧭 Select Zone", zones)
time_of_day = st.sidebar.selectbox("⏱️ Time Range", ["Morning (6AM-12PM)", "Afternoon (12PM-6PM)", "Evening (6PM-12AM)", "Night (12AM-6AM)"])

# Fake data
def generate_violation_data():
    base_zones = [z.split(" -")[0] for z in zones]
    data = {
        "Zone": random.choices(base_zones, k=100),
        "Time": random.choices(["Morning", "Afternoon", "Evening", "Night"], k=100),
        "Violation Type": random.choices(["Helmet", "Wrong Way", "Red Light", "Triple Seat"], k=100),
        "Count": np.random.randint(1, 20, 100)
    }
    return pd.DataFrame(data)

violation_df = generate_violation_data()

# Heatmap
st.subheader("🌐 Violation Heatmap Grid")
heatmap_data = violation_df.groupby(["Zone", "Violation Type"]).sum().reset_index()
styled_html = heatmap_data.pivot(index="Zone", columns="Violation Type", values="Count").fillna(0).to_html(classes="cool-table", border=0)
st.markdown(styled_html, unsafe_allow_html=True)

# Violation Type Breakdown with Plotly Neon Bars
st.subheader("⚠️ AI Violation Breakdown by Type")
zone_key = selected_zone.split(" -")[0]
time_label = time_of_day.split(" ")[0]

filtered_data = violation_df[
    (violation_df["Zone"] == zone_key) &
    (violation_df["Time"] == time_label)
]

if not filtered_data.empty:
    type_chart = filtered_data.groupby("Violation Type")["Count"].sum().reset_index()
    fig = px.bar(
        type_chart,
        x="Violation Type",
        y="Count",
        title=f"{zone_key} - {time_label} Violations",
        color="Violation Type",
        color_discrete_sequence=["#00f7ff", "#ff4c4c", "#f4ff00", "#9c27b0"],
    )
    fig.update_layout(
        plot_bgcolor="#0f0f23",
        paper_bgcolor="#0f0f23",
        font=dict(color="#c7f5ff"),
        title_font=dict(size=20, color="#00f7ff")
    )
    st.plotly_chart(fig, use_container_width=True)
else:
    st.info("No violations recorded in this zone and time window (simulated data).")

# AI Recommendations
st.subheader("🤖 Adaptive AI Traffic Recommendations")
if selected_zone == "Zone B - School" and time_label == "Morning":
    st.info("🚸 Helmet violations spike near schools during mornings. Deploy banners or enforcement from 7–9 AM.")
elif selected_zone == "Zone E - Highway" and time_label == "Evening":
    st.warning("⚠️ Wrong-way violations rise on highways post 8 PM. Suggest reflective cones or blinking barricades.")
else:
    st.success("✅ Violation levels are stable. Continue automated camera-based monitoring.")
