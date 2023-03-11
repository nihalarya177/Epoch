import streamlit as st
from components.data_profiling import get_data_profile_report
from sklearn.datasets import load_iris
import pandas as pd
from streamlit_pandas_profiling import st_profile_report


def load_view():
    iris = load_iris(as_frame=True)
    data = pd.concat([iris.data, iris.target], axis=1)
    with st.spinner("Wait for it..."):
        report = get_data_profile_report(data)
    st_profile_report(report=report)
