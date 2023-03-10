import streamlit as st
import pandas as pd
import zipfile
import shutil
from random import randint

from components import sagemaker_connection

def load_view():
    if 'key' not in st.session_state:
        st.session_state.key = str(randint(1000, 100000000))
    if 'init' not in st.session_state:
        st.session_state.csv_uploaded = False
        st.session_state.init = True
    st.markdown('''# **Data Loading**''')
    st.write('This is the data loading page where you can upload your data files to get analytics')
    st.subheader('Uploading of Data File')

    try:
        uploaded_file = st.file_uploader('Please upload the data file', type="csv", key=st.session_state.key, help='Rerun if cache error')
        if uploaded_file is not None:
            st.session_state.csv_uploaded = True
    except:
        st.warning('Failed to upload file, please try again', icon='🚨')
    
    if st.session_state.csv_uploaded == True:
        uploaded_df = pd.read_csv(uploaded_file)
        uploaded_df_small = uploaded_df.head(5)
        st.write('This is a sample of your file')
        st.dataframe(uploaded_df_small)
