import streamlit as st
from components.data_profiling import get_data_profile_report
from sklearn.datasets import load_iris
import pandas as pd
from streamlit_pandas_profiling import st_profile_report
from sklearn.datasets import fetch_openml


def load_view():
    if st.session_state.get("pipeline") is None:
        st.warning("Please first load your data in the Data loading page")
    else:
        report = st.session_state.get("pipeline").report
        st_profile_report(report=report)


load_view()
