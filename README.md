Flood Risk Analysis in the Ganga–Brahmaputra–Meghna (GBM) Basin
Project Overview
Flooding is a recurring natural hazard in the Ganga–Brahmaputra–Meghna (GBM) basin, affecting millions of people every year. This project presents a geospatial analysis of flood risk using gauging station danger level data to identify high‑risk flood zones and evaluate whether nearby stations fall within critical influence areas.

The study applies spatial distance analysis and interactive mapping techniques to visualize flood risk patterns and support flood preparedness and planning at a regional scale.

Objectives
The main objectives of this project are:

To spatially visualize flood danger levels across gauging stations in the GBM basin

To classify gauging stations into low, medium, and high flood risk categories

To identify high‑risk flood zones based on extreme danger levels

To analyze the proximity of gauging stations to high‑risk flood zones using distance‑based geospatial techniques

To develop an interactive web application for intuitive exploration of flood risk patterns

Study Area
The analysis is strictly limited to the Ganga–Brahmaputra–Meghna (GBM) basin, one of the most flood‑prone river systems in South Asia.
All non‑GBM stations are filtered out to ensure spatial and thematic accuracy.

Dataset Description
The dataset consists of flood gauging stations with the following key attributes:

Station Name

Latitude and Longitude

River Name

State

Basin

Danger Level (numeric value representing flood severity)

The dataset is provided in CSV format and processed using Python‑based geospatial libraries.

Methodology
1. Data Preprocessing
Converted latitude, longitude, and danger level values to numeric format

Removed records with missing spatial coordinates

Filtered the dataset to retain only GBM basin stations

2. Risk Classification
Gauging stations were classified into three flood risk categories using percentile‑based thresholds:

High Risk – Upper quartile (extreme danger levels)

Medium Risk – Moderate danger levels

Low Risk – Relatively safer locations

3. Identification of High‑Risk Flood Zones
High‑risk gauging stations were treated as flood risk zones, representing areas with severe flood potential.

4. Spatial Distance Analysis
The geodesic distance between each gauging station and the nearest high‑risk zone was calculated

A 50 km threshold was used to determine whether a station lies within the influence of a high‑risk flood zone

Stations within this threshold were marked as near high‑risk zones

5. Geospatial Visualization
Flood risk levels were visualized using color‑coded markers:

🔴 Red – High Risk

🟠 Orange – Medium Risk

🟢 Green – Low Risk

50 km influence circles were drawn around high‑risk zones

Interactive popups provide detailed station information

Streamlit Web Application
An interactive web application was developed using Streamlit and Folium to present the analysis results.

Key Features
Interactive flood risk map of the GBM basin

Visual differentiation of risk categories

Influence zones around high‑risk flood areas

Informative popups for each gauging station

User‑friendly interface for academic and decision‑support purposes

Technologies Used
Python

Pandas – data handling and preprocessing

Geopy – distance calculation using geodesic methods

Folium – interactive map visualization

Streamlit – web application deployment

Project Structure
gbm-flood-risk-streamlit/
│
├── app.py                # Streamlit application code
├── flood_gauges.csv      # Dataset
├── requirements.txt      # Required Python libraries
├── README.md             # Project documentation

How to Run the Application Locally
1. Clone the repository

2. Install dependencies using:

pip install -r requirements.txt
Run the Streamlit app:

streamlit run app.py
Key Insights
High flood risk stations are spatially clustered along specific river stretches in the GBM basin

Several gauging stations lie within 50 km of high‑risk flood zones, indicating regions of heightened vulnerability

Spatial proximity analysis enhances understanding beyond individual station data

Conclusion
This project demonstrates how geospatial techniques can be effectively applied to flood risk assessment using gauging station data. The interactive visualization provides clear spatial insights that can assist researchers, planners, and disaster management authorities in identifying flood‑prone regions and prioritizing mitigation efforts.

Academic Note
This project was developed as part of an academic geospatial analytics assignment and is intended for educational and analytical purposes.


└── .gitignore

