import streamlit as st


st.set_page_config(layout="wide", page_title="Epoch Solution")

import myutils as utl

# Files to be imported from views folder for
from views import (
    data_loading,
    unsupervised_analysis,
    supervised_analysis,
    data_profile_report,
)

utl.inject_custom_css()
utl.navbar_component()

# Main navigation function for the app
def navigation():
    route = utl.get_current_route()
    if route == "data-loading":
        data_loading.load_view()
        print(st.session_state.pipeline)
        utl.set_session_state(st.session_state.pipeline)
    elif route == "unsupervised-analysis":
        unsupervised_analysis.load_view()
    elif route == "supervised-analysis":
        supervised_analysis.load_view()
    elif route == "profile-report":
        st.session_state.pipeline = utl.get_session_state()
        print(st.session_state.pipeline)
        data_profile_report.load_view()

    st.markdown(
        """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .css-163ttbj {
            top : 75px;
            padding-bottom: 75px;
        }
        .css-1vq4p4l {
            padding: 2rem 1rem 1.5rem;
        }
        .navbar {
            padding-left: 50px;
        }
        </style>
    """,
        unsafe_allow_html=True,
    )


navigation()
