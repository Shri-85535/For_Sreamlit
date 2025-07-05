import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objs as go
from datetime import datetime
import random
import time


st.set_page_config(page_title="City AI Core - Live Violation Dashboard", layout="wide")

# Custom Styling
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@600&display=swap');
        html, body, [class*="css"] {
            font-family: 'Orbitron', sans-serif;
            background-color: #0f0f23 !important;
            color: #c7f5ff !important;
        }
        .card {
            background-color: #1a1a2e;
            padding: 1rem;
            border-radius: 15px;
            box-shadow: 0 0 15px rgba(0, 255, 255, 0.15);
            margin-bottom: 1rem;
        }
        .card h2 {
            color: #00ffe1;
            font-size: 20px;
        }
        .card strong {
            color: #ffffff !important;
            font-size: 22px;
        }
        .card small {
            color: #00ff88;
        }
        .highlight-title {
            color: #00ffe1;
            font-size: 24px;
            margin-top: 0.5rem;
            margin-bottom: 0.5rem;
        }
        .pulse-dot {
            height: 10px;
            width: 10px;
            background-color: red;
            border-radius: 50%;
            display: inline-block;
            animation: pulse 1s infinite;
        }
        @keyframes pulse {
            0% { box-shadow: 0 0 0 0 rgba(255,0,0, 0.7); }
            70% { box-shadow: 0 0 0 10px rgba(255,0,0, 0); }
            100% { box-shadow: 0 0 0 0 rgba(255,0,0, 0); }
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar
st.sidebar.title("📡 Navigation")
page = st.sidebar.radio("Go to", ["Live Dashboard", "AI Insights", "Export PDF (Soon)"])
#auto_refresh = st.sidebar.checkbox("🔄 Auto-refresh every 30s", value=False)

auto_refresh = st.sidebar.checkbox("🔄 Auto-refresh every 30s", value=False)

if auto_refresh:
    st.rerun()

if page == "Live Dashboard":
    st.markdown("<h1 class='highlight-title'>🧠 City AI Core - Traffic Command Center <span class='pulse-dot'></span></h1>", unsafe_allow_html=True)
    st.caption(f"Last updated: {datetime.now().strftime('%I:%M:%S %p')}")

    # Main Grid Layout
    top_row = st.columns(4)
    with top_row[0]:
        st.markdown(f"<div class='card'><h2>🚗 Vehicles on Road</h2><strong>{random.randint(5500, 5800)}</strong><br><small>↑ 7.5% today</small></div>", unsafe_allow_html=True)
    with top_row[1]:
        st.markdown(f"<div class='card'><h2>⚠️ Detected Violations</h2><strong>{random.randint(1000, 1200)}</strong><br><small>↑ 12% since yesterday</small></div>", unsafe_allow_html=True)
    with top_row[2]:
        st.markdown(f"<div class='card'><h2>🎯 AI Rules Triggered</h2><strong>{random.randint(20, 30)}</strong><br><small>+5 school zones</small></div>", unsafe_allow_html=True)
    with top_row[3]:
        st.markdown(f"<div class='card'><h2>🚧 Zones Monitored</h2><strong>{random.randint(12, 16)}</strong><br><small>6 pending review</small></div>", unsafe_allow_html=True)

    mid_row = st.columns(3)
    with mid_row[0]:
        st.markdown("<div class='card'><h2>🎥 Camera Uptime</h2><strong>Live: 96.7%</strong><br><small>Offline: 3 zones</small></div>", unsafe_allow_html=True)
    with mid_row[1]:
        st.markdown(f"<div class='card'><h2>📞 Emergency Calls</h2><strong>{random.randint(6, 10)}</strong><br><small>Avg. Duration: 11m</small></div>", unsafe_allow_html=True)
        # Line chart moved below this row

        # Fill the gap with mini alert trend chart
        st.markdown("<div class='card'><h2>🚦 Alert Trends</h2></div>", unsafe_allow_html=True)
        alerts_df = pd.DataFrame({
            "Time": pd.date_range(end=datetime.now(), periods=10, freq="h"),
            "Alerts": [random.randint(5, 20) for _ in range(10)]
        })
        fig_alerts = go.Figure()
        fig_alerts.add_trace(go.Scatter(
            x=alerts_df["Time"].dt.strftime("%H:%M"),
            y=alerts_df["Alerts"],
            mode="lines+markers",
            line=dict(color="orange")
        ))
        fig_alerts.update_layout(template="plotly_dark", height=160, margin=dict(t=10, b=10, l=10, r=10))
        st.plotly_chart(fig_alerts, use_container_width=True)
    with mid_row[2]:
        st.markdown("<div class='card'><h2>🌍 City Map Coverage</h2></div>", unsafe_allow_html=True)
        st.map(pd.DataFrame({'lat': [27.4705], 'lon': [94.9125]}))

    # Live Violation Feed
    st.markdown("<div class='card'><h2>📈 Live Violation Feed</h2>", unsafe_allow_html=True)
    current_time = datetime.now()
    live_x = [(current_time - pd.Timedelta(seconds=i)).strftime("%H:%M:%S") for i in range(29, -1, -1)]
    live_y = [random.randint(10, 60) for _ in range(30)]
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=live_x, y=live_y, mode='lines+markers', line=dict(color='cyan')))
    fig.update_layout(template="plotly_dark", height=300, xaxis_title="Time", yaxis_title="Violations")
    st.plotly_chart(fig, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

    # Bottom Graphs
    bottom_row = st.columns(2)
    with bottom_row[0]:
        st.markdown("<div class='card'><h2>🔥 Violation Heatmap</h2></div>", unsafe_allow_html=True)
        zones = ['School', 'Market', 'Highway', 'Bus Stand', 'Residential']
        heat_df = pd.DataFrame({"Zones": zones, "Violations": [random.randint(30, 100) for _ in zones]})
        fig2 = go.Figure(data=go.Bar(x=heat_df["Zones"], y=heat_df["Violations"], marker_color='red'))
        fig2.update_layout(template="plotly_dark", height=300)
        st.plotly_chart(fig2, use_container_width=True)

    with bottom_row[1]:
        st.markdown("<div class='card'><h2>👥 Violation by Vehicle Type</h2></div>", unsafe_allow_html=True)
        types = ['2-Wheelers', 'Cars', 'Autos', 'Buses', 'Trucks']
        values = [random.randint(50, 200) for _ in types]
        fig3 = go.Figure(data=go.Pie(labels=types, values=values, hole=0.3))
        fig3.update_layout(template="plotly_dark", height=300)
        st.plotly_chart(fig3, use_container_width=True)

    st.markdown("---")
    st.markdown("🟢 Built by Scintinova | Demo UI | © 2025")

elif page == "AI Insights":
    st.markdown("<h1 class='highlight-title'>📊 AI Behavior Insights</h1>", unsafe_allow_html=True)
    st.markdown("""
    - 🚨 **Market Area Spike**: +43% wrong turns between **7–9 PM**
    - 🏫 **School Zones Strict**: Active from **7 AM – 5 PM**
    - 🌙 **Night Mode Active**: Highway leniency after **10 PM**
    - 🧠 **AI Triggered**: Auto-flagged 19 cameras for model drift
    - 🕶️ **Prediction**: Helmet violations expected post-weekend
    """)

elif page == "Export PDF (Soon)":
    st.markdown("<h1 class='highlight-title'>📄 Export Dashboard to PDF</h1>", unsafe_allow_html=True)
    st.info("Coming soon: Export visual dashboard and insights as a printable CM briefing report.")
