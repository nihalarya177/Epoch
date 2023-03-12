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
        st.markdown(
            """
                <style>
                    div[data-testid="stVerticalBlock"] div[style*="flex-direction: column;"] div[data-testid="stVerticalBlock"] {
                        border: 1px rgba(38,39,48,255);
                        border-radius: 7px;
                        background: #d4f1f4;
                        padding: 50px;
                        padding-right:150px;
                    }

                    div[role="listbox"] ul {
                        background-color: red;
                    }

                    div[data-baseweb="select"] > div {
                        background-color: white;
                    }
                </style>
                """,
            unsafe_allow_html=True,
        )
        with st.container():
            st_profile_report(report=report)


load_view()

