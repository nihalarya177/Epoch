import streamlit as st

st.set_page_config(layout="wide", page_title="Epoch Solution")
# print(sys.path)
import webbrowser
import urllib
import base64
from typing import List
from st_pages import Page, show_pages, add_page_title
from streamlit_extras.switch_page_button import switch_page
import os

ROOT_DIR = os.path.abspath(os.curdir)
# print(ROOT_DIR)
# Specify what pages should be shown in the sidebar, and what their titles and icons
# should be
show_pages(
    [
        Page(
            f"{ROOT_DIR}/Streamlit/pages.py",
            "Usable AI",
            "🕵️",
        ),
        Page(
            f"{ROOT_DIR}/Streamlit/views/data_loading.py",
            "Data Loading",
            "🕵️",
        ),
        Page(
            f"{ROOT_DIR}/Streamlit/views/supervised_analysis.py",
            "Supervised Analysis",
            "🤖",
        ),
        Page(
            f"{ROOT_DIR}/Streamlit/views/data_profile_report.py",
            "Data Profiling",
            "🕵️",
        ),
        # Page(
        #     f"{ROOT_DIR}/Streamlit/views/unsupervised_learning.py",
        #     "Data Profiling",
        #     "🕵️",
        # ),
        # Page("Streamlit/keyword_wordcloud.py", "Keywords", "🧐"),
        # Page("Streamlit/presentation.py", "Presentation", "🧐"),
    ]
)

# # # # Optional -- adds the title and icon to the current page
add_page_title()
