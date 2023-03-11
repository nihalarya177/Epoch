import streamlit as st
from sklearn.datasets import fetch_openml
import pandas as pd
from components.preprocessing import PreprocessPipeline
from components.cars import CarClassifier


def data_loader_view():
    st.markdown("""# **File Upload**""")
    st.write("This is the page to plot graphsonto our application")


def load_view():
    st.write("hello")
    titanic = fetch_openml("titanic", version=1, as_frame=True)
    data = titanic["data"]
    data = pd.concat([data, titanic.target], axis=1)
    pipe = PreprocessPipeline(df=data, thresh=0.5)
    data = pipe.get_rule_mining_df()

    # column options
    options = ["None"]
    options.extend(data.columns.to_list())
    option = st.selectbox("Please select your Response Variable?", tuple(options))
    st.text(str)
    st.table(data.head())

    # if column select tarin CARS and isplay the rules
    if option != "None":
        x = data.drop(option, axis=1).copy()
        y = data[option]
        classifier = CarClassifier(minconf=0.67)
        classifier.fit(x, y)
        st.table(classifier.rules)
