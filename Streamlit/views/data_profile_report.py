import streamlit as st
from components.data_profiling import get_data_profile_report
from sklearn.datasets import load_iris
import pandas as pd
from streamlit_pandas_profiling import st_profile_report
from views import data_loading



def load_view():
    pipeline = data_loading.get_pipeline_session_state()
    print(pipeline)
    if "init" not in st.session_state:
        st.session_state.init = True
        st.session_state.pipeline = pipeline
    else:
        st.session_state.pipeline = pipeline
    st.table(st.session_state.pipeline.df.head())
    if st.session_state.pipeline is None:        
        iris = load_iris(as_frame=True)
        data = pd.concat([iris.data, iris.target], axis=1)
        with st.spinner("Wait for it..."):
            report = get_data_profile_report(data)
    else:
        report = st.session_state.pipeline.report
    st_profile_report(report=report)

