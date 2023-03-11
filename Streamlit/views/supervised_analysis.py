import streamlit as st
from sklearn.datasets import fetch_openml
import pandas as pd
from components.preprocessing import PreprocessPipeline
from components.cars import CarClassifier
from components.summarizer import get_openai_response


def data_loader_view():
    st.markdown("""# **File Upload**""")
    st.write("This is the page to plot graphsonto our application")


def load_view():
    titanic = fetch_openml("titanic", version=1, as_frame=True)
    data = titanic["data"]
    data = pd.concat([data, titanic.target], axis=1)
    pipe = PreprocessPipeline(df=data, thresh=0.5)
    data = pipe.get_rule_mining_df()

    # column options
    options = ["None"]
    options.extend(data.columns.to_list())
    option = st.selectbox("Please select your Response Variable?", tuple(options))

    # if column select tarin CARS and isplay the rules
    if option != "None":
        with st.spinner("Generating rules..."):
            x = data.drop(option, axis=1).copy()
            y = data[option]
            classifier = CarClassifier(minconf=0.67)
            classifier.fit(x, y)
            st.table(classifier.rules)
            # summarizing the rules
            resp = get_openai_response(
                f"Kindly summarise the inferences from the association rules provided below. Explain each association rule separately and do not add technical jargon to the response. The response should be understandable by a child. \n \n {classifier.rules.drop(columns=['sup','rsup','err','maj']).rename(columns={'acc':'accuracy'}).reset_index(drop=True).__str__()}"
            )
            st.text(resp.choices[0].text)
