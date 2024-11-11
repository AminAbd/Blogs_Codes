import streamlit as st
import pydeck as pdk
import pandas as pd
st.title("Map Example with Pydeck")

# Sample data
data = {
    "latitude": [37.7749, 37.7849, 37.7949],
    "longitude": [-122.4194, -122.4294, -122.4394]
}
df = pd.DataFrame(data)

# Create the map
st.pydeck_chart(pdk.Deck(
    initial_view_state=pdk.ViewState(
        latitude=37.7749,
        longitude=-122.4194,
        zoom=11
    ),
    layers=[
        pdk.Layer(
            "ScatterplotLayer",
            data=df,
            get_position="[longitude, latitude]",
            get_color="[200, 30, 0, 160]",
            get_radius=200,
        ),
    ],
))
