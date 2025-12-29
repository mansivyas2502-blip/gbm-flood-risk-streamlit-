# -----------------------------------
# Streamlit + Folium Flood Risk App
# -----------------------------------
import streamlit as st
from streamlit_folium import st_folium
import streamlit as st
import pandas as pd
import folium
from geopy.distance import geodesic
from streamlit_folium import st_folium

# -----------------------------------
# Page title
# -----------------------------------

st.set_page_config(layout="wide")
st.title("Flood Risk Analysis – Ganga–Brahmaputra–Meghna Basin")

st.write("""
This application visualizes flood risk using **gauging station danger levels**.
It identifies **high‑risk flood zones** and checks whether nearby stations lie
within **50 km influence zones**, helping prioritize flood‑prone regions.
""")

# -----------------------------------
# Load data
# -----------------------------------

df = pd.read_csv("flood_gauges.csv")

# Clean numeric columns
df["Latitude"] = pd.to_numeric(df["Latitude"], errors="coerce")
df["Longitude"] = pd.to_numeric(df["Longitude"], errors="coerce")
df["Danger Level"] = pd.to_numeric(df["Danger Level"], errors="coerce")

df = df.dropna(subset=["Latitude", "Longitude"])

# -----------------------------------
# Filter GBM basin ONLY
# -----------------------------------

gbm_df = df[df["Basin"] == "Ganga - Brahmaputra - Meghna/Barak"].copy()

# -----------------------------------
# Risk classification
# -----------------------------------

def risk_category(val):
    if val >= gbm_df["Danger Level"].quantile(0.75):
        return "High"
    elif val >= gbm_df["Danger Level"].quantile(0.40):
        return "Medium"
    else:
        return "Low"

gbm_df["Risk"] = gbm_df["Danger Level"].apply(risk_category)

high_risk = gbm_df[gbm_df["Risk"] == "High"]

# -----------------------------------
# Distance to nearest high‑risk zone
# -----------------------------------

def nearest_high_risk_distance(row):
    min_d = float("inf")
    for _, hr in high_risk.iterrows():
        d = geodesic(
            (row["Latitude"], row["Longitude"]),
            (hr["Latitude"], hr["Longitude"])
        ).km
        min_d = min(min_d, d)
    return min_d

gbm_df["Distance_to_HighRisk_km"] = gbm_df.apply(nearest_high_risk_distance, axis=1)
gbm_df["Near_HighRisk"] = gbm_df["Distance_to_HighRisk_km"] <= 50

# -----------------------------------
# Create map
# -----------------------------------

m = folium.Map(location=[25.5, 85], zoom_start=6)

risk_colors = {
    "High": "red",
    "Medium": "orange",
    "Low": "green"
}

# Stations layer
stations_layer = folium.FeatureGroup(name="Gauging Stations")

for _, row in gbm_df.iterrows():
    border = "black" if row["Near_HighRisk"] else risk_colors[row["Risk"]]

    folium.CircleMarker(
        location=[row["Latitude"], row["Longitude"]],
        radius=6,
        color=border,
        fill=True,
        fill_color=risk_colors[row["Risk"]],
        fill_opacity=0.7,
        popup=f"""
        <b>Station:</b> {row['Station']}<br>
        <b>State:</b> {row['State']}<br>
        <b>Danger Level:</b> {row['Danger Level']}<br>
        <b>Risk:</b> {row['Risk']}<br>
        <b>Distance to High Risk (km):</b> {row['Distance_to_HighRisk_km']:.2f}
        """
    ).add_to(stations_layer)

stations_layer.add_to(m)

# High‑risk influence zones
zones_layer = folium.FeatureGroup(name="50 km High‑Risk Influence Zones")

for _, row in high_risk.iterrows():
    folium.Circle(
        location=[row["Latitude"], row["Longitude"]],
        radius=50000,
        color="red",
        fill=False
    ).add_to(zones_layer)

zones_layer.add_to(m)

folium.LayerControl().add_to(m)

# -----------------------------------
# Show map
# -----------------------------------
st.subheader("Flood Risk Map (GBM Basin)")
st_folium(m, width=900, height=600)

st_folium(m, width=1300, height=650)
