import streamlit as st
import pandas as pd
import zipfile
import shutil
from random import randint

from myutils import inject_custom_css
from components import sagemaker_connection, data_type_checker

st.set_page_config(layout="wide", page_title="Epoch Solution")

inject_custom_css()
t = "<div>Hello there my <span class='highlight blue'>name <span class='bold'>yo</span> </span> is <span class='highlight red'>Fanilo <span class='bold'>Name</span></span></div>"

#def button_click():
    #st.session_state.button_clicked = True

def load_view():
    if 'key' not in st.session_state:
        st.session_state.key = str(randint(1000, 100000000))
    if 'init' not in st.session_state:
        st.session_state.csv_uploaded = False
        st.session_state.init = True
        st.session_state.datatypes = []
        st.session_state.button_clicked = False
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
        with st.container():
            st.subheader('Uploaded Data File')
            st.write('This is a sample of your file')
            st.dataframe(uploaded_df_small)
        st.markdown(
                    """
                <style>
                    div[data-testid="stVerticalBlock"] div[style*="flex-direction: column;"] div[data-testid="stVerticalBlock"] {
                        border: 1px rgba(38,39,48,255);
                        border-radius: 7px;
                        background: rgba(38,39,48,255);
                        padding: 50px;
                        padding-right:50px;
                    }

                    div[role="listbox"] ul {
                        background-color: red;
                    }

                    div[data-baseweb="select"] > div {
                        background-color: rgba(14,17,23,255);
                    }
                </style>
                """,
                    unsafe_allow_html=True,
                )
        with st.container():
            st.subheader('Data Type Check')
            st.write('We automatically detected these as the column datatypes')
            st.write('If there are any that are wrongly detected, you can either change it or you can continue without changing it if you are not sure')
            #data_types = data_type_checker.data_types()
            #testing
            actual_data_types = []
            data_types = ['Numerical', 'Categorical', 'Categorical', 'Time Series']
            options = ['Numerical', 'Time Series', 'Categorical']
            columns = list(uploaded_df.columns)
            col1, col2 = st.columns(2)
            for i in range(len(data_types)):
                data_option = []
                data_option.append(data_types[i])
                temp = [ele for ele in options if ele not in data_option]
                sorted_options = data_option+temp
                with col1:
                    st.subheader(columns[i])
                    st.write(" ")
                    st.write(" ")
                    st.write(" ")
                with col2:
                    actual_data_types.append(st.selectbox(label="", options=sorted_options, key=i))
            st.session_state.datatypes = actual_data_types
            st.button('Continue')
            st.write(st.session_state.button_clicked)
            if st.session_state.button_clicked==True:
                st.write('continue to analysis page')
        
            

                
