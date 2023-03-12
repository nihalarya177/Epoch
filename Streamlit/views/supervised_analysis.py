import streamlit as st
import time
from sklearn.datasets import fetch_openml
import pandas as pd
from components.preprocessing import PreprocessPipeline
from components.cars import CarClassifier
from components.summarizer import get_openai_response

# from myutils import inject_custom_css

# inject_custom_css()



def data_loader_view():
    st.markdown("""# **File Upload**""")
    st.write("This is the page to plot graphs onto our application")


def load_view():
    # titanic = fetch_openml("titanic", version=1, as_frame=True)
    if st.session_state.get("pipeline") is None:
        st.warning("Please first load your data in the Data loading page")
        # data = titanic["data"]
        # data = pd.concat([data, titanic.target], axis=1)
        # pipe = PreprocessPipeline(df=data, thresh=0.5)
    else:
        pipe = st.session_state.get("pipeline")
        data = pipe.get_rule_mining_df()

        # column options
        options = ["None"]
        options.extend(data.columns.to_list())
        option = st.selectbox("Please select your Response Variable?", tuple(options))

        # if column select tarin CARS and isplay the rules
        if option != "None":
            with st.container():
                st.subheader("Associate Rules")
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

            with st.spinner("Generating correlations..."):
                st.subheader("Correlation")
                corr_resp = pipe.get_top_feature_text(col=option)
                st.write(corr_resp[0])
                st.write(corr_resp[1])


load_view()

