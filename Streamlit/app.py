import streamlit as st 
import pandas as pd
import numpy as np

st.title("Simple DataFrame Viewer")

#simple text

st.write("This is a simple Streamlit app to display a DataFrame.")

#create a sample DataFrame
data = pd.DataFrame({
    'first_column': np.random.randn(5),
    'second_column': np.random.randn(5)
})

#display the dataframe
st.write("Here is a sample DataFrame:")
st.write(data)

#add a slider to filter the dataframe
chart_data = pd.DataFrame(
    np.random.randn(20, 3),columns=['a', 'b', 'c'])

st.line_chart(chart_data)