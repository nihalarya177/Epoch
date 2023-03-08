import streamlit as st
import myutils as utl
# Files to be imported from views folder for 
from views import data_loading

#st.set_page_config(layout="wide", page_title="Epoch Solution")

st.set_option('deprecation.showPyplotGlobalUse', False)
utl.inject_custom_css()
utl.navbar_component()

# Main navigation function for the app
def navigation():
    route = utl.get_current_route()
    if route == "data-loading":
        data_loading.load_view()
    '''elif route == "mechanical-extraction":
        mechanical_extraction.load_view()
    elif route == "mechanical-loading":
        mechanical_loading.load_view()
    elif route == "mechanical-weibull-lognormal":
        mechanical_weibull_lognormal.load_view()
    elif route == "bltc":
        bltc.load_view()
    elif route == "options":
        options.load_view()
    elif route == "configuration":
        configuration.load_view()
    elif route == None:
        data_loading.load_view()'''
    
    st.markdown("""
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
    """, unsafe_allow_html=True)
        
navigation()
