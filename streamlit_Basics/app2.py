import streamlit as st

st.title("Interactive Streamlit App")

# Add a slider
number = st.slider("Pick a number", 0, 100)

# Display the selected number
st.write("You selected:", number)