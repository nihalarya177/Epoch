import streamlit as st
import pandas as pd
from random import randint

# from myutils import inject_custom_css
from components.preprocessing import PreprocessPipeline

from views import supervised_analysis

conv_dict = {'Int64': 'Numerical',
             'float64': 'Numerical',
             'Float64': 'Numerical',
             'int64': 'Numerical',
             'object': 'String',
             'Object': 'String',
             'category': 'Categorical',
             'Category':'Categorical',
             'Datetime64[ns]':'Time Series'}


from components.eda_function import *

def submit_button_callback():
    st.session_state.button_clicked = True

def load_view():
    if 'button_clicked' not in st.session_state:
        st.session_state.button_clicked = False
    if "key" not in st.session_state:
        st.session_state.key = str(randint(1000, 100000000))
    if "init" not in st.session_state:
        st.session_state.pipeline = None
        st.session_state.csv_uploaded = False
        st.session_state.init = True
        st.session_state.datatypes = []
    st.markdown("""# **Data Loading**""")
    st.write(
        "This is the data loading page where you can upload your data files to get analytics"
    )
    st.subheader("Uploading of Data File")

    try:
        uploaded_file = st.file_uploader(
            "Please upload the data file",
            type="csv",
            key=st.session_state.key,
            help="Rerun if cache error",
        )
        if uploaded_file is not None:
            st.session_state.csv_uploaded = True
    except:
        st.warning("Failed to upload file, please try again", icon="🚨")

    if st.session_state.csv_uploaded == True:
        uploaded_df = pd.read_csv(uploaded_file, index_col=[0])
        uploaded_df_small = uploaded_df.head(5)
        with st.container():
            st.subheader("Uploaded Data File")
            st.write("This is a sample of your file")
            st.dataframe(uploaded_df_small)
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
            st.subheader("Table Description")
            st.write("Automatically generated table description")
            pipe = PreprocessPipeline(uploaded_df)
            with st.spinner("Generating auto description..."):
                st.session_state["pipeline"] = pipe
                description = get_df_description(pipe.cleaned_df)
                # desc = f'<p style="fcolor:Green; font-size: 24px;">{description}</p>'
                st.markdown(description)
            st.subheader("Data Type Check")
            st.write("We automatically detected these as the column datatypes")
            st.write(
                "If there are any that are wrongly detected, you can either change it or you can continue without changing it if you are not sure"
            )
            # data_types = data_type_checker.data_types()
            # testing

            if st.session_state.pipeline is None:
                pipe = PreprocessPipeline(uploaded_df)
                st.session_state.pipeline = pipe


            print(st.session_state["pipeline"])

            actual_data_types = []

            datas = [i.__str__() for i in list(st.session_state.pipeline.cleaned_df.dtypes.values)]
            data_types = [conv_dict[i] for i in datas]
            options = ["Numerical", "Time Series", "Categorical", "String"]
            columns = list(uploaded_df.columns)

            col1, col2 = st.columns(2)
            for i in range(len(data_types)):
                data_option = []
                data_option.append(data_types[i])
                temp = [ele for ele in options if ele not in data_option]
                sorted_options = data_option + temp
                with col1:
                    st.subheader(columns[i])
                    st.write(" ")
                    st.write(" ")
                with col2:
                    actual_data_types.append(
                        st.selectbox(label="", options=sorted_options, key=i)
                    )
            st.session_state.datatypes = actual_data_types

            if st.button("Continue"):
                st.session_state.button_clicked == True
                st.write("Continue to analysis page")


load_view()
