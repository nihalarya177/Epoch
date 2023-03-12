import streamlit as st
import time
from sklearn.datasets import fetch_openml
import pandas as pd
from components.preprocessing import PreprocessPipeline
from components.cars import CarClassifier
from components.summarizer import get_openai_response



def data_loader_view():
    st.markdown("""# **File Upload**""")
    st.write("This is the page to plot graphs onto our application")


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
                st.markdown("""# **Rule Explanation**""")
                t = st.empty()
                ai_rules = resp.choices[0].text
                for i in range(len(ai_rules) + 1):
                    t.markdown("## %s" % ai_rules[0:i])
                    if i%2 ==0:
                        time.sleep(0.01)
                    else:
                        time.sleep(0.03)
