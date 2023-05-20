import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import folium
from folium import plugins
from streamlit_folium import folium_static
from windrose import WindroseAxes

# Set themels
sns.set_theme(style="whitegrid")

# Load data (replace with your own dataset)
# Assuming that the dataset contains features: 'turbine_id', 'wind_speed', 'power_output', 'longitude', 'latitude', 'wind_direction'
df = pd.read_csv('wind_turbine_data.csv')

st.title('Wind Turbine Optimization Dashboard')

# Select Turbine
turbine_id_list = df['turbine_id'].unique().tolist()
selected_turbine = st.selectbox('Select a Wind Turbine', turbine_id_list)

# Filter data
df_selected = df[df['turbine_id'] == selected_turbine]

# Show Turbine Location on Map
m = folium.Map(location=[df_selected['latitude'].mean(),
               df_selected['longitude'].mean()], zoom_start=13)
for idx, row in df_selected.iterrows():
    folium.Marker([row['latitude'], row['longitude']]).add_to(m)
st.header('Turbine Location')
folium_static(m)

# Show Wind Speed vs Power Output Graph
fig, ax = plt.subplots()
sns.scatterplot(data=df_selected, x='wind_speed', y='power_output', ax=ax)
ax.set_title('Wind Speed vs Power Output')
st.header('Wind Speed vs Power Output')
st.pyplot(fig)

# Show Wind Rose Diagram for Wind Direction
ax = WindroseAxes.from_ax()
ax.bar(df_selected['wind_direction'], df_selected['wind_speed'],
       normed=True, opening=0.8, edgecolor='white')
ax.set_legend()
st.header('Wind Rose Diagram')
st.pyplot(fig)
