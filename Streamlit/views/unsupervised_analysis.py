import streamlit as st
from sklearn.datasets import fetch_openml
import pandas as pd
from pycaret.datasets import get_data

from components import eda_function, preprocessing



def load_view():
    st.markdown('''# **Exploratory Data Analysis**''')
    st.write('This page shows you reports and different graphs of your data')
    data = get_data('iris')
    eda_function.launch_eda(data)