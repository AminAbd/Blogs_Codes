import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.title("Data Visualization with Streamlit")

# Generate some data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Plot the data
fig, ax = plt.subplots()
ax.plot(x, y)

# Display the plot in the Streamlit app
st.pyplot(fig)