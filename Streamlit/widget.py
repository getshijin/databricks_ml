import streamlit as st 
import pandas as pd
import numpy as np

st.title("Simple Widget Demonstration")

name =st.text_input("Enter your name:")



if name: 
    st.write(f"Hello, {name}!")