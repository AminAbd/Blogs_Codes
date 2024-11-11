import streamlit as st
import pandas as pd

import streamlit as st
import pandas as pd

st.title("Upload Your CSV File")

# Use a descriptive label for the file uploader
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.write("Data Preview:")
    st.write(data)
